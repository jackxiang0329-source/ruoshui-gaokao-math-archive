# 三千弱水 · 高考数学真题与专题题库

**统一整理历年真题 PDF 与专题 TeX/PDF，完整原件另行保存**。收录 11 个固定上游版本，支持年份检索、导数题定位、去重和数学质检。详细来源与许可证请看 [sources.json](sources.json)。

## 主要入口

| 入口 | 用途 |
|---|---|
| [统一命名的历年真题 PDF](papers/) | 775 份按年份、卷别、科类归档 |
| [编译文件命名与去重记录](catalog/NAMING.md) | 1,014 条路径/SHA 映射、2 份年份异常待核验 |
| [专题资料 TeX/PDF 统一目录](topics/) | 58 组专题源码和 PDF 同名配对（含独立试卷） |
| [13 份复核证明 TeX 合订](derivative/reviewed/README.md) | 1 份可编译 TeX，PDF 与源码同名发布 |
| [按年份统一检索](catalog/YEAR_INDEX.md) | 全部 64 个年份合订为 1 份文档，按原始文件 SHA 去重 |
| [按专题检索](catalog/TOPICS.md) | 原来的 7 个专题文件合订为 1 份 |
| [题目级去重审核](catalog/QUESTION_DEDUP.md) | 6 组确认同题、1 组不同变式、14 组仍待核验 |
| [数学证明合订本](derivative/reviewed/PROOFS.md) | 原 14 份数学复核 Markdown 合为 1 份，保留每题 TeX |
| [完整来源 Markdown 合订本](archive/SOURCE_MARKDOWN.md) | 215 个上游 Markdown 原文、各自 SHA、原路径与独立链接 |
| [固定上游完整快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive) | **11/11 个完整原始来源，7,222/7,222 个文件，不合并、不删除** |
| [全部索引 CSV](catalog/documents.csv) | 代表文件、原始来源链接、年份与专题等 |

## Markdown 精简结果

从最初的 **338 个 Markdown 文件精简到 24 个**，文件数减少 **314 个（约 93%）**。

精简不是简单删除内容：原有 215 份上游 Markdown 合并归档，14 份数学审核文档合并为一份，64 份年份导航合并为一份，7 份专题导航合并为一份，历史审计和阶段索引也已经合并归档。

**两个分支的区别**：主分支 `main` 是精简的工作区，其中 `mirror/` 继续精简：确定年份的真题 PDF 已移到 `papers/`，独立专题 TeX/PDF 移到 `topics/calculus/`，重复副本已清理；215 个原始 Markdown 归并到 [正文合订本](archive/SOURCE_MARKDOWN.md)。完整的 7,222 个独立原件只在 `full-source-archive` 分支按原路径保留，且该分支的 11 个来源 Git Tree SHA 与锁定版本均严格匹配。恢复单独原件、编译第三方项目或核对原始相对链接时，应使用完整快照分支。

## 其它资料

[已审核导数题索引](derivative/reviewed/README.md) · [导数题总索引](index/DERIVATIVE_PROBLEMS_2010_2026.md) · [重复题独立审计](index/DUPLICATE_AUDIT.md) · [迁移与 QA 历史](metadata/HISTORICAL_REPORTS.md) · [历史镜像审计](mirror/HISTORICAL_AUDITS.md) · [镜像当前说明](mirror/STATUS.md)

## 自动任务

- 每 30 分钟：读取 `full-source-archive`，核对 11 个来源 SHA 和文件数，**不向精简主分支回填独立 Markdown**（[校验工作流](.github/workflows/mirror-all-upstream.yml)）。
- 每 30 分钟：从完整快照的 Git 文件树更新精简的检索与去重目录（[目录工作流](.github/workflows/curate-archive.yml)）。

当前两个周期任务只处理 **固定的上游版本**，不会自动发现/导入后来发布的版本。SHA 核对、文件去重也不能代替数学正确性、版权和 PDF 排版检查。

## 恢复与溯源

[完整快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive) 中的独立文件、原始路径和 Git SHA 保留不变；[源文件清单](archive/source-markdown-paths.csv) 可逐一查回 215 个 Markdown 原件。分开的题目证明、迁移记录还可通过 Git 历史或各合订本记录的原始 SHA 恢复。
