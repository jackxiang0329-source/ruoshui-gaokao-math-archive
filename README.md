# 三千弱水 · 高考数学真题与导数压轴题库

> 高考数学历年真题与高中导数大题资源总库：保留 11 个上游仓库，聚合 TeX / Markdown / PDF / ZIP，逐步建设可检索、可复核的专题题库。

**仓库状态**：已建立上游来源清单及 Git 子模块；`upstream/` 中是指向原仓库固定版本的链接，**不是将数百 MB 二进制文件平铺复制**。独立文件级索引见 [index](index/)（运行索引脚本后生成）。数学答案和试题版权均未被自动验证。

[11 仓库完整镜像进度](mirror/STATUS.md)：按固定 Git SHA 核验已入库文件；仍有大型仓库未完成，不能仅凭子模块认为源码齐全。

## 使用

完整下载 11 个上游的文件及本项目分类目录：

```bash
git clone --recurse-submodules https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive.git
```

主仓库的 GitHub ZIP **包含本仓库 materials/ 下已实体入库的 TeX/PDF**，但**不包含 upstream/ 里的子模块实体**。请使用上面的递归克隆命令，或在 GitHub 网页直接进入各个子模块仓库。首次克隆可能需要数 GB 空间。

## 内容导航

- **[已实体入库的 TeX + PDF（可直接下载）](materials/README.md)**：首批 6 套导数专题，6 份 TeX 与 6 份原始配套 PDF；全部为 Git 实体文件，非子模块。
- **[高中导数大题](derivative/)**：单调性、极值、含参讨论、恒成立、隐零点、双零点、构造函数、零点个数。
- **[历年高考真题](past-papers/)**：按年份、地区和卷种建立元数据；不擅自合并不同版本。
- **[来源清单](sources.json)**：11 个上游项目的地址、默认分支、侧重点与许可核查结果。
- **[原始文件索引](index/)**：TeX、Markdown、PDF、ZIP 与候选导数/高考文件的 CSV 列表。
- **[版权与出处](metadata/source-attribution.md)**：每个原仓库继续适用自己的许可证；第三方试题和插图另行判断。

## 自动同步

`.github/workflows/sync-upstream.yml` 提供人工触发与按来源/脚本修改触发的同步流程：更新 Git 子模块、生成文件级索引并运行验证。在仓库的 **Actions** 页面可手动运行。

如果自动提交因仓库的 Actions 写入策略失败，需要在 **Settings → Actions → General → Workflow permissions** 允许 GitHub Actions 具有读写权限，或改为本地执行 `bash scripts/sync_sources.sh` 并推送。

## 11 个来源

| 来源 | 用途 |
|---|---|
| [Dreamaker203/math-lecture-notes](https://github.com/Dreamaker203/math-lecture-notes) | 导数压轴题专题 TeX/PDF |
| [DxAThing/Gaokao-Math-Problems-Compilation](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation) | 大型高考题库 LaTeX |
| [deekur/gaokaomath](https://github.com/deekur/gaokaomath) | 历年高考 PDF |
| [hbinfrog/first_round_review](https://github.com/hbinfrog/first_round_review) | 高三一轮复习、导数讲义 |
| [TsubameHata/gaokao_math_corpus](https://github.com/TsubameHata/gaokao_math_corpus) | 新高考 Markdown / YAML 结构化题面 |
| [ajsadhotmail/2024-China-Gaokao-Math](https://github.com/ajsadhotmail/2024-China-Gaokao-Math) | 2024 新高考 I 卷 TeX/PDF |
| [shaodongtang/gaokao_exam](https://github.com/shaodongtang/gaokao_exam) | 试卷 LaTeX 模板 |
| [Yan-Zero/MathPaper](https://github.com/Yan-Zero/MathPaper) | 历史高考 TeX 试卷 |
| [daxmate/math](https://github.com/daxmate/math) | 历史试卷与排版 |
| [sdmf6/math-atlas](https://github.com/sdmf6/math-atlas) | 题库检索与导出工具 |
| [SakurakaiCat/mathex](https://github.com/SakurakaiCat/mathex) | TeX 习题册 |

## 审核原则

`unreviewed → transcribed → math-checked → latex-compiled → reviewed`。**文件名命中 ≠ 已确认是导数大题；上游已有解析 ≠ 数学正确**。保留固定提交 SHA、原始路径与来源链接，后续逐题核验。

## 许可证

上游保持独立许可，不能把整个聚合库声称为一个统一许可证。部分原仓库存在许可声明不完整或第三方素材权利不明确的情况，详见 [sources.json](sources.json)。


## 高考导数题目级索引（2026-10-24）

已登记 2010—2026 年导数相关解答题 **248 条来源记录**：
2010—2014 年 127 条、2015—2019 年 63 条、2020—2026 年 58 条。
带卷别的来源记录数不等于去重后的独立题目数。

- [2010—2026 年统一索引](index/DERIVATIVE_PROBLEMS_2010_2026.md) / [CSV](index/derivative-problems-2010-2026.csv) / [JSON](index/derivative-problems-2010-2026.json)
- [2010—2014 年地方卷与重点卷](index/DERIVATIVE_PROBLEMS_2010_2014.md)
- [2015—2019 年重点卷](index/DERIVATIVE_PROBLEMS_2015_2019.md)
- [2020—2026 年主要试卷](index/DERIVATIVE_PROBLEMS_2020_2026.md)
- [2010 安徽文科第20题独立证明](derivative/reviewed/2010-anhui-liberal-q20.md) / [TeX](derivative/reviewed/2010-anhui-liberal-q20.tex)
- [2011 安徽文、理科共同题独立证明](derivative/reviewed/2011-anhui-derivative-common.md) / [TeX](derivative/reviewed/2011-anhui-derivative-common.tex)
- [2019 全国Ⅱ卷文科第21题独立证明](derivative/reviewed/2019-national2-liberal-q21.md) / [TeX](derivative/reviewed/2019-national2-liberal-q21.tex)
- [2024 新高考Ⅰ、Ⅱ卷两题独立证明](derivative/reviewed/2024-two-proofs.md) / [TeX](derivative/reviewed/2024-two-proofs.tex)
- [2010 北京理科第18题](derivative/reviewed/2010-beijing-science-q18.md)、[2013 福建理科第17题](derivative/reviewed/2013-fujian-science-q17.md)、[2014 重庆文科第19题](derivative/reviewed/2014-chongqing-liberal-q19.md) 的独立复核
- [2014 安徽文理共同题：完整参数分类](derivative/reviewed/2014-anhui-common-q.md)，同时记录[上游解析缺失问题](metadata/quality-findings.json)
- [15 条数学质检状态的溯源清单](metadata/review-provenance.json)
- [疑似重复题复核索引：6 组同题、1 组变式、14 组待核查](index/DUPLICATE_AUDIT.md)
- [已完成数学证明与可独立编译源码目录](derivative/reviewed/README.md)
- [数学复核溯源和重复索引自动一致性检查](scripts/validate_review_traceability.py)
- [第六轮质检报告](metadata/ROUND_06_REPORT.md)
- [2023 全国乙卷文科第20题完整证明](derivative/reviewed/2023-national-b-liberal-q20.md) / [TeX](derivative/reviewed/2023-national-b-liberal-q20.tex) / [2023 新高考Ⅰ卷第19题证明](derivative/reviewed/2023-new-gaokao-1-q19.md) / [TeX](derivative/reviewed/2023-new-gaokao-1-q19.tex)
- [2025 上海卷第19题证明](derivative/reviewed/2025-shanghai-q19.md) / [TeX](derivative/reviewed/2025-shanghai-q19.tex) / [2025 全国Ⅱ卷第18题证明](derivative/reviewed/2025-national2-q18.md) / [TeX](derivative/reviewed/2025-national2-q18.tex)
- [2025 北京卷第20题转录顺序冲突审计](derivative/reviewed/2025-beijing-q20-transcription-audit.md)：暂不升格数学核验
- [第七轮审校报告](metadata/ROUND_07_REPORT.md)
- [机器扫描候选](scripts/scan_derivative_questions.py)、[索引一致性脚本](scripts/validate_question_index.py)、[第五轮报告](metadata/ROUND_05_REPORT.md)

共 **15 条来源记录**完成独立数学核验，实际对应 **13 道不同题目**（2011 安徽文理卷同题保留两份出处）。
余下 233 条记录尚需逐题数学复核；多卷同题只打上疑似重复组标签，并未全面去重。

本轮仅在 GitHub 写入源码、索引和质检文本，**不产生本地 PDF 或 ZIP**。
新增的 TeX 尚未编译；GitHub Actions 曾在获得 Runner 前失败，自动同步未完成验收。
