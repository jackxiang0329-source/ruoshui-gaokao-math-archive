# 2025 北京卷第20题：直线标号顺序的转录冲突

上游固定来源：[LaTeX 题目及答案](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2025/beijing.tex#L432)。

公开文本交叉参照：
- https://kaosj.com/papers/2025/06/2025-beijing-gaokao-math-paper/
- https://www.yeyulingfeng.com/wendang/166251.html

本条是**题目转录与解析一致性审计**，不是对该题全部小问的数学验收。总索引先保留 source-identified，直到取得可靠的原卷影像。

## 问题

上游 LaTeX 题干第三问按 $l_2,l_1$ 顺序分别对应 $x_1,x_2$；但其解答实际按 $l_1,l_2$ 顺序算出两横截距。两个公开的试卷文字版本则均给出 $l_1,l_2$ 的次序。这是**上游题干与解答内部不一致**，不能在未经原卷影像核对时声称试卷原题错误。

## 独立核算：两种标号导致相反的结果

由已知 $f'(x)=\ln(1+x)/(1+x)$、$f(0)=0$，得到
$$
f(x)=\frac12\ln^2(1+x),\qquad x>-1.
$$
对 $a>0$，令
$$
b=\frac{\ln(1+a)}{1+a}>0,\qquad A=f(a)=\frac12\ln^2(1+a)>0.
$$
则切线 $l_1$ 为 $y=A+b(x-a)$，垂线 $l_2$ 为 $y=A-(x-a)/b$，因此各自的**实际**横截距为
$$
T=a-\frac{A}{b}=a-\frac{(1+a)\ln(1+a)}2 \quad(l_1),
$$
$$
N=a+Ab=a+\frac{\ln^3(1+a)}{2(1+a)}\quad(l_2).
$$
并且 $b'(a)=[1-\ln(1+a)]/(1+a)^2$，故 $0<b\le1/e$，最大值在 $a=e-1$ 取得。

**若遵照公开转录及上游答案的顺序**，即 $x_1=T,x_2=N$：
$$
\frac{2a-x_1-x_2}{x_2-x_1}
=\frac{1-b^2}{1+b^2}
\in\boxed{\left[\frac{e^2-1}{e^2+1},\,1\right)}.
$$

**若按当前上游 LaTeX 题干的字面顺序**，即 $x_1=N,x_2=T$：
$$
\frac{2a-x_1-x_2}{x_2-x_1}
=\frac{b^2-1}{1+b^2}
\in\boxed{\left(-1,\,-\frac{e^2-1}{e^2+1}\right]}.
$$

两个答案只差下标次序，但符号完全相反。不能忽略这个差异。

## 复核状态与剩余工作

- [x] 已核对上游原题与解析中分别写出的标号顺序。
- [x] 已直接核算两条直线的横截距及对应值域。
- [x] 公开试卷文字版本的顺序与上游解答相符。
- [ ] 尚未获得权威原卷扫描图像确认下标位置。
- [ ] 本题全部三问尚未完成独立数学质检，亦未实际编译 TeX。

处理：原题索引保持 source-identified；将此项记入源文件转录勘误，避免静默发布含混答案。
