#!/usr/bin/env python3
"""Validate canonical and annual derivative question indexes without network access.

This checks data consistency and provenance shape, not mathematics, copyright,
or the exact text at upstream source lines.
"""
from __future__ import annotations
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index"
COLUMNS = (
    "id", "year", "paper", "problem_number", "type", "topic", "stage",
    "source_id", "source_path", "source_line", "upstream_commit", "source_url",
    "duplicate_group",
)
PARTS = ["2010-2014", "2015-2019", "2020-2026"]
STAGES = {"source-identified", "math-checked"}
KINDS = {"core", "application", "needs-review"}

def load_json(name):
    value = json.loads((INDEX / name).read_text(encoding="utf-8"))
    assert isinstance(value.get("entries"), list), name
    assert value.get("count") == len(value["entries"]), name + ": count mismatch"
    return value["entries"]

def load_csv(name):
    with (INDEX / name).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        assert tuple(reader.fieldnames or ()) == COLUMNS, name + ": columns mismatch"
        return list(reader)

def main():
    all_entries = load_json("derivative-problems-2010-2026.json")
    assert all_entries, "Empty canonical index"
    by_id = {}
    duplicate_groups = defaultdict(list)
    for record in all_entries:
        uid = record["id"]
        assert uid not in by_id, "Duplicate ID: " + uid
        by_id[uid] = record
        assert record["type"] in KINDS, uid
        assert record["stage"] in STAGES, uid
        assert isinstance(record["year"], int) and 1952 <= record["year"] <= 2100, uid
        assert isinstance(record["problem_number"], int) and record["problem_number"] > 0, uid
        assert isinstance(record["source_line"], int) and record["source_line"] > 0, uid
        assert record["source_path"].startswith("content/" + str(record["year"]) + "/"), uid
        assert len(record["upstream_commit"]) == 40, uid
        assert ("/blob/" + record["upstream_commit"] + "/" + record["source_path"]
                + "#L" + str(record["source_line"])) in record["source_url"], uid
        if record.get("duplicate_group"):
            duplicate_groups[record["duplicate_group"]].append(uid)
    for group, members in duplicate_groups.items():
        assert len(members) >= 2, "Unpaired duplicate group: " + group

    slices = []
    for part in PARTS:
        entries = load_json("derivative-problems-" + part + ".json")
        for entry in entries:
            key = entry["id"]
            assert key in by_id, "Missing canonical ID: " + key
            assert all(entry.get(k, "") == by_id[key].get(k, "") for k in COLUMNS), (
                "Mismatch with canonical record: " + key
            )
        slices.extend(entries)
    assert len(slices) == len(all_entries), "Partition total mismatch"
    assert {item["id"] for item in slices} == set(by_id), "Partition IDs mismatch"

    for part in ["2010-2026", *PARTS]:
        expected = all_entries if part == "2010-2026" else load_json(
            "derivative-problems-" + part + ".json"
        )
        csv_entries = load_csv("derivative-problems-" + part + ".csv")
        assert len(csv_entries) == len(expected), part + ": CSV length mismatch"
        for obj, row in zip(expected, csv_entries):
            assert all(str(obj.get(k, "")) == row[k] for k in COLUMNS), (
                part + ": CSV/JSON mismatch for " + obj["id"]
            )
    count = Counter(str(r["year"]) for r in all_entries)
    passed = sum(r["stage"] == "math-checked" for r in all_entries)
    print("PASS:", len(all_entries), "unique IDs,", passed, "math-checked,",
          len(duplicate_groups), "suspected duplicate/variant groups")
    print("By year:", dict(sorted(count.items())))

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, AssertionError) as exc:
        print("VALIDATION ERROR:", exc, file=sys.stderr)
        raise SystemExit(1)
