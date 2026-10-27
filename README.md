# 三千弱水 · 高考数学题库

**主分支为精简检索与发布目录**。全部 11 个上游来源、7,222 个原始文件仍在 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，有原始路径与 Git SHA，可随时恢复原始 LaTeX 工程。

## 一目了然的入口

- **[历年真题 PDF](papers/)**：775 份，`papers/YYYY/gaokao-YYYY-卷别-科类-paper.pdf`，不对来源不明的 PDF 伪造 TeX。
- **[专题 TeX/PDF 统一目录](topics/INDEX.md)**：143 对成品与源文件同名，按导数、培优、高中、初中、衔接、高考拓展分类；2024 新高考排版工程保留图片资源。
- **[已独立复核导数解答](derivative/reviewed/)**：13 个证明合并为 1 份可编译 TeX；PDF 须实际编译成功才发布。
- **[年份目录](catalog/YEAR_INDEX.md)**、**[专题检索](catalog/TOPICS.md)**、**[重复题审核](catalog/QUESTION_DEDUP.md)**、**[原路径/SHA 对照表](catalog/normalized_files.csv)**。

```text
papers/YYYY/           历年高考真题 PDF
topics/                 讲义、培优、测试、排版实例 TeX/PDF
derivative/reviewed/     数学审核解答合订 TeX
catalog/                去重、命名和索引
index/                  题目级原始资料和历史索引
archive/                上游 Markdown 合订
metadata/               审核来源记录
scripts/ tests/ .github/ 工具和自动校验
upstream/               固定版 11 个 gitlink
```

上游巨大的 `mirror/` 不在精简 `main` 中重复保存。需要原始第三方项目中的插图、模块与编译配置时，请直接使用 `full-source-archive` 分支。文件配对和 SHA 检查不等于真题真伪、数学推导、版权与 PDF 编译排版审核。
