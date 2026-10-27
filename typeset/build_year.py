#!/usr/bin/env python3
"""Prepare a source-backed yearly XeLaTeX volume (strict source/image checks)."""
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).parent
COVERAGE=json.loads((ROOT/"source-coverage.json").read_text(encoding="utf-8"))["years"]
def build(source,year,report):
    if year not in COVERAGE: raise ValueError("Unknown year "+year)
    count=COVERAGE[year]
    docs=sorted((source/"content"/year).glob("*.tex"))
    idx=source/"index"/(year+".tex")
    if not idx.is_file() or len(docs)!=count: raise ValueError("Missing source papers/index")
    names=re.findall(r"\\input\{(?:\./)?content/(\d{4})/([^{}]+\.tex)\}",idx.read_text(encoding="utf-8"))
    if len(names)!=count or any(y!=year for y,n in names) or {n for y,n in names}!={p.name for p in docs}:
        raise ValueError("Year index mismatches source")
    missing=set()
    questions=0
    for p in docs:
        text=p.read_text(encoding="utf-8")
        questions+=text.count(r"\begin{problem}")
        for name in re.findall(r"(?:img|img_repaint)/\d{4}/[^\s{}\\]+\.(?:png|jpg|jpeg|pdf|tex)",text,re.I):
            if not (source/name).is_file(): missing.add(name)
    if missing: raise ValueError("Missing embedded figures "+str(sorted(missing)[:15]))
    if questions<=0: raise ValueError("No questions detected")
    style=source/"styles.tex"
    text=style.read_text(encoding="utf-8")
    text,n=re.subn(r"\\setCJKmainfont\{SimSun\}\s*\[\s*BoldFont\s*=\s*SimHei\s*,\s*ItalicFont\s*=\s*KaiTi\s*\]",
                   lambda m:r"\setCJKmainfont{FandolSong-Regular}[BoldFont=FandolHei-Regular,ItalicFont=FandolKai-Regular]",
                   text,count=1,flags=re.S)
    if n!=1 or r"\setmainfont{Times New Roman}" not in text: raise ValueError("Upstream font preset changed")
    text=text.replace(r"\setmainfont{Times New Roman}",r"\setmainfont{TeX Gyre Termes}")
    text=text.replace(r"\setmathfont{STIX}",r"\setmathfont{TeX Gyre Termes Math}")
    text=text.replace(r"\setmathfont{Asana Math}",r"\setmathfont{TeX Gyre Termes Math}")
    style.write_text(text,encoding="utf-8")
    wrapper=r"""% RuoShui adaptation of CC BY-SA 4.0 Gaokao math compilation;
% origin DxAThing/Gaokao-Math-Problems-Compilation and deekur/gaokaomath.
\documentclass[UTF8,a4paper,oneside,11pt]{ctexbook}
\input{styles.tex}
\showanswerfalse
\tallpagefalse
\geometry{left=22mm,right=22mm,top=20mm,bottom=20mm,headheight=17pt}
\renewcommand{\baselinestretch}{1.18}
\ctexset{chapter={format=\centering\bfseries\zihao{-2},beforeskip=9pt,afterskip=14pt,pagestyle=plain},section={format=\bfseries\zihao{4},beforeskip=1em,afterskip=.5em}}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small 三千弱水 · 高考数学}
\fancyhead[R]{\small YEAR年 · 真题重排版}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{.25pt}
\begin{document}
\mainmatter
\input{index/YEAR.tex}
\end{document}
""".replace("YEAR",year)
    (source/("__ruoshui_"+year+".tex")).write_text(wrapper,encoding="utf-8")
    report.parent.mkdir(parents=True,exist_ok=True)
    report.write_text(json.dumps({"year":year,"source_papers":count,"question_environments":questions,
      "figures_present":True,"visual_review":"pending","mathematics_review":"not_certified"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(year,count,questions)
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--year",required=True)
    p.add_argument("--source",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    a=p.parse_args()
    build(a.source.resolve(),a.year,a.report)
