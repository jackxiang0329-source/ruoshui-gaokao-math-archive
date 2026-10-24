# 2011 年安徽文理科共同题：指数分式函数（数学独立复核）

上游：[文科第 18 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2011/anhui_liberal.tex#L447)、[理科第 16 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2011/anhui_science.tex#L362)。已对照完整题干，数学表达式和两个小问一致，保留两个原始卷别 ID，使用一份数学证明。

对于 \(a>0\)，定义
\[
f(x)=\frac{e^x}{1+ax^2},\qquad x\in\mathbb R.
\]

## 一、求导与符号

因 \(a>0\)，分母 \(1+ax^2\) 始终为正。求导得到
\[
f'(x)=\frac{e^x(1+ax^2-2ax)}{(1+ax^2)^2}
     =\frac{e^x\{a(x-1)^2+1-a\}}{(1+ax^2)^2}.
\]
所以导数符号等于 \(Q_a(x)=a(x-1)^2+1-a\) 的符号。

## 二、当 a=4/3 时的极值

此时
\[
Q_{4/3}(x)=\frac43\left(x-\frac12\right)\left(x-\frac32\right).
\]
随着 \(x\) 增大，导数依次为正、负、正，因此
\[
x=\frac12\quad\text{是严格极大值点},\qquad
x=\frac32\quad\text{是严格极小值点}.
\]
对应函数值分别为
\[
f(1/2)=\frac{3\sqrt e}{4},\qquad f(3/2)=\frac{e^{3/2}}4.
\]

## 三、全实数上单调的参数范围

当 \(0<a<1\) 时，\(Q_a(x)>0\) 对一切实数成立，故 \(f\) 严格递增。

当 \(a=1\) 时，\(Q_1(x)=(x-1)^2\ge0\)，仅 \(x=1\) 时等于零。由于任意非退化区间内都存在导数严格为正的点，函数在整个实数轴上仍然**严格递增**。不能漏掉这一端点。

当 \(a>1\) 时，\(Q_a(0)=1>0\)，而 \(Q_a(1)=1-a<0\)，导数符号发生变化，故函数不可能在全实数轴单调递增或递减。

结合 \(a>0\)，答案为
\[
\boxed{0<a\le 1}.
\]

**复核项：**文理卷同题关系、定义域、导数符号、两个极值点、边界 \(a=1\)、参数范围的必要性与充分性。

**状态：**文科第 18 题和理科第 16 题均为 math-checked；对应源码尚未完成新的 TeX 编译。
