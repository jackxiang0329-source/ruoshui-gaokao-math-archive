# 2011 年新课标全国卷文理科第 21 题：变式的独立数学复核

## 固定上游来源与题目关系

- [理科第 21 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2011/new_curriculum_science.tex#L583)：第一问求 \(a,b\)，第二问求恒成立不等式中的参数 \(k\) 的范围。
- [文科第 21 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2011/new_curriculum_liberal.tex#L473)：第一问相同，第二问只需证明理科中 \(k=0\) 的特殊情形。

两题属于 **confirmed_variant**，而非完全同题。保留两条来源记录；同一份证明分别覆盖理科一般情形与文科特殊情形。配套独立编译源码：[2011-newcurriculum-q21-variants.tex](2011-newcurriculum-q21-variants.tex)。

## （1）求 \(a,b\)

设
\[
f(x)=a\frac{\ln x}{x+1}+\frac{b}{x},\quad x>0.
\]
曲线在 \((1,f(1))\) 处的切线为 \(x+2y-3=0\)，即 \(y=(3-x)/2\)。切点纵坐标为 \(1\)，斜率为 \(-1/2\)。

因为
\[
f(1)=b,\qquad
f'(x)=a\frac{(x+1)/x-\ln x}{(x+1)^2}-\frac b{x^2},
\]
所以 \(b=1\)，且 \(f'(1)=a/2-b=-1/2\)，即
\[
\boxed{a=b=1}.
\]
反向代入时函数值及斜率均满足指定切线，解为充要。

## （2）理科参数 \(k\) 的充分必要条件

对 \(x>0\) 且 \(x\ne1\)，代入 \(a=b=1\) 并整理：
\[
\begin{aligned}
D_k(x)
&=f(x)-\frac{\ln x}{x-1}-\frac{k}{x}\\
&=\frac{1-k}{x}-\frac{2\ln x}{x^2-1}
=\frac{H(x)-k}{x},
\end{aligned}
\]
其中
\[
H(x)=1-\frac{2x\ln x}{x^2-1}
=\frac{N(x)}{x^2-1},\qquad
N(x)=x^2-1-2x\ln x.
\]

首先证明 **\(H(x)>0\)**。有 \(N(1)=0\)，并且
\[
N'(x)=2(x-1-\ln x).
\]
由基本不等式 \(\ln x\le x-1\)（等号仅 \(x=1\)），可知 \(N'(x)>0\) 在 \(x>0,\ x\ne1\) 时成立。因此 \(N\) 在整个 \((0,\infty)\) 上严格递增（虽然 \(N'(1)=0\)，但不影响严格递增）。于是
\[
N(x)<0\ (0<x<1),\qquad N(x)>0\ (x>1).
\]
由于分母 \(x^2-1\) 同号，得到
\[
\boxed{H(x)>0\quad (x>0,\ x\ne1)}.
\]

其次计算 **端点极限**。洛必达法则给出
\[
\lim_{x\to1}H(x)
=1-\lim_{x\to1}\frac{2x\ln x}{x^2-1}
=1-\lim_{x\to1}\frac{2(\ln x+1)}{2x}
=0.
\]

- **充分性：**如果 \(k\le0\)，那么 \(H(x)-k>0\) 对所有 \(x>0,\ x\ne1\) 恒成立，因 \(x>0\)，所以 \(D_k(x)>0\)。
- **必要性：**如果 \(k>0\)，由于 \(H(x)\to0\)（\(x\to1\)），存在足够接近但不等于 \(1\) 的 \(x>0\)，使 \(H(x)<k\)，此时 \(D_k(x)<0\)，与题设矛盾。

故理科答案是
\[
\boxed{k\in(-\infty,0]}.
\]

## （3）文科第二问

取理科结果中的 \(k=0\)。由 \(H(x)>0\) 和 \(x>0\)，严格得到
\[
\boxed{f(x)>\frac{\ln x}{x-1}\quad(x>0,\ x\ne1).}
\]

**数学质检检查点：**求导及切线相切条件；原题域 \(x>0\) 和排除点 \(x=1\)；分子分母同号及严格性；\(k=0\) 边界可以取到；\(k>0\) 的必要性依赖 \(x\to1\) 的极限而非误把 \(x=1\) 当成原定义域内检验点。

**状态：**两条来源记录均可标为 \`math-checked\`，但仍须保留 \`confirmed_variant\` 分组，不得合并为同题。配套 TeX 已在本地通过两遍 XeLaTeX 编译，生成一页 A4 PDF 并进行渲染目视检查。此结论不代表官方试卷影像真伪、第三方再分发许可或者其他试题已经核验。
