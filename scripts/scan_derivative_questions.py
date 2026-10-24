#!/usr/bin/env python3
"""Index machine candidates from Gaokao TeX question bodies only.

This is a *locator*, not a math checker. It may have false positives or misses.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

EVENT = re.compile(r"\\section\{([^}]+)\}|\\begin\{problem\}|\\end\{problem\}")
SOL_START = re.compile(r"\\begin\{(?:solution|answer|analysis)\}")
FUNCTION = re.compile(r"函数|导函数|导数|[fg]\s*\(\s*[xt]\s*\)")
STRONG = re.compile(r"导数|导函数|求导|可导|切线|极值|极小值|极大值|[fg]\s*'\s*\(|\\prime")
WEAK = re.compile(r"单调|恒成立|零点|不等式|最值|最大值|最小值")
TRANS = re.compile(r"\\ln\b|\\log\b|\\e\^|e\^|\\exp\b")
TRIG = re.compile(r"\\sin|\\cos|\\tan")
PERIOD = re.compile(r"最小正周期|周期")
COLUMNS = [
    "id", "year", "paper", "question", "signals", "confidence", "status",
    "text_hash", "path", "line", "commit", "url"
]

def scan_file(text: str, path: str, sha: str) -> list[dict]:
    parts = Path(path).parts
    if len(parts) != 3 or parts[0] != "content":
        raise ValueError("Expected content/<year>/<paper>.tex: " + path)
    year, paper = parts[1], Path(path).stem
    section = ""
    start = None
    offset = None
    q = 0
    records = []
    for match in EVENT.finditer(text):
        token = match.group()
        if match.group(1) is not None and start is None:
            section = match.group(1).strip()
        elif token == r"\begin{problem}":
            if start is not None:
                # A malformed nested problem is not a trustworthy extraction.
                start = None
                offset = None
            else:
                start, offset = match.end(), match.start()
        elif token == r"\end{problem}" and start is not None:
            q += 1
            body = text[start:match.start()]
            start = None
            if "解答题" not in section or "选考" in section:
                continue
            # Some upstream TeX files place the solution inside the problem.
            # NEVER classify using solution/analysis text; it can leak cues.
            body = SOL_START.split(body, maxsplit=1)[0]
            body = re.sub(r"(?m)^\s*%.*$", "", body)
            body = re.sub(r"\s+", " ", body)
            if not FUNCTION.search(body):
                continue
            signals = []
            if STRONG.search(body):
                signals.append("derivative")
            if WEAK.search(body):
                signals.append("function-analysis")
            if TRANS.search(body):
                signals.append("transcendental")
            if (PERIOD.search(body) and TRIG.search(body)
                    and "derivative" not in signals):
                continue  # Ordinary trigonometric-period question.
            if "derivative" not in signals and len(signals) < 2:
                continue
            line = text.count("\n", 0, offset) + 1
            url = ("https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/"
                   + sha + "/" + quote(path, safe="/") + "#L" + str(line))
            records.append({
                "id": f"{year}-{paper}-q{q:02d}", "year": year,
                "paper": paper, "question": q, "signals": "+".join(signals),
                "confidence": "high" if "derivative" in signals else "medium",
                "status": "machine-candidate-not-reviewed",
                "text_hash": hashlib.sha256(body.encode("utf-8")).hexdigest(),
                "path": path, "line": line, "commit": sha, "url": url,
            })
    return records

def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--source-dir", type=Path,
                     default=Path("upstream/gaokao-math-problems-compilation"))
    cli.add_argument("--output-dir", type=Path, default=Path("index"))
    cli.add_argument("--commit", default="")
    args = cli.parse_args()
    source = args.source_dir.resolve()
    if not (source / "content").is_dir():
        raise SystemExit("Missing upstream content dir: " + str(source))
    sha = args.commit or subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    files = sorted((source / "content").glob("*/*.tex"))
    rows = []
    for file in files:
        path = file.relative_to(source).as_posix()
        text = file.read_text(encoding="utf-8-sig")
        rows.extend(scan_file(text, path, sha))
    rows.sort(key=lambda r: (r["year"], r["paper"], int(r["question"])))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "derivative-machine-candidates.csv"
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    summary = [
        "# 高考试卷逐题机器候选", "",
        f"扫描 LaTeX 试卷 {len(files)} 份，产生 {len(rows)} 条机器候选。", "",
        "候选仅表示题干文字与规则匹配，**不代表数学核验或题型确认**。",
        "解析优先使用题干内容，不用解答区作分类证据。", "",
        "[候选索引 CSV](derivative-machine-candidates.csv)", "",
    ]
    (args.output_dir / "DERIVATIVE_MACHINE.md").write_text(
        "\n".join(summary), encoding="utf-8"
    )
    print(f"Scanned {len(files)} TeX papers; {len(rows)} unreviewed candidates")

if __name__ == "__main__":
    main()
