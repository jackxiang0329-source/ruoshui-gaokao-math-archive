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