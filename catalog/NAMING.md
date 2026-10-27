# 高考数学试卷命名与去重规范

2026-10-27 主分支整理：将 **775 份**可确认年份的高考试卷 PDF 统一改名并按年份存入 `papers/YYYY/`；另外移除 **91 份** SHA 完全相同且有保留副本的 PDF。**2 份**目录年份与文件名不一致，暂不更名，见 [核验清单](naming_review.csv)。

统一文件名：`gaokao-YYYY-<地区或卷别>-<general|liberal|science>[-spring]-paper.pdf`。旧课程、延期考试、初试等特殊差异尽量在中段明确体现；所有适用省份和原始文件名仍由映射保留。

[原始路径 → 当前路径、原始 SHA 映射](normalized_files.csv)。内容完全相同不等于所有同名或相似题目都相同；未经人工核验的不同试题和图片没有删除。部分 PDF-only 来源没有 TeX，不能伪造其源文件配对。

11 个原始上游的完整文件、目录和 SHA 保留在 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，不对其执行删除或重命名。原始多文件 LaTeX 工程和插图依赖暂留原路径，避免破坏编译。

## 已整理的配套编译文件（第二批）

- 导数专题 **6 组 TeX/PDF（12 个文件）**，统一命名为 `topics/calculus/topic-calculus-<unit>-<guide|test>.{tex,pdf}`。
- 合并去除与上述专题 TeX 内容完全一致的重复副本 **6 份**。
- 已审核单题解答 **13 个 TeX** 改名为 `derivative/reviewed/gaokao-YYYY-<卷别及题号>-solution.tex`。配套 PDF 只能在实际编译成功后发布，不能虚构成品。
- 保留独立多文件上游工程的相对 `\\input` / 图片依赖，暂不贸然将它们拆开合并。

## 第三批：独立解答 TeX 真正合订

2026-10-27 已将 13 份已经独立审核的 TeX 改为 **1 个真实合订源码**：[`derivative/reviewed/gaokao-2010-2025-calculus-reviewed-solutions.tex`](../derivative/reviewed/gaokao-2010-2025-calculus-reviewed-solutions.tex)。合订版保留正文、各题标题、原始 Git Blob SHA 与恢复入口；采用同一主文件名生成 `.pdf`。独立原件仍可从 [合订前快照分支](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/snapshot-before-tex-merge-2026-10-27/derivative/reviewed) 恢复。此类 `merge` 映射不声称合并文件 SHA 等于某一独立源码 SHA。

## 第四批：非真题独立测试卷的同名配对整理

已把 **52 组测试卷、104 个文件**从镜像的测试卷原目录迁移到规范化 `topics/`，每组 TeX/PDF 主文件名一致，Git Blob SHA 不改变。按用途分为初中测试 6 组、培优 20 组、高中章节 17 组、高考满分突破 9 组。源文件均为独立 `\\documentclass` 文档、未检出外部 `\\input` / `\\includegraphics` 等依赖；完整原件可从 `full-source-archive` 恢复。此前 6 组 `topics/calculus/` 配对不变。
