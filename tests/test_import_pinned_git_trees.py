"""Isolated no-network end-to-end regression for pinned real Git object import."""
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts/import_pinned_git_trees.py"
SPEC = importlib.util.spec_from_file_location("pinned_full_mirror", MODULE)
mirror = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mirror)


def command(where, *args):
    return subprocess.check_output(["git", "-C", str(where), *args],
                                   stderr=subprocess.PIPE, text=True).strip()


def run(where, *args):
    subprocess.run(["git", "-C", str(where), *args], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


class PinnedGitTreeImportTests(unittest.TestCase):
    def test_real_binary_full_tree_and_idempotence(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            source = folder / "source"
            source.mkdir()
            run(source, "init", "-q")
            run(source, "config", "user.email", "ci@example.invalid")
            run(source, "config", "user.name", "Archive QA")
            (source / "old.txt").write_text("全新内容\n", encoding="utf-8")
            (source / "binary.pdf").write_bytes(b"%PDF-1.7\n\x00\xfe\xff\n")
            run(source, "add", ".")
            run(source, "commit", "-qm", "pinned source")
            pin = command(source, "rev-parse", "HEAD")
            tree = command(source, "rev-parse", "HEAD^{tree}")

            bare = folder / "target.git"
            run(folder, "init", "-q", "--bare", str(bare))
            work = folder / "working"
            run(folder, "clone", "-q", str(bare), str(work))
            run(work, "config", "user.email", "ci@example.invalid")
            run(work, "config", "user.name", "Archive QA")
            old = work / "mirror/source/old.txt"
            old.parent.mkdir(parents=True)
            old.write_text("outdated\n")
            run(work, "add", ".")
            run(work, "commit", "-qm", "partial source")
            run(work, "push", "-q", "origin", "HEAD:refs/heads/main")
            before = command(work, "rev-parse", "HEAD")
            result, status, count = mirror.import_one(
                work, source_id="source", source_url=source.as_uri(),
                pin=pin, parent=before, push=True)
            self.assertEqual((status, count), ("pushed", 2))
            self.assertEqual(command(bare, "rev-parse", "refs/heads/main"), result)
            self.assertEqual(command(work, "rev-parse", f"{result}:mirror/source"), tree)
            self.assertEqual(command(work, "rev-parse", f"{result}:mirror/source/binary.pdf"),
                             command(source, "rev-parse", "HEAD:binary.pdf"))
            self.assertEqual(command(work, "rev-parse", "HEAD"), before,
                             "Working branch must not move")
            self.assertEqual(old.read_text(), "outdated\n",
                             "Working-tree file must not change")
            again, status, count = mirror.import_one(
                work, source_id="source", source_url=source.as_uri(),
                pin=pin, parent=result, push=True)
            self.assertEqual((again, status, count), (result, "unchanged", 2))

            # The hosted runner sparsely checks out only scripts/tests.
            # Pinned mirror folders remain in the Git index, outside the
            # working tree. A newer fixed pin must still replace that subtree.
            run(work, "sparse-checkout", "init", "--cone")
            run(work, "sparse-checkout", "set", "scripts", "tests")
            (source / "old.txt").write_text("第二版本\\n", encoding="utf-8")
            run(source, "add", ".")
            run(source, "commit", "-qm", "pinned source version 2")
            second_pin = command(source, "rev-parse", "HEAD")
            second_tree = command(source, "rev-parse", "HEAD^{tree}")
            newer, newer_status, newer_count = mirror.import_one(
                work, source_id="source", source_url=source.as_uri(),
                pin=second_pin, parent=result, push=True)
            self.assertEqual((newer_status, newer_count), ("pushed", 2))
            self.assertEqual(command(bare, "rev-parse", "refs/heads/main"), newer)
            self.assertEqual(command(work, "rev-parse", f"{newer}:mirror/source"),
                             second_tree)

    def test_invalid_pin_or_source_id_rejected(self):
        with self.assertRaises(ValueError):
            mirror.import_one(Path("."), source_id="../escape",
                              source_url="file:///nothing", pin="a"*40,
                              parent="b"*40, push=False)
        with self.assertRaises(ValueError):
            mirror.import_one(Path("."), source_id="good",
                              source_url="file:///nothing", pin="unfixed",
                              parent="b"*40, push=False)


if __name__ == "__main__":
    unittest.main()
