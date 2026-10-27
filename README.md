# 三千弱水 · 高考数学题库

**主分支只放可浏览的真题、专题 TeX/PDF、题目索引和必要工具。** 11 个上游来源的 7,222 份原始文件完整保存在 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，可以按原路径恢复。

## 三个主要入口

- **[历年真题 PDF](papers/)**：775 份，按 **1950s—2020s 共 8 个年代目录**整理；每份试卷仍有独立 PDF，文件名包含完整年份、卷别和科类。
- **[专题 TeX / PDF](topics/INDEX.md)**：143 对同名源码与成品，按导数、培优、章节、高考拓展、衔接等主题归档。
- **[导数题复核合订](derivative/reviewed/)**：13 份独立复核源码并为一个 TeX 文档；只有实际编译成功后才发布对应 PDF。

## 查找与管理

[按年份检索](catalog/YEAR_INDEX.md) · [按专题检索](catalog/TOPICS.md) · [题目级去重](catalog/QUESTION_DEDUP.md) · [文件路径/SHA 对照](catalog/normalized_files.csv) · [命名规范](catalog/NAMING.md)。

```text
papers/1950s/ ... 2020s/   历年高考真题 PDF（年代分组）
topics/<分类>/               专题 TeX + 同名 PDF
derivative/reviewed/          审核解答 TeX 合订
catalog/                      检索、去重、映射
index/                        统一题目级 JSON/CSV、历史分析
archive/ metadata/            上游文本合订和审核溯源
scripts/ tests/ .github/      维护和自动核验
```

**避免误删：** 历年试卷各卷与不同题目变式不能按相似标题直接合并；PDF-only 资源不伪造 TeX 配对。源工程如需原图片、原宏包或其他依赖，请使用固定快照分支。重命名和 SHA 一致性不等于重新编译、数学正确性与版权审核。
