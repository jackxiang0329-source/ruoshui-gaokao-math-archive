#!/usr/bin/env python3
"""Create a portable XeLaTeX source ZIP with complete Chinese content and figures.
No font binaries are copied; use system TeX Live / Fandol fonts.
"""
import argparse,hashlib,json,zipfile
from pathlib import Path

def bundle(root,year,papers,out):
    requested=[
        root/"styles.tex",root/"statistical-charts.tex",
        root/"index"/(year+".tex"),root/("__ruoshui_"+year+".tex"),
    ]
    requested += sorted((root/"content"/year).rglob("*.tex"))
    for sub in ("img","img_repaint"):
        d=root/sub/year
        if d.is_dir(): requested += sorted(p for p in d.rglob("*") if p.is_file())
    for rel in ("tools/typeset/generated_image_layout.tex","tools/crop/manual_image_layout.tex"):
        p=root/rel
        if p.is_file(): requested.append(p)
    requested+=sorted(p for p in papers.glob("*.tex") if p.is_file())
    if not (root/"styles.tex").is_file() or not (root/"index"/(year+".tex")).is_file():
        raise ValueError("Missing build dependencies")
    if not (root/"content"/year).is_dir() or len(list(papers.glob("*.tex")))==0:
        raise ValueError("Missing Chinese body sources")
    out.parent.mkdir(parents=True,exist_ok=True)
    entries={}
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for path in requested:
            if not path.is_file(): raise ValueError("Missing required file "+str(path))
            relative=path.relative_to(root).as_posix() if path.is_relative_to(root) else "retypeset_tex/"+path.name
            data=path.read_bytes()
            entries[relative]={"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
            archive.writestr(relative,data)
        note=("RuoShui Gaokao "+year+" | complete Chinese XeLaTeX source bundle\n"
              "Start: latexmk -xelatex -interaction=nonstopmode __ruoshui_"+year+".tex\n"
              "Individual full-text TeX sources: retypeset_tex/\n"
              "Styles, original sources, and original figures are in relative paths.\n"
              "Fonts: TeX Live Fandol / TeX Gyre Termes; no proprietary fonts included.\n"
              "Source: DxAThing/Gaokao-Math-Problems-Compilation, deekur/gaokaomath.\n"
              "Keep origin attribution; third-party image/exam rights may differ.\n")
        archive.writestr("README-SOURCE.txt",note)
        archive.writestr("MANIFEST.json",json.dumps(entries,ensure_ascii=False,indent=2)+"\n")
    print("Bundled",len(entries),"items:",out,out.stat().st_size,"bytes")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--year",required=True)
    p.add_argument("--papers",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    bundle(a.root,a.year,a.papers,a.out)
