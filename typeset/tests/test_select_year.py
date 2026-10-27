"""Safeguards to keep modern 2000+ examination PDFs in their original layout."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("gaokao_year_selector", ROOT / "select_year.py")
SELECT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SELECT)


class LastCenturyOnlyTests(unittest.TestCase):
    def test_explicit_modern_years_are_rejected(self):
        for year in ("2000", "2024", "2025", "2026"):
            with self.subTest(year=year):
                with self.assertRaises(ValueError):
                    SELECT.select_year(year)

    def test_historical_years_can_be_selected(self):
        self.assertEqual(SELECT.select_year("1952"), "1952")
        self.assertEqual(SELECT.select_year("1999"), "1999")

    def test_default_choice_ignores_modern_years(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source-coverage.json").write_text(
                json.dumps({"years": {
                    "1952": 1, "1999": 5, "2000": 10, "2025": 6, "2026": 6
                }}), encoding="utf-8")
            self.assertEqual(SELECT.select_year(root=root), "1999")
            (root / "annual").mkdir()
            (root / "annual" / "ruoshui-gaokao-1999.pdf").write_bytes(b"test")
            self.assertEqual(SELECT.select_year(root=root), "1952")
            (root / "annual" / "ruoshui-gaokao-1952.pdf").write_bytes(b"test")
            self.assertEqual(SELECT.select_year(root=root), "")


if __name__ == "__main__":
    unittest.main()
