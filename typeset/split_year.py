#!/usr/bin/env python3
"""Split only on exact PDF chapter bookmarks, never via OCR."""
import argparse,json,re
from pathlib import Path
from pypdf import PdfReader,PdfWriter
p=argparse.ArgumentParser()
for name in ("year","root","annual","entry","dest","report"):
    p.add_argument("--"+name,required=True)
a=p.parse_args()
root=Path(a.root)
index=(root/"index"/(a.year+".tex")).read_text(encoding="utf-8")
names=[n for y,n in re.findall(r"\\input\{(?:\./)?content/(\d{4})/([^{}]+\.tex)\}",index) if y==a.year]
reader=PdfReader(a.annual)
chapters=[x for x in reader.outline if not isinstance(x,list)]
starts=[reader.get_destination_page_number(x) for x in chapters]
if len(names)!=len(chapters) or not starts or starts[0]!=0 or any(i>=j for i,j in zip(starts,starts[1:])):
    raise ValueError("PDF bookmarks do not match original source chapters")
bounds=starts+[len(reader.pages)]
if any(i>=j for i,j in zip(bounds,bounds[1:])): raise ValueError("Missing PDF chapter pages")
wrapper=Path(a.entry).read_text(encoding="utf-8")
original=r"\input{index/"+a.year+".tex}"
if wrapper.count(original)!=1: raise ValueError("Source wrapper entrypoint differs")
dest=Path(a.dest);dest.mkdir(parents=True,exist_ok=True)
rows=[]
for n,ch,i,j in zip(names,chapters,bounds,bounds[1:]):
    name="ruoshui-gaokao-"+a.year+"-"+Path(n).stem
    if not re.fullmatch(r"[a-zA-Z0-9_-]+",name): raise ValueError("Unsafe paper name")
    pdf=dest/(name+".pdf")
    writer=PdfWriter()
    for k in range(i,j):writer.add_page(reader.pages[k])
    writer.add_metadata({"/Title":str(ch.title)})
    with pdf.open("wb") as out:writer.write(out)
    if len(PdfReader(str(pdf)).pages)!=j-i: raise ValueError("PDF page loss")
    (dest/(name+".tex")).write_text(wrapper.replace(original,r"\input{content/"+a.year+"/"+n+"}"),encoding="utf-8")
    rows.append({"source":"content/"+a.year+"/"+n,"title":str(ch.title),
        "pdf":pdf.as_posix().split("project/",1)[-1],
        "pages":j-i,"annual_page_range":[i+1,j],
        "published_original_pdf_match":"pending"})
meta=Path(a.report)
record=json.loads(meta.read_text(encoding="utf-8"))
record.update({"individual_papers":len(rows),"all_annual_pages_accounted_for":True,"papers":rows})
meta.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("PASS:",len(rows),"independent PDFs;",len(reader.pages),"annual pages")
