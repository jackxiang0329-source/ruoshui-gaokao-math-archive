import importlib.util
import unittest
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts" / "validate_pinned_sources.py"
spec = importlib.util.spec_from_file_location("pins", path)
pins = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pins)


class PinTests(unittest.TestCase):
    def setUp(self):
        self.pin = "a" * 40
        self.source = {"id": "gaokaomath", "initial_commit": self.pin}

    def test_happy_path(self):
        raw = b"160000 " + self.pin.encode() + b" 0\tupstream/gaokaomath\0"
        links = pins.parse_gitlinks(raw)
        self.assertEqual(links, {"upstream/gaokaomath": self.pin})
        pins.check_manifest(links, [self.source])

    def test_changed_pin_rejected(self):
        with self.assertRaises(pins.PinMismatch):
            pins.check_manifest({"upstream/gaokaomath": "b" * 40}, [self.source])

    def test_missing_extra_or_duplicate_rejected(self):
        for links, sources in [
            ({}, [self.source]),
            ({"upstream/gaokaomath": self.pin, "upstream/extra": self.pin}, [self.source]),
            ({"upstream/gaokaomath": self.pin}, [self.source, self.source]),
        ]:
            with self.assertRaises(pins.PinMismatch):
                pins.check_manifest(links, sources)

    def test_unmerged_regular_file_and_path_traversal_rejected(self):
        for data in [
            b"100644 " + b"a" * 40 + b" 0\tupstream/gaokaomath\0",
            b"160000 " + b"a" * 40 + b" 2\tupstream/gaokaomath\0",
            b"160000 " + b"a" * 40 + b" 0\tupstream/../escape\0",
        ]:
            with self.assertRaises(pins.PinMismatch):
                pins.parse_gitlinks(data)

    def test_malformed_gitlink_rejected(self):
        with self.assertRaises(pins.PinMismatch):
            pins.parse_gitlinks(b"not a gitlink\0")


if __name__ == "__main__":
    unittest.main()
