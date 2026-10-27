# 高考数学试卷命名与去重规范

2026-10-27 主分支整理：将 **775 份**可确认年份的高考试卷 PDF 统一改名并按年份存入 `papers/YYYY/`；另外移除 **91 份** SHA 完全相同且有保留副本的 PDF。**2 份**目录年份与文件名不一致，暂不更名，见 [核验清单](naming_review.csv)。

统一文件名：`gaokao-YYYY-<地区或卷别>-<general|liberal|science>[-spring]-paper.pdf`。旧课程、延期考试、初试等特殊差异尽量在中段明确体现；所有适用省份和原始文件名仍由映射保留。

[原始路径 → 当前路径、原始 SHA 映射](normalized_files.csv)。内容完全相同不等于所有同名或相似题目都相同；未经人工核验的不同试题和图片没有删除。部分 PDF-only 来源没有 TeX，不能伪造其源文件配对。

11 个原始上游的完整文件、目录和 SHA 保留在 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，不对其执行删除或重命名。原始多文件 LaTeX 工程和插图依赖暂留原路径，避免破坏编译。
