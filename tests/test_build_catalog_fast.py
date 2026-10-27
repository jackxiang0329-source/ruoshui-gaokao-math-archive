import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_catalog_fast.py"
spec = importlib.util.spec_from_file_location("build_catalog_fast", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PublishedYearIndexTests(unittest.TestCase):
    def test_links_and_stable_anchors(self):
        papers = [
            {"year": "1952", "path": "papers/1950s/gaokao-1952-unspecified-general-paper.pdf"},
            {"year": "2026", "path": "papers/2020s/gaokao-2026-national-1-general-paper.pdf"},
        ]
        text = module.render_published_year_index(papers)
        self.assertIn("# 1952—2026 高考数学年份总目录", text)
        self.assertIn("## 1952 年数学资料", text)
        self.assertIn("## 2026 年数学资料", text)
        for paper in papers:
            self.assertIn("](../" + paper["path"] + ")", text)
        self.assertIn("documents.csv", text)
        self.assertEqual(text.count("](../papers/"), 2)

    def test_empty_and_duplicate_inventory_rejected(self):
        with self.assertRaises(ValueError):
            module.render_published_year_index([])
        paper = {"year": "2024", "path": "papers/2020s/example.pdf"}
        with self.assertRaises(ValueError):
            module.render_published_year_index([paper, paper])

    def test_wrong_decade_is_rejected(self):
        bogus = "papers/2010s/gaokao-2024-national-general-paper.pdf"
        data = b"100644 blob " + b"a" * 40 + b"\t" + bogus.encode() + b"\0"
        with patch.object(module, "call", return_value=data):
            with self.assertRaises(ValueError):
                module.published_papers()


if __name__ == "__main__":
    unittest.main()
