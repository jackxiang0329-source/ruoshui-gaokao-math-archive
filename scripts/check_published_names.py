#!/usr/bin/env python3
"""Check published names, Git blob SHA preservation, and TeX/PDF pairing."""
import csv
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = re.compile(r"papers/(\d{4})/gaokao-\1-[a-z0-9-]+-(?:general|science|liberal)(?:-spring)?-paper\.pdf")
TOPIC = re.compile(r"topics/[a-z0-9-]+/topic-[a-z0-9-]+\.(?:tex|pdf)")
SOLUTION = re.compile(r"derivative/reviewed/gaokao-[0-9]{4}-[a-z0-9-]+-solution\.tex")

def main():
    result = subprocess.check_output(["git", "-C", str(ROOT), "ls-tree", "-r", "HEAD"])
    sha = {}
    for line in result.decode("utf-8", "surrogateescape").splitlines():
        meta, path = line.split("\t", 1)
        if meta.split()[1] == "blob":
            sha[path] = meta.split()[2]
    with (ROOT / "catalog" / "normalized_files.csv").open(encoding="utf-8-sig", newline="") as fp:
        mapping = list(csv.DictReader(fp))
    assert len({m["original_path"] for m in mapping}) == len(mapping)
    for m in mapping:
        a, b = m["original_path"], m["canonical_path"]
        assert a not in sha, "Old filename retained: " + a
        assert sha.get(b) == m["blob_sha"], "Published content differs: " + b
    exam = [p for p in sha if p.startswith("papers/")]
    assert len(exam) >= 775
    assert all(PDF.fullmatch(p) for p in exam), "Nonstandard exam PDF name"
    topics = [p for p in sha if p.startswith("topics/") and p.endswith((".tex", ".pdf"))]
    assert len(topics) >= 12
    for p in topics:
        assert TOPIC.fullmatch(p), "Nonstandard topic file: " + p
        other = p[:-4] + (".pdf" if p.endswith(".tex") else ".tex")
        assert other in sha, "Missing topic partner: " + p
    proofs = [p for p in sha if p.startswith("derivative/reviewed/") and p.endswith(".tex")]
    assert len(proofs) == 13
    assert all(SOLUTION.fullmatch(p) for p in proofs)
    print("PASS:", len(mapping), "SHA-preserving mappings;", len(exam), "exam PDFs;", len(topics)//2, "topic pairs;", len(proofs), "solution TeX")

if __name__ == "__main__":
    main()
