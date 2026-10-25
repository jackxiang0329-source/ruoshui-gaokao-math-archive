#!/usr/bin/env python3
"""Fail-closed validation of 11 pinned Git submodule revisions.

Compare sources.json initial_commit, tracked gitlinks, .gitmodules and optionally
the checked-out submodule HEADs. This does NOT authenticate external exam papers.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"^[0-9a-f]{40}$")
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class PinMismatch(RuntimeError):
    pass


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(root), *args], stderr=subprocess.PIPE
    )


def parse_gitlinks(data: bytes) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in data.split(b"\0"):
        if not line:
            continue
        try:
            meta, raw_path = line.split(b"\t", 1)
            mode, sha, stage = meta.decode("ascii").split()
            path = os.fsdecode(raw_path)
        except (ValueError, UnicodeError) as exc:
            raise PinMismatch("Invalid git ls-files output") from exc
        if (mode != "160000" or stage != "0" or not SHA.fullmatch(sha)
                or not path.startswith("upstream/")
                or not SLUG.fullmatch(path[9:])
                or path in result):
            raise PinMismatch("Unsafe, unmerged, duplicate or non-gitlink entry: " + path)
        result[path] = sha
    return result


def check_manifest(gitlinks: dict[str, str], sources: list[dict]) -> None:
    expected: dict[str, str] = {}
    for source in sources:
        slug, pin = source["id"], source["initial_commit"]
        if not SLUG.fullmatch(slug) or not SHA.fullmatch(pin):
            raise PinMismatch("Bad source slug or commit pin: " + slug)
        key = "upstream/" + slug
        if key in expected:
            raise PinMismatch("Duplicate source id: " + slug)
        expected[key] = pin
    if expected != gitlinks:
        raise PinMismatch(
            f"Sources and Git index differ: "
            f"missing={sorted(expected.keys() - gitlinks.keys())}; "
            f"extra={sorted(gitlinks.keys() - expected.keys())}; "
            f"wrong_pin={sorted(k for k in expected.keys() & gitlinks.keys() if expected[k] != gitlinks[k])}"
        )


def validate(root: Path = ROOT, *, index_only: bool = False) -> int:
    sources = json.loads((root / "sources.json").read_text(encoding="utf-8"))["repositories"]
    if len(sources) != 11:
        raise PinMismatch("Expected exactly 11 upstream repositories")
    indexed = parse_gitlinks(git(root, "ls-files", "--stage", "-z", "--", "upstream"))
    check_manifest(indexed, sources)
    for source in sources:
        name = "upstream/" + source["id"]
        for field, expected in (
            ("url", "https://github.com/" + source["repo"] + ".git"),
            ("branch", source["branch"]),
        ):
            key = "submodule." + name + "." + field
            found = git(root, "config", "-f", ".gitmodules", "--get", key).decode().strip()
            if found != expected:
                raise PinMismatch(f".gitmodules {key}: expected {expected}; got {found}")
        if not index_only:
            actual_head = git(root / name, "rev-parse", "HEAD").decode().strip()
            if actual_head != source["initial_commit"]:
                raise PinMismatch("Submodule checkout changed from pinned version: " + name)
    return len(sources)


def main() -> None:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--index-only", action="store_true",
                     help="Check committed gitlinks without downloading submodule contents")
    args = cli.parse_args()
    try:
        n = validate(index_only=args.index_only)
    except (OSError, KeyError, ValueError, PinMismatch, subprocess.CalledProcessError) as exc:
        cli.exit(1, "FAIL: " + str(exc) + "\n")
    print(f"PASS: {n} pinned Git submodules verified" +
          (" (index metadata only)" if args.index_only else " (including checkout HEAD)"))


if __name__ == "__main__":
    main()
