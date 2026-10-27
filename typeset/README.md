# 高考数学 · 历年试卷 XeLaTeX 统一精排

主分支原有的 775 份 PDF 不修改、不删除。完整来源分支有 777 份逐卷 TeX，分布于 64 个收录年份；2007 年大纲卷 II 文理两份额外 TeX 不属于已确认的一对一原 PDF 对照。

## 样式与构建

XeLaTeX / A4，中文 Fandol 宋体、TeX Gyre Termes 英文字体与数学字体，左右 22mm、上下 24mm，统一试卷章标题、页眉、页码、段距；沿用已固定上游的数学题干和插图，答案默认隐藏。原始 TeX 不直接改写，只在 Actions 临时目录替换原项目要求的专有系统字体。

工作流：GitHub Actions > XeLaTeX typeset archived Gaokao maths by year > Run workflow。year 留空时自动选尚未构建的最近年份。每次生成当年所有试卷的一册 PDF（annual/）、可追溯 TeX 入口（tex/）、检查报告（reports/）。后续再按原始 775 份 PDF 的独立卷别拆册，**不能将年册误称为 775 份逐卷 PDF**。

正式发布前必须通过原图存在性、试题 TeX 环境数量、XeLaTeX 实际编译、PDF 页数、可提取文本及字体缺字检测。通过不等于 PDF 逐页视觉、原卷真实性或数学证明全部通过。第三方图片权利需另外核对。

署名：DxAThing/Gaokao-Math-Problems-Compilation（其原创整理部分 CC BY-SA 4.0），原来源 deekur/gaokaomath（适用部分 CC BY 4.0）；原始试题和图片并不必然处于这些许可之下。

## 逐卷文件

通过 PDF 书签章节和年度 TeX 索引自动切分为 papers/YYYY/ 内逐卷 PDF 与 TeX。全部页码必须恰好覆盖，来源数量与 PDF 章数不一致则阻止发布。卷与原始 775 份 PDF 的逐一对应状态尚待人工核对，逐卷拆分版暂沿用年册页码。
