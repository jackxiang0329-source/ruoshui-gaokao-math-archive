"""Fail-closed, dependency-free regression checks for imported mirror manifests."""
import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "validate_import_batches.py"
spec = importlib.util.spec_from_file_location("import_batch_audit", MODULE)
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)

PIN = "a" * 40
BEFORE = "b" * 40
AFTER = "c" * 40
BLOB = "d" * 40
PATH = "img/1963/高考-q1.png"
KEY = "mirror/source/" + PATH
SOURCES = {"source": {"repo": "example/maths", "initial_commit": PIN}}
MANIFEST = {
    "source_id": "source", "source_repo": "example/maths", "source_commit": PIN,
    "baseline_commit": BEFORE, "audited_after_commit": AFTER, "count": 1,
    "total_upstream_bytes": 12, "files": [{"path": PATH, "sha": BLOB, "mode": "100644", "size": 12}],
    "group_counts": {"img/1963": {"files": 1, "bytes": 12}},
}
STATUS = {
    "expected": 2, "verified": 1, "missing": 1, "full": 0,
    "sources": [{"id": "source", "expected": 2, "verified": 1, "missing": 1, "complete": False}],
    "audited_commit": AFTER,
    "latest_direct_import": {
        "manifest": "mirror/IMPORT_BATCH_HISTORICAL_FIGURES_2026_10_25.json",
        "source": "source", "source_pin": PIN, "baseline_commit": BEFORE,
        "mirror_commit": AFTER, "new_verified": 1, "new_bytes": 12,
    },
}


def record():
    return dict(MANIFEST, files=[dict(MANIFEST["files"][0])],
                group_counts={"img/1963": {"files": 1, "bytes": 12}})


class BatchAuditTests(unittest.TestCase):
    def pass_batch(self, manifest=None, baseline=None, after=None, current=None):
        return qa.validate_batch(manifest or record(), SOURCES,
                                 {} if baseline is None else baseline,
                                 {KEY: ("100644", BLOB, 12)} if after is None else after,
                                 {KEY: ("100644", BLOB, 12)} if current is None else current)

    def test_good_batch_and_status(self):
        self.assertEqual(self.pass_batch(), 1)
        qa.validate_status(STATUS, record(), {"source"})

    def test_reject_regression_or_fabricated_baseline(self):
        for which, value in [("baseline", {KEY: ("100644", BLOB, 12)}),
                             ("after", {}), ("current", {}),
                             ("current", {KEY: ("100755", BLOB, 12)}),
                             ("current", {KEY: ("100644", BLOB, 13)}),
                             ("current", {KEY: ("100644", "e" * 40, 12)})]:
            with self.subTest(which=which, value=value), self.assertRaises(qa.BatchAuditError):
                self.pass_batch(**{which: value})

    def test_reject_manifest_tampering(self):
        variants = [
            ("count", 2), ("total_upstream_bytes", 13), ("source_commit", "b" * 40),
            ("source_repo", "attacker/other"), ("baseline_commit", AFTER),
            ("group_counts", {"img/1963": {"files": 2, "bytes": 12}}),
        ]
        for field, bad in variants:
            modified = record()
            modified[field] = bad
            with self.subTest(field=field), self.assertRaises(qa.BatchAuditError):
                self.pass_batch(manifest=modified)

    def test_reject_paths_and_duplicate(self):
        for bad in ("/etc/passwd", "../a.tex", "img//file.tex", "img/./a.tex",
                    "img/1963/../file.tex", "img\\1963\\a.tex", "img/1963/\x00evil"):
            modified = record()
            modified["files"][0]["path"] = bad
            with self.subTest(path=bad), self.assertRaises(qa.BatchAuditError):
                self.pass_batch(manifest=modified)
        modified = record()
        modified["files"] *= 2
        modified["count"] = 2
        with self.assertRaises(qa.BatchAuditError):
            self.pass_batch(manifest=modified)

    def test_reject_status_forgery(self):
        import copy
        for mutate in (
            lambda d: d.update(verified=2),
            lambda d: d["sources"][0].update(complete=True),
            lambda d: d["latest_direct_import"].update(new_bytes=9),
            lambda d: d["latest_direct_import"].update(baseline_commit=PIN),
        ):
            data = copy.deepcopy(STATUS)
            mutate(data)
            with self.assertRaises(qa.BatchAuditError):
                qa.validate_status(data, record(), {"source"})

    def test_git_tree_parse_real_commits(self):
        # A true Git fixture guards against merely testing mocked dictionaries.
        import subprocess
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "qa@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "QA Test"], check=True)
            path = root / "mirror/source/img/1963/高考-q1.png"
            path.parent.mkdir(parents=True)
            path.write_bytes(b"hello world!")
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-qm", "fixture"], check=True)
            tree = qa.git_tree(root, "HEAD", "mirror/source")
            expected_sha = subprocess.check_output(["git", "-C", str(root), "hash-object", str(path)]).decode().strip()
            self.assertEqual(tree[KEY], ("100644", expected_sha, 12))


if __name__ == "__main__":
    unittest.main()
