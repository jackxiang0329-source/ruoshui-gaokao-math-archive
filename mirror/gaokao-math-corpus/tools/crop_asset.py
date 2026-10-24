"""Crop one figure or table from a source page image.

Usage (run from the repository root)::

    uv run python tools/crop_asset.py work/2024-I/2.jpg \
        corpus/papers/2024/I/assets/11-fig-01.png \
        --box 1068 1289 1307 1794

The box is ``left top right bottom`` in source-image pixels. The script
performs one deterministic crop, validates the coordinates, creates the
output directory, and writes a PNG. It does not detect objects or retry
alternative cropping methods; choosing and checking coordinates remains part
of the transcription task.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crop one figure or table from a page image using pixel coordinates."
    )
    parser.add_argument("source", type=Path, help="Source page image.")
    parser.add_argument("output", type=Path, help="Output PNG asset path.")
    parser.add_argument(
        "--box",
        type=int,
        nargs=4,
        required=True,
        metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
        help="Crop box in source-image pixels.",
    )
    return parser.parse_args(argv)


def crop_asset(source: Path, output: Path, box: tuple[int, int, int, int]) -> None:
    with Image.open(source) as image:
        left, top, right, bottom = box
        width, height = image.size
        if not (0 <= left < right <= width and 0 <= top < bottom <= height):
            raise ValueError(
                f"invalid crop box {box} for image size {(width, height)}; "
                "expected 0 <= left < right <= width and "
                "0 <= top < bottom <= height"
            )
        output.parent.mkdir(parents=True, exist_ok=True)
        image.crop(box).save(output, format="PNG")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if not args.source.is_file():
        raise SystemExit(f"source image does not exist: {args.source}")
    try:
        crop_asset(args.source, args.output, tuple(args.box))
    except (OSError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
