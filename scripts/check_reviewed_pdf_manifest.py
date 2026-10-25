#!/usr/bin/env python3
"""Fail if the manual reviewed-PDF build omits or invents a standalone TeX.

No YAML dependency needed; reads the indented literal root_file list of the
latex-action step. Checks coverage only, not actual PDF compilation.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = Path('.github/workflows/build-reviewed-pdfs.yml')


class ManifestError(ValueError):
    pass


def declared_tex(text: str) -> list[str]:
    """Extract a unique latex-action root_file: | list, rejecting other forms."""
    lines = text.splitlines()
    headers = [(i, len(line) - len(line.lstrip()))
               for i, line in enumerate(lines) if line.strip() == 'root_file: |']
    if len(headers) != 1:
        raise ManifestError('Exactly one literal root_file: | section required')
    start, depth = headers[0]
    paths = []
    for line in lines[start + 1:]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= depth:
            break
        value = line.strip()
        if not value.startswith('derivative/reviewed/') or not value.endswith('.tex'):
            raise ManifestError('Unexpected TeX root_file: ' + value)
        paths.append(value)
    if len(paths) != len(set(paths)) or not paths:
        raise ManifestError('Empty or duplicate TeX root list')
    return paths


def check(root: Path = ROOT) -> tuple[int, list[str]]:
    action = (root / WORKFLOW).read_text(encoding='utf-8')
    listed = declared_tex(action)
    folder = root / 'derivative/reviewed'
    actual = sorted('derivative/reviewed/' + p.name for p in folder.glob('*.tex'))
    missing = sorted(set(actual) - set(listed))
    extra = sorted(set(listed) - set(actual))
    if missing or extra:
        raise ManifestError(f'PDF root_file does not cover all reviewed TeX: missing={missing}; stale={extra}')
    return len(actual), actual


def main() -> int:
    try:
        count, _ = check()
    except (ManifestError, OSError) as exc:
        print('REVIEWED PDF LIST FAILED: ' + str(exc), file=sys.stderr)
        return 1
    print(f'PASS: all {count} reviewed TeX sources appear exactly once in PDF build roots')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
