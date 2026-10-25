#!/usr/bin/env python3
"""Fail closed unless a mirrored source exactly matches its pinned Git tree.

Checks original bytes, executable/symlink modes and the *staged* Git index.
This does not certify mathematical correctness, PDF rendering or licensing.
"""
import argparse
import hashlib
import json
import os
import stat
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MirrorIntegrityError(RuntimeError):
    pass


def git(directory, *args):
    return subprocess.check_output(
        ["git", "-C", str(directory), *args], stderr=subprocess.PIPE
    )


def git_blob_sha(payload):
    header = b"blob " + str(len(payload)).encode("ascii") + b"\0"
    return hashlib.sha1(header + payload).hexdigest()


def parse_entries(raw, *, staged=False):
    """Parse NUL-separated git ls-tree/ls-files records, including UTF-8 paths."""
    entries = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            meta, name = record.split(b"\t", 1)
            parts = meta.decode("ascii").split()
            if staged:
                mode, sha, stage = parts
                if stage != "0":
                    raise MirrorIntegrityError("Unmerged index entry")
            else:
                mode, object_type, sha = parts
                if object_type != "blob":
                    raise MirrorIntegrityError(
                        "Gitlink/submodule cannot be counted as a physical file: "
                        + os.fsdecode(name)
                    )
            path = os.fsdecode(name)
        except (ValueError, UnicodeError) as exc:
            raise MirrorIntegrityError("Malformed Git tree/index entry") from exc
        if path in entries or Path(path).is_absolute() or ".." in Path(path).parts:
            raise MirrorIntegrityError("Duplicate or unsafe path: " + path)
        if mode not in ("100644", "100755", "120000"):
            raise MirrorIntegrityError("Unsupported Git mode: " + mode)
        entries[path] = (mode, sha)
    return entries


def check_bytes(mirror_dir, expected):
    for path, (mode, sha) in expected.items():
        file = mirror_dir / path
        if mode == "120000":
            if not file.is_symlink():
                raise MirrorIntegrityError("Missing or changed symlink: " + path)
            payload = os.fsencode(os.readlink(file))
        else:
            if not file.is_file() or file.is_symlink():
                raise MirrorIntegrityError("Missing regular file: " + path)
            payload = file.read_bytes()
            if payload.startswith(b"version https://git-lfs.github.com/spec/v1\n"):
                raise MirrorIntegrityError(
                    "Unresolved Git LFS pointer, not original asset: " + path
                )
            executable = bool(file.stat().st_mode & stat.S_IXUSR)
            if executable != (mode == "100755"):
                raise MirrorIntegrityError("Executable mode changed: " + path)
        got = git_blob_sha(payload)
        if got != sha:
            raise MirrorIntegrityError(
                "Corrupt file: " + path + " (expected " + sha + ", got " + got + ")"
            )


def check_index(root, mirror_prefix, expected):
    raw = git(root, "ls-files", "--stage", "-z", "--", mirror_prefix)
    all_staged = parse_entries(raw, staged=True)
    prefix = mirror_prefix.rstrip("/") + "/"
    actual = {
        key[len(prefix):]: val
        for key, val in all_staged.items()
        if key.startswith(prefix)
    }
    if actual != expected:
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        mismatched = sorted(
            path for path in set(actual) & set(expected)
            if actual[path] != expected[path]
        )
        raise MirrorIntegrityError(
            "Staged mirror differs from pinned tree: "
            + repr({"missing": missing[:8], "extra": extra[:8],
                    "wrong_sha_or_mode": mismatched[:8]})
        )


def verify(source_id, upstream_dir, root=ROOT):
    manifest = json.loads((root / "sources.json").read_text(encoding="utf-8"))
    sources = {x["id"]: x for x in manifest["repositories"]}
    if source_id not in sources:
        raise MirrorIntegrityError("Unknown source id: " + source_id)
    pinned = sources[source_id]["initial_commit"]
    actual = git(upstream_dir, "rev-parse", "HEAD").decode().strip()
    if actual != pinned:
        raise MirrorIntegrityError("Upstream HEAD is not pinned: " + actual)
    expected = parse_entries(git(upstream_dir, "ls-tree", "-rz", "HEAD"))
    if not expected:
        raise MirrorIntegrityError("Pinned upstream tree has no files")
    prefix = "mirror/" + source_id
    check_bytes(root / prefix, expected)
    check_index(root, prefix, expected)
    return len(expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--upstream-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        n = verify(args.source_id, args.upstream_dir.resolve())
    except (MirrorIntegrityError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, "FAIL: " + str(exc) + "\n")
    print("PASS: {} pinned source files checked byte-for-byte and staged".format(n))


if __name__ == "__main__":
    main()
