# 第十轮质检：2011 年新课标文理第 21 题的独立证明（2026-10-25）

## 原题与来源固定

- 上游固定提交：DxAThing/Gaokao-Math-Problems-Compilation，f1ae169b58a75b3db6e35c670b3f0d5c78718188。
- [理科卷第 21 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2011/new_curriculum_science.tex#L583)。
- [文科卷第 21 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2011/new_curriculum_liberal.tex#L473)。
- 第一问相同；理科第二问求参数 k 的充要范围，文科只须证明其中 k=0 的特例。此前已独立比较并确认是变式，不能按一题合并；分别保留来源 ID、题号和行号。
- 本轮新增独立解答：[Markdown](../derivative/reviewed/2011-newcurriculum-q21-variants.md) 和 [XeLaTeX 源码](../derivative/reviewed/2011-newcurriculum-q21-variants.tex)。

## 完整数学结论

设 f(x)=a ln(x)/(x+1)+b/x，在 x=1 处的切线为 x+2y-3=0。由 f(1)=1 与 f'(1)=-1/2 得到 a=b=1。

令 D_k(x)=f(x)-ln(x)/(x-1)-k/x=(H(x)-k)/x，其中 H(x)=(x²-1-2x ln x)/(x²-1)，定义域为 x>0 且 x≠1。记 N(x)=x²-1-2x ln x；因为 N'(x)=2(x-1-ln x)>0（x>0,x≠1），N(1)=0，所以 N(x) 与 x²-1 同号，因此 H(x)>0。另一方面 lim(x→1) H(x)=0。

- k≤0 时 D_k(x)>0 恒成立，满足充分性，包括端点 k=0。
- k>0 时，由 H(x)→0 可在 x=1 附近选 x≠1 满足 H(x)<k，使 D_k(x)<0；故必要性成立。
- 理科答案：**k∈(-∞,0]**。文科只需取 **k=0** 即得严格不等式。

数学警戒点：k=0 时严格大于号仍成立；必要性须在 x≠1 的邻域选取反例，不可直接代入原函数不允许的 x=1。

## XeLaTeX / PDF 实测

- 配套 TeX 连续 **两次 XeLaTeX 编译成功**，生成 **一页 A4 PDF**，日志未检出 Overfull/Underfull 警告。
- PDF 经图片渲染目视核查，文字、公式及页边距完整。
- 本地编译源码与 GitHub 开发分支 TeX 的 Git Blob SHA 均为：0d5402f9e78635453847206008ab4465fb72c09c，确认通过编译的版本与仓库源码一致。
- PDF 二进制文件仅作为本地交付，没有写入 GitHub；仓库保留可复现的 LaTeX 源码。

## 跨文件复核及进度

已更新规范索引、2010—2014 分区 JSON/CSV、两份阅读索引、数学审核溯源、独立证明清单、根 README 和 PDF 手动构建根文件清单。从 GitHub 再次读取并独立交叉复算：

| 审核指标 | 数量 |
|---|---:|
| 固定来源记录 | 248 |
| 2010—2014 / 2015—2019 / 2020—2026 | 127 / 63 / 58 |
| math-checked 来源记录 | 20 |
| 对应不同数学题 | 17 |
| 未完成数学审核的来源记录 | 228 |
| 数学独立证明文档 | 15 |
| 已确认同题 / 变式 / 待复核分组 | 7 / 2 / 12 |

交叉核对规范记录、分区信息、CSV、审核出处和去重分类后，**0 项冲突**。

原始镜像上次严格核验仍是 **1,993/7,222**；本轮不新增来自上游的原始实体文件，故不将新增的证明文件虚报为镜像覆盖数。

## 边界与后续

此前 GitHub Actions 实际运行在没有 Runner steps 的状态失败，本轮远程 CI 不能据此判定通过。数学独立证明不等于官方高考原卷影像鉴真、全部 TeX 编译验收或第三方题目及图片授权已经确认。PR 保留草稿，不自动合并主分支。
