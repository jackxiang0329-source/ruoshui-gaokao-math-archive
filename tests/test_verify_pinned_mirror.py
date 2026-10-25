import importlib.util
import unittest
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / "scripts" / "verify_pinned_mirror.py"
spec = importlib.util.spec_from_file_location("verify_pinned_mirror", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestPinnedMirror(unittest.TestCase):
    def test_known_git_blob_sha(self):
        self.assertEqual(
            module.git_blob_sha(b"hello\n"),
            "ce013625030ba8dba906f756967f9e9ca394464a",
        )

    def test_unicode_paths_and_modes(self):
        digest = module.git_blob_sha(b"abc")
        name = "试卷 2015.pdf"
        original = ("100644 blob " + digest + "\t" + name).encode() + b"\0"
        staged = ("100644 " + digest + " 0\tmirror/id/" + name).encode() + b"\0"
        self.assertEqual(module.parse_entries(original), {name: ("100644", digest)})
        self.assertEqual(
            module.parse_entries(staged, staged=True),
            {"mirror/id/" + name: ("100644", digest)},
        )

    def test_gitlink_fails_closed(self):
        with self.assertRaises(module.MirrorIntegrityError):
            module.parse_entries(b"160000 commit " + b"a" * 40 + b"\tsubmodule\0")

    def test_unmerged_index_fails_closed(self):
        with self.assertRaises(module.MirrorIntegrityError):
            module.parse_entries(b"100644 " + b"a" * 40 + b" 2\ttest\0", staged=True)

    def test_unresolved_lfs_pointer_rejected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            name = "test.pdf"
            payload = b"version https://git-lfs.github.com/spec/v1\n" + b"oid sha256:x\n"
            (Path(tmp) / name).write_bytes(payload)
            with self.assertRaises(module.MirrorIntegrityError):
                module.check_bytes(Path(tmp), {name: ("100644", module.git_blob_sha(payload))})


if __name__ == "__main__":
    unittest.main()
