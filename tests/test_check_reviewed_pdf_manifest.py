"""PDF source-manifest coverage: fixtures need no network or TeX installation."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / 'scripts/check_reviewed_pdf_manifest.py'
spec = importlib.util.spec_from_file_location('pdf_manifest', MODULE)
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)


class PdfManifestTests(unittest.TestCase):
    def fixture(self, listed):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / 'derivative/reviewed').mkdir(parents=True)
        (root / '.github/workflows').mkdir(parents=True)
        for name in ['a.tex', 'b.tex']:
            (root / 'derivative/reviewed' / name).write_text('% tiny fixture\n')
        contents = 'name: Build PDF\non:\n  workflow_dispatch:\njobs:\n  pdf:\n    with:\n      root_file: |\n'
        contents += ''.join('        '+entry+'\n' for entry in listed)
        contents += '    latexmk_use_xelatex: true\n'
        (root / qa.WORKFLOW).write_text(contents)
        return root

    def test_full_coverage(self):
        self.assertEqual(qa.check(self.fixture([
            'derivative/reviewed/a.tex', 'derivative/reviewed/b.tex']))[0], 2)

    def test_missing_file(self):
        with self.assertRaisesRegex(qa.ManifestError, 'missing='):
            qa.check(self.fixture(['derivative/reviewed/a.tex']))

    def test_stale_entry(self):
        with self.assertRaisesRegex(qa.ManifestError, 'stale='):
            qa.check(self.fixture(['derivative/reviewed/a.tex', 'derivative/reviewed/b.tex',
                                   'derivative/reviewed/c.tex']))

    def test_duplicate_and_external_path(self):
        with self.assertRaises(qa.ManifestError):
            qa.declared_tex('root_file: |\n  derivative/reviewed/a.tex\n  derivative/reviewed/a.tex')
        with self.assertRaises(qa.ManifestError):
            qa.declared_tex('root_file: |\n  ../outside.tex')


if __name__ == '__main__':
    unittest.main()
