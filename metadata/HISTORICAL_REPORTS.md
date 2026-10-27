# 历史迁移、导入和质检报告（内容合订归档）

此前分散的 7 份报告在这里完整保留，按照日期/轮次查看；其进度指标是当时快照，不代表当前镜像或数学审核状态。

**现行状态**请以 [高考数学仓库首页](../README.md)、[实时去重索引](../catalog/README.md) 和 [镜像验收](../mirror/STATUS.md) 为准。

## 原始文件与对应章节

- `metadata/IMPORT_REPORT.md` → [第 1 节](#record-01) · 原始 Blob `e06184c7666e7c1b2edf9bd2753ffe66898bb930`
- `metadata/ROUND_04_REPORT.md` → [第 2 节](#record-02) · 原始 Blob `07f5f74e6f3c90ebc3de4a8f8419dc40c9fad33e`
- `metadata/ROUND_05_REPORT.md` → [第 3 节](#record-03) · 原始 Blob `3cc5f5af39af2e0beb9068fc0d6a7160c074e54c`
- `metadata/ROUND_06_REPORT.md` → [第 4 节](#record-04) · 原始 Blob `d54548d87fcf795f478fedac5b49efffce1a60c9`
- `metadata/ROUND_07_REPORT.md` → [第 5 节](#record-05) · 原始 Blob `47e01360b49825f5a31aca44e2db2780abc37bf1`
- `metadata/ROUND_08_REPORT.md` → [第 6 节](#record-06) · 原始 Blob `1239c05b5e4bc3703282c99b98e2e6b015eb7782`
- `metadata/README_HISTORY_PRE_CURATION_2026_10_27.md` → [第 7 节](#record-07) · 原始 Blob `b5bfe5f78d98bd5b185701bc99d01467bd3e7e55`

---

## record-01

**原始文件：** `metadata/IMPORT_REPORT.md` · 原始内容 Blob SHA：`e06184c7666e7c1b2edf9bd2753ffe66898bb930`

以下为原始 Markdown 正文（仅将文档位置合并，历史判断不作更新）。

# 首轮导入质检报告（2026-10-24）

## 已确认完成

- [x] `main` 分支包含 11 个 `mode 160000` Git 子模块，且 `.gitmodules` 已登记各上游地址和分支。
- [x] 所有 11 个来源均由 GitHub 的 Git Trees API 读取固定提交版本；返回 `truncated: false`，不存在树截断。
- [x] 已提交 2,688 个支持格式文件的原始路径与源文件永久链接，见 [index/files.csv](../index/files.csv)。
- [x] 已提交文件名粗筛的导数候选 28 项、高考候选 2,170 项。
- [x] 已提交按项目格式统计、许可证状态、来源归属记录。
- [x] 已提交上游同步脚本、索引构建脚本、格式校验脚本和 GitHub Actions 工作流。

## 原始文件格式统计

| 格式 | 文件数 |
|---|---:|
| .tex | 1,432 |
| .md / .markdown | 215 |
| .pdf | 1,019 |
| .zip | 2 |
| .sty / .cls / .yml / .yaml 等 | 20 |
| **合计** | **2,688** |

这是不同上游仓库中的**文件项数**，并非去重后的数学题数。

## 已知限制与未完成事项

- [ ] **GitHub Actions 首次执行失败**：运行 [40087493443](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40087493443) 在 runner 分配前结束，作业未产生步骤记录和可下载的日志；无法据此断定是脚本、权限、配额或平台故障。自动同步未验证成功。
- [ ] 大型上游仓库**使用子模块指针而非平铺文件副本**。主仓库 ZIP 不含上游二进制文件；需要 `git clone --recurse-submodules`。
- [ ] 文件名粗筛不能提取完整试卷内部的独立导数大题；尚未形成逐题 `.tex`、`.md`、PDF 输出。
- [ ] 尚未独立验证全部题目准确性、每题来源年份和重题情况。
- [ ] 不能将各上游许可证统一改成一个许可证，也不能擅自重新分发权利不明的第三方内容。
- [ ] 本仓库目前为 **Private**。如需对外公开，需由仓库所有者在 GitHub 设置中修改可见性。

## 下一阶段重点

1. 优先从 [Dreamaker203 导数专题](../upstream/math-lecture-notes/) 与 [hbinfrog 导数讲义](../upstream/first-round-review/) 提取题目结构，并建立题目级规范化元数据。
2. 从高考 LaTeX 大型题库识别导数相关的解答题，核验年份、卷种和题号。
3. 对每道题建立原题、答案、逐步推导、关键条件、编译验证及数学质检日志。
4. 统一排版为 XeLaTeX 源码与可复编译 PDF，确保保留上游出处与许可。

> 机器校验的“文件存在”与数学证明的“正确”是两个不同等级的结论。

---

## record-02

**原始文件：** `metadata/ROUND_04_REPORT.md` · 原始内容 Blob SHA：`07f5f74e6f3c90ebc3de4a8f8419dc40c9fad33e`

以下为原始 Markdown 正文（仅将文档位置合并，历史判断不作更新）。

# 第四轮：高中导数题库扩大索引与质量检查

日期：2026-10-24。仓库：`jackxiang0329-source/ruoshui-gaokao-math-archive`。

## 已完成并推送到 main

- 2010—2014 重点卷种新增 **45** 条来源定位；
- 2015—2019 重点卷种新增 **63** 条来源定位；
- 与原有 2020—2026 的 **58** 条合并，生成 [2010—2026 统一索引](../index/DERIVATIVE_PROBLEMS_2010_2026.md)，合计 **166** 条；
- 每项记录年份、卷别、实际 TeX problem 环境序号、上游原路径、起始行、固定提交 SHA、分类和审核状态；
- 将 2019 全国Ⅱ卷文科第21题完成独立推导复核，补充 [MD](../derivative/reviewed/2019-national2-liberal-q21.md) 与 [TeX](../derivative/reviewed/2019-national2-liberal-q21.tex)；
- 三期分年索引与统一索引同步更新，3 条标为 `math-checked`，其他 163 条均不得认定已审核正确；
- 对文理卷相似题以 `duplicate_group` 标注，不在没有充分证据时合并或删除记录。

## 一致性质检

直接比对仓库读取的四个 JSON 索引后，已经核实：
- 统一索引的 166 个 ID 全部唯一；
- 45、63、58 条三期数据恰好构成统一索引；
- 三期分卷与主索引的核验状态和行号无冲突；
- 原始路径、年份、固定提交及题号起始行的形式一致；
- 已核验题目为 2019 全国Ⅱ卷文科第21题、2024 新高考Ⅰ卷第18题、新高考Ⅱ卷第16题。

新提交的 `scripts/validate_question_index.py` 可在今后自动检查 JSON/CSV 之间的一致性与重复标记配对；
**该 Python 脚本尚未在 GitHub Actions 上成功运行**，不可将静态核查说成 CI 已通过。

## 未完成和限制

1. 上述均是**来源定位记录**，部分不同试卷可能实际属于同题、变式或重复录入，166 不表示独立题数。
2. 2010—2019 年仍有大量省市卷、选考题与小题没有逐题检索；不是历年高考导数题的全集。
3. 163 道尚未完成数学独立复核。已复核的 2019 年新 TeX 尚未编译。
4. GitHub Actions 工作流仍在获得 Runner 前失败，缺少可用执行步骤日志；不能声称已解决。
5. 本轮没有生成本地 PDF 或 ZIP，也未推送未经授权的整卷复制文件。

下一步：按 2010—2014 地方卷补全来源、逐卷排查重复，继续审查 166 道的关键推导，优先纠正错误再将状态升级。

---

## record-03

**原始文件：** `metadata/ROUND_05_REPORT.md` · 原始内容 Blob SHA：`3cc5f5af39af2e0beb9068fc0d6a7160c074e54c`

以下为原始 Markdown 正文（仅将文档位置合并，历史判断不作更新）。

# 第五轮：地方高考导数大题扩库与独立质检（2026-10-24）

## 实际已提交

- 补录 2010—2014 年地方卷及大纲卷导数相关解答题 **82 条**：2010 年 19、2011 年 16、2012 年 15、2013 年 12、2014 年 20。
- 总索引由 166 条增加到 **248 条来源记录**，其中 2010—2014 分卷合计 127 条，2015—2019 63 条，2020—2026 58 条。
- 新增 14 组疑似相同题目或文理变式，保留全部卷别，不自动去重。
- 逐题剔除关键词扫描的明显误判：圆切线、椭圆切线、仅含三角函数周期/最值的普通题和绝对值选考题。
- 独立完成 2010 安徽文科第20题及 2011 安徽文科第18题、理科第16题的数学证明。已核对原题及单调区间、极值、关键临界参数。
- 数学复核累计 **6 条记录、5 道不同题目**；剩余 242 条记录尚未独立数学核验。

## 严谨性检查

2010 安徽文科：对于 f(x)=sin(x)-cos(x)+x+1，严格限定 0<x<2π，仅有驻点 x=π 和 3π/2；单调性按导数正、负、正分段，极大值 π+2，极小值 3π/2。

2011 安徽文理同题：a>0，f(x)=e^x/(1+ax²)。导函数符号由 a(x-1)²+1-a 决定；当 a=4/3 时极大值点为 1/2、极小值点为 3/2；全实轴单调的充要条件是 0<a≤1。临界值 a=1 **必须保留**，因为仅一个导数零点不破坏严格单调。

## 边界与遗留问题

1. 248 是来源记录数而非严格去重题数，不代表 17 年的高考导数题已收齐。
2. 242 条记录尚未完成数学独立复核。
3. 本轮新上传的 TeX 没有进行实际 XeLaTeX 编译；没有生成或上传任何本地文件。
4. GitHub Actions 执行器分配前失败的问题尚未确认解决。
5. 题干及插图等第三方版权应依来源许可证具体判断，不擅自统一授权。

---

## record-04

**原始文件：** `metadata/ROUND_06_REPORT.md` · 原始内容 Blob SHA：`d54548d87fcf795f478fedac5b49efffce1a60c9`

以下为原始 Markdown 正文（仅将文档位置合并，历史判断不作更新）。

# 第六轮：深度数学质检、重复关系与校验闭环

日期：2026-10-24。所有文件均直接提交到 GitHub，**未生成本地 PDF、ZIP、TeX 或 Markdown 文件**。

## 本轮完成

1. 新增 **4 道不同题目**的独立数学证明（5 条来源记录）：2010 北京理科第18题、2013 福建理科第17题、2014 重庆文科第19题、2014 安徽文理科共同题；均提供 Markdown 和自包含的 LaTeX 源码。
2. 2010—2026 年题目索引保持 248 条，数学独立核验由 **6 条提升为 11 条**，相当于 9 道不同题目；剩余 237 条尚未独立数学复核。
3. 2010 北京理科题核查了 `k=0`、`0<k<1`、`k=1`、`k>1` 四个参数区间，临界值 `k=1` 虽只有一个驻点，函数仍严格递增。
4. 2013 福建理科题明确 `a≤0` 无极值点、`a>0` 唯一极小值点；2014 重庆文科题明确排除 `x=-1` 伪驻点。
5. 2014 安徽文理共同题核对了 `a=1`、`a=4` 两个边界。安徽文科上游解答末尾只剩孤立的 “1” 且**缺少完整最小值参数分类**；安徽理科版本完整，本库发布独立补正，见 [quality-findings.json](quality-findings.json)。
6. 新建 [重复题复核索引](../index/DUPLICATE_AUDIT.md)：共 21 组，确认同题 6 组，确认实质变式 1 组，其余 14 组待审核。
7. 实质变式例证：2012 山东文理卷第三问分别出现 `g(x)=xf'(x)` 与 `g(x)=(x²+x)f'(x)`，不能合并为同一题。
8. 新建数学核验到证明文件的 [溯源关系](review-provenance.json)，并增加 Python 脚本 [validate_review_traceability.py](../scripts/validate_review_traceability.py)，检查状态、链接、来源、重复组与修正证明是否一致。

## 尚未完成的项目

- 本轮新增 4 份 LaTeX **仅作为源码提交，没有经过实际编译验证**，不能宣称 PDF 已生成或通过复编。
- GitHub Actions 在此前多次运行仍于获得 Runner 之前失败；新增的测试与校验脚本**未在 Actions 中成功执行**。
- 248 条是不同卷别的来源记录数，不是完整 2010—2026 年高考真题题数，更不是严格去重后的独立题数。
- 上游材料许可证仍分别有效，不能统一宣称本仓库拥有原题和图片版权。

后续优先级：逐题数学核查更多的 2020—2026 年真题；对未审核的 14 组重复关系逐题比对；待 Actions 恢复后在远端运行实际编译与测试。

---

## record-05

**原始文件：** `metadata/ROUND_07_REPORT.md` · 原始内容 Blob SHA：`47e01360b49825f5a31aca44e2db2780abc37bf1`

以下为原始 Markdown 正文（仅将文档位置合并，历史判断不作更新）。

# 第七轮：2023—2025 年导数题数学复核与源码勘误

日期：2026-10-24。本轮操作**仅通过 GitHub 连接提交文件，无本地生成物**。

## 完成内容

1. 对 2023 全国乙卷文科第20题、2023 新高考Ⅰ卷第19题、2025 上海卷第19题、2025 全国Ⅱ卷第18题完成独立数学推导，已发布四篇 Markdown 证明，并补充四份独立的中文 XeLaTeX 源码（仅 GitHub 文本文件）。
2. 题目级总索引保持 **248 条**；数学复核通过由 11 条增加到 **15 条**（按已经确认的共同题合并，相当于 **13 道不同题目**）。尚余 233 条来源记录未完成数学审核。
3. 同步修改主索引和 2020—2026 分期 JSON/CSV/Markdown，质检溯源表中的 15 个来源记录均有证明路径。
4. 确认 2025 全国Ⅱ卷第18题的链式法则中间公式误写减号，正确形式是 g'(t)=f'(x1+t)+f'(x1-t)。独立证明给出更直接的严格递减论证和 x1<x2<2x1。
5. 发现 2025 北京卷第20题上游题干采用 l2,l1 分别对应 x1,x2，而其答案按 l1,l2 计算；两份公开试卷转录也采用 l1,l2。两种对应关系使分式结果正负相反，见专题审计文档。尚未验证权威原卷影像，故本题仍为 source-identified。
6. 质量发现清单由 1 项增至 3 项。原上游仓库没有被修改。

## 审查限制

- 尚有 233 条来源记录的数学正确性未独立确认；全库覆盖和跨卷去重并未完成。
- 2025 北京卷题目文字的下标顺序仍需以原卷影像最终核实，不能擅称官方错题。
- 本轮四份新数学证明均有 Markdown 与独立的 ctexart/XeLaTeX 源码，全部通过 GitHub 连接直接提交。**未实际运行 XeLaTeX 编译、未生成 PDF 或本地文件**，不能将这四份新源码标记为 latex-compiled。
- GitHub Actions 先前仍报告失败；在实际运行成功前，新增校验脚本不能被称作 CI 通过。

## 重要链接

- [最新题目级索引](../index/DERIVATIVE_PROBLEMS_2010_2026.md)
- [数学核验溯源](review-provenance.json)
- [质量问题记录](quality-findings.json)
- [北京卷下标顺序冲突审计](../derivative/reviewed/2025-beijing-q20-transcription-audit.md)
- [全国Ⅱ卷链式法则勘误及证明](../derivative/reviewed/2025-national2-q18.md)
- [四份新证明的 Markdown/TeX 双格式目录](../derivative/reviewed/README.md)

## GitHub Actions 启动限制

核对 2026-10-24 的一次最近失败运行时，GitHub API 将同步 job 报为 `conclusion=failure`，但 `steps=null`；未取得可供确认失败具体根因的执行步骤。这不足以证明是同步 Python 脚本中的异常，自动运行仍然没有验收。

---

## record-06

**原始文件：** `metadata/ROUND_08_REPORT.md` · 原始内容 Blob SHA：`1239c05b5e4bc3703282c99b98e2e6b015eb7782`

以下为原始 Markdown 正文（仅将文档位置合并，历史判断不作更新）。

# 第八轮质检：数学审核与固定来源一致性（2026-10-25）

## 数学复核提交

- 对 [2023 北京卷第 20 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2023/beijing.tex#L627) 重新核对了全部三问。独立证明见 [Markdown](../derivative/reviewed/2023-beijing-q20.md) 与 [TeX](../derivative/reviewed/2023-beijing-q20.tex)。
- 参数为 $a=-1,b=1$；导函数的导数为 $g'(x)=-x(x^2-6x+6)e^{1-x}$；全域恰有 3 个极值点。逐区间验证了根的唯一性及导数变号。
- 三组 JSON/CSV 索引、主索引以及审核溯源已同步：总来源记录 248；独立数学核验 **16 条记录，对应 14 道不同题目**；余下 232 条来源记录未核验。
- 未声称新 TeX 已编译，也未把数学证明自动当作试卷真伪或版权审核。

## 工程安全修复

原同步脚本使用 \`git submodule update --remote\`，会检出未固定的上游分支 HEAD，与 \`sources.json\` 已记录 SHA 及主仓库 gitlink 不一致。

- 修改同步流程，只检出 Git 树中已固定的子模块提交，停止 \`--remote\` 漂移。
- 引入 [validate_pinned_sources.py](../scripts/validate_pinned_sources.py)：检查来源清单中 11 个 SHA、Git 暂存树 gitlink 模式与 SHA、\`.gitmodules\` 的 URL/分支，并在实体检出后验证 HEAD。
- 引入 5 条针对模式、丢失项、多余项、篡改 SHA、路径绕过的单元测试。
- 引入 [offline-qa 工作流](../.github/workflows/audit-archive.yml)：不下载数 GB 子模块即可检查来源锁定、单元测试、题目级索引与质检溯源，避免网络克隆失败掩盖本地元数据错误。

## 验收边界

数学结果通过独立解析及符号计算、数值交叉验证。文本代码已写入 GitHub；新 CI 在 GitHub Runner 真正完成之前，不声明在线测试通过。本轮未生成 PDF、ZIP 或编译成品；未进行原卷影像质检。

---

## record-07

**原始文件：** `metadata/README_HISTORY_PRE_CURATION_2026_10_27.md` · 原始内容 Blob SHA：`b5bfe5f78d98bd5b185701bc99d01467bd3e7e55`

以下为原始 Markdown 正文（仅将文档位置合并，历史判断不作更新）。

# 三千弱水 · 高考数学真题与导数压轴题库

> 高考数学历年真题与高中导数大题资源总库：保留 11 个上游仓库，聚合 TeX / Markdown / PDF / ZIP，逐步建设可检索、可复核的专题题库。

**当前镜像状态（2026-10-26）**：已将 `sources.json` 锁定的 **11/11 个上游仓库完整实体镜像** 到 `mirror/`，对应 **7,222/7,222（100%）** 个原始源文件，缺失 0 个；对照全部 11 个上游根 Git Tree SHA 与主仓库镜像根 SHA，全部一致。历史 `upstream/` 子模块保留作出处参考，实际文件可直接通过本仓库 `mirror/` 下载。

**GitHub Actions 每 30 分钟自动复核/续传**（UTC 每小时 07、37 分，单轮上限 28 分钟，见 [自动镜像工作流](.github/workflows/mirror-all-upstream.yml)）。若锁定版本已全量镜像则跳过；上游之后的新提交**不会自动改变锁定 SHA**，需要单独更新 `sources.json`。数学答案、版权、第三方图片与 PDF 排版仍需独立验证。

[11 仓库最新镜像状态](mirror/STATUS.md) · [机器可读全量核验](mirror/MIRROR_STATUS.json) · [成功的 GitHub Actions 运行](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40354890353)。



## 历史分批迁移记录（当时进度，不代表当前完整度）

以下旧批次中的百分比、缺失数量与金额字节均为当时的快照；请以前述最新 **11/11、7,222/7,222** 为准。

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

- [2010—2019 十年逐年份核验明细](../mirror/HISTORICAL_AUDITS.md#audit-2010-2019)
- [2010—2019 原始 TeX 文件目录](mirror/gaokao-math-problems-compilation/content/)
- 2010—2019 年逐年数量：38、36、36、38、38、32、20、16、14、14。

## 1994 年历史试卷与配套插图补充

1994 年原始试卷 TeX 已完成 **7/7** 文件级严格匹配；1953—1963 年另补充 40 张原始 PNG。详见[本轮审计](../mirror/HISTORICAL_AUDITS.md#audit-1994-and-images-2026-10-25)。文件复刻不代表试题真实性、数学正确性或编译/视觉验收。

## 历史插图与重绘图原始源码（2026-10-25 续批）

本批按固定上游 Git 提交净增 **126** 个实体文件：1963—1965 与 1978—1984 年的 **40 张原始 PNG**，以及 1998—2010 年所选年份的 **86 份重绘图 TeX**。该范围纳入原已有文件后 **132/132** 文件严格匹配；11 源总覆盖 **1,993/7,222**。详见[专项审计](../mirror/HISTORICAL_AUDITS.md#audit-historical-figures-2026-10-25)及[逐文件 SHA 清单](mirror/IMPORT_BATCH_HISTORICAL_FIGURES_2026_10_25.json)。图片视觉、编译、数学与授权尚未验收。

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
- [2010—2014 年地方卷与重点卷](../index/HISTORICAL_PERIOD_INDEXES.md#period-2010-2014)
- [2015—2019 年重点卷](../index/HISTORICAL_PERIOD_INDEXES.md#period-2015-2019)
- [2020—2026 年主要试卷](../index/HISTORICAL_PERIOD_INDEXES.md#period-2020-2026)
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
- [第六轮质检报告](#record-04)
- [2023 全国乙卷文科第20题完整证明](derivative/reviewed/2023-national-b-liberal-q20.md) / [TeX](derivative/reviewed/2023-national-b-liberal-q20.tex) / [2023 新高考Ⅰ卷第19题证明](derivative/reviewed/2023-new-gaokao-1-q19.md) / [TeX](derivative/reviewed/2023-new-gaokao-1-q19.tex)
- [2025 上海卷第19题证明](derivative/reviewed/2025-shanghai-q19.md) / [TeX](derivative/reviewed/2025-shanghai-q19.tex) / [2025 全国Ⅱ卷第18题证明](derivative/reviewed/2025-national2-q18.md) / [TeX](derivative/reviewed/2025-national2-q18.tex)
- [2025 北京卷第20题转录顺序冲突审计](derivative/reviewed/2025-beijing-q20-transcription-audit.md)：暂不升格数学核验
- [第七轮审校报告](#record-05)
- [第八轮质检与版本锁定记录](#record-06) / [2023 北京卷第20题](derivative/reviewed/2023-beijing-q20.md) / [TeX](derivative/reviewed/2023-beijing-q20.tex)
- [机器扫描候选](scripts/scan_derivative_questions.py)、[索引一致性脚本](scripts/validate_question_index.py)、[第五轮报告](#record-03)

共 **16 条来源记录**完成独立数学核验，实际对应 **14 道不同题目**（2011 安徽文理卷同题保留两份出处）。
余下 232 条记录尚需逐题数学复核；多卷同题只打上疑似重复组标签，并未全面去重。

本轮仅在 GitHub 写入源码、索引和质检文本，**不产生本地 PDF 或 ZIP**。
新增的 TeX 尚未编译；GitHub Actions 曾在获得 Runner 前失败，自动同步未完成验收。

