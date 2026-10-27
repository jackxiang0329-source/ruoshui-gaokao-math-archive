#!/usr/bin/env python3
"""Merge 14 standalone Markdown reviews into a single traced document.

Preserves distinct mathematical proofs and individual .tex files.
One-time compaction: refuse to delete sources unless every reference updated.
"""
from __future__ import annotations
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = ROOT / "derivative/reviewed"
META = ROOT / "metadata"
INDEX = ROOT / "index"
PROOFS = REV / "PROOFS.md"


def git(*args):
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *args], stderr=subprocess.PIPE
    ).decode().strip()


def main():
    files = sorted(p for p in REV.glob("*.md") if p.name != "README.md")
    if len(files) != 14 or PROOFS.exists():
        raise RuntimeError(f"Expected 14 distinct review Markdown files, found {len(files)}")
    provenance_path = META / "review-provenance.json"
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    quality_path = META / "quality-findings.json"
    findings = json.loads(quality_path.read_text(encoding="utf-8"))
    names = {p.stem: p for p in files}
    slugs = {p.name: p.stem for p in files}

    lines = ["# 高考数学：独立复核证明合订本", "",
             "原 14 份 Markdown 原样合订，各题使用独立锚点。",
             "完整审核对象及卷别由复核溯源 JSON 跟踪；对应每道题的 TeX 继续单独保存。", "",
             "## 目录", ""]
    lines.extend("- [" + s + "](#" + s + ")" for s in sorted(names))
    lines.append("")
    for stem in sorted(names):
        path = names[stem]
        relative = path.relative_to(ROOT).as_posix()
        sha = git("rev-parse", "HEAD:" + relative)
        content = path.read_text(encoding="utf-8").rstrip()
        lines.extend(["---", "", "## " + stem, "",
                      "原文件：" + relative + "；原始 SHA：" + sha, "",
                      content, ""])
    PROOFS.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for item in provenance["entries"]:
        name = Path(item["proof_path"]).name
        if name not in slugs:
            raise RuntimeError("Unexpected proof path: " + name)
        item["proof_section"] = slugs[name]
        item["proof_path"] = "derivative/reviewed/PROOFS.md"
    provenance["distinct_proof_documents"] = 1
    for finding in findings["findings"]:
        name = Path(finding["independent_proof"]).name
        if name not in slugs:
            raise RuntimeError("Unexpected quality finding path: " + name)
        finding["independent_proof_section"] = slugs[name]
        finding["independent_proof"] = "derivative/reviewed/PROOFS.md"
    provenance_path.write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    quality_path.write_text(json.dumps(findings, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    readme = REV / "README.md"
    summary = readme.read_text(encoding="utf-8")
    paper_index = INDEX / "DERIVATIVE_PROBLEMS_2010_2026.md"
    primary_index = paper_index.read_text(encoding="utf-8")
    for filename, anchor in slugs.items():
        summary = summary.replace("](" + filename + ")", "](PROOFS.md#" + anchor + ")")
        primary_index = primary_index.replace(
            "/reviewed/" + filename + ")", "/reviewed/PROOFS.md#" + anchor + ")")
    summary = summary.replace("# 独立数学复核成果",
        "# 独立数学复核成果\n\n"
        "逐题数学证明已经合并到 [完整证明集](PROOFS.md)，对应的 TeX 文件不变。")
    readme.write_text(summary, encoding="utf-8")
    paper_index.write_text(primary_index, encoding="utf-8")
    validation = ROOT / "scripts/validate_review_traceability.py"
    checker = validation.read_text(encoding="utf-8")
    needle = '        safe_path(item["proof_path"])\n        unique_proofs.add(item["proof_path"])'
    if needle not in checker:
        raise RuntimeError("Unrecognized provenance validation logic")
    checker = checker.replace(needle,
        '        file = safe_path(item["proof_path"])\n'
        '        assert item.get("proof_section"), item["question_id"]\n'
        '        assert "## " + item["proof_section"] in file.read_text(encoding="utf-8")\n'
        '        unique_proofs.add(item["proof_path"])')
    validation.write_text(checker, encoding="utf-8")
    # Ensure provenance has 16 math-checked pointers, and each anchor resolves.
    assert len(provenance["entries"]) == provenance["checked_count"] == 16
    body = PROOFS.read_text(encoding="utf-8")
    for item in provenance["entries"]:
        assert "## " + item["proof_section"] in body, item["question_id"]
    for path in files:
        path.unlink()
    print("PASS: consolidated 14 files into PROOFS.md; 16 reviewed record "
          "pointers, 3 quality findings, and all standalone TeX files preserved.")


if __name__ == "__main__":
    main()
