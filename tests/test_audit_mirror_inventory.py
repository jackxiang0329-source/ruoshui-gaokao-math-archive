import importlib.util
import unittest
from pathlib import Path

module = Path(__file__).resolve().parents[1] / "scripts" / "audit_mirror_inventory.py"
spec = importlib.util.spec_from_file_location("mirror_audit", module)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class MirrorAuditTests(unittest.TestCase):
    def test_unicode_and_git_mode(self):
        sha = "a" * 40
        raw = ("100644 blob " + sha + "\t高考/数学 2026.tex").encode() + b"\0"
        self.assertEqual(
            audit.parse_tree(raw),
            {"高考/数学 2026.tex": ("100644", sha)},
        )

    def test_prefix_removed_safely(self):
        sha = "a" * 40
        raw = ("100755 blob " + sha + "\tmirror/x/tex/a.tex").encode() + b"\0"
        self.assertEqual(
            audit.parse_tree(raw, "mirror/x/"),
            {"tex/a.tex": ("100755", sha)},
        )

    def test_reject_nonblob_and_unsafe(self):
        samples = [
            b"160000 commit " + b"a" * 40 + b"\tsubmodule\0",
            b"100644 blob " + b"a" * 40 + b"\t../escape\0",
            b"100644 blob " + b"a" * 40 + b"\tmirror/b/file\0",
        ]
        for i, sample in enumerate(samples):
            with self.subTest(i=i), self.assertRaises(audit.AuditError):
                audit.parse_tree(sample, "mirror/a/" if i == 2 else "")

    def test_count_sha_and_mode_not_just_filename(self):
        sha = "a" * 40
        expected = {"good": ("100644", sha), "mode": ("120000", sha)}
        actual = {"good": ("100644", sha), "mode": ("100644", sha),
                  "extra": ("100644", sha)}
        result = audit.compare(expected, actual)
        self.assertEqual(
            (result["expected"], result["verified"], result["missing"], result["extra"]),
            (2, 1, 1, 1),
        )
        self.assertFalse(result["complete"])

    def test_exact_equality(self):
        expected = {"a": ("100644", "a" * 40)}
        self.assertTrue(audit.compare(expected, expected)["complete"])


if __name__ == "__main__":
    unittest.main()
