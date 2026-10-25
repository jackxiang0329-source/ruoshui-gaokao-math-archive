# 2010 年陕西高考文理第 23 题：独立数学复核

**上游固定版本**：[理科第 23 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2010/shaanxi_science.tex#L500)、[文科第 23 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2010/shaanxi_liberal.tex#L509)。

逐题比较两个来源的全部三问：函数 $f(x)=\sqrt{x}$、$g(x)=a\ln x$、切线条件、最小值函数 $\varphi(a)$、两个均值的不等式完全一致，仅排版和措辞略有不同。保留理科与文科两个来源 ID，合用本数学证明。

## （1）两曲线的公切线

公共定义域为 $x>0$。设交点横坐标为 $t>0$。交点重合和切线斜率相等同时要求
\[
\sqrt t=a\ln t,\qquad \frac1{2\sqrt t}=\frac at.
\]
由第二式得 $a=\sqrt t/2>0$；代回第一式，除以 $\sqrt t>0$ 得 $\ln t=2$，即 $t=e^2$、$a=e/2$。交点为 $(e^2,e)$，斜率为 $1/(2e)$，故
\[
\boxed{y-e=\frac{x-e^2}{2e}}\quad\Longleftrightarrow\quad
\boxed{x-2ey+e^2=0}.
\]
反向代入交点与两个导数，确实均成立，故解充分且必要。

## （2）最小值及参数范围

对 $x>0$，
\[
h(x)=\sqrt{x}-a\ln x,\qquad
h'(x)=\frac{\sqrt{x}-2a}{2x}.
\]

- $a>0$ 时，$h'$ 在 $(0,4a^2)$ 为负，在 $(4a^2,\infty)$ 为正，因此唯一的全局最小值在 $x=4a^2$ 取得，且
  \[
  \boxed{\varphi(a)=h(4a^2)=2a\bigl[1-\ln(2a)\bigr],\quad a>0}.
  \]
- $a=0$ 时，$h(x)=\sqrt{x}>0$ 的下确界是 $0$，但不被定义域内的点取到。
- $a<0$ 时，$h(x)=\sqrt{x}+|a|\ln x$ 在 $x\to0^+$ 趋于 $-\infty$，故没有最小值。

所以**最小值存在当且仅当 $a>0$**。

## （3）导函数的平均数不等式

由上式，在 $t>0$ 时
\[
\varphi'(t)=-2\ln(2t),\qquad
\frac{\varphi'(a)+\varphi'(b)}2
=-\ln(4ab)=\varphi'(\sqrt{ab}).
\]
$\varphi'$ 在 $(0,\infty)$ 上严格递减。又对任意 $a,b>0$，
\[
\frac{2ab}{a+b}\le \sqrt{ab}\le\frac{a+b}{2}.
\]
将这个顺序代入严格递减的 $\varphi'$，不等号反向，即
\[
\boxed{\varphi'\left(\frac{a+b}{2}\right)
\le \frac{\varphi'(a)+\varphi'(b)}{2}
\le\varphi'\left(\frac{2ab}{a+b}\right)}.
\]
两侧等号均当且仅当 $a=b$ 时成立。

**复核项：**两来源原题的全部小问、定义域 $x>0$、交点和斜率的充分必要性、$a\le0$ 的非取到边界、极小值的全局性、均值不等式方向与等号条件。

**文件状态：**数学推导独立审核；配套 TeX 已在本地通过两轮 XeLaTeX 编译及 PDF 页面视觉检查。镜像哈希和数学正确性不证明官方原卷真实性或第三方权利许可。
