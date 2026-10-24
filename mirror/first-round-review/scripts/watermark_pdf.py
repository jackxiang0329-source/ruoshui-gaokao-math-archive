#!/usr/bin/env python3
"""Tile a diagonal text watermark over every page of a PDF in place."""

import argparse
import os
import tempfile
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


FONT_CANDIDATES = (
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
)


def register_watermark_font() -> str:
    for font_path in FONT_CANDIDATES:
        if Path(font_path).is_file():
            pdfmetrics.registerFont(
                TTFont("WatermarkCJK", font_path, subfontIndex=0)
            )
            return "WatermarkCJK"
    raise RuntimeError("未找到可嵌入的中文字体，请安装 Noto Sans CJK 或文泉驿微米黑")


def add_watermark(pdf_path: Path, text: str) -> None:
    if not pdf_path.is_file():
        raise FileNotFoundError(f"文件不存在：{pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("文件必须是 PDF")
    if not text:
        raise ValueError("水印内容不能为空")

    font_name = register_watermark_font()
    reader = PdfReader(pdf_path)
    if reader.is_encrypted and not reader.decrypt(""):
        raise ValueError("该 PDF 需要打开密码，无法直接添加水印")
    writer = PdfWriter()

    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        font_size = min(18.0, max(10.0, 105.0 / max(len(text), 1)))
        layer_data = BytesIO()
        layer = canvas.Canvas(layer_data, pagesize=(width, height))
        layer.setFillColorRGB(0.48, 0.48, 0.48)
        layer.setFillAlpha(0.16)
        layer.setFont(font_name, font_size)

        # 5 x 5 = 25 watermarks. Insets keep rotated text inside the page.
        margin_x = max(72.0, width * 0.12)
        margin_y = max(58.0, height * 0.07)
        for row in range(5):
            y = margin_y + row * (height - 2 * margin_y) / 4
            for col in range(5):
                x = margin_x + col * (width - 2 * margin_x) / 4
                layer.saveState()
                layer.translate(x, y)
                layer.rotate(35)
                layer.drawCentredString(0, 0, text)
                layer.restoreState()

        layer.save()
        layer_data.seek(0)
        page.merge_page(PdfReader(layer_data).pages[0], over=True)
        writer.add_page(page)

    if reader.metadata:
        writer.add_metadata(
            {key: str(value) for key, value in reader.metadata.items() if value is not None}
        )

    with tempfile.NamedTemporaryFile(
        prefix=f".{pdf_path.stem}-watermark-",
        suffix=".pdf",
        dir=pdf_path.parent,
        delete=False,
    ) as stream:
        temporary = Path(stream.name)
        writer.write(stream)

    try:
        PdfReader(temporary)
        os.replace(temporary, pdf_path)
    finally:
        temporary.unlink(missing_ok=True)

    print(f"已添加水印：{pdf_path}（每页 25 个）")


def main() -> None:
    parser = argparse.ArgumentParser(description="给 PDF 满屏添加斜向文字水印")
    parser.add_argument("file", type=Path, help="需要添加水印的 PDF 文件")
    parser.add_argument("text", help="水印文字")
    args = parser.parse_args()
    add_watermark(args.file, args.text)


if __name__ == "__main__":
    main()
