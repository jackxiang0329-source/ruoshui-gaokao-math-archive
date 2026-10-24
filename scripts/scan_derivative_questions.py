#!/usr/bin/env python3
"""Index possible derivative solution questions from the upstream Gaokao TeX sources.

This indexes locations only. False positives, false negatives, and math errors remain possible.
"""
import argparse
import csv
import hashlib
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

EVENT = re.compile(r"\\section\{([^}]+)\}|\\begin\{problem\}|\\end\{problem\}")
FUNCTION = re.compile(r"函数|曲线|[fg]\s*\(\s*[xt]\s*\)")
STRONG = re.compile(r"导数|求导|可导|切线|极值|极小值|极大值|[fg]\s*'\s*\(|\\prime")
WEAK = re.compile(r"单调|恒成立|零点|不等式|最值|最大值|最小值")
TRANS = re.compile(r"\\ln\b|\\log\b|\\e\^|e\^|\\exp\b")
COLS = ["id","year","paper","question","signals","confidence","status",
        "text_hash","path","line","commit","url"]

def scan_file(text, path, sha):
    year=Path(path).parts[1]
    paper=Path(path).stem
    section=""
    start=None
    q=0
    records=[]
    for match in EVENT.finditer(text):
        token=match.group()
        if match.group(1) is not None and start is None:
            section=match.group(1)
        elif token==r"\begin{problem}":
            start=match.end()
            start_offset=match.start()
        elif token==r"\end{problem}" and start is not None:
            q+=1
            body=re.sub(r"\s+"," ",text[start:match.start()])
            start=None
            if "解答题" not in section or not FUNCTION.search(body):
                continue
            signals=[]
            if STRONG.search(body):
                signals.append("derivative")
            if WEAK.search(body):
                signals.append("function-analysis")
            if TRANS.search(body):
                signals.append("transcendental")
            if "derivative" not in signals and len(signals)<2:
                continue
            line=text.count("\n",0,start_offset)+1
            url=("https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/"
                 +sha+"/"+quote(path,safe="/")+"#L"+str(line))
            records.append(dict(
                id=f"{year}-{paper}-q{q:02d}",year=year,paper=paper,
                question=q,signals="+".join(signals),
                confidence="high" if "derivative" in signals else "medium",
                status="machine-candidate-not-reviewed",
                text_hash=hashlib.sha256(body.encode("utf-8")).hexdigest(),
                path=path,line=line,commit=sha,url=url))
    return records

def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--source-dir",type=Path,default=Path("upstream/gaokao-math-problems-compilation"))
    cli.add_argument("--output-dir",type=Path,default=Path("index"))
    cli.add_argument("--commit",default="")
    args=cli.parse_args()
    source=args.source_dir.resolve()
    if not (source/"content").is_dir():
        raise SystemExit("Missing submodule content dir: "+str(source))
    sha=args.commit or subprocess.check_output(
        ["git","-C",str(source),"rev-parse","HEAD"],text=True).strip()
    files=sorted((source/"content").glob("*/*.tex"))
    rows=[]
    for file in files:
        path=file.relative_to(source).as_posix()
        rows.extend(scan_file(file.read_text(encoding="utf-8-sig"),path,sha))
    rows.sort(key=lambda x:(x["year"],x["paper"],int(x["question"])))
    args.output_dir.mkdir(parents=True,exist_ok=True)
    with (args.output_dir/"derivative-machine-candidates.csv").open("w",encoding="utf-8-sig",newline="") as output:
        writer=csv.DictWriter(output,fieldnames=COLS)
        writer.writeheader()
        writer.writerows(rows)
    print("papers:",len(files),"machine candidates:",len(rows))
    (args.output_dir/"DERIVATIVE_MACHINE.md").write_text(
        "# LaTeX 逐题机器候选\n\n"
        +f"源文件 {len(files)} 份；候选 {len(rows)} 道；固定 SHA {sha}。\n\n"
        +"全部候选均未人工复核，分类和答案均不能视为正确。\n"
        +"[CSV](derivative-machine-candidates.csv)\n",encoding="utf-8")

if __name__=="__main__":
    main()
