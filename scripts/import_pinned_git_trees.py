#!/usr/bin/env python3
"""Import all 11 pinned upstream Git trees as REAL blobs and trees, not links.

Requires Git, Python 3 and network access to GitHub. The working tree and
user's ordinary index are never changed. Fetch full upstream objects without
blob filters; compare exact subtree SHA before each fast-forward push.

Usage: python scripts/import_pinned_git_trees.py --push
       python scripts/import_pinned_git_trees.py --source gaokaomath --push
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN_RE = re.compile(r"[0-9a-f]{40}\Z")
REPO_RE = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
ID_RE = re.compile(r"[a-z0-9][a-z0-9-]*\Z")


def git(root: Path, *args: str, env: dict[str, str] | None = None,
        capture: bool = True) -> str:
    cmd = ["git", "-C", str(root), *args]
    proc = subprocess.run(cmd, check=True, text=True,
                          stdout=subprocess.PIPE if capture else None,
                          stderr=subprocess.PIPE if capture else None, env=env)
    return proc.stdout.strip() if capture else ""


def object_count(root: Path, revision: str) -> tuple[int, int]:
    raw = subprocess.check_output(["git", "-C", str(root), "ls-tree", "-r", "-z", revision])
    blobs = gitlinks = 0
    for item in raw.split(b"\0"):
        if not item:
            continue
        mode = item.split(b" ", 1)[0]
        if mode == b"160000":
            gitlinks += 1
        else:
            blobs += 1
    return blobs, gitlinks


def import_one(root: Path, *, source_id: str, source_url: str, pin: str,
               parent: str, push: bool) -> tuple[str, str, int]:
    if not ID_RE.fullmatch(source_id) or not PIN_RE.fullmatch(pin):
        raise ValueError("Unsafe source id or pin")
    if not source_url.startswith("https://github.com/") and not source_url.startswith("file://"):
        raise ValueError("Unapproved upstream URL")

    print(f"Fetching {source_id} @ {pin[:12]} (full Git objects)", flush=True)
    git(root, "fetch", "--no-tags", "--depth=1", source_url, pin, capture=False)
    fetched_commit = git(root, "rev-parse", f"{pin}^{{commit}}")
    if fetched_commit != pin:
        raise RuntimeError(f"Pinned commit mismatch: {source_id}")
    pinned_tree = git(root, "rev-parse", f"{pin}^{{tree}}")
    blobs, nested_links = object_count(root, pin)
    if nested_links:
        raise RuntimeError(f"{source_id} has {nested_links} nested Git submodules: "
                           "cannot claim a full file import; handle them separately")

    dest = f"mirror/{source_id}"
    try:
        existing = git(root, "rev-parse", f"{parent}:{dest}")
    except subprocess.CalledProcessError:
        existing = ""
    if existing == pinned_tree:
        print(f"SKIP {source_id}: pinned tree already complete ({blobs} Git blobs)", flush=True)
        return parent, "unchanged", blobs

    with tempfile.TemporaryDirectory(prefix="gaokao-index-") as temp:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(temp) / "index"),
                   GIT_TERMINAL_PROMPT="0")
        git(root, "read-tree", parent, env=env)
        if existing:
            # --sparse is required when the runner only checks out scripts/tests.
            git(root, "rm", "-r", "-f", "--cached", "--sparse", "-q", "--", dest, env=env)
        git(root, "read-tree", f"--prefix={dest}/", pinned_tree, env=env)
        new_tree = git(root, "write-tree", env=env)
        exact = git(root, "rev-parse", f"{new_tree}:{dest}")
        if exact != pinned_tree:
            raise RuntimeError(f"FATAL: subtree digest mismatch for {source_id}")

    if not push:
        print(f"PREVIEW {source_id}: would import {blobs} exact blobs; no push", flush=True)
        return parent, "preview", blobs

    message = f"mirror: import {source_id} pinned {pin[:12]} ({blobs} objects)"
    new_commit = git(root, "commit-tree", new_tree, "-p", parent, "-m", message)
    git(root, "push", "origin", f"{new_commit}:refs/heads/main", capture=False)
    print(f"IMPORTED {source_id}: {blobs} blobs, tree {pinned_tree[:12]}, "
          f"commit {new_commit[:12]}", flush=True)
    return new_commit, "pushed", blobs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--source", default="all", help="All or one source ID")
    parser.add_argument("--push", action="store_true", help="Actually fast-forward push to origin/main")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        git(root, "rev-parse", "--show-toplevel")
        git(root, "fetch", "--no-tags", "origin", "refs/heads/main", capture=False)
        parent = git(root, "rev-parse", "FETCH_HEAD")
        sources = json.loads(git(root, "show", f"{parent}:sources.json"))["repositories"]
        if len(sources) != 11 or len({s["id"] for s in sources}) != 11:
            raise ValueError("Expected 11 distinct pinned upstream repositories")
        if args.source != "all" and args.source not in {s["id"] for s in sources}:
            raise ValueError("Unknown source: " + args.source)
        total = 0
        for source in sources:
            sid, repo, pin = source["id"], source["repo"], source["initial_commit"]
            if args.source != "all" and args.source != sid:
                continue
            if not REPO_RE.fullmatch(repo) or not PIN_RE.fullmatch(pin):
                raise ValueError(f"Invalid pinned repository descriptor: {sid}")
            parent, state, blobs = import_one(
                root, source_id=sid, source_url=f"https://github.com/{repo}.git",
                pin=pin, parent=parent, push=args.push)
            total += (blobs if state == "pushed" else 0)
        print(f"DONE: {total} source blobs in new fast-forward commits; "
              f"push={'enabled' if args.push else 'disabled'}")
        if args.push:
            print("For a fresh mirror audit run: python3 scripts/audit_mirror_inventory.py")
        return 0
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print("MIRROR IMPORT FAILED (not claiming completion): " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
