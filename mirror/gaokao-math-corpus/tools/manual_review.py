"""Render a paper for manual review and mark it approved after review.

Usage (run from the repository root)::

    uv run python tools/manual_review.py render --paper-dir corpus/papers/2024/I
    uv run python tools/manual_review.py approve --paper-dir corpus/papers/2024/I

``render`` writes a single review HTML file under ``build/review/``.  Open it
and compare every item with the source pages before running ``approve``.
The approve command updates the unified ``status`` fields; it does not add
answers, solutions, or descriptive annotations.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from typing import Any

import yaml


TYPE_LABELS = {
    "mcq_single_answer": "单选题",
    "mcq_multiple_answers": "多选题",
    "fill_blank": "填空题",
    "solution": "解答题",
}


def read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def write_yaml(path: Path, data: Any) -> None:
    text = yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )
    path.write_text(text, encoding="utf-8")


def split_item_file(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"missing YAML front matter: {path}")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError(f"invalid YAML front matter: {path}")
    meta = yaml.safe_load(parts[1])
    return meta, parts[2].strip()


def write_item_file(path: Path, meta: dict[str, Any], body: str) -> None:
    front_matter = yaml.safe_dump(
        meta,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )
    path.write_text(f"---\n{front_matter}---\n\n{body.strip()}\n", encoding="utf-8")


def paper_dir_from_args(args: argparse.Namespace) -> Path:
    if args.paper_dir:
        return args.paper_dir
    return Path("corpus/papers") / str(args.year) / args.volume


def markdown_to_review_html(markdown: str, item_dir: Path) -> str:
    image_pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    blocks: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            text = "\n".join(paragraph)
            blocks.append(f"<p>{image_pattern.sub(render_image, html.escape(text))}</p>")
            paragraph.clear()

    def render_image(match: re.Match[str]) -> str:
        alt = html.escape(match.group(1))
        raw_src = match.group(2)
        src_path = (item_dir / raw_src).resolve()
        src = html.escape(src_path.as_uri())
        return f'<img src="{src}" alt="{alt}">'

    for line in markdown.splitlines():
        if not line.strip():
            flush_paragraph()
            continue
        paragraph.append(line)
    flush_paragraph()
    return "\n".join(blocks)


def render_item(paper_dir: Path, item: dict[str, Any]) -> str:
    item_path = paper_dir / item["path"]
    meta, body = split_item_file(item_path)
    number = int(meta["number"])
    type_label = TYPE_LABELS.get(meta["type"], meta["type"])
    status = (
        f"{meta.get('status', '-')}"
    )

    options_html = ""
    options = meta.get("options")
    if options:
        option_parts = []
        for key in ("A", "B", "C", "D", "E"):
            if key in options:
                option_parts.append(
                    "<li>"
                    f"<strong>{html.escape(key)}.</strong> "
                    f"{html.escape(str(options[key]))}"
                    "</li>"
                )
        options_html = "<ol class=\"options\">" + "\n".join(option_parts) + "</ol>"

    uncertain_notes = meta.get("uncertain_notes") or []
    notes_html = ""
    if meta.get("needs_confirmation") or uncertain_notes:
        notes = "".join(f"<li>{html.escape(str(note))}</li>" for note in uncertain_notes)
        notes_html = f"<div class=\"notes\"><strong>待确认</strong><ul>{notes}</ul></div>"

    body_html = markdown_to_review_html(body, item_path.parent)
    return f"""
<section class="item" id="item-{number:02d}">
  <h2>{number:02d}. {html.escape(type_label)} <span>{html.escape(status)}</span></h2>
  <div class="body">{body_html}</div>
  {options_html}
  {notes_html}
</section>
"""


def render_paper(args: argparse.Namespace) -> int:
    paper_dir = paper_dir_from_args(args)
    paper_path = paper_dir / "paper.yml"
    if not paper_path.exists():
        raise SystemExit(f"paper.yml not found: {paper_path}")

    paper_data = read_yaml(paper_path)
    paper = paper_data["paper"]
    items = paper_data["items"]
    output = args.output or Path("build/review") / f"{paper['id']}.html"
    output.parent.mkdir(parents=True, exist_ok=True)

    item_html = "\n".join(render_item(paper_dir, item) for item in items)
    document = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>{html.escape(paper["title"])}</title>
  <script>
    window.MathJax = {{ tex: {{ inlineMath: [['$', '$']], displayMath: [['$$', '$$']] }} }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 960px; margin: 24px auto; line-height: 1.6; }}
    h1 {{ font-size: 24px; }}
    h2 {{ font-size: 18px; border-top: 1px solid #ddd; padding-top: 16px; }}
    h2 span {{ color: #666; font-size: 13px; font-weight: normal; margin-left: 8px; }}
    .item {{ margin-bottom: 28px; }}
    .options {{ list-style: none; padding-left: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px 24px; }}
    img {{ max-width: 360px; display: block; margin: 8px 0; }}
    .notes {{ border-left: 4px solid #d97706; padding-left: 12px; color: #92400e; }}
  </style>
</head>
<body>
  <h1>{html.escape(paper["title"])}</h1>
  <p>paper_id: {html.escape(paper["id"])}; paper_scheme_id: {html.escape(paper["paper_scheme_id"])}</p>
  {item_html}
</body>
</html>
"""
    output.write_text(document, encoding="utf-8")
    print(output)
    return 0


def approve_paper(args: argparse.Namespace) -> int:
    paper_dir = paper_dir_from_args(args)
    paper_path = paper_dir / "paper.yml"
    paper_data = read_yaml(paper_path)
    paper_data["paper"]["status"] = "approved"
    write_yaml(paper_path, paper_data)

    for item in paper_data["items"]:
        item_path = paper_dir / item["path"]
        meta, body = split_item_file(item_path)
        meta["status"] = "approved"
        write_item_file(item_path, meta, body)

    print(f"approved {len(paper_data['items'])} items in {paper_dir}")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render or approve a paper for manual review.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("render", "approve"):
        sub = subparsers.add_parser(command)
        sub.add_argument("--paper-dir", type=Path)
        sub.add_argument("--year", type=int, default=2024)
        sub.add_argument("--volume", choices=["I", "II"], default="I")
        if command == "render":
            sub.add_argument("--output", type=Path)

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.command == "render":
        return render_paper(args)
    if args.command == "approve":
        return approve_paper(args)
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
