# 高考数学仓库 · 统一命名规范

## 1. 历年真题

路径：`papers/<年代>/gaokao-YYYY-<卷别>-<general|liberal|science>[-spring]-paper.pdf`。

例：`papers/2020s/gaokao-2024-new-gaokao-1-general-paper.pdf`。

- **每份真题保留独立 PDF**；文件名自带年份，不再为每一年单独创建文件夹。
- 共 **775 份**，分别位于 **1950s、1960s、1970s、1980s、1990s、2000s、2010s、2020s** 八个目录。
- 仅以 Git Blob SHA 完全一致识别文件级重复；同一年份、同名或内容相似，不足以证明卷别和题目一致。
- 少数元信息与文件名年份有冲突，详见 [待核对清单](naming_review.csv)，不得猜测更名。
- 未核实同源的 PDF 与 TeX 不能假设为直接编译配对。

## 2. 非历年真题资料

`topics/<分类>/topic-<分类>-<主题>-<guide|test>.tex` 与同主名 `.pdf` 成对发布。**143 对**已核对文件对应关系；其中的 2024 新高考Ⅰ卷排版示例留在 `topics/gaokao-typeset/`，插图资源与编译入口同目录。

[专题检索](../topics/INDEX.md) 给出各对 TeX/PDF 链接。未经实际重新编译的资料不标注为新编译通过。

## 3. 已复核数学解答

`derivative/reviewed/gaokao-2010-2025-calculus-reviewed-solutions.tex` 是 13 份独立解答的合订源码；只有真实编译产生时才添加同名 PDF。

## 4. 去重、溯源和恢复

[原路径→规范路径→原 SHA](normalized_files.csv) 用于机器检查，汇总全部 1,190 条历史映射；[来源合订本](../archive/SOURCE_MARKDOWN.md) 保存旧 Markdown，独立上游原件在 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)。

曾经分散在多个历史时期的重复统计与索引保留在 Git 历史及 [历史合订说明](../index/HISTORICAL_PERIOD_INDEXES.md)。不擅自删除不同数学变式、依赖图形或尚未审核的来源。
