#!/usr/bin/env python3
"""Lossless deduplication: curate navigational aliases; NEVER modify mirror/."""
from __future__ import annotations
import argparse
import csv
import difflib
import hashlib
import itertools
import json
import re
import subprocess
import unicodedata
import zlib
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DOC = {".tex",".md",".markdown",".yaml",".yml",".pdf",".doc",".docx",".zip"}
TEXT = {".tex",".md",".markdown",".yaml",".yml"}
IMAGES = {".png",".jpg",".jpeg",".svg",".ico",".gif",".webp"}
YEAR = re.compile(r"(?<!\d)(19[5-9]\d|20[0-2]\d)(?!\d)")
TOPICS = {
    "calculus": ("导数","求导","微分","切线","极值","derivative"),
    "functions": ("函数","function"),
    "geometry": ("几何","圆锥","椭圆","抛物","双曲","空间向量"),
    "sequences": ("数列","等差","等比","sequence"),
    "probability": ("概率","统计","随机变量"),
    "trigonometry": ("三角","解三角形"),
    "inequalities": ("不等式","inequality"),
}

def git(*args):
    return subprocess.check_output(["git","-C",str(ROOT),*args],stderr=subprocess.PIPE)

def year_of(path):
    found = YEAR.search(path)
    return found.group(1) if found else ""

def kind_of(path, ext):
    parts = path.lower().split("/")
    if ext in IMAGES or any(p in {"img","img_repaint","images","image","figure","figures"} for p in parts):
        return "asset"
    if parts[-1] in {"readme.md","license.md","changelog.md"} or parts[-1].endswith(".gitkeep"):
        return "metadata"
    return "document" if ext in DOC else "support"

def normalize(raw, ext):
    try: s = raw.decode("utf-8-sig")
    except UnicodeError: return ""
    if ext == ".tex":
        mark = r"\begin{document}"
        if mark in s:
            s = s.split(mark,1)[1].split(r"\end{document}",1)[0]
        s = re.sub(r"(?m)^[ \t]*%[^\n]*$", "", s)
        s = re.sub(r"\\(?:left|right|displaystyle|textstyle|quad|qquad)\b","",s)
    return re.sub(r"\s+","",unicodedata.normalize("NFKC",s).casefold())

def shingles(body):
    if len(body) > 30000: body = body[:24000]+body[-6000:]
    return {zlib.crc32(body[i:i+11].encode("utf-8")) for i in range(0,max(0,len(body)-10),4)}

def filename_key(path):
    s = YEAR.sub("",Path(path).stem.casefold())
    s = re.sub(r"(真题|高考|数学|试卷|原卷|答案|扫描|word|docx)","",s)
    return re.sub(r"[^\w\u4e00-\u9fff]","",s)

def topics_for(path):
    s = "/".join(path.split("/")[2:]).casefold()
    return [key for key,words in TOPICS.items() if any(w.casefold() in s for w in words)]

def index_file(path, sub=False):
    return ("../../" if sub else "../")+quote(path,safe="/")

def dump_csv(path, fields, data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8-sig",newline="") as out:
        writer=csv.DictWriter(out,fieldnames=fields,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)

def inventory(ref):
    raw=git("ls-tree","-l","-r","-z",ref,"--","mirror/")
    items=[]
    for entry in raw.split(b"\0"):
        if not entry: continue
        meta,name=entry.split(b"\t",1)
        mode,typ,sha,size=meta.decode("ascii").split()
        path=name.decode("utf-8","surrogateescape")
        if typ!="blob" or len(path.split("/"))<3: continue
        ext=Path(path).suffix.lower()
        items.append({"path":path,"sha":sha,"mode":mode,"size":int(size),
                      "ext":ext,"source":path.split("/")[1],"year":year_of(path),
                      "kind":kind_of(path,ext)})
    return sorted(items,key=lambda x:x["path"])

def curate(ref,output,limit=1200):
    sources=json.loads((ROOT/"sources.json").read_text(encoding="utf-8"))["repositories"]
    source_ids={s["id"] for s in sources}
    if len(source_ids)!=11: raise RuntimeError("Expected exactly 11 source ids")
    items=inventory(ref)
    if not items or any(x["source"] not in source_ids for x in items):
        raise RuntimeError("Invalid source paths")
    groups=defaultdict(list)
    for r in items: groups[r["sha"]].append(r)
    representatives={sha:min(g,key=lambda r:(r["kind"]!="document",len(r["path"]),r["path"]))
                     for sha,g in groups.items()}
    docs=[r for r in representatives.values() if r["kind"]=="document"]
    text_by_sha={}
    norm_groups=defaultdict(list)
    for r in docs:
        if r["ext"] not in TEXT or r["size"]<400 or r["size"]>1500000: continue
        body=normalize(git("cat-file","blob",r["sha"]),r["ext"])
        if len(body)<400: continue
        text_by_sha[r["sha"]]=body
        norm_groups[hashlib.sha256(body.encode("utf-8")).hexdigest()].append(r)
    redirects={sha:sha for sha in representatives}
    normalized_group_count=0
    for g in norm_groups.values():
        if len(g)<2: continue
        normalized_group_count+=1
        g.sort(key=lambda x:(len(x["path"]),x["path"]))
        for item in g[1:]: redirects[item["sha"]]=g[0]["sha"]
    def canonical(r):
        return representatives[redirects[r["sha"]]]
    aliases=[]
    for r in items:
        leader=canonical(r)
        if leader["path"]!=r["path"]:
            aliases.append({"original_path":r["path"],"canonical_path":leader["path"],
                            "reason":"same_git_blob" if r["sha"]==leader["sha"] else "normalized_body_equal_assets_unverified",
                            "blob_sha":r["sha"],"source":r["source"]})
    unique_docs=sorted((r for r in docs if canonical(r)["path"]==r["path"]),
                       key=lambda r:(r["year"] or "9999",r["source"],r["path"]))
    doc_rows=[{"year":r["year"],"source":r["source"],"format":r["ext"],
               "title":Path(r["path"]).stem,"canonical_path":r["path"],
               "sha":r["sha"],"topic_hints":";".join(topics_for(r["path"])),
               "review_status":"unreviewed"} for r in unique_docs]

    years=defaultdict(list)
    topics=defaultdict(list)
    for r in unique_docs:
        if r["year"]: years[r["year"]].append(r)
        for t in topics_for(r["path"]): topics[t].append(r)
    same_year=defaultdict(list)
    for r in unique_docs:
        if r["year"] and r["sha"] in text_by_sha: same_year[r["year"]].append(r)
    sim=[]
    for year, candidates in sorted(same_year.items()):
        sh={r["sha"]:shingles(text_by_sha[r["sha"]]) for r in candidates}
        for a,b in itertools.combinations(candidates,2):
            x,y=text_by_sha[a["sha"]],text_by_sha[b["sha"]]
            if min(len(x),len(y))/max(len(x),len(y))<.58: continue
            sa,sb=sh[a["sha"]],sh[b["sha"]]
            if min(len(sa),len(sb))<50: continue
            ratio=len(sa&sb)/len(sa|sb)
            if ratio>=.72:
                sim.append({"year":year,"path_a":a["path"],"path_b":b["path"],
                            "jaccard_score":f"{ratio:.4f}","status":"review_only_not_merged"})
    sim.sort(key=lambda x:(-float(x["jaccard_score"]),x["year"],x["path_a"],x["path_b"]))
    sim_total=len(sim)
    sim=sim[:limit]
    binary_year=defaultdict(list)
    for r in unique_docs:
        if r["year"] and r["ext"] in {".pdf",".doc",".docx"} and len(filename_key(r["path"]))>=5:
            binary_year[(r["year"],r["ext"])].append(r)
    names=[]
    for (year,ext),candidate in sorted(binary_year.items()):
        for a,b in itertools.combinations(candidate,2):
            ak,bk=filename_key(a["path"]),filename_key(b["path"])
            if ak==bk or (len(ak)>=7 and len(bk)>=7 and
                          difflib.SequenceMatcher(None,ak,bk).ratio()>=.92):
                names.append({"year":year,"format":ext,"path_a":a["path"],
                              "path_b":b["path"],"status":"filename_only_not_merged"})
    names.sort(key=lambda x:(x["year"],x["path_a"],x["path_b"]))
    output.mkdir(parents=True,exist_ok=True)
    dump_csv(output/"documents.csv",
             ["year","source","format","title","canonical_path","sha","topic_hints","review_status"],doc_rows)
    dump_csv(output/"aliases.csv",
             ["original_path","canonical_path","reason","blob_sha","source"],aliases)
    dump_csv(output/"similar_review.csv",
             ["year","path_a","path_b","jaccard_score","status"],sim)
    dump_csv(output/"filename_review.csv",
             ["year","format","path_a","path_b","status"],names)
    for year, group in sorted(years.items()):
        lines=[f"# {year} 年试卷与数学资料","",
               "按原始内容去重的导航；不是数学正确性审核。",""]
        for r in sorted(group,key=lambda x:(x["source"],x["path"])):
            lines.append(f"- [{Path(r['path']).name}]({index_file(r['path'],True)}) · {r['source']} · {r['ext']}")
        (output/"years").mkdir(exist_ok=True)
        (output/"years"/(year+".md")).write_text("\n".join(lines)+"\n",encoding="utf-8")
    for topic,group in sorted(topics.items()):
        lines=[f"# {topic} 专题（文件名线索）","",
               "仅文件名和路径初筛，未确认试卷内的具体题目。",""]
        for r in sorted(group,key=lambda x:(x["year"],x["path"])):
            lines.append(f"- [{Path(r['path']).name}]({index_file(r['path'],True)}) · {r['year'] or '未知年份'} · {r['source']}")
        (output/"topics").mkdir(exist_ok=True)
        (output/"topics"/(topic+".md")).write_text("\n".join(lines)+"\n",encoding="utf-8")
    repeat=[g for g in groups.values() if len(g)>1]
    stats={"source_count":len(source_ids),"original_files":len(items),
           "unique_git_blobs":len(groups),"exact_duplicate_copies":len(items)-len(groups),
           "exact_duplicate_groups":len(repeat),
           "duplicate_bytes":sum((len(g)-1)*g[0]["size"] for g in repeat),
           "normalized_body_groups":normalized_group_count,
           "normalized_body_extra_aliases":sum(k!=v for k,v in redirects.items()),
           "all_aliases":len(aliases),"unique_curated_documents":len(unique_docs),
           "similar_text_pairs_to_review":sim_total,"similar_pairs_listed":len(sim),
           "filename_pairs_to_review":len(names),"year_pages":len(years),
           "topic_pages":len(topics)}
    (output/"stats.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=["# 高考数学 · 去重后的统一资料目录","",
           "从这里浏览题库。11 个上游仓库的原始文件全部保留在 mirror 目录，不删除、不覆盖。","",
           f"**{len(items):,} 个原始文件；{len(groups):,} 个不同 Git 内容；完全重复副本 {len(items)-len(groups):,} 个。**",
           f"正文规范化一致的额外文件别名 {stats['normalized_body_extra_aliases']} 个，正文相同不代表图片相同。","",
           f"[**去重后文件列表：{len(unique_docs):,} 份资料**](documents.csv) · "
           "[重复路径与来源对应表](aliases.csv) · [自动统计](stats.json)","",
           "## 按年份浏览",""]
    sorted_years=sorted(years,reverse=True)
    for i in range(0,len(sorted_years),10):
        lines.append(" · ".join(f"[{y}](years/{y}.md)" for y in sorted_years[i:i+10]))
        lines.append("")
    lines.extend(["## 按专题浏览（仅文件名提示）",""])
    for t in sorted(topics):
        lines.append(f"- [{t}](topics/{t}.md)：{len(topics[t])} 份")
    lines.extend(["","## 相似内容等待人工复核","",
                  f"- [正文相似：{sim_total} 对候选](similar_review.csv)（展示前 {len(sim)} 对）",
                  f"- [PDF/DOC 文件名相似：{len(names)} 对候选](filename_review.csv)",
                  "- [现有导数题逐题重复核查](../index/DUPLICATE_AUDIT.md)","",
                  "## 原则","",
                  "相同 SHA 自动折叠为同一导航入口；规范化后正文相同则折叠文本导航并记录原件出处。",
                  "内容高度相似只进入复核清单，不擅自认定同题，更不删除答案、图片或源仓库。",
                  "保留全部来源和许可证信息，程序在 GitHub Actions 定期重建。",""])
    (output/"README.md").write_text("\n".join(lines),encoding="utf-8")
    return stats

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--ref",default="HEAD")
    parser.add_argument("--output",type=Path,default=ROOT/"catalog")
    a=parser.parse_args()
    print(json.dumps(curate(a.ref,a.output),ensure_ascii=False,indent=2))
