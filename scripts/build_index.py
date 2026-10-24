#!/usr/bin/env python3
"""Generate filename-based indexes without redistributing large upstream PDFs."""
from __future__ import annotations
import csv
import datetime as dt
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
OUTPUT = ROOT / "index"
OUTPUT.mkdir(exist_ok=True)
VALID = {".tex",".md",".markdown",".pdf",".sty",".cls",".yaml",".yml",".zip"}
DERIV = re.compile(r"导数|求导|微分|隐零点|双零点|极值|单调|恒成立|derivati|calculus", re.I)
GAOKAO = re.compile(r"高考|Gaokao|新高考|全国卷|北京卷|上海卷|江苏卷|\b(?:19\d{2}|20\d{2})\b", re.I)
COLUMNS = ["source_id","original_path","extension","derivative_filename_hit","gaokao_filename_hit","review_status","upstream_commit","url"]

def git(path, *args):
    return subprocess.check_output(["git","-C",str(path),*args], stderr=subprocess.PIPE).decode("utf-8","replace")

def save_csv(filename, data):
    with (OUTPUT / filename).open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(data)

def main():
    all_rows, derivative, exams, totals = [], [], [], []
    for src in MANIFEST["repositories"]:
        folder = ROOT / "upstream" / src["id"]
        if not (folder / ".git").exists():
            raise SystemExit("Submodule not initialized: " + str(folder))
        sha = git(folder,"rev-parse","HEAD").strip()
        counts = Counter()
        d_count = e_count = 0
        for name in git(folder,"ls-files","-z").split("\0"):
            if not name:
                continue
            extension = Path(name).suffix.lower()
            if extension not in VALID:
                continue
            counts[extension] += 1
            is_deriv = bool(DERIV.search(name))
            is_exam = bool(GAOKAO.search(name))
            row = {
                "source_id":src["id"],
                "original_path":name,
                "extension":extension,
                "derivative_filename_hit":int(is_deriv),
                "gaokao_filename_hit":int(is_exam),
                "review_status":"unreviewed",
                "upstream_commit":sha,
                "url":"https://github.com/" + src["repo"] + "/blob/" + sha + "/" + quote(name,safe="/"),
            }
            all_rows.append(row)
            if is_deriv:
                derivative.append(row)
                d_count += 1
            if is_exam:
                exams.append(row)
                e_count += 1
        totals.append((src, sha, counts, d_count, e_count))
    for rows in (all_rows,derivative,exams):
        rows.sort(key=lambda x:(x["source_id"],x["original_path"]))
    save_csv("files.csv",all_rows)
    save_csv("derivative-candidates.csv",derivative)
    save_csv("gaokao-candidates.csv",exams)
    lines = [
        "# 上游资源文件索引", "",
        "> 于 " + dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d") + " UTC 自动生成；候选仅匹配文件名。", "",
        "本项目不对原试卷、第三方题解和插图重新授权。", "",
        "| 上游仓库 | 类别 | TeX | Markdown | PDF | ZIP | 导数候选 | 高考候选 | 许可核查 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for src,sha,counts,d_count,e_count in totals:
        project = src["repo"]
        lines.append(
            f"| [{project}](https://github.com/{project}/tree/{sha}) | {src['category']} | "
            f"{counts['.tex']} | {counts['.md']+counts['.markdown']} | {counts['.pdf']} | "
            f"{counts['.zip']} | {d_count} | {e_count} | {src['license_status']} |"
        )
    lines.extend([
        "", f"共索引 **{len(all_rows)}** 个文件；导数候选 **{len(derivative)}** 项；高考候选 **{len(exams)}** 项。",
        "", "- [完整文件清单](files.csv)", "- [导数候选](derivative-candidates.csv)",
        "- [高考候选](gaokao-candidates.csv)", "",
        "**限制：**仅按文件名初筛；完整试卷内的导数大题经常无法由文件名匹配，仍需后续逐题整理与数学复核。", ""
    ])
    (OUTPUT / "INDEX.md").write_text("\n".join(lines),encoding="utf-8")
    print("indexed",len(all_rows),"derivative",len(derivative),"gaokao",len(exams))

if __name__ == "__main__":
    main()
