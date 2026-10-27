#!/usr/bin/env python3
"""Fail if a published retypeset PDF lacks selectable Chinese or source body."""
import argparse
import json
import re
import subprocess
from pathlib import Path

CJK = re.compile(r"[\u3400-\u9fff]")

def cmd(*args):
    return subprocess.run(args, check=True, capture_output=True).stdout.decode("utf-8","replace")

def verify(project,report_path):
    doc=json.loads(report_path.read_text(encoding="utf-8"))
    examined=[]
    for paper in doc["papers"]:
        pdf=project/paper["pdf"]
        tex=pdf.with_suffix(".tex")
        if not pdf.is_file() or not tex.is_file():
            raise ValueError("PDF/TeX pair absent: "+str(pdf))
        source=tex.read_text(encoding="utf-8")
        n_source=len(CJK.findall(source))
        text=cmd("pdftotext","-layout",str(pdf),"-")
        n_pdf=len(CJK.findall(text))
        if n_source<40 or not paper.get("full_chinese_tex_embedded"):
            raise ValueError("TeX source is only a wrapper or lacks Chinese: "+str(tex))
        if n_pdf<40:
            raise ValueError("PDF missing searchable Chinese text: "+str(pdf))
        fonts=cmd("pdffonts",str(pdf))
        embedded=[line for line in fonts.splitlines()[2:]
                  if ("Fandol" in line or "Noto" in line) and re.search(r"\byes\s+yes\s+(?:yes|no)\s+\d+\s+\d+\s*$",line)]
        if not embedded:
            raise ValueError("PDF lacks embedded CJK font: "+str(pdf))
        examined.append({"source":paper["source"],"pdf_chinese_chars":n_pdf,
          "tex_chinese_chars":n_source,"embedded_cjk_font":True})
    if len(examined)!=doc.get("individual_papers"):
        raise ValueError("Incomplete per-paper Chinese check")
    doc["chinese_text_QA"]="passed"
    doc["chinese_quality_checks"]=examined
    report_path.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("Passed CJK PDF and full-TeX checks:",len(examined))

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--project",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    a=p.parse_args()
    verify(a.project,a.report)
