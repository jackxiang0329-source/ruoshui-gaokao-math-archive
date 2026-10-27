"""Static regression guard for the merged XeLaTeX solution layout.

This test checks source structure; actual PDF compilation and visual rendering
are verified separately by the GitHub Actions build workflow.
"""
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "derivative/reviewed/gaokao-2010-2025-calculus-reviewed-solutions.tex"


class ReviewedSolutionsLayoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = TEX.read_text(encoding="utf-8")

    def test_13_provenance_blocks_and_single_document(self):
        source = self.source
        starts = re.findall(r"(?m)^% SOURCE_ENTRY path=.+ sha=[0-9a-f]{40}$", source)
        ends = re.findall(r"(?m)^% END_SOURCE_ENTRY path=.+$", source)
        self.assertEqual(len(starts), 13)
        self.assertEqual(len(ends), 13)
        self.assertEqual(source.count(r"\begin{document}"), 1)
        self.assertEqual(source.count(r"\end{document}"), 1)

    def test_fixed_source_hyperlinks_without_page_overflow_urls(self):
        source = self.source
        fixed = re.findall(
            r"\\href\{(https://github\.com/[^}]+)\}\{原始 TeX 题干（固定版）\}",
            source,
        )
        self.assertEqual(len(fixed), 14)
        self.assertTrue(all("/blob/" in url and "#L" in url for url in fixed))
        self.assertNotIn(r"\url{", source)

    def test_unsupported_roman_number_glyphs_removed(self):
        for glyph in "ⅠⅡ":
            self.assertNotIn(glyph, self.source)


if __name__ == "__main__":
    unittest.main()
