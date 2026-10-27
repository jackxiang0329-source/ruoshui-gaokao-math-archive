# 三千弱水 · 高考数学题库

按“**历年真题 / 专题资料 / 已审解答 / 检索目录**”阅读。主分支只保留有明确用途的发布文件；11 个上游原工程完整保存于 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)（原路径和 Blob SHA 未改动）。

## 主要入口

- **[历年真题 PDF](papers/)**：775 份，`papers/YYYY/gaokao-YYYY-地区-科类-paper.pdf`；PDF-only 不伪造 TeX 配对。
- **[专题 TeX / PDF](topics/INDEX.md)**：142 组同名配对（原有 6 组导数专题 + 新整理 136 组讲义、测试卷、培优和衔接资料），名称统一 `topics/<类型>/topic-<类型>-编号.{tex,pdf}`。
- **[已独立复核导数解答](derivative/reviewed/)**：13 份合并为 1 个 TeX 编译入口；PDF 仅在真实编译成功后发布。
- **[按年份查找](catalog/YEAR_INDEX.md)**、**[按专题查找](catalog/TOPICS.md)**、**[题目级去重](catalog/QUESTION_DEDUP.md)**。
- **[旧路径与文件 SHA 对应](catalog/normalized_files.csv)**、**[讲义 TeX/PDF 配对映射](catalog/topic_pairs.csv)**。
- **[上游 Markdown 合订本](archive/SOURCE_MARKDOWN.md)** 与 [独立溯源](archive/source-markdown-paths.csv)。

## 结构

```text
papers/YYYY/             历年真题 PDF（统一命名）
topics/<type>/           非历年真题专题（TeX 与 PDF 同名）
derivative/reviewed/     严格审核的合订解答 TeX
catalog/                 年份、专题、去重、文件映射
index/                   历史题目级原始索引
archive/                 上游 Markdown 原文合订
metadata/                审核与溯源
scripts/ tests/ .github/ 维护脚本、测试、自动化
upstream/                锁定的 11 个 Git 子模块
```

**精简策略：**原始多文件工程和大量插图不再重复存储于精简主分支；需编译上游原始工程或检查图片时，请在完整快照分支检出同一路径。对于 136 组独立文件，只调整路径和名称，保留原 PDF 与 TeX 内容及 SHA；不视为重新编译验证。对于历年真题，只有真正确认来自同一版式/源文件的 TeX 才可作为配对源文件。

## 规则与质检

详见 [命名规范](catalog/NAMING.md) 和 [上游来源清单](sources.json)。原文件字节一致性、命名、一一配对由 [检查脚本](scripts/check_published_names.py) 验证。自动目录任务按固定完整快照生成链接，不把旧镜像回填到主分支。内容同名或相似不等于同题；原题版权、数学正确性和 PDF 版式仍需分别审查。
