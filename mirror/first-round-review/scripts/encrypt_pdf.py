#!/usr/bin/env python3
"""Protect a PDF from editing while keeping it readable without a password."""

import argparse
import os
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions as UAP


OWNER_PASSWORD = "hB!n.Fr00G25#"


def encrypt_pdf(pdf_path: Path) -> None:
    if not pdf_path.is_file():
        raise FileNotFoundError(f"文件不存在：{pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("文件必须是 PDF")

    reader = PdfReader(pdf_path)
    if reader.is_encrypted and not reader.decrypt(""):
        raise ValueError("该 PDF 已设置打开密码，无法直接重新加密")

    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    allowed = (
        UAP.PRINT
        | UAP.EXTRACT
        | UAP.EXTRACT_TEXT_AND_GRAPHICS
        | UAP.PRINT_TO_REPRESENTATION
    )
    writer.encrypt(
        user_password="",
        owner_password=OWNER_PASSWORD,
        permissions_flag=allowed,
        algorithm="AES-256",
    )

    with tempfile.NamedTemporaryFile(
        prefix=f".{pdf_path.stem}-encrypt-",
        suffix=".pdf",
        dir=pdf_path.parent,
        delete=False,
    ) as stream:
        temporary = Path(stream.name)
        writer.write(stream)

    try:
        check = PdfReader(temporary)
        if not check.is_encrypted or not check.decrypt(""):
            raise RuntimeError("加密结果验证失败")
        os.replace(temporary, pdf_path)
    finally:
        temporary.unlink(missing_ok=True)

    print(f"已加密：{pdf_path}（打开无需密码，编辑受限）")


def main() -> None:
    parser = argparse.ArgumentParser(description="为 PDF 设置编辑权限密码")
    parser.add_argument("file", type=Path, help="需要加密的 PDF 文件")
    args = parser.parse_args()
    encrypt_pdf(args.file)


if __name__ == "__main__":
    main()
