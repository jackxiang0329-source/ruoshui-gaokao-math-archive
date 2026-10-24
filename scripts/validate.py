#!/usr/bin/env python3
"""Check submodules, source manifest and generated CSV inventories."""
import csv
import json
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))["repositories"]
assert len(sources) == 11
assert len(set(s["id"] for s in sources)) == 11
for src in sources:
    path = "upstream/" + src["id"]
    result = subprocess.run(
        ["git","config","-f",".gitmodules","--get","submodule." + path + ".url"],
        cwd=ROOT,check=True,text=True,capture_output=True
    ).stdout.strip()
    assert result == "https://github.com/" + src["repo"] + ".git", (path,result)
    assert (ROOT / path / ".git").exists(), "Submodule checkout missing: " + path
for name in ("files.csv","derivative-candidates.csv","gaokao-candidates.csv","derivative-machine-candidates.csv"):
    with (ROOT / "index" / name).open(encoding="utf-8-sig",newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert all(r["review_status"] == "unreviewed" for r in rows), name
print("PASS: 11 source URLs and 3 CSV indexes verified.")
