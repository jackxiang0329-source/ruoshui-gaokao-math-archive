# 高考数学：独立复核证明合订本

原 14 份 Markdown 原样合订，各题使用独立锚点。
完整审核对象及卷别由复核溯源 JSON 跟踪；对应每道题的 TeX 继续单独保存。

## 目录

- [2010-anhui-liberal-q20](#2010-anhui-liberal-q20)
- [2010-beijing-science-q18](#2010-beijing-science-q18)
- [2011-anhui-derivative-common](#2011-anhui-derivative-common)
- [2013-fujian-science-q17](#2013-fujian-science-q17)
- [2014-anhui-common-q](#2014-anhui-common-q)
- [2014-chongqing-liberal-q19](#2014-chongqing-liberal-q19)
- [2019-national2-liberal-q21](#2019-national2-liberal-q21)
- [2023-beijing-q20](#2023-beijing-q20)
- [2023-national-b-liberal-q20](#2023-national-b-liberal-q20)
- [2023-new-gaokao-1-q19](#2023-new-gaokao-1-q19)
- [2024-two-proofs](#2024-two-proofs)
- [2025-beijing-q20-transcription-audit](#2025-beijing-q20-transcription-audit)
- [2025-national2-q18](#2025-national2-q18)
- [2025-shanghai-q19](#2025-shanghai-q19)

---

## 2010-anhui-liberal-q20

原文件：derivative/reviewed/2010-anhui-liberal-q20.md；原始 SHA：8baec191da72cb3811715af8babfc593861e5b3c

# 2010 年安徽文科卷第 20 题：单调与极值（数学独立复核）

上游题目：[2010 安徽文科第 20 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2010/anhui_liberal.tex#L426)。数学核验对照上游完整题干完成，保留原题版权归属。

已知函数 \(f(x)=\sin x-\cos x+x+1\)，定义域 \(0<x<2\pi\)。

## 导数及全部驻点

\[
f'(x)=\cos x+\sin x+1=1+\sqrt2\sin\left(x+\frac\pi4\right).
\]

在开区间 \((0,2\pi)\) 中，方程 \(f'(x)=0\) 只有两个解：
\[
x=\pi,\qquad x=\frac{3\pi}{2}.
\]
因为三角方程是 \(\sin(x+\pi/4)=-1/\sqrt2\)，所有满足指定区间的解恰是上述两点。

在三个区间 \((0,\pi)\)、\((\pi,3\pi/2)\)、\((3\pi/2,2\pi)\) 中，导函数符号依次为正、负、正（可分别取 \(\pi/2\)、\(5\pi/4\)、\(7\pi/4\) 验证）。

所以 \(f\) 在 \((0,\pi)\) 及 \((3\pi/2,2\pi)\) 上严格递增，在 \((\pi,3\pi/2)\) 上严格递减。

## 极值

在 \(x=\pi\) 处由增转减，取得严格极大值
\[
f(\pi)=\pi+2.
\]
在 \(x=3\pi/2\) 处由减转增，取得严格极小值
\[
f(3\pi/2)=\frac{3\pi}{2}.
\]

定义域端点不属于函数定义域，不能计作极值点。

**复核项：**原题与卷号、定义域、全部驻点、导数符号、单调区间、极值点和极值函数值均已独立核对。

**状态：**math-checked；对应 TeX 尚未编译，不标记 latex-compiled。

---

## 2010-beijing-science-q18

原文件：derivative/reviewed/2010-beijing-science-q18.md；原始 SHA：f59c9021843fb466ec270ca33165025c2a985d72

# 2010 北京卷理科第 18 题：含参对数函数的完整单调性讨论

[原题 LaTeX 固定版本](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2010/beijing_science.tex#L352) · 状态：**math-checked**（不是 LaTeX 编译通过）

对函数
\[
 f_k(x)=\ln(1+x)-x+\frac{k}{2}x^2,\qquad k\ge0,
\]
首先明确**定义域为 \(x>-1\)**。

## 1. 当 \(k=2\) 时求切线

\[
f_2(1)=\ln 2,\qquad f_k'(x)=\frac1{1+x}-1+kx,
\qquad f_2'(1)=\frac32.
\]
故曲线在点 \((1,\ln 2)\) 的切线为
\[
\boxed{y-\ln2=\tfrac32(x-1)}.
\]

## 2. 按参数分类讨论单调性

对全部 \(x>-1\)，有
\[
f_k'(x)=\frac{x(kx+k-1)}{1+x},
\]
分母恒为正。不能只根据驻点数判断，应检查符号：

1. **\(k=0\)**：\(f_0'(x)=-x/(1+x)\)，故在 \((-1,0)\) 严格递增，在 \((0,+\infty)\) 严格递减。
2. **\(0<k<1\)**：记 \(r=(1-k)/k>0\)。在 \((-1,0)\)、\((0,r)\)、\((r,+\infty)\) 导数依次为正、负、正。因此递增区间为 \((-1,0)\)、\((r,+\infty)\)，递减区间为 \((0,r)\)。
3. **\(k=1\)**：\(f_1'(x)=x^2/(1+x)\ge0\)，仅在 \(x=0\) 为零。由导函数在每个非退化子区间内均严格为正的点构成的开区间非空，可用中值定理证明函数在 **整个 \((-1,+\infty)\) 严格递增**。这是易误判边界。
4. **\(k>1\)**：\(r=(1-k)/k=-1+1/k\in(-1,0)\)。导数在 \((-1,r)\)、\((r,0)\)、\((0,+\infty)\) 依次为正、负、正。故递增区间是 \((-1,r)\)、\((0,+\infty)\)，递减区间是 \((r,0)\)。

## 独立检查

- [x] 对数定义域及 \(k\ge0\)；
- [x] 切线点是否在定义域；
- [x] 导数因式分解；
- [x] \(k=0\)、\(0<k<1\)、\(k=1\)、\(k>1\) 四类；
- [x] 根 \(r\) 的相对位置和全部符号区间；
- [x] \(k=1\) 单点导数为零不妨碍严格单调；
- [ ] 新 TeX 尚未实际编译，不能标记 \`latex-compiled\`。

原题与上游解答供定位；本文件为独立推导，不代表整卷已审定。

---

## 2011-anhui-derivative-common

原文件：derivative/reviewed/2011-anhui-derivative-common.md；原始 SHA：c1f3333295c78baa1f18c1e8322f31909336dd00

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

---

## 2013-fujian-science-q17

原文件：derivative/reviewed/2013-fujian-science-q17.md；原始 SHA：43aa680deabc0a577df8c35b23791863fd6ab724

# 2013 福建卷理科第 17 题：切线与极值存在性

[固定版本原题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2013/fujian_science.tex#L356) · 状态：**math-checked**（数学通过；新 TeX 未编译）

题目中的函数为
\[
f_a(x)=x-a\ln x,\qquad a\in\mathbb R,\quad x>0.
\]

## 1. 当 \(a=2\) 时的切线

求导可得
\[
f_a'(x)=1-\frac a x=\frac{x-a}{x}.
\]
在 \(a=2\)、\(x=1\) 时，\(f_2(1)=1\)，\(f_2'(1)=-1\)。故切线为
\[
y-1=-(x-1),\qquad \boxed{x+y-2=0}.
\]

## 2. 所有实参数的极值

分母 \(x>0\) 始终正，故只需要看 \(x-a\) 的符号。

- **\(a\le0\)**：对于每个 \(x>0\)，\(x-a>0\)。函数严格递增，没有极值点。
- **\(a>0\)**：\(x=a\) 是定义域内唯一驻点，导数在 \((0,a)\) 为负、在 \((a,\infty)\) 为正；所以存在唯一的**严格极小值点** \(x=a\)，极小值为
\[
\boxed{f_a(a)=a-a\ln a}.
\]
不存在极大值。

这里必须限定 **\(a>0\)** 才能将 \(x=a\) 称为函数极值点；否则驻点甚至不在定义域。

## 独立检查

- [x] \(\ln x\) 的定义域；
- [x] 切线斜率与通过的点；
- [x] \(a\le0\) 与 \(a>0\) 完备分类；
- [x] 驻点仅在 \(a>0\) 时有效；
- [x] 极值点及极值函数值；
- [ ] 新 TeX 待编译。

---

## 2014-anhui-common-q

原文件：derivative/reviewed/2014-anhui-common-q.md；原始 SHA：dc1dd858832801c956bdf8d5d395a5aa14028d41

# 2014 安徽高考文理卷共同导数题：完整参数端点核验

来源：[安徽文科第 20 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2014/anhui_liberal.tex#L628)、[安徽理科第 18 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2014/anhui_science.tex#L279)。两套卷**题干相同**，所以共享一份独立数学证明，但总索引保留两份卷别记录。

函数
\[
f_a(x)=1+(1+a)x-x^2-x^3,\qquad a>0,
\]
在整个 \(\mathbb R\) 上有定义。要求研究单调性，并在 \([0,1]\) 上**分别指出最大值、最小值在何处取得**。

## 1. 全体实数上的单调性

\[
f_a'(x)=1+a-2x-3x^2=-3(x-\alpha)(x-\beta),
\]
其中
\[
\alpha=\frac{-1-\sqrt{4+3a}}3<0,\qquad
\beta =\frac{-1+\sqrt{4+3a}}3>0.
\]
因此导数符号依次为负、正、负，函数分别在
\((-\infty,\alpha)\) 严格递减，\((\alpha,\beta)\) 严格递增，
\((\beta,\infty)\) 严格递减。

## 2. 在 \([0,1]\) 上的最大值取点

令 \(r=\beta\)。由于 \(r>0\)，并且
\[
r\le1\quad\Longleftrightarrow\quad a\le4,
\]
得出

- **\(0<a<4\)**：在 \(x=r=(-1+\sqrt{4+3a})/3\) 处唯一取得最大值。
- **\(a\ge4\)**：在 \(x=1\) 处唯一取得最大值（\(a=4\) 时 \(r=1\)，两种表述吻合）。

## 3. 在 \([0,1]\) 上的最小值取点

因为 \(f\) 在 \([0,1]\) 先增后减（或全增），内部不存在严格小于两端点的函数值。直接比较
\[
f(0)=1,\qquad f(1)=a
\]
得到**完整充要分类**：
\[
\boxed{\begin{cases}
x=1,&0<a<1,\\
x=0\ \text{或}\ 1,&a=1,\\
x=0,&a>1.
\end{cases}}
\]
\(a=1\) 是非常重要的边界：**两个端点同时取得最小值**，不能只写一个位置。

## 4. 上游解析的明确质量问题

已对照两个来源的完整题干与解答：

- 文科版本在最小值比较 \(f(0)=1,f(1)=a\) 后，结尾仅残留了一个孤立的 \`1\`，**缺少参数分类和完整取点结论**；这是文本/答案完整性问题。
- 理科版本有完整的三段最小值分类，且与独立推导吻合。
- 本仓库不在未经授权的上游文件内擅自改写，而在 \`metadata/quality-findings.json\` 记录这一发现，维持两条固定提交来源。

## 独立检查

- [x] 定义域与 \(a>0\)；
- [x] 导数根符号、单调性；
- [x] 边界 \(a=4\) 的最大值位置；
- [x] 边界 \(a=1\) 的双端点最小值；
- [x] 文、理卷原题一致性与解析版本差异；
- [ ] 新 TeX 未编译。

**状态：**文、理两条来源记录可标 \`math-checked\`，不等于上游两份解析均准确完整。

---

## 2014-chongqing-liberal-q19

原文件：derivative/reviewed/2014-chongqing-liberal-q19.md；原始 SHA：6e3116292e533cdf4741d6527b88a78066c5a3fe

# 2014 重庆卷文科第 19 题：垂直切线、极值与定义域

[固定版本原题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2014/chongqing_liberal.tex#L560) · 状态：**math-checked**（数学通过；新 TeX 未编译）

函数
\[
f_a(x)=\frac{x}{4}+\frac a x-\ln x-\frac32,\quad a\in\mathbb R
\]
的定义域是 \(x>0\)。已知其在 \(x=1\) 处的切线**垂直于**直线 \(y=\tfrac12x\)。

## 1. 求参数

\[
f_a'(x)=\frac14-\frac a{x^2}-\frac1x.
\]
已知直线斜率为 \(1/2\)，所以垂线斜率是 \(-2\)，而非 \(2\) 或 \(-1/2\)。
由
\[
f_a'(1)=\frac14-a-1=-2
\]
严格得到
\[
\boxed{a=\frac54}.
\]

## 2. 讨论单调性和极值

代入上述参数，
\[
f'(x)=\frac{x^2-4x-5}{4x^2}
=\frac{(x-5)(x+1)}{4x^2}.
\]
在定义域内 \(x+1>0\)，分母也始终为正，因此 \(f'\) 在 \((0,5)\) 为负、在 \((5,\infty)\) 为正。函数先严格递减后严格递增。

唯一极小值点为 \(x=5\)，对应极小值
\[
f(5)=\frac54+\frac14-\ln5-\frac32
=\boxed{-\ln5}.
\]
**不存在极大值**；负根 \(x=-1\) 不属于定义域，必须剔除。

## 独立检查

- [x] 对数和倒数的共同定义域；
- [x] 切线垂直条件的斜率；
- [x] 导数表达式及因式分解；
- [x] 排除 \(x=-1\)；
- [x] 单调性、唯一极小值及函数值；
- [ ] 新 TeX 待编译。

---

## 2019-national2-liberal-q21

原文件：derivative/reviewed/2019-national2-liberal-q21.md；原始 SHA：f88bdd6a0b0fd61688e1083b769f29dc9dbfa1b7

# 2019 年全国Ⅱ卷（文科）第 21 题：独立数学复核

**上游题目**：[固定提交版本中的第 21 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2019/national_paper_2_liberal.tex#L418)。本页仅陈述本题必要数学条件和独立推理，未复制原题整套试卷。

**已确认内容**：对函数
\[
f(x)=(x-1)\ln x-x-1,\qquad x>0,
\]
有且仅有一个极值点（严格极小值点），且方程 \(f(x)=0\) 恰有两个互为倒数的正实数根。

## 1. 定义域、导数与极值点的唯一性

必须首先限定 \(x>0\)。直接计算：
\[
f'(x)=\ln x-\frac1x,\qquad
f''(x)=\frac1x+\frac1{x^2}=\frac{x+1}{x^2}>0\quad(x>0).
\]
所以 \(f'\) 在整个定义域内严格递增。另一方面，
\[
f'(1)=-1<0,\qquad f'(e)=1-e^{-1}>0.
\]
由连续性和严格单调性，存在唯一 \(\alpha\in(1,e)\)，满足 \(f'(\alpha)=0\)。因此 \(f\) 在 \((0,\alpha)\) 上严格递减，在 \((\alpha,+\infty)\) 上严格递增，\(\alpha\) 是唯一的极值点，且为严格极小值点。

## 2. 方程的两个零点

有 \(f(1)=-2<0\)。在左端，
\[
\lim_{x\to0^+}f(x)=+\infty,
\]
因为 \((x-1)\ln x\to+\infty\)。在右端，
\[
\lim_{x\to+\infty}f(x)=+\infty,
\]
因为 \((x-1)\ln x-x-1=x(\ln x-1)-\ln x-1\to+\infty\)。

由介值定理和前一节的严格单调性，在 \((0,1)\) 内恰有一个根 \(u\)，在 \((\alpha,+\infty)\) 内恰有一个根 \(v\)，且在其他区间无根。

## 3. 两根互为倒数

对每个 \(x>0\)，利用 \(\ln(1/x)=-\ln x\) 可直接验算恒等式
\[
f(1/x)=\frac{f(x)}{x}.
\]
由 \(f(u)=0\) 得 \(f(1/u)=0\)。因为 \(u\in(0,1)\)，所以 \(1/u>1\)。函数在 \((1,\alpha]\) 严格下降且 \(f(1)<0\)，不存在零点；故 \(1/u=v\)。于是
\[
\boxed{uv=1}.
\]

## 复核清单

- [x] 定义域 \(x>0\)；
- [x] \(f'\) 与 \(f''\) 的符号、严格性；
- [x] 极值点存在性和唯一性（不是仅声称“驻点唯一”）；
- [x] 两端极限及恰有两个实根；
- [x] \(f(1/x)=f(x)/x\) 的恒等式和两根对应关系；
- [x] 原题年份、卷别、题号、源码起始行核对；
- [ ] 未提供独立 PDF 编译证明；该页为 Markdown 数学证明，未生成本地文件。

**状态**：`math-checked`（数学独立复核通过），不是 `latex-compiled` 或整卷质检通过。

**许可提示**：保留上游来源与其许可证，原始试题及其附属素材的版权须按原授权判断。

---

## 2023-beijing-q20

原文件：derivative/reviewed/2023-beijing-q20.md；原始 SHA：198dfd49ced89b60cb1e80ad00685614c1c27394

# 2023 北京卷第 20 题：独立完整证明

**固定题源：**[2023 北京卷第 20 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2023/beijing.tex#L627)（固定版本第 627 行）。
**审核状态：数学独立核验完成；TeX 尚未实际编译。**

题设：$f(x)=x-x^3e^{ax+b}$ 在 $x=1$ 处的切线为 $y=-x+1$。求 $a,b$，讨论 $g=f'$ 的单调区间，并确定 $f$ 的极值点个数。定义域为整个实数域。

## 一、参数

由切线方程有 $f(1)=0$，$f'(1)=-1$。又
$$
f'(x)=1-(3x^2+ax^3)e^{ax+b}.
$$
所以 $e^{a+b}=1$，$1-(3+a)e^{a+b}=-1$，即
$$
\boxed{a=-1,\quad b=1}.
$$

## 二、单调区间

令 $g(x)=f'(x)$，直接独立求导得
$$
g(x)=1-x^2(3-x)e^{1-x},\qquad
g'(x)=-x(x^2-6x+6)e^{1-x}.
$$
设 $\alpha=3-\sqrt3$，$\beta=3+\sqrt3$，则
$0<\alpha<3<\beta$，而 $e^{1-x}>0$ 恒成立。因子
$-x(x-\alpha)(x-\beta)$ 在区间
$(-\infty,0)$、$(0,\alpha)$、$(\alpha,\beta)$、$(\beta,\infty)$
依次为正、负、正、负。

因此 $g$ 在 $(-\infty,0)$ 和 $(\alpha,\beta)$ 上严格递增，
在 $(0,\alpha)$ 和 $(\beta,\infty)$ 上严格递减。

## 三、极值点个数：存在性、唯一性及变号

计算
$$
g(-1)=1-4e^2<0,\quad g(0)=1>0,\quad
g(1)=-1<0,\quad g(3)=1>0.
$$
注意 $1<\alpha$，并且 $g$ 在 $(0,\alpha)$ 上严格递减，
因此 $g(\alpha)<g(1)<0$。

由连续性及上述严格单调性，$g$ 在 $(-1,0)$ 恰有一个零点
$r_1$（由负变正），在 $(0,1)$ 恰有一个零点 $r_2$
（由正变负），在 $(\alpha,3)$ 恰有一个零点 $r_3$
（由负变正）。三个区间分别处于 $g$ 的严格单调区间中，
故不会在这些单调区间内产生其他零点。

当 $x\ge3$ 时，$x^2(3-x)\le0$，故 $g(x)\ge1>0$，
不存在遗漏的零点。由此 $g$ 在全体实数上恰有上述三个零点，
且均变号；故 $f$ 有两个极小值点、一个极大值点，即
$$
\boxed{\text{$f$ 恰有 3 个极值点。}}
$$

### 严格质检

- [x] 切点函数值及切线斜率两个条件同时使用。
- [x] $f'$ 和 $g'$ 独立求导，并核对系数与指数。
- [x] 四段严格单调性、临界点、边界 $x=3$ 已核对。
- [x] 零点均有连续性、唯一性和两侧变号的证明。
- [x] 数值交叉检查：零点约为 $-0.289374$、$0.488667$、$2.305838$；严格证明不依赖小数。
- [ ] 未实际执行 XeLaTeX；未核验权威原卷 PDF 影像、版权及第三方材料完整正确性。

---

## 2023-national-b-liberal-q20

原文件：derivative/reviewed/2023-national-b-liberal-q20.md；原始 SHA：d5d4ca6cc7c7c9ac1883df7d74c8617ea88afd94

# 2023 全国乙卷文科第 20 题：导数、切线与最小参数

**原题：**[固定版本 LaTeX](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2023/national_paper_b_liberal.tex#L246)。**状态：数学独立核验完成；未经 TeX 编译。**

已核对题干：$x>0$，$f_a(x)=(1/x+a)\ln(1+x)$；(1) $a=-1$ 时在 $x=1$ 处求切线；(2) 求 $f_a$ 在 $(0,+\infty)$ 单调递增时的全部 $a$。

## 切线

直接求导得
$$
f_a'(x)=-\frac{\ln(1+x)}{x^2}+\frac{1/x+a}{1+x}.
$$
当 $a=-1$，$f_{-1}(1)=0$，$f_{-1}'(1)=-\ln2$，故
$$
\boxed{y=-(\ln2)(x-1)}.
$$

## 全域递增的必要充分条件

整理为
$$
f_a'(x)=\frac{a-G(x)}{1+x},\qquad
G(x)=\frac{(1+x)\ln(1+x)-x}{x^2},\quad x>0.
$$
设
$$
H(x)=\frac{x^2}{2}+x-(1+x)\ln(1+x).
$$
则 $H(0)=0$，且 $H'(x)=x-\ln(1+x)>0$（$x>0$），因此
$$
G(x)<\frac12\quad(x>0).
$$
再对分子连续两次应用洛必达法则，或者在 $x=0$ 作二阶泰勒展开，可得
$$
\lim_{x\to0^+}G(x)=\frac12.
$$
故 $\sup_{x>0}G(x)=1/2$，但上确界不在定义域内取到。

若 $a\ge1/2$，对每个 $x>0$ 都有 $a>G(x)$，故 $f_a'(x)>0$，函数严格递增。若 $a<1/2$，极限性质保证存在足够小的 $x>0$ 使 $G(x)>a$，从而导数为负，违反全域单调递增。综上
$$
\boxed{a\in[\frac12,+\infty)}.
$$

### 检查

- [x] 函数只在 $x>0$ 有定义，不把 $x=0$ 作为取值点。
- [x] 求导和切线坐标正确。
- [x] 临界参数 $a=1/2$ 必须包含；导数在定义域始终正。
- [x] 上确界为 $1/2$ 且只作为右端极限达到。
- [ ] 尚未进行 XeLaTeX 编译；不宣称整个上游题解无误。

---

## 2023-new-gaokao-1-q19

原文件：derivative/reviewed/2023-new-gaokao-1-q19.md；原始 SHA：6fb7bb3c0f7c3ed3391a6866a7ea9a261cf13d7d

# 2023 新高考Ⅰ卷第 19 题：指数函数单调与参数不等式

**原题：**[固定版本 LaTeX](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2023/new_gaokao_paper_1.tex#L554)。**状态：数学独立核验完成；尚未编译。**

题干函数为
$$
f_a(x)=a(e^x+a)-x,\qquad a\in\mathbb R,\quad x\in\mathbb R.
$$

## （1）单调性

$$
f_a'(x)=ae^x-1.
$$
若 $a\le0$，则 $ae^x\le0$，$f_a'(x)<0$，故函数在全实数上严格递减。

若 $a>0$，导函数恰在 $x_*=-\ln a$ 为零；当 $x<x_*$ 时 $f_a'<0$，当 $x>x_*$ 时 $f_a'>0$。故在 $(-\infty,-\ln a)$ 严格递减，在 $(-\ln a,\infty)$ 严格递增，且有唯一严格极小值
$$
f_a(-\ln a)=1+a^2+\ln a.
$$

## （2）当 $a>0$ 时的严格不等式

须证对于 **所有实数 $x$**，$f_a(x)>2\ln a+\tfrac32$。由最小值公式，足以证明
$$
a^2-\ln a-\frac12>0.
$$
令 $G(a)=a^2-\ln a-\frac12$（$a>0$），则
$$
G'(a)=2a-\frac1a=\frac{2a^2-1}{a}.
$$
$G$ 在 $(0,1/\sqrt2)$ 递减、在 $(1/\sqrt2,\infty)$ 递增，因此
$$
G(a)\ge G(1/\sqrt2)=\ln\sqrt2>0.
$$
故有严格链式估计
$$
\boxed{f_a(x)\ge1+a^2+\ln a>2\ln a+\frac32}.
$$

### 检查

- [x] $a=0$ 属于严格递减情形。
- [x] $a>0$ 才能使用 $\ln a$ 与唯一极小值点。
- [x] 不等式是对所有 $x\in\mathbb R$，并且末步保证**严格大于**。
- [x] 参数辅助函数在端点 $a\to0^+,\infty$ 的行为与唯一最小值一致。
- [ ] 未执行 XeLaTeX 编译。

---

## 2024-two-proofs

原文件：derivative/reviewed/2024-two-proofs.md；原始 SHA：ff6564db529ca6d4519ae84fb6f5a9dc6147aad1

# 2024 新高考两道导数解答题（独立复核）

本次只包含 2024 年新高考Ⅰ卷第 18 题与新高考Ⅱ卷第 16 题的独立重写分析及来源链接。不等同于高考试卷原文复刻。完整 TeX 在 `2024-derivative-two-proofs.tex`，本地编译生成同名 PDF。

## 2024 新高考Ⅰ卷第 18 题

设 \(f(x)=\ln\frac{x}{2-x}+ax+b(x-1)^3\), \(x\in(0,2)\)。分析导数非负的参数范围、中心对称性和 \(f(x)>-2\) 恰在 \(x>1\) 的取值条件。

1. 当 \(b=0\) 时 \(f'(x)=\frac{2}{x(2-x)}+a\)，且 \(x(2-x)\le1\)，因此 \(a\ge -2\)，最小值 **−2**。
2. \(f(2-x)=2a-f(x)\)，所以图像中心为 **\((1,a)\)**。
3. 连续性给出 \(f(1)=-2\)，故 \(a=-2\)。令 \(t=x-1\)，有 \(H_b(t)=\ln\frac{1+t}{1-t}-2t+bt^3\)（奇函数）。令 \(R(t)=H_{-2/3}(t)\)，则 \(R(0)=0\) 且 \(R'(t)=\frac{2t^4}{1-t^2}>0\)（\(0<t<1\)）。结合 \(\lim_{t\to0^+}H_b(t)/t^3=b+2/3\)，得到充要条件 **\(b\ge-2/3\)**。

源码：<https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2024/new_gaokao_paper_1.tex#L537>

## 2024 新高考Ⅱ卷第 16 题

设 \(f(x)=e^x-ax-a^3\)。

1. \(a=1\) 时，切线 **\(y=(e-1)x-1\)**。
2. \(a\le0\) 时没有极小值；当 \(a>0\) 时 \(f''(x)>0\)，唯一极小值点在 \(x=\ln a\)，极小值为 \(a(1-\ln a-a^2)\)。由于 \(a^2+\ln a-1\) 在 \(a>0\) 严格递增且在 \(a=1\) 为零，所以极小值严格为负的充要条件是 **\(a>1\)**。

源码：<https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2024/new_gaokao_paper_2.tex#L448>

## 质检状态

- 原题出处及题号：已对照上游 LaTeX 题目结构确认。
- 计算与参数端点：已独立推导核验。
- TeX 排版：XeLaTeX 双轮编译，另行记录构建日志。
- 第三方原试题的权利范围：未独立确权；不要将本资料的原创证明许可解释为原始高考试题版权授权。

上游贡献者及许可证说明：<https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/main/LICENSE>。

---

## 2025-beijing-q20-transcription-audit

原文件：derivative/reviewed/2025-beijing-q20-transcription-audit.md；原始 SHA：9089f5ed41283ffde55770fef5dd06348654903f

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

---

## 2025-national2-q18

原文件：derivative/reviewed/2025-national2-q18.md；原始 SHA：cf58802a96e8f3b6d36e342040318a409a656eab

# 2025 全国Ⅱ卷第 18 题：唯一极值、唯一零点与对称差的单调性

**原题：**[固定版本 LaTeX](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2025/national_paper_2.tex#L496)。**状态：数学独立核验完成；尚未编译。**

题干：$0<k<\frac13$，$x>-1$ 时定义
$$
f(x)=\ln(1+x)-x+\frac{x^2}{2}-kx^3.
$$
题目在 $x>0$ 上研究唯一极值点 $x_1$、唯一零点 $x_2$，并讨论 $g(t)=f(x_1+t)-f(x_1-t)$（$0<t<x_1$）。

## 1. 唯一极值点、唯一正零点

$$
f'(x)=\frac1{1+x}-1+x-3kx^2
=x^2\left(\frac1{1+x}-3k\right).
$$
置 $c=\frac1{3k}-1>0$。因 $x>0$ 时 $x^2>0$ 且 $1/(1+x)$ 严格递减，故
$$
f'(x)>0\ (0<x<c),\qquad f'(x)<0\ (x>c).
$$
所以 $x_1=c$ 是唯一极值点，且为严格极大值点。

函数在 $[0,+\infty)$ 连续并有 $f(0)=0$。由 $f'>0$ 得 $f(c)>0$；又因负三次项占优，$\lim_{x\to\infty}f(x)=-\infty$。$f$ 在 $(c,\infty)$ 严格递减，因此存在唯一 $x_2>c$ 使 $f(x_2)=0$。**$x=0$ 虽也是零点，但不属于题目要求的开区间 $(0,\infty)$**，不可把它误计入。

## 2. $g(t)$ 严格递减

特别注意链式法则的符号：
$$
g'(t)=f'(c+t)+f'(c-t),
$$
**不是** $f'(c+t)-f'(c-t)$。

令 $H(x)=\frac{x^2}{1+x}$，对于 $x>0$，
$$
H'(x)=\frac{x(x+2)}{(1+x)^2}>0.
$$
利用 $3k=1/(1+c)$ 和
$$
f'(x)=\frac{x^2(c-x)}{(1+x)(1+c)},
$$
得到
$$
g'(t)=\frac{t}{1+c}\bigl[H(c-t)-H(c+t)\bigr]<0
\quad(0<t<c),
$$
因为 $0<c-t<c+t$ 且 $H$ 严格递增。所以 $g$ 在 $(0,c)$ 严格递减。

## 3. 比较 $2x_1$ 与 $x_2$

由 $g(0)=0$（连续延拓）及 $g$ 严格递减，
$$
g(c)=f(2c)-f(0)=f(2c)<0.
$$
结合 $f(c)>0$ 及 $f$ 在 $(c,\infty)$ 严格递减，唯一正零点满足
$$
\boxed{x_1=c<x_2<2c=2x_1}.
$$
这是严格不等式，两个端点均不能取等号。

### 上游源码勘误与检查

上游解答有一行把 $g'(t)$ 误写为 $f'(c+t)-f'(c-t)$，随后实际运算却是正确的**加号**。本证明已修正并登记到质量问题清单；不因此认定题目或最终答案错误。

- [x] 参数范围 $0<k<1/3$ 与 $c>0$。
- [x] $x=0$ 不属于题目要求的正零点。
- [x] 两个导数符号区间及唯一性。
- [x] 差函数链式法则、$H$ 的严格单调性。
- [x] $x_2<2x_1$ 的严格性及边界。
- [ ] 尚未执行 XeLaTeX 编译。

---

## 2025-shanghai-q19

原文件：derivative/reviewed/2025-shanghai-q19.md；原始 SHA：c654f2b75bb52addf90ec7029c6dd602a4a72e5f

# 2025 上海卷第 19 题：含参对数函数的极大值存在性

**原题：**[固定版本 LaTeX](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2025/shanghai.tex#L381)。**状态：数学独立核验完成；尚未编译。**

对 $x>0$，考虑
$$
f_m(x)=x^2-(m+2)x+m\ln x,\qquad m\in\mathbb R.
$$

## （1）附加条件 $f_m(1)=0$ 的不等式

$$
f_m(1)=1-(m+2)=-m-1=0\ \Longrightarrow\ m=-1.
$$
于是
$$
f_{-1}(x)=x^2-x-\ln x.
$$
要求 $f_{-1}(x)\le x^2-1$，等价于 $x+\ln x\ge1$。由于
$$
\frac{\mathrm d}{\mathrm dx}(x+\ln x)=1+\frac1x>0
$$
且 $1+\ln1=1$，解集恰为
$$
\boxed{[1,+\infty)}.
$$

## （2）存在极大值的参数全体

求导并因式分解：
$$
f_m'(x)=2x-(m+2)+\frac m x
=\frac{(2x-m)(x-1)}{x},\quad x>0.
$$
因此仅需比较合法驻点 $1$ 与 $m/2$：

- $m\le0$：$m/2\le0$ 在定义域外，$x=1$ 处导数由负变正，只有极小值。
- $0<m<2$：$0<m/2<1$，导数正、负、正，$x=m/2$ 是严格极大值点。
- $m=2$：$f_m'(x)=2(x-1)^2/x\ge0$；函数严格递增，不存在极大值。这里驻点是重根，**不能只凭 $f'(1)=0$ 判定极值**。
- $m>2$：$1<m/2$，导数正、负、正，$x=1$ 是严格极大值点。

结论：
$$
\boxed{m\in(0,2)\cup(2,+\infty)}.
$$

### 检查

- [x] $\ln x$ 定义域和非法负驻点剔除。
- [x] $f(1)=0$ 的参数推导、等价不等式。
- [x] $m=0,m=2$ 两个易错端点。
- [x] 导数二次因式分解与每类符号表。
- [ ] 未执行 XeLaTeX 编译。

