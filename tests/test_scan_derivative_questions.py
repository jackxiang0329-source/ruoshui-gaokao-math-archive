import importlib.util
import unittest
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"scripts"/"scan_derivative_questions.py"
spec=importlib.util.spec_from_file_location("scan",p)
scan=importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)

class TestScan(unittest.TestCase):
    def test_numbering_and_section(self):
        tex=r"""\section{单选题}
\begin{problem}函数 $f(x)$ 求导。\end{problem}
\section{解答题}
\begin{problem}设函数 $f(x)=\ln x+ax$，讨论单调性。\end{problem}
\begin{problem}设函数 $f(x)=\ln x$，求曲线的切线。\end{problem}"""
        r=scan.scan_file(tex,"content/2024/new_gaokao_paper_1.tex","deadbeef")
        self.assertEqual([x["question"] for x in r],[2,3])
        self.assertEqual(r[0]["confidence"],"medium")
        self.assertEqual(r[1]["confidence"],"high")

if __name__=="__main__":
    unittest.main()
