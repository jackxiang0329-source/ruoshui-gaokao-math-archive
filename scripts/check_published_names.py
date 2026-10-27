#!/usr/bin/env python3
"""Check published filenames, exact copies and proof-merge provenance."""
import csv
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = re.compile(r"papers/(\d{4})/gaokao-\1-[a-z0-9-]+-(general|science|liberal)(-spring)?-paper\.pdf")
TOPIC = re.compile(r"topics/[a-z0-9-]+/topic-[^\s/]+\.(tex|pdf)")
MASTER = "derivative/reviewed/gaokao-2010-2025-calculus-reviewed-solutions.tex"

def main():
    result = subprocess.check_output(["git", "-C", str(ROOT), "ls-tree", "-r", "HEAD"])
    blobs = {}
    for ln in result.decode("utf-8", "surrogateescape").splitlines():
        if not ln: continue
        metadata, path = ln.split("\t", 1)
        if metadata.split()[1] == "blob":
            blobs[path] = metadata.split()[2]
    merged_text = (ROOT / MASTER).read_text(encoding="utf-8")
    with (ROOT / "catalog" / "normalized_files.csv").open(encoding="utf-8-sig", newline="") as fh:
        mapping = list(csv.DictReader(fh))
    assert len({r["original_path"] for r in mapping}) == len(mapping)
    merged = 0
    for record in mapping:
        old, new, sha = record["original_path"], record["canonical_path"], record["blob_sha"]
        assert old not in blobs, "Unremoved file: " + old
        if record["action"] == "merge":
            assert new == MASTER and MASTER in blobs
            assert ("sha=" + sha) in merged_text, "Missing original SHA in master: " + old
            merged += 1
        else:
            assert blobs.get(new) == sha, "Changed blob: " + new
    assert merged == 26, "Expected legacy and normalized proof provenance entries"
    papers = [p for p in blobs if p.startswith("papers/")]
    assert len(papers) == 775 and all(PDF.fullmatch(p) for p in papers)
    topic_files = [p for p in blobs if p.startswith("topics/") and p.endswith((".tex",".pdf"))]
    assert len(topic_files) == 116
    for p in topic_files:
        assert TOPIC.fullmatch(p)
        assert (p[:-4] + (".pdf" if p.endswith(".tex") else ".tex")) in blobs
    assert [p for p in blobs if p.startswith("derivative/reviewed/") and p.endswith(".tex")] == [MASTER]
    assert merged_text.count("% SOURCE_ENTRY path=") == 13
    print("PASS:",len(mapping),"provenance entries;",len(papers),"exam PDFs; 58 TeX/PDF topic pairs; 13 proof sections")

if __name__ == "__main__":
    main()
