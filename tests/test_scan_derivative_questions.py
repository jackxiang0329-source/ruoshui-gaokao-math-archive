import importlib.util
import unittest
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "scripts" / "scan_derivative_questions.py"
spec = importlib.util.spec_from_file_location("scanner", path)
scanner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scanner)

class TestDerivativeScanner(unittest.TestCase):
    def scan(self, tex):
        return scanner.scan_file(tex, "content/2011/anhui_liberal.tex", "a" * 40)

    def test_global_problem_numbering(self):
        text = r"""\section{选择题}
\begin{problem}设函数 $f(x)$，求导数。\end{problem}
\section{解答题}
\begin{problem}已知函数 $f(x)=\ln x+ax$，讨论单调性。\end{problem}
\begin{problem}已知函数 $f(x)=\ln x$，求曲线在一点的切线。\end{problem}"""
        result = self.scan(text)
        self.assertEqual([r["question"] for r in result], [2, 3])
        self.assertEqual(result[0]["confidence"], "medium")
        self.assertEqual(result[1]["confidence"], "high")
        self.assertEqual(result[0]["line"], 4)

    def test_solution_text_does_not_trigger_candidate(self):
        text = r"""\section{解答题}
\begin{problem}设函数 $f(x)=x^2$，求 $f(1)$。
\begin{solution}由导数和极值可知答案是 1。\end{solution}
\end{problem}"""
        self.assertEqual(self.scan(text), [])

    def test_no_geometry_tangent_false_positive(self):
        text = r"""\section{解答题}
\begin{problem}已知圆 $C: x^2+y^2=1$，求圆的切线方程。\end{problem}"""
        self.assertEqual(self.scan(text), [])

    def test_elective_is_excluded(self):
        text = r"""\section{选考题：解答题}
\begin{problem}设函数 $f(x)=e^x$，求切线方程。\end{problem}"""
        self.assertEqual(self.scan(text), [])

    def test_explicit_derivative(self):
        text = r"""\section{解答题}
\begin{problem}设函数 $f(x)=x^3+ax$，求导数和极值点。\end{problem}"""
        rows = self.scan(text)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["status"], "machine-candidate-not-reviewed")

if __name__ == "__main__":
    unittest.main()
