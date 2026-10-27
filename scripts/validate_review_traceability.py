#!/usr/bin/env python3
"""Verify math-review provenance, duplicate audit, and confirmed quality findings.

This is a consistency gate. It cannot certify the mathematical truth of proofs,
the copyright status of source material, or a successful TeX compilation.
"""
from __future__ import annotations
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def safe_path(path: str) -> Path:
    item = Path(path)
    assert not item.is_absolute() and ".." not in item.parts, f"unsafe file: {path}"
    resolved = ROOT / item
    assert resolved.is_file(), f"missing referenced proof: {path}"
    return resolved

def main() -> None:
    index = load("index/derivative-problems-2010-2026.json")
    records = {e["id"]: e for e in index["entries"]}
    assert len(records) == index["count"], "duplicate or missing source IDs"
    reviewed = {k for k, v in records.items() if v["stage"] == "math-checked"}

    refs = load("metadata/review-provenance.json")
    proof_entries = refs["entries"]
    ids = [e["question_id"] for e in proof_entries]
    assert len(ids) == len(set(ids)), "duplicate math review pointers"
    assert set(ids) == reviewed, "math-checked / proof provenance mismatch"
    assert refs["checked_count"] == len(reviewed), "review count mismatch"
    unique_proofs = set()
    for item in proof_entries:
        record = records[item["question_id"]]
        assert item["review_status"] == "math-checked", item["question_id"]
        assert item["source_url"] == record["source_url"], item["question_id"]
        assert item["proof_path"].endswith(".md"), item["question_id"]
        file = safe_path(item["proof_path"])
        assert item.get("proof_section"), item["question_id"]
        assert "## " + item["proof_section"] in file.read_text(encoding="utf-8")
        unique_proofs.add(item["proof_path"])
    assert refs["distinct_proof_documents"] == len(unique_proofs), "proof count mismatch"

    grouped = defaultdict(list)
    for entry in records.values():
        if entry.get("duplicate_group"):
            grouped[entry["duplicate_group"]].append(entry)
    audit = load("index/duplicate-audit.json")
    names = [g["duplicate_group"] for g in audit["groups"]]
    assert len(names) == len(set(names)), "duplicate audit group IDs"
    assert set(names) == set(grouped), "duplicate audit / canonical group mismatch"
    allowed = {"confirmed_same_problem", "confirmed_variant", "unverified"}
    for group in audit["groups"]:
        key = group["duplicate_group"]
        assert group["status"] in allowed, key
        expected = {p["id"]: p["source_url"] for p in grouped[key]}
        member_ids = group["member_ids"]
        assert len(member_ids) == group["n_records"], key
        assert len(member_ids) == len(set(member_ids)), key
        assert set(member_ids) == set(expected), key
        assert group["source_urls"] == [expected[x] for x in member_ids], key
    counts = {
        kind: sum(g["status"] == kind for g in audit["groups"])
        for kind in allowed
    }
    summary = audit["summary"]
    assert summary["groups"] == len(grouped)
    assert summary["grouped_source_records"] == sum(map(len, grouped.values()))
    for kind in allowed:
        assert summary[kind] == counts[kind], "duplicate audit summary mismatch"

    findings = load("metadata/quality-findings.json")["findings"]
    for issue in findings:
        src_id = issue["affected_record_id"]
        assert src_id in records, f"unknown quality finding source {src_id}"
        assert issue["source_url"] == records[src_id]["source_url"], src_id
        if issue.get("other_related_record_id"):
            other = issue["other_related_record_id"]
            assert other in records, f"unknown related record {other}"
            assert issue["related_source_url"] == records[other]["source_url"]
        safe_path(issue["independent_proof"])

    print(f"PASS: {len(records)} indexed questions, {len(reviewed)} mathematical "
          f"review pointers, {len(grouped)} duplicate groups, "
          f"{len(findings)} documented source findings.")

if __name__ == "__main__":
    try:
        main()
    except (OSError, KeyError, ValueError, AssertionError) as exc:
        print(f"REVIEW VALIDATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
