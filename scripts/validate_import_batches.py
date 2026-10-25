#!/usr/bin/env python3
"""Audit recorded mirror import batches against *committed* Git objects offline.

Checks that each listed blob is absent/not strictly matching at baseline, exactly
present at the audited commit, and remains exactly present at HEAD. Git SHA, mode,
and object size must all agree. Also validates the claimed batch counts, per-folder
aggregates, fixed source pin, and selected mirror status bookkeeping.

This checks copying integrity only; NOT mathematics, provenance authenticity, PDF
rendering, image quality or rights to distribute any content.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"[0-9a-f]{40}\Z")
MODES = {"100644", "100755", "120000"}


class BatchAuditError(ValueError):
    """A batch claim or pinned Git object failed verification."""


def positive_int(value: object, label: str, *, allow_zero: bool = False) -> int:
    if type(value) is not int or value < (0 if allow_zero else 1):
        raise BatchAuditError(f"{label} must be an integer >= {0 if allow_zero else 1}")
    return value


def safe_path(raw: object) -> str:
    if not isinstance(raw, str) or not raw or "\\" in raw or "\x00" in raw:
        raise BatchAuditError("Invalid manifest path")
    p = PurePosixPath(raw)
    if (p.is_absolute() or any(part in ("", ".", "..") for part in raw.split("/"))
            or raw.startswith("/") or str(p) != raw):
        raise BatchAuditError("Unsafe/noncanonical manifest path: " + repr(raw))
    return raw


def git_tree(root: Path, ref: str, prefix: str) -> dict[str, tuple[str, str, int]]:
    """Git ls-tree -l -r -z (not a possibly modified working-tree listing)."""
    raw = subprocess.check_output(
        ["git", "-C", str(root), "ls-tree", "-r", "-l", "-z", ref, "--", prefix],
        stderr=subprocess.PIPE,
    )
    entries: dict[str, tuple[str, str, int]] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            meta, name = record.split(b"\t", 1)
            mode, kind, sha, size = meta.decode("ascii").split()
            path = name.decode("utf-8", errors="strict")
            if (kind != "blob" or mode not in MODES or not SHA.fullmatch(sha)
                    or not path.startswith(prefix + "/") or path in entries):
                raise BatchAuditError("Unsafe, duplicate or non-blob Git entry: " + path)
            entries[path] = (mode, sha, positive_int(int(size), "Git blob size", allow_zero=True))
        except (UnicodeError, ValueError) as exc:
            if isinstance(exc, BatchAuditError):
                raise
            raise BatchAuditError("Malformed ls-tree record") from exc
    return entries


def validate_batch(
    manifest: dict,
    sources: dict,
    baseline: dict[str, tuple[str, str, int]],
    after: dict[str, tuple[str, str, int]],
    current: dict[str, tuple[str, str, int]],
) -> int:
    """Pure validator; dependency-injected Git trees allow adversarial tests."""
    if not isinstance(manifest, dict) or not isinstance(sources, dict):
        raise BatchAuditError("Invalid manifest or source list")
    source_id = manifest.get("source_id")
    source = sources.get(source_id)
    if not source:
        raise BatchAuditError("Source missing from sources.json: " + repr(source_id))
    if (manifest.get("source_repo") != source["repo"]
            or manifest.get("source_commit") != source["initial_commit"]):
        raise BatchAuditError("Source URL or fixed commit does not match sources.json")
    for field in ("baseline_commit", "audited_after_commit"):
        if not isinstance(manifest.get(field), str) or not SHA.fullmatch(manifest[field]):
            raise BatchAuditError("Invalid commit field: " + field)
    if manifest["baseline_commit"] == manifest["audited_after_commit"]:
        raise BatchAuditError("Baseline and audited commits must differ")
    rows = manifest.get("files")
    if not isinstance(rows, list) or not rows:
        raise BatchAuditError("Nonempty files array required")
    if positive_int(manifest.get("count"), "count") != len(rows):
        raise BatchAuditError("Manifest file count mismatch")
    seen: set[str] = set()
    sizes = 0
    groups: dict[str, dict[str, int]] = defaultdict(lambda: {"files": 0, "bytes": 0})
    for row in rows:
        if not isinstance(row, dict):
            raise BatchAuditError("Malformed file entry")
        path = safe_path(row.get("path"))
        if path in seen:
            raise BatchAuditError("Duplicate manifest path: " + path)
        seen.add(path)
        declared = row.get("sha")
        if not isinstance(declared, str) or not SHA.fullmatch(declared):
            raise BatchAuditError("Invalid blob SHA: " + path)
        mode = row.get("mode")
        if mode not in MODES:
            raise BatchAuditError("Unsupported Git mode: " + path)
        size = positive_int(row.get("size"), "file size", allow_zero=True)
        expected = (mode, declared, size)
        key = f"mirror/{source_id}/{path}"
        if baseline.get(key) == expected:
            raise BatchAuditError("File was already strictly matched in baseline: " + path)
        if after.get(key) != expected:
            raise BatchAuditError("Audited commit disagrees with manifest: " + path)
        if current.get(key) != expected:
            raise BatchAuditError("HEAD missing or changed imported file: " + path)
        sizes += size
        parts = path.split("/")
        if len(parts) < 3:
            raise BatchAuditError("Expected original year/category grouping: " + path)
        group = "/".join(parts[:2])
        groups[group]["files"] += 1
        groups[group]["bytes"] += size
    if positive_int(manifest.get("total_upstream_bytes"), "total_upstream_bytes") != sizes:
        raise BatchAuditError("Batch total bytes mismatch")
    if manifest.get("group_counts") != dict(groups):
        raise BatchAuditError("Per-group file counts or byte totals mismatch")
    return len(rows)


def validate_status(status: dict, manifest: dict, source_ids: set[str],
                    manifest_path: str = "mirror/IMPORT_BATCH_HISTORICAL_FIGURES_2026_10_25.json") -> None:
    """Check stored progress accounting without claiming a fresh upstream audit."""
    rows = status.get("sources")
    if not isinstance(rows, list) or {r.get("id") for r in rows} != source_ids or len(rows) != len(source_ids):
        raise BatchAuditError("Status must list each pinned source exactly once")
    totals = {"expected": 0, "verified": 0, "missing": 0, "full": 0}
    for row in rows:
        n = [positive_int(row.get(k), k, allow_zero=True) for k in ("expected", "verified", "missing")]
        if n[0] != n[1] + n[2] or type(row.get("complete")) is not bool:
            raise BatchAuditError("Incorrect source coverage arithmetic: " + repr(row.get("id")))
        if row["complete"] != (n[2] == 0):
            raise BatchAuditError("Incorrect source complete flag")
        for k, v in zip(("expected", "verified", "missing"), n):
            totals[k] += v
        totals["full"] += int(row["complete"])
    for key, total in totals.items():
        if status.get(key) != total:
            raise BatchAuditError("Mirror status total mismatch: " + key)
    latest = status.get("latest_direct_import")
    if latest and latest.get("manifest") == manifest_path:
        checks = {
            "source": manifest["source_id"], "source_pin": manifest["source_commit"],
            "baseline_commit": manifest["baseline_commit"],
            "mirror_commit": manifest["audited_after_commit"],
            "new_verified": manifest["count"], "new_bytes": manifest["total_upstream_bytes"],
        }
        for k, v in checks.items():
            if latest.get(k) != v:
                raise BatchAuditError("Latest import metadata mismatch: " + k)
        if status.get("audited_commit") != manifest["audited_after_commit"]:
            raise BatchAuditError("Audited status commit mismatch")


def verify(root: Path) -> int:
    sources_data = json.loads((root / "sources.json").read_text(encoding="utf-8"))
    sources = {s["id"]: s for s in sources_data["repositories"]}
    files = sorted((root / "mirror").glob("IMPORT_BATCH_*.json"))
    if not files:
        raise BatchAuditError("No import batch manifests found")
    count = 0
    manifest_by_path = {}
    for file in files:
        manifest = json.loads(file.read_text(encoding="utf-8"))
        sid = manifest.get("source_id")
        if sid not in sources or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", sid):
            raise BatchAuditError("Unrecognized or unsafe source id")
        for field in ("baseline_commit", "audited_after_commit"):
            value = manifest.get(field)
            if not isinstance(value, str) or not SHA.fullmatch(value):
                raise BatchAuditError("Invalid commit field: " + field)
        prefix = f"mirror/{sid}"
        baseline = git_tree(root, manifest["baseline_commit"], prefix)
        after = git_tree(root, manifest["audited_after_commit"], prefix)
        current = git_tree(root, "HEAD", prefix)
        count += validate_batch(manifest, sources, baseline, after, current)
        manifest_by_path[file.relative_to(root).as_posix()] = manifest
    status = json.loads((root / "mirror/MIRROR_STATUS.json").read_text(encoding="utf-8"))
    latest_path = status.get("latest_direct_import", {}).get("manifest")
    if latest_path and latest_path not in manifest_by_path:
        raise BatchAuditError("Latest import refers to a missing manifest: " + repr(latest_path))
    manifest_path = latest_path or next(iter(manifest_by_path))
    validate_status(status, manifest_by_path[manifest_path], set(sources), manifest_path)
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT,
                        help="Repository root containing Git history and sources.json")
    args = parser.parse_args()
    try:
        count = verify(args.root.resolve())
    except (BatchAuditError, KeyError, OSError, subprocess.CalledProcessError, ValueError) as exc:
        print("IMPORT BATCH QA FAILED: " + str(exc), file=sys.stderr)
        return 1
    print(f"PASS: {count} imported blobs retain audited Git SHA, mode, and size; metadata consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
