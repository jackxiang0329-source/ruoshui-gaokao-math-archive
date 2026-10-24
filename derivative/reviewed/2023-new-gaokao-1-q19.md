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
