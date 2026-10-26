# 三千弱水 · 高考数学真题与导数压轴题库

> 高考数学历年真题与高中导数大题资源总库：保留 11 个上游仓库，聚合 TeX / Markdown / PDF / ZIP，逐步建设可检索、可复核的专题题库。

**仓库状态**：已建立上游来源清单及 Git 子模块；`upstream/` 中是指向原仓库固定版本的链接，**不是将数百 MB 二进制文件平铺复制**。独立文件级索引见 [index](index/)（运行索引脚本后生成）。数学答案和试题版权均未被自动验证。

[11 仓库完整镜像进度](mirror/STATUS.md)（2026-10-26 最新：**3,121/7,222（43.22%）**，仍缺 **4,101** 个，剩余约 **475.8 MB** 原始文件；6/11 来源完整）。以此前全 11 源审计和最新 DxAThing 单源 Git 树重新核对为依据；主仓库存在同时进行的其他提交，故不将全部增量归于本轮。



## 2026-10-26 续迁：1995 与 1996 年原始插图全量镜像

直接将固定上游的 **1995 年 50 张 PNG** 和 **1996 年 49 张 PNG**，共 **99 个真实 Git Blob / 11,056,044 字节** 迁入主分支。全部源文件 SHA/mode 一致，两年份完整目录 Git Tree SHA 与固定上游一致。`img/1995` 对应 `9a3a33432a1cbcfaee2de9fef6aa7105bc9e148e`；`img/1996` 对应 `b56f14715eefa656a6a8b0f46ef7174d91af8384`。

按照之前已核验的 **3,022/7,222** 增量得到 **3,121/7,222（43.22%）**，尚缺 **4,101** 个，上游原始剩余大小估算 **475.8 MB**。完整来源仍为 6/11。这不是重新扫描全部 11 个来源。试题数学准确性、图形目视和第三方再分发许可不因 Git SHA 一致而自动通过。

[1995 逐文件审计](mirror/DIRECT_IMPORT_1995_50_FILES_2026_10_26.json) · [1996 逐文件审计](mirror/DIRECT_IMPORT_1996_49_FILES_2026_10_26.json) · [镜像进度](mirror/STATUS.md)。

## 2026-10-26 续迁：1998 年高考数学原始插图 43/43 完整镜像

另新增 **43 张原始 PNG / 1,588,322 字节**，1998 全年图形目录树 SHA `0ffd9d92a086ca15c754fde5f044f0dcf551b288` 与固定上游匹配；逐文件 SHA 与 mode 完全一致。和本轮 2000 年 82 张合计 **125** 张原件，共 3,213,761 字节。按核验增量推算累计 **3,022/7,222（41.84%）**、缺 **4,200**、剩余约 486.8 MB；完整来源仍 6/11。此统计不是新一轮全部 11 源独立重审。

[1998 年逐文件 SHA 清单](mirror/DIRECT_IMPORT_1998_43_FILES_2026_10_26.json) · [2000 年清单](mirror/DIRECT_IMPORT_2000_82_FILES_2026_10_26.json)。

## 2026-10-26 续迁：2000 年高考数学原始插图 82/82 完整镜像

已直接向 `main` 写入 DxAThing 固定版本的 **82 张原始 PNG / 1,625,439 字节**，原始 SHA 与 Git mode 82/82 完全一致，整年 `img/2000` Git Tree SHA 与上游严格相同（`1d84545611a4d89149f7223cc1433853aca23bd7`）。非子模块、非链接、非 LFS 占位。完成此次独立年份核验后，按原有 11 来源审计及 DxAThing 单源复核基线增量统计 **2,979/7,222（41.25%）**，仍缺 **4,243**、约 **488.4 MB**，已有 **6/11** 个来源完整。这是可追溯的增量统计，**并非重新复核全部 11 来源**。版权、数学正确性及视觉编译仍需另审。

[82 文件逐路径及 SHA/大小清单](mirror/DIRECT_IMPORT_2000_82_FILES_2026_10_26.json) · [镜像状态](mirror/STATUS.md)。

## 2026-10-26 续迁：1999 年插图完整入库

本次提交 [1999 年 26 张原始插图](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/5a59ae69c5595c9e5418d55f24d56177e5878b3c)，原始文件合计 1,713,325 字节。1999 年全年插图目录 28/28 已与上游目录 Git SHA 一致；另有 1 张来自同期其他提交，不冒充本轮导入。最新独立 DxAThing 源树核验匹配 1,768/5,546，整体按 11 源历史全量审计基线加 DxAThing 新增核验得 2,897/7,222。详见 [逐文件清单](mirror/DIRECT_IMPORT_1999_CONTINUATION_2026_10_26.json) 及 [当前统计](mirror/MIRROR_STATUS.json)。

## 2026-10-26 续迁 91 个原始文件并全量复核 11 源

本轮真实导入 **86 张原始 PNG** 与 **5 份历史试卷 PDF**，共 **91 个 Git Blob／6,077,141 字节**，均保持原始 SHA 和 Git 模式。1958 年图片目录补齐 37 张，当前 38/38；1991、1992、1993 年分别完整导入 15、18、16 张，四个年份目录 Git 树 SHA 与固定上游版本相同。

重新审核全部 11 个锁定上游仓库的递归 Git 树，同时纠正旧台账漏算的 49 个 **原先已经存在** 的 deekur PDF。**当前准确进度为 2,755/7,222（38.15%），仍缺 4,467 个，剩余原始数据 494,315,160 字节**；不是声称 49 个文件属于本轮新导入。

- [本轮 91 文件的逐路径导入清单](mirror/DIRECT_IMPORT_91_FILES_2026_10_26.json)
- [11 个来源全量 Git SHA / mode 核验](mirror/AUDIT_FULL_11_POST_IMPORT_2026_10_26.json)
- [最新进度与下一步导入边界](mirror/STATUS.md)

## 上一轮实体迁移（历史记录）：1988—1990 年 PNG 与 14 份高中数学 PDF

已将 **60 张 1988—1990 年试题原始 PNG** 以及 **14 份高中数学测试卷原始 PDF** 直接写入 `mirror/`，不是子模块或外站链接。新增 **74 文件 / 2,659,734 字节**。1988、1989、1990 各自的完整插图目录树 SHA 与固定上游 Git 提交一致；14 份 PDF 逐文件 SHA 与模式一致。

- [本轮逐文件 SHA 和 mode 审计清单](mirror/DIRECT_IMPORT_74_FILES_2026_10_26.json)
- [11 来源最新实体进度](mirror/STATUS.md) / [机器可读汇总](mirror/MIRROR_STATUS.json)
- 剩余约 **522.9 MB** 上游原始数据仍待补齐，主要是图片与 PDF；部分大于 1 MB 的原件需要使用 [完整 Git 对象导入脚本](scripts/README_FULL_IMPORT.md)，不能视为全量迁移成功。

## 2010—2019 年试卷 TeX：完整的十年固定版镜像

已按固定上游 Git SHA 和模式实体导入该大型题库 `content/2010/` 至 `content/2019/` 的全部 **282 份 TeX**。当批新增 **244 份**，2013 年 38 份在此前完成。**完整指与上游目录一致，不代表试卷真伪、数学解答、XeLaTeX 编译或版权已审核。**

- [2010—2019 十年逐年份核验明细](mirror/AUDIT_2010_2019.md)
- [2010—2019 原始 TeX 文件目录](mirror/gaokao-math-problems-compilation/content/)
- 2010—2019 年逐年数量：38、36、36、38、38、32、20、16、14、14。

## 1994 年历史试卷与配套插图补充

1994 年原始试卷 TeX 已完成 **7/7** 文件级严格匹配；1953—1963 年另补充 40 张原始 PNG。详见[本轮审计](mirror/AUDIT_1994_AND_IMAGES_2026_10_25.md)。文件复刻不代表试题真实性、数学正确性或编译/视觉验收。

## 历史插图与重绘图原始源码（2026-10-25 续批）

本批按固定上游 Git 提交净增 **126** 个实体文件：1963—1965 与 1978—1984 年的 **40 张原始 PNG**，以及 1998—2010 年所选年份的 **86 份重绘图 TeX**。该范围纳入原已有文件后 **132/132** 文件严格匹配；11 源总覆盖 **1,993/7,222**。详见[专项审计](mirror/AUDIT_HISTORICAL_FIGURES_2026_10_25.md)及[逐文件 SHA 清单](mirror/IMPORT_BATCH_HISTORICAL_FIGURES_2026_10_25.json)。图片视觉、编译、数学与授权尚未验收。

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

`.github/workflows/sync-upstream.yml` 提供固定版本的子模块同步、文件级索引生成与验证：只按主仓库的 Gitlink / `sources.json` 锁定 SHA 检出，不自动升级上游分支。新增 `.github/workflows/audit-archive.yml` 可在不克隆大型子模块的条件下独立验收索引与溯源一致性。在仓库的 **Actions** 页面可手动运行。

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


## 较早的上游仓库实体镜像记录（2026-10-26 历史快照）

11 个上游均固定到 `sources.json` 记录的 Git 提交。**6 个已完全镜像，5 个仍缺源文件**。以前次完整树审计 2,297 为基线，加本次确证的 62 个新 PNG，得到 **2,359/7,222（32.66%）** 个 SHA 与 Git 模式相符的原始实体文件，缺 **4,863** 个，待迁原始大小约 **557.6 MB**。

- [最新状态与边界说明](mirror/STATUS.md) / [机器可读镜像统计](mirror/MIRROR_STATUS.json) / [本轮新增 62 张 PNG 的 SHA 清单](mirror/DIRECT_IMPORT_62_PNG_2026_10_26.json)。来自 DxAThing 固定版本 `img/1977/`，62/147 实体到齐，原始字节 2,605,421，均按 SHA＋模式复核。
- [上一轮导入 149 文件的清单](mirror/DIRECT_IMPORT_149_FILES_2026_10_26.json)，包含 131 张重绘图 TeX、12 份历年试卷 PDF、6 份数学专题 PDF；该批使 `img_repaint/*.tex` 达到 320/320。
- [完整文件导入操作说明](scripts/README_FULL_IMPORT.md) / [Windows 双击脚本](scripts/一键导入11个仓库.cmd) / [Git 原对象导入源码](scripts/import_pinned_git_trees.py)。

**SHA 一致只证明原始对象搬运忠实**；题目真伪、数学审核、图片视觉效果、LaTeX 及 PDF 编译和再分发权利仍未因此验证。

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
- [第八轮质检与版本锁定记录](metadata/ROUND_08_REPORT.md) / [2023 北京卷第20题](derivative/reviewed/2023-beijing-q20.md) / [TeX](derivative/reviewed/2023-beijing-q20.tex)
- [机器扫描候选](scripts/scan_derivative_questions.py)、[索引一致性脚本](scripts/validate_question_index.py)、[第五轮报告](metadata/ROUND_05_REPORT.md)

共 **16 条来源记录**完成独立数学核验，实际对应 **14 道不同题目**（2011 安徽文理卷同题保留两份出处）。
余下 232 条记录尚需逐题数学复核；多卷同题只打上疑似重复组标签，并未全面去重。

本轮仅在 GitHub 写入源码、索引和质检文本，**不产生本地 PDF 或 ZIP**。
新增的 TeX 尚未编译；GitHub Actions 曾在获得 Runner 前失败，自动同步未完成验收。
