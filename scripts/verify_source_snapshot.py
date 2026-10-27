#!/usr/bin/env python3
"""Verify the full pinned 11-source tree in the separate archive branch."""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = "refs/remotes/origin/full-source-archive"


def git(*args):
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *args], stderr=subprocess.PIPE
    ).decode("utf-8").strip()


def verify():
    manifest = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    status = json.loads(git("show", REF + ":mirror/MIRROR_STATUS.json"))
    records = {r["id"]: r for r in status["sources"]}
    assert len(records) == len(manifest["repositories"]) == 11
    n = 0
    for src in manifest["repositories"]:
        sid = src["id"]
        entry = records[sid]
        assert src["initial_commit"] == entry["upstream_commit"], sid
        actual = git("rev-parse", REF + ":mirror/" + sid)
        assert actual == entry["expected_tree_sha"] == entry["actual_tree_sha"], sid
        assert entry["verified"] == entry["expected"] and entry["missing"] == 0
        n += entry["verified"]
        print("PASS", sid, entry["verified"], actual, flush=True)
    assert n == 7222, n
    print("PASS: all 11 full original source trees verified on "
          "full-source-archive; main is the compact working branch.", flush=True)


if __name__ == "__main__":
    verify()
