import importlib.util
import unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"scripts/curate_archive.py"
S=importlib.util.spec_from_file_location("curate_archive",P)
m=importlib.util.module_from_spec(S)
S.loader.exec_module(m)
class RulesTests(unittest.TestCase):
    def test_year(self):
        self.assertEqual(m.year_of("mirror/mathpaper/2022/paper.tex"),"2022")
        self.assertEqual(m.year_of("mirror/mathpaper/README.md"),"")
    def test_equivalent_typography(self):
        a=b"\\begin{document}\n% note\n$\\left(x+1\\right)$\\end{document}"
        b=b"\\begin{document}$(x+1)$\\end{document}"
        self.assertEqual(m.normalize(a,".tex"),m.normalize(b,".tex"))
    def test_distinct_questions(self):
        a=b"\\begin{document}x^2\\end{document}"
        b=b"\\begin{document}x^3\\end{document}"
        self.assertNotEqual(m.normalize(a,".tex"),m.normalize(b,".tex"))
    def test_matching_tokens(self):
        self.assertEqual(m.shingles("abcdefgh" * 100),m.shingles("abcdefgh" * 100))
        self.assertNotEqual(m.shingles("abcdefgh" * 100),m.shingles("xyzuvw" * 140))
if __name__=="__main__":
    unittest.main()
