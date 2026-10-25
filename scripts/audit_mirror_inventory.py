#!/usr/bin/env python3
"""Recalculate *committed* mirror completeness against 11 pinned upstream trees.

Requires the 11 upstream submodules to be initialized at sources.json pins.
A matching blob SHA and Git mode count as mirrored; a gitlink, working-tree copy,
LFS pointer substitution, or filename-only inventory does not. Git SHA does not
certify mathematics, PDF legibility, provenance authenticity, or licensing.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMIT = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_MODES = {"100644", "100755", "120000"}


class AuditError(RuntimeError):
    pass


def git(cwd: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(cwd), *args], stderr=subprocess.PIPE
    )


def parse_tree(data: bytes, prefix: str = "") -> dict[str, tuple[str, str]]:
    """Parse NUL-delimited git ls-tree -r -z output, preserving Unicode paths."""
    records: dict[str, tuple[str, str]] = {}
    for record in data.split(b"\0"):
        if not record:
            continue
        try:
            metadata, pathbytes = record.split(b"\t", 1)
            mode, kind, sha = metadata.decode("ascii").split()
            path = os.fsdecode(pathbytes)
        except (ValueError, UnicodeError) as exc:
            raise AuditError("Malformed ls-tree record") from exc
        if kind != "blob" or mode not in ALLOWED_MODES or not COMMIT.fullmatch(sha):
            raise AuditError("Non-blob or unsupported object at " + path)
        if prefix:
            if not path.startswith(prefix):
                raise AuditError("Path outside requested mirror: " + path)
            path = path[len(prefix):]
        if (not path or path.startswith("/") or ".." in Path(path).parts
                or path in records):
            raise AuditError("Unsafe or duplicate Git tree path: " + path)
        records[path] = (mode, sha)
    return records


def compare(expected: dict, actual: dict) -> dict:
    matched = sum(actual.get(path) == value for path, value in expected.items())
    missing = sorted(path for path, value in expected.items() if actual.get(path) != value)
    unexpected = sorted(set(actual).difference(expected))
    return {
        "expected": len(expected),
        "verified": matched,
        "missing": len(missing),
        "extra": len(unexpected),
        "missing_examples": missing[:12],
        "extra_examples": unexpected[:12],
        "complete": matched == len(expected) and not unexpected,
    }


def audit_source(root: Path, source: dict) -> dict:
    sid = source["id"]
    pin = source["initial_commit"]
    if not COMMIT.fullmatch(pin):
        raise AuditError("Invalid pinned commit for " + sid)
    upstream = root / "upstream" / sid
    try:
        checked = git(upstream, "rev-parse", "HEAD").decode("ascii").strip()
    except (subprocess.CalledProcessError, OSError) as exc:
        raise AuditError("Initialize the pinned upstream submodule: " + sid) from exc
    if checked != pin:
        raise AuditError("Wrong upstream checkout for " + sid + ": " + checked)
    original = parse_tree(git(upstream, "ls-tree", "-r", "-z", pin))
    # Compare against HEAD Git *objects*, not possibly dirty working-tree files.
    mirror_prefix = "mirror/" + sid + "/"
    mirrored = parse_tree(
        git(root, "ls-tree", "-r", "-z", "HEAD", "--", mirror_prefix),
        mirror_prefix,
    )
    result = compare(original, mirrored)
    result["id"] = sid
    return result


def audit(root: Path, selected: str = "all") -> dict:
    manifest = json.loads((root / "sources.json").read_text(encoding="utf-8"))
    sources = manifest["repositories"]
    if len(sources) != 11 or len({source["id"] for source in sources}) != 11:
        raise AuditError("Expected exactly 11 distinct sources")
    if selected != "all":
        sources = [source for source in sources if source["id"] == selected]
        if not sources:
            raise AuditError("Unknown source: " + selected)
    results = [audit_source(root, item) for item in sources]
    return {
        "date": datetime.now(timezone.utc).date().isoformat(),
        "method": "Compare committed mirror Git blob SHA and mode with pinned source Git trees.",
        "expected": sum(row["expected"] for row in results),
        "verified": sum(row["verified"] for row in results),
        "missing": sum(row["missing"] for row in results),
        "full": sum(row["complete"] for row in results),
        "extra": sum(row["extra"] for row in results),
        "sources": results,
        "note": "SHA+mode verifies copying only, not questions, mathematical proofs, PDF rendering, or licenses.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default="all", help="all or sources.json id")
    parser.add_argument("--output", type=Path,
                        help="Optional output JSON path; defaults to stdout only")
    args = parser.parse_args()
    try:
        report = audit(ROOT, args.source)
        serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(serialized, encoding="utf-8")
        else:
            print(serialized, end="")
    except (AuditError, OSError, KeyError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, "AUDIT FAILED: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
