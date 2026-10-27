#!/usr/bin/env python3
"""Fast, reproducible Git-object-only catalog. Never changes original mirrors."""
from __future__ import annotations
import csv
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "catalog"
EXT = {".pdf", ".tex", ".md", ".markdown", ".doc", ".docx", ".zip",
       ".yaml", ".yml"}
YEAR = re.compile(r"(?<!\d)(19[5-9]\d|20[0-2]\d)(?!\d)")
TOPICS = {
    "calculus": ("导数", "求导", "微分", "切线", "极值"),
    "functions": ("函数", "function"),
    "geometry": ("几何", "圆锥", "椭圆", "抛物", "双曲"),
    "sequences": ("数列", "等差", "等比"),
    "probability": ("概率", "统计", "随机变量"),
    "trigonometry": ("三角",),
    "inequalities": ("不等式",),
}

def call(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args],
                                   stderr=subprocess.PIPE)

def inventory():
    tree = call("ls-tree", "-r", "-z", "refs/remotes/origin/full-source-archive", "--", "mirror/")
    rows = []
    for entry in tree.split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        mode, typ, sha = meta.decode("ascii").split()
        p = path.decode("utf-8", "surrogateescape")
        if typ != "blob" or len(p.split("/")) < 3:
            continue
        rows.append({"path": p, "mode": mode, "sha": sha,
                     "source": p.split("/")[1],
                     "year": (YEAR.search(p).group(1) if YEAR.search(p) else ""),
                     "ext": Path(p).suffix.lower()})
    return sorted(rows, key=lambda r: r["path"])

def is_document(row):
    path = row["path"].lower()
    if row["ext"] not in EXT:
        return False
    if Path(path).name in {"readme.md", "license.md", "changelog.md"}:
        return False
    return not any("/" + segment + "/" in path
                   for segment in ("img", "img_repaint", "images", "figures", "image"))

def topics(path):
    name = "/".join(path.split("/")[2:]).casefold()
    return [kind for kind, words in TOPICS.items()
            if any(word.casefold() in name for word in words)]

def published_path_mapping():
    """Main-branch paths for deduplicated, renamed PDFs (immutable sources unaffected)."""
    path = DEST / "normalized_files.csv"
    if not path.is_file():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return {r["original_path"]: r["canonical_path"]
                for r in csv.DictReader(stream)}

PUBLISHED_PATHS = published_path_mapping()

def source_link(row, depth):
    if row["ext"] in {".md", ".markdown"}:
        return ("https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive"
                "/blob/full-source-archive/" + quote(row["path"], safe="/"))
    published = PUBLISHED_PATHS.get(row["path"])
    if published:
        return "../" * depth + quote(published, safe="/")
    return ("https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive"
            "/blob/full-source-archive/" + quote(row["path"], safe="/"))


def csv_file(path, fields, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as out:
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def published_papers():
    """List actual published exam PDFs from HEAD, even in a sparse checkout."""
    raw = call("ls-tree", "-r", "-z", "HEAD", "--", "papers/")
    results = []
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        meta, name = entry.split(b"\t", 1)
        _mode, kind, _sha = meta.decode("ascii").split()
        if kind != "blob":
            continue
        path = name.decode("utf-8", "surrogateescape")
        if not path.endswith(".pdf"):
            continue
        match = re.fullmatch(
            r"papers/(\d{3}0)s/gaokao-(\d{4})-[a-z0-9-]+-"
            r"(?:general|science|liberal)(?:-spring)?-paper\.pdf", path)
        if not match or int(match.group(2)) // 10 * 10 != int(match.group(1)):
            raise ValueError("Invalid published exam PDF path: " + path)
        results.append({"year": match.group(2), "path": path})
    return sorted(results, key=lambda row: (row["year"], row["path"]))


def render_published_year_index(papers):
    """Keep all historical year anchors, without repeating upstream TeX inventories."""
    by_year = defaultdict(list)
    for row in papers:
        by_year[row["year"]].append(row["path"])
    if not by_year:
        raise ValueError("Published exam PDF list is empty")
    paths = [path for group in by_year.values() for path in group]
    if len(paths) != len(set(paths)):
        raise ValueError("Duplicate published exam PDF path")
    labels = sorted(by_year)
    lines = [f"# {labels[0]}—{labels[-1]} 高考数学年份总目录", "",
             "此页仅列主分支已发布的逐卷真题 PDF；上游 TeX、扫描图及完整来源请查 [文件索引](documents.csv) 和 [原件存档](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)。",
             "卷别以文件名标识；文件收录不表示原卷真实性或答案已经审核。", "",
             f"已发布 **{len(paths)} 份 PDF**，跨 **{len(labels)} 个年份**。", ""]
    for year in labels:
        lines.extend([f"## {year} 年数学资料", ""])
        for path in sorted(by_year[year]):
            lines.append("- [" + Path(path).name + "](../" + quote(path, safe="/") + ")")
        lines.append("")
    return "\n".join(lines) + "\n"

def main():
    sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))["repositories"]
    valid = {s["id"] for s in sources}
    rows = inventory()
    if len(valid) != 11 or not rows or any(r["source"] not in valid for r in rows):
        raise SystemExit("Source manifest and 11 Git mirrors inconsistent")
    duplicates = defaultdict(list)
    for row in rows:
        duplicates[row["sha"]].append(row)
    canonical = {}
    aliases = []
    for sha, group in sorted(duplicates.items()):
        first = min(group, key=lambda r: (not is_document(r), len(r["path"]), r["path"]))
        canonical[sha] = first
        for item in group:
            if item["path"] != first["path"]:
                aliases.append({"original_path": item["path"],
                                "canonical_path": PUBLISHED_PATHS.get(first["path"], first["path"]),
                                "reason": "identical_git_blob",
                                "blob_sha": sha, "source": item["source"]})
    documents = sorted((r for r in canonical.values() if is_document(r)),
                       key=lambda r: (r["year"] or "9999", r["source"], r["path"]))
    doc_rows = [{"year": r["year"], "source": r["source"],
                 "format": r["ext"], "title": Path(PUBLISHED_PATHS.get(r["path"], r["path"])).stem,
                 "canonical_path": PUBLISHED_PATHS.get(r["path"], r["path"]), "sha": r["sha"],
                 "topic_hints": ";".join(topics(r["path"])),
                 "review_status": "unreviewed",
                 "source_url": source_link(r, 1)} for r in documents]
    DEST.mkdir(parents=True, exist_ok=True)
    csv_file(DEST / "documents.csv",
             ["year", "source", "format", "title", "canonical_path",
              "sha", "topic_hints", "review_status", "source_url"], doc_rows)
    csv_file(DEST / "aliases.csv",
             ["original_path", "canonical_path", "reason", "blob_sha", "source"],
             sorted(aliases, key=lambda r: r["original_path"]))
    years, topics_map = defaultdict(list), defaultdict(list)
    for row in documents:
        if row["year"]:
            years[row["year"]].append(row)
        for tag in topics(row["path"]):
            topics_map[tag].append(row)
    # One compact year list for the main-branch published PDFs; preserve all old anchors.
    published = published_papers()
    rendered = render_published_year_index(published)
    redirects = [
        {"old_path": f"catalog/years/{year}.md",
         "new_path": "catalog/YEAR_INDEX.md",
         "anchor": f"{year}-年数学资料"}
        for year in sorted(years)
    ]
    (DEST / "YEAR_INDEX.md").write_text(rendered, encoding="utf-8")
    # Only purge old generated year/decade navigations; reject edited files.
    for old_dir, pattern in [
        (DEST / "years", r"^# (?:19|20)\d{2} 年数学资料\n"),
        (DEST / "periods", r"^# (?:19|20)\d{2}s 高考数学资料合订目录\n"),
    ]:
        if old_dir.exists():
            for old in old_dir.glob("*.md"):
                if not re.match(pattern, old.read_text(encoding="utf-8")):
                    raise RuntimeError("Refusing to remove a hand-edited page: " + str(old))
                if old_dir.name == "periods":
                    redirects.append({"old_path": "catalog/periods/" + old.name,
                                      "new_path": "catalog/YEAR_INDEX.md",
                                      "anchor": ""})
                old.unlink()
            if not any(old_dir.iterdir()):
                old_dir.rmdir()
    consolidated_topics = ["# 专题分类合订目录", "",
                           "只通过原文件名/路径进行初筛；不是对试卷内各题的数学审核。", ""]
    for tag, group in sorted(topics_map.items()):
        consolidated_topics.extend([f"## {tag}", ""])
        for row in sorted(group, key=lambda r: (r["year"], r["path"])):
            consolidated_topics.append("- [" + Path(PUBLISHED_PATHS.get(row["path"], row["path"])).name + "](" +
                                       source_link(row, 1) + ") · " +
                                       (row["year"] or "未知年份") + " · " + row["source"])
        consolidated_topics.append("")
        redirects.append({"old_path": f"catalog/topics/{tag}.md",
                          "new_path": "catalog/TOPICS.md", "anchor": tag})
    (DEST / "TOPICS.md").write_text(
        "\n".join(consolidated_topics) + "\n", encoding="utf-8")
    legacy_topics = DEST / "topics"
    if legacy_topics.exists():
        for old in legacy_topics.glob("*.md"):
            old_text = old.read_text(encoding="utf-8")
            if not re.match(r"^# [a-z]+ · 关键词初筛\n", old_text):
                raise RuntimeError("Refusing to delete non-generated topic page: " + str(old))
            old.unlink()
        if not any(legacy_topics.iterdir()):
            legacy_topics.rmdir()
    csv_file(DEST / "legacy_markdown_paths.csv",
             ["old_path", "new_path", "anchor"], redirects)
    stats = {"sources": len(valid), "original_files": len(rows),
             "unique_git_blobs": len(duplicates),
             "exact_duplicate_copies": len(rows) - len(duplicates),
             "exact_duplicate_groups": sum(len(g) > 1 for g in duplicates.values()),
             "canonical_documents": len(documents),
             "published_exam_pdfs": len(published),
             "year_sections": len(years), "period_volumes": 0, "year_index_volumes": 1,
             "topic_sections": len(topics_map), "topic_volumes": 1,
             "removed_generated_markdown_pages": len(years) + len(topics_map),
             "source_branch": "full-source-archive",
             "merge_rule": "Exact source trees are preserved on full-source-archive; historical merged Markdown lives on snapshot-before-lean-metadata-20261027"}
    (DEST / "stats.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# 高考数学 · 统一去重目录", "",
             "[命名与去重规范](NAMING.md) · [归档原路径 SHA](normalized_files.csv) · [需要人工核对的 2 份年份异常 PDF](naming_review.csv)", "",
             "**推荐从这里查找试卷和题目。** 全量原始文件位于 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)；旧版上游 Markdown 合订本在 [整理前快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/snapshot-before-lean-metadata-20261027/archive/SOURCE_MARKDOWN.md)。", "",
             f"- 来源仓库：**{len(valid)}**",
             f"- 原始文件：**{len(rows):,}**",
             f"- 不同文件内容：**{len(duplicates):,}**",
             f"- 折叠完全重复副本：**{len(rows)-len(duplicates):,}**",
             f"- 代表性资料文件：**{len(documents):,}**", "",
             "[完整文件索引](documents.csv) · [重复别名与出处](aliases.csv)"
             " · [自动统计](stats.json)", "",
             "## 按年份", ""]
    lines.append("[1952—2026 已发布真题 PDF](YEAR_INDEX.md) · "
                 "[查看年代分组 PDF](../papers/) · [上游全部资料](documents.csv)")
    lines.append("")
    lines += ["## 按专题（合订为一份）", ""]
    for tag, group in sorted(topics_map.items()):
        lines.append("- [" + tag + "](TOPICS.md#" + tag + ") · " +
                     str(len(group)) + " 份")
    lines += ["", "[旧页面路径对照](legacy_markdown_paths.csv) · 年份页仅收录已发布真题；"
              "其他上游 TeX/Markdown 原件可从 [完整来源 CSV](documents.csv) 和"
              " [固定原件快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive) 查找。", ""]
    lines += ["", "## 题目级去重与相似题复核", "",
              "- [8 组已确认同题、8 组明确不同变式及 5 组待审](QUESTION_DEDUP.md)",
              "- [完整题目级核查表](reviewed_problem_groups.csv)",
              "- [历史独立核验说明](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/snapshot-before-lean-metadata-20261027/index/DUPLICATE_AUDIT.md)", "",
              "**注意**：文件内容高度相似并不等于题目条件完全一致。"
              "没有经过题干逐问验证的内容不直接合并。", "",
              "本目录由 GitHub Actions 每 30 分钟检查并重建；"
              "相同结果不会再次提交。", ""]
    (DEST / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2), flush=True)

if __name__ == "__main__":
    main()
