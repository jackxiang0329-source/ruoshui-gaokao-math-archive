#!/usr/bin/env python3
"""Validate upstream sources and all generated inventory schemas."""
import csv
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sources=json.loads((ROOT/"sources.json").read_text(encoding="utf-8"))["repositories"]
assert len(sources)==11, "Expected exactly eleven sources"
assert len({x["id"] for x in sources})==11, "Duplicate source IDs"
for source in sources:
    subdir="upstream/"+source["id"]
    result=subprocess.run(
        ["git","config","-f",".gitmodules","--get","submodule."+subdir+".url"],
        cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip()
    assert result=="https://github.com/"+source["repo"]+".git", (subdir,result)
    assert (ROOT/subdir/".git").exists(), "Uninitialized submodule "+subdir

for name in ("files.csv","derivative-candidates.csv","gaokao-candidates.csv"):
    with (ROOT/"index"/name).open(encoding="utf-8-sig",newline="") as handle:
        rows=list(csv.DictReader(handle))
    assert all(row.get("review_status")=="unreviewed" for row in rows), name

with (ROOT/"index"/"derivative-machine-candidates.csv").open(encoding="utf-8-sig",newline="") as handle:
    machine=list(csv.DictReader(handle))
assert all(row.get("status")=="machine-candidate-not-reviewed" for row in machine)
assert all(row.get("source_path","").startswith("content/") for row in machine)
assert all(row.get("line","").isdigit() and int(row["line"])>0 for row in machine)
assert len({row["id"] for row in machine})==len(machine), "Duplicate machine question IDs"
print("PASS: source pointers, file inventories, and machine question inventory")
