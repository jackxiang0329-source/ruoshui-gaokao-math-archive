#!/usr/bin/env python3
"""Safely consolidate original Markdown while retaining every source Git Blob.

Only changes the compact main branch. Full source files and their exact tree
SHA survive on the full-source-archive branch.
"""
from __future__ import annotations
import csv
import io
import re
import subprocess
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
REF = "refs/remotes/origin/full-source-archive"
REPO = "jackxiang0329-source/ruoshui-gaokao-math-archive"


def git(*args, input=None):
    p = subprocess.run(["git", "-C", str(ROOT), *args], input=input,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return p.stdout


def source_md(ref):
    found = {}
    for item in git("ls-tree", "-r", "-z", ref, "--", "mirror/").split(b"\0"):
        if not item:
            continue
        header, rawpath = item.split(b"\t", 1)
        mode, typ, oid = header.decode("ascii").split()
        if typ != "blob":
            continue
        path = rawpath.decode("utf-8", "surrogateescape")
        if path.lower().endswith((".md", ".markdown")) and len(path.split("/")) > 2:
            found[path] = (mode, oid)
    return found


def blobs(oids):
    stream = io.BytesIO(git("cat-file", "--batch",
                            input=("\n".join(oids) + "\n").encode("ascii")))
    for oid in oids:
        info = stream.readline().decode("ascii").strip().split()
        if len(info) != 3 or info[0] != oid or info[1] != "blob":
            raise RuntimeError("Unexpected Git Blob response: " + repr(info))
        nbytes = int(info[2])
        data = stream.read(nbytes)
        if len(data) != nbytes or stream.read(1) != b"\n":
            raise RuntimeError("Git object corrupted: " + oid)
        yield data
    if stream.read():
        raise RuntimeError("Unexpected data remaining in Git Blob stream")


def main():
    original = source_md(REF)
    current = source_md("HEAD")
    if len(original) != 215 or current != original:
        raise RuntimeError("Guard: expected 215 identical source Markdown "
                           "paths and Blob SHA/modes on archive and main, got "
                           + str(len(original)) + " and " + str(len(current)))
    names = sorted(original)
    unique_sha = list(dict.fromkeys(original[p][1] for p in names))
    body = {}
    for oid, raw in zip(unique_sha, blobs(unique_sha)):
        body[oid] = raw.decode("utf-8")  # abort rather than replace unknown chars

    outdir = ROOT / "archive"
    outdir.mkdir(exist_ok=True)
    pages = [
        "# 上游 Markdown 原始正文合订本（215 个源文件）", "",
        "这里只合并阅读入口，不更改题干。所有原件仍可在"
        " [完整固定版本快照](https://github.com/" + REPO +
        "/tree/full-source-archive) 按原路径查看、下载和构建。", "",
        "每节标注原始文件 Git Blob SHA；原文被封装为 Markdown 代码区块，"
        "避免 YAML front matter、相对图片和其它标记跨文件冲突。", "",
        "原资料的许可状态和第三方作品权利不因合订而改变。", ""
    ]
    rows = []
    for i, path in enumerate(names, 1):
        mode, oid = original[path]
        original_text = body[oid]
        fence = chr(96) * max(6, 1 + max(
            (len(hit) for hit in re.findall(chr(96) + "+", original_text)),
            default=0))
        link = ("https://github.com/" + REPO + "/blob/full-source-archive/"
                + quote(path, safe="/"))
        pages.extend(["---", "", "## " + str(i).zfill(3) + " · " + path,
                      "", "[原始文件独立链接](" + link + ")"
                      " · SHA " + oid + " · mode " + mode, "",
                      fence + "markdown", original_text, fence, ""])
        rows.append({"original_path": path, "blob_sha": oid, "mode": mode,
                     "byte_count": len(original_text.encode("utf-8")),
                     "original_link": link})
    (outdir / "SOURCE_MARKDOWN.md").write_text(
        "\n".join(pages) + "\n", encoding="utf-8")
    with (outdir / "source-markdown-paths.csv").open(
            "w", newline="", encoding="utf-8-sig") as stream:
        w = csv.DictWriter(stream, fieldnames=[
            "original_path", "blob_sha", "mode", "byte_count", "original_link"])
        w.writeheader()
        w.writerows(rows)
    # Source snapshot + consolidated content are BOTH verified first.
    subprocess.run(["git", "-C", str(ROOT), "rm", "--cached", "--sparse",
                    "-q", "--", *names], check=True)
    print(f"Consolidated {len(names)} source Markdown files into one volume; "
          "each original SHA preserved in full-source-archive.", flush=True)


if __name__ == "__main__":
    main()
