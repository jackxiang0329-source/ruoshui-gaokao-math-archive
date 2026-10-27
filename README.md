# 三千弱水 · 高考数学题库

**主分支用于查找、下载和重新编译已发布资料；历史导入文件不在这里重复堆放。**

## 直接进入

- **[历年高考真题 PDF](papers/)**：775 份，按 1950s—2020s 共 8 个年代目录归档；文件名写明年份、卷别、科类。
- **[专题 TeX/PDF](topics/INDEX.md)**：143 对同主文件名的源码和 PDF，按学科/用途分类；2024 新高考排版工程保留图形依赖。
- **[已审核导数题解答](derivative/reviewed/)**：13 份证明汇成 1 个 TeX 编译入口。

## 按内容检索

[年份总目录](catalog/YEAR_INDEX.md) · [专题分类](catalog/TOPICS.md) · [导数逐题索引](index/DERIVATIVE_PROBLEMS_2010_2026.md) · [逐题 JSON](index/derivative-problems-2010-2026.json) · [逐题 CSV](index/derivative-problems-2010-2026.csv) · [重复题复核](catalog/QUESTION_DEDUP.md) · [文件来源与 SHA](catalog/normalized_files.csv) · [命名规则](catalog/NAMING.md)。

## 文件怎么放

```text
papers/                 真题 PDF（8 个年代目录）
topics/                 专题 TeX + 对应 PDF
derivative/reviewed/     已审核数学证明合订
catalog/                 可检索目录、去重与原路径映射
index/                   当前题目级数据及审核证据
metadata/                数学审核溯源和问题记录
scripts/ tests/ .github/ 维护、测试和定时工作流
```

## 历史资料与恢复

- [整理之前的完整主分支快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/snapshot-before-lean-metadata-20261027)：包含旧的导入表、历史报告、早期阶段索引、Markdown 合订本与原路径对照，不丢失历史资料。
- [11 个上游完整原件](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)：7,222 个固定版本文件，保留原始多文件 TeX 工程、图片及各自 Git SHA。
- 当前主分支仍保留审核证明、题目数据和回溯所需的索引。旧快照和完整原件是恢复用存档，避免它们挤占日常浏览入口。

**注意：** 不同卷别、不同题目变式不能按相似名称删除。文件配对和 SHA 校验不代表重新编译、数学正确性、原卷真伪及版权审核全部完成。
