# 11 个固定上游仓库：实体镜像进度（2026-10-26）

## 2026-10-26 本次续迁：1988—1990 年 60 张插图及高中数学 14 份 PDF

从此前经增量验证的 **2,541/7,222** 出发，向主分支实际导入 **74 个真实 Git Blob**（原始文件字节总量 **2,659,734**）：

- **DxAThing**：1988 年 23 张 PNG、1989 年 23 张 PNG、1990 年 14 张 PNG，共 **60 张原始插图**，各年份 **完整目录树 SHA** 均与锁定源提交 `f1ae169b58a75b3db6e35c670b3f0d5c78718188` 完全相同。提交：[1988](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/67bc4881fd033f9eb8a3b0553a99a9c4f7eb654c) / [1989](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/b6859c48efd41cec83b1a013a37ed7527a0f12a3) / [1990](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/7538d353e1b661a9d9f8ee2cb65a9ad1ef614b50)。
- **Dreamaker203**：新增 **14 份高中数学测试卷 PDF**，逐文件 Git Blob SHA、模式与固定源提交 `b89f6207bc5b84f501837ea6da3899799a8787d8` 相同。提交：[14 份 PDF](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/57cc6e4ef39eecd3931aeb932123dcdb5ff8375b)。

| 来源 | 严格匹配 / 固定源文件 | 尚缺 |
|---|---:|---:|
| DxAThing 大型高考 LaTeX / 插图 | **1,540 / 5,546** | 4,006 |
| Dreamaker203 数学讲义 | **216 / 373** | 157 |
| deekur 历年试卷 PDF | 344 / 782 | 438 |
| hbinfrog 高三复习 | 43 / 47 | 4 |
| Yan-Zero MathPaper | 37 / 39 | 2 |
| 其他 6 个已完整来源 | 435 / 435 | 0 |
| **总计** | **2,615 / 7,222（36.21%）** | **4,607** |

至此 **6/11 个来源完整**，5 个仍未完整；固定源剩余原始 Blob 大小估算 **522,909,935 字节**。本统计为可追溯的 **之前增量核验 + 本轮 74 个严格比对**，不是重新全量扫描所有来源。大于 1 MB 的二进制文件通过当前轻量内容接口经常无法读取，完整源树仍需仓库的 Git 对象批量导入脚本。

[本轮 74 个文件逐路径 SHA / mode / 字节清单](DIRECT_IMPORT_74_FILES_2026_10_26.json) · [更新后机器台账](MIRROR_STATUS.json)。文件搬运 SHA 一致不等于试题真实、答案准确、LaTeX 编译通过、出版质检通过或第三方版权授权已核实。

---

## 上一次续批（历史快照）：1987 年全部试题插图

本批将固定来源 `DxAThing/Gaokao-Math-Problems-Compilation@f1ae169b58a75b3db6e35c670b3f0d5c78718188` 的 1987 年五个图形子目录 **29 张 PNG（669,570 字节）** 真正写入 `mirror/gaokao-math-problems-compilation/img/1987/`，逐图 Blob SHA 与 Git mode 已校验。目标全部五个目录树 SHA 与原始固定版本一致，冲突 0。提交：[8aaa7ef8](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/8aaa7ef87fccd30521edaaac7eeee9ea28089724)。

在之前增量核验 **2,512/7,222** 基线上，累计 **2,541/7,222（35.18%）**，缺 **4,681**，6/11 个仓库完整，剩余原始字节估算 **525,569,669**。这不是重新递归审计全部 11 源；试题真实性、数学正确性、版权、TeX 编译与视觉排版不在本轮校验范围。



上一批已验证 **2,541 / 7,222（35.18%）** 个实体源文件按固定上游 SHA 和 Git mode 一致，尚缺 **4,681**，完整来源 **6 / 11**。这属于以前次 2,475 条核验为基线加 37 条新文件的**增量核验**，不是重新遍历全部 11 个上游仓库。

| 来源 | 已验证 | 总数 | 尚缺 |
|---|---:|---:|---:|
| 大型高考 LaTeX 题库（DxAThing） | 1,480 | 5,546 | 4,066 |
| 数学讲义 | 202 | 373 | 171 |
| 历年高考 PDF（deekur） | 344 | 782 | 438 |
| 高三复习 | 43 | 47 | 4 |
| MathPaper | 37 | 39 | 2 |
| 其他 6 个完整来源 | 435 | 435 | 0 |
| **合计** | **2,541** | **7,222** | **4,681** |

## 本轮 GitHub 实体导入：37 个文件

- [1985 年试题图形，19 张 PNG](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/017c216fae62a361855f6bb8e64c03d75e1ed27f)：286,374 字节；目标 `img/1985` 子树 Git SHA `cea972bb9d2cd3342cdb4378585bba1dc560a4d3` 与固定上游一致。
- [1993 年试卷，5 份 PDF](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/69cfda014a4cc2c57a2d0bfd63911b6079547ac9)：2,258,616 字节；1993 年目录树 Git SHA 与固定上游一致。
- [1978—1984 年试卷，13 份 PDF](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/f7a6d93369e903665f4bf3649c52522781635e2a)：6,206,037 字节；各年度目录树 Git SHA 与固定上游逐个一致。

本轮新增 **8,751,027 字节**原始文件，均以仓库真实 Blob 对象入库而非 Gitlink、LFS 占位或原站链接。估算剩余固定源文件原始大小 **525,569,669 字节**（约 526.2 MB），历史基线的大小统计口径保持不变。

验收边界：Git 树和 Blob SHA 仅证明拷贝内容与模式一致，**不代表试卷真伪、数学答案正确、PDF 出版质量或第三方再分发许可已审核通过**。现有 GitHub Actions 全量镜像工作流最近历史运行失败且 Runner 未给出执行步骤；不能将其视为自动导入成功。剩余主要包含大量二进制文件，优先使用仓库已有的 `scripts/import_pinned_git_trees.py --push` 对 11 个固定源进行完整 Git 对象传输。

[机器可读状态](MIRROR_STATUS.json) · [完整导入手册](../scripts/README_FULL_IMPORT.md)

---

## 历史记录


## 本轮新增 1977 目录原始 PNG（62 个文件，已提交 main）

最新主分支 `main@62e1edf78807453ba4b62694b25650de5dcf44e4` 已逐文件读取固定上游 `DxAThing/Gaokao-Math-Problems-Compilation@f1ae169b58a75b3db6e35c670b3f0d5c78718188` 的 `img/1977/` 树，与主仓库完整递归 Git 树按 Blob SHA 与 Git 模式逐路径复核，**新增实体 PNG 62/62 一致、冲突 0**，共计 **2,605,421 字节**。该上游图片年份目录现为 **62/147**；其余 85 张尚未到齐。[62 个文件 SHA、大小及路径清单](DIRECT_IMPORT_62_PNG_2026_10_26.json)。

以前一轮全 11 来源严格核对 **2,297/7,222** 为基线，加上本轮独立验证且此前缺失的 62 个文件，累计实体严格匹配 **2,359/7,222（32.66%）**；缺 **4,863** 个，上游原始剩余字节 **557,579,772**（约 557.6 MB）。本轮没有重新逐文件遍历其余 10 个上游，所以上述总数是「原全量审计＋本批已验证增量」的可追溯计算，不冒称独立重跑的全库审计。

| 固定来源 ID | 已按 SHA+模式匹配 | 源文件总数 | 未匹配 |
|---|---:|---:|---:|
| math-lecture-notes | 202 | 373 | 171 |
| gaokao-math-problems-compilation | 1,316 | 5,546 | 4,230 |
| gaokaomath | 326 | 782 | 456 |
| first-round-review | 43 | 47 | 4 |
| mathpaper | 37 | 39 | 2 |
| 其他 6 个已完整来源 | 435 | 435 | 0 |
| **总计** | **2,359** | **7,222** | **4,863** |

仍有 **6/11** 个来源完整，其余 5 个仍缺真实文件；单靠 Git 子模块不能代替源文件。本次仅确认二进制镜像内容与 Git 模式匹配，不保证数学证明、官方真题身份、插图效果、LaTeX 编译或第三方版权许可。

---

## 历史镜像核验与导入批次（以下数值均为当时快照，不代表最新覆盖率）

## 2026-10-26 全部 11 来源重新核验

按 11 个固定 Git SHA 的递归树与主分支 main@faf453a6b0d2bca6be018e23b863e00d12740ab1 逐一比对，**严格匹配 2,113 / 7,222（29.26%）**，未匹配 **5,109** 个，剩余源 Blob 约 **564,705,708 字节**；完整来源 **6 / 11**。

| 来源 | 匹配 / 期望 | 尚缺 |
|---|---:|---:|
| math-lecture-notes | 190 / 373 | 183 |
| gaokao-math-problems-compilation | 1,105 / 5,546 | 4,441 |
| gaokaomath | 303 / 782 | 479 |
| first-round-review | 43 / 47 | 4 |
| mathpaper | 37 / 39 | 2 |
| 其他 6 个已完整仓库 | 全部匹配 | 0 |

本轮直接新增 8 份原始重绘图 TeX，合计 21,746 字节，提交 [faf453a6](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/faf453a6b0d2bca6be018e23b863e00d12740ab1)。同时发现上一次进度记录后还有其他提交，故实际新总量**不是单纯在旧统计上加 8**；以本次完整树对照为准。下文 2026-10-25 的记录均为历史批次快照，不能当作当前结果。


按 `sources.json` 锁定的 11 个上游 Git SHA，对 `main@6e0c3f2c7dec775519341fab98db756da2661323` 的递归 Git 树逐路径比较原始 Blob SHA 和文件模式。**子模块 Gitlink 不计入实体文件。**

**严格一致：2,105 / 7,222（29.15%）**；未严格匹配：**5,117**；完整来源：**6 / 11**；剩余固定上游 Blob 原始大小约 **564,727,454 字节**。

| 来源 ID | 应有 Blob | SHA + mode 严格匹配 | 未匹配 | 状态 |
|---|---:|---:|---:|---|
| math-lecture-notes | 373 | 190 | 183 | 未完整 |
| gaokao-math-problems-compilation | 5546 | 1097 | 4449 | 未完整 |
| gaokaomath | 782 | 303 | 479 | 未完整 |
| first-round-review | 47 | 43 | 4 | 未完整 |
| gaokao-math-corpus | 207 | 207 | 0 | 完整 |
| 2024-china-gaokao-math | 7 | 7 | 0 | 完整 |
| gaokao-exam-template | 18 | 18 | 0 | 完整 |
| mathpaper | 39 | 37 | 2 | 未完整 |
| daxmate-math | 21 | 21 | 0 | 完整 |
| math-atlas | 110 | 110 | 0 | 完整 |
| mathex | 72 | 72 | 0 | 完整 |

## 2026-10-26 追加导入与独立全量复核

已向 main 提交 [10 份原始 TeX 图形源码](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/ae9fc963a2ba7960bdbfe7012079cba6567cf049)，原始大小 26,526 字节；10/10 Blob SHA 和 Git 模式与上游固定版本完全一致。主分支新增记录在最近一次 88 文件导入快照之后。复核所有 11 个固定来源后，严格匹配 **2,105 / 7,222**，未匹配 **5,117**，剩余字节 **564,727,454**。其他导入批次仍保留其历史快照，不能与此处总数混淆。

## 最新批次：新增 88 个固定上游实体文件（2026-10-25）

从旧镜像严格匹配 2,007/7,222 的主分支提交 `20129a5dbc6d926386be3775f4e2addb0a2d6c9e` 出发，连续导入以下**实际文件**：

- **12 份历史高考试卷 PDF**：来自 `deekur/gaokaomath`，746,186 字节，1958／1985／1990 等目录。保留“来源网络，不确定真实性”等原文件名。
- **12 份数学讲义和专题测试 PDF**：来自 `Dreamaker203/math-lecture-notes`，878,307 字节。
- **64 份原版 TeX 插图／重绘文件**：来自 `DxAThing/Gaokao-Math-Problems-Compilation`，143,778 字节。

新增 **88 文件／1,768,271 字节**，其每个路径的 SHA、Git mode 和字节数均与上游固定版本一致。导入后以主分支 `6e0c3f2c7dec775519341fab98db756da2661323` 为终点，读取全部 11 个上游固定版本的递归 Git 树再次核对，得到 **2,095/7,222（29.01%）** 严格匹配，无已匹配项目退化；另有 5,127 个上游文件尚未到齐。[查看 88 个实体文件的机器审计清单](DIRECT_IMPORT_88_FILES_2026_10_25.json)。

这只验证文件复制忠实，不代表每套试卷来源官方性、图片质量、TeX 编译、数学正确性或再分发权利。完整迁移仍可使用 [Windows 一键导入器](../scripts/README_FULL_IMPORT.md)，将约 564.8 MB 的剩余源 Git 对象完整复制，而不是通过聊天接口伪造文件。

### 前一次 14 文件批次（历史快照）

## 本轮新入库 14 个 Git 实体文件（2026-10-25）

来自三个原始仓库，已直接上传到本仓库主分支，不是子模块、文件名或链接：

- **历年高考试卷 PDF**：gaokaomath 新增 4 份，分别为 1958 年两份、1977 年一份、1985 年一份，合计 287,532 字节。
- **数学讲义测试 PDF**：math-lecture-notes 新增 6 份，合计 406,568 字节。
- **原版图片重绘 TeX 源码**：gaokao-math-problems-compilation 新增 4 份，合计 530 字节。

本批源对象合计 **14 文件 / 694,630 字节**，上传重建每个原始 Blob 后比对原始 SHA，最终再把 11 个固定版来源的递归 Git 树与自己的主分支 Git 树逐条比较：**2,007 / 7,222 完整匹配，模式或 SHA 冲突计 0（仅计已匹配项目）**。提交为 [PDF 批次](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/0967ec93616050d13182bc88ad66b0f4f9f8c7f4) 和 [讲义／TeX 批次](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/commit/d0d8195f5e63940375b4ca29e0a2d25f967d002a)。[逐文件 SHA 和字节数清单](DIRECT_IMPORT_14_FILES_2026_10_25.json)。

其余超过约 566 MB 的大型二进制内容需要完整 Git 对象传输。新增可在 Windows 双击的 [11 来源一键导入工具](../scripts/README_FULL_IMPORT.md)，使用原生 Git 传送整棵树，保留 PDF、PNG、DOCX 字节与文件模式；已在隔离本地 Git 回归环境验证 SHA、快进推送和不修改工作树。**这不等于所有 11 个来源已经导入完毕**；GitHub Actions 远程环境仍不能宣布正常。

## 本轮 126 文件（2026-10-25）

以 `main@97d236947c30b45c979d261bbb16e055c8bfa92e` 上核验的 **1,867** 个为基线，新增 **40 张 PNG**、**86 份重绘图 TeX**，合计 **126 文件 / 669,703 字节**；文件导入终点 `main@9bd7183eb106e815399e156c273fdd368fa7d37c` 独立核验得到 **1,993/7,222**。具体逐年份与逐路径 SHA 见[审计报告](AUDIT_HISTORICAL_FIGURES_2026_10_25.md)及 [JSON](IMPORT_BATCH_HISTORICAL_FIGURES_2026_10_25.json)。未进行图像目视质检、数学审核、PDF 编译、第三方许可裁定或 CI 成功验收。

## 上一批（历史快照，不代表最新统计）

### 上一批独立复核与 44 文件补全

- 对上次未同步汇总的并行导入进行完整重新统计：`main@46efd8fe7e121a46b94c71e980b498b53f80380c` 已严格匹配 **1,823** 个文件，而非文档旧值 1,540。历史记录保留，不把差额 283 冒称本轮新增。
- 从固定上游 `DxAThing/Gaokao-Math-Problems-Compilation@f1ae169b58a75b3db6e35c670b3f0d5c78718188` 实际新增 **4 份 1994 年 TeX 与 40 张 1953—1963 年 PNG**，原始总大小 **178,810 字节**；所有新 Blob SHA 和模式一致。
- 文件提交 `388956f27777d33f754e1abcbc18b5e035e51fe8` 已写入 `main`，随后直接重取固定版上游树及 `main` Git 树独立计算，得到 **1,867/7,222**。其中 1994 年全部 **7/7** 份原始 TeX 实体一致。
- [本轮新文件审计](AUDIT_1994_AND_IMAGES_2026_10_25.md)；2010—2019 年 282/282 份 TeX 的历史审计见 [十年核验](AUDIT_2010_2019.md)。
- **注意：**本轮仅验证 Git 文件完整性；试卷真伪、数学证明、LaTeX/PDF 编译、插图视觉及第三方授权未因此通过。

## 历史批次：2010—2019 年全部 282 份试卷 TeX 到齐

从已核验的主分支 `c955845b730c12be9ae893dffeec14f5026721fc` 继续新增 `content/2010/`—`content/2019/` **244 个原始 TeX Git Blob**，逐年合计 38 + 36 + 36 + 38 + 38 + 32 + 20 + 16 + 14 + 14 = **282 个**，其中 2013 年 38 个此前已入库。

对当时 GitHub `main` 树逐路径比对 10 个固定上游 Git 年份树：**282/282 严格匹配 SHA 和模式，异常 0，新增 244 个文件原始字节合计 5,620,920**。汇总镜像覆盖 **1,540/7,222**，缺 **5,682**，未完整源还是 **5/11**，尚余源 Blob 字节数估计 **574,588,580**（采用此前可重复计算口径减去本批经核实新增原始大小）。

[十年逐年审计](AUDIT_2010_2019.md)。此结论只涉及 Git 数据完整性，**未宣称数学审校、PDF 编译、试题真实性或法律授权已经完成，也未宣称 GitHub Actions 成功**。

## 上一批次（历史记录）：新增 138 个文件

本次以先前主分支提交 `cd405ded34e1100763c2a9ac69cce870335fe651` 为基准，和追加完成时的 Git 树逐项比较。**实际新增 138 个 Git Blob，全部与固定上游原始 SHA 和文件模式严格一致，未发现错误导入**：

- `math-lecture-notes`：39 个（38 个高中数学 TeX、1 个 Markdown 说明），累计 **172/373**；尚余 201 个 PDF。
- `gaokao-math-problems-compilation`：61 个年份 `index/*.tex` + 38 个 `content/2013/*.tex`，累计 **322/5,546**。**64/64 份年份索引**以及 **2013 年全部 38/38 份卷别 TeX** 已按 SHA 和模式实体匹配。
- 新增源 Blob 原始字节数 **1,895,889**；总严格匹配 **1,296/7,222**，仍缺 **5,926**；从此前剩余 582,105,389 字节扣减后，尚余约 **580,209,500 字节（580.2 MB）**。完整来源仍 **6/11**。
- 这一结果是仓库 Git 树和固定源 Git 树的独立核对，不代表 XeLaTeX 编译、数学核验、试题真实性、第三方再分发许可或 GitHub Actions 成功。源二进制文件尚需在具备完整 Git 传输能力的环境复制。

**以下记录为本日较早各次导入的历史快照，数字不表示当前总计。**

## 2026-10-25 追加直接 GitHub 导入

- 本轮新增 **71 个实际 Blob 文件**（不是 gitlink，也不是仅更新文件名）：其中 `gaokao-math-problems-compilation` 新增 2020—2023 年 46 份试卷 TeX，`math-lecture-notes` 新增 25 份源码和 PDF；详细见 [直接导入记录](IMPORT_PROGRESS_2026_10_25.md)。
- 现有 6 个来源完整，其余 5 个来源未完整；余下约 585.1 MB，含 46 个 1 MB 及以上的缺失 Blob，连接器不能完整获取这些二进制内容。
- GitHub Actions 离线检查及全量同步仍曾在无 Runner 步骤记录的情况下失败；因此不把提交视作 CI 成功。

## 2026-10-25 续批：历史试卷与测试卷实体补充

- 对比上一个 952 个文件的仓库快照，**本续批额外加入 206 个经过 SHA/模式比对的实体 Blob**。
- `gaokao-math-problems-compilation` 从 81 个提升为 **223 个**：本续批新增 141 份 1952—1994 年部分历史试卷 TeX。包括 1992 年一份曾因连接中断而重新成功导入的试卷；这些历史文件仍需真伪及数学审核。
- `math-lecture-notes` 从 69 个提升为 **133 个**：本续批新增 65 份测试卷及讲义 TeX。
- 文件级总体严格匹配 **1,158 / 7,222**，缺失或 SHA/模式不一致 **6,064**，剩余约 582.1 MB；完整上游仍为 **6 / 11**。
- 新增 [固定提交镜像审计脚本](../scripts/audit_mirror_inventory.py) 和 [5 条单元测试](../tests/test_audit_mirror_inventory.py)，可在初始化全部上游子模块后复算 Git 对象统计。此处未宣称 GitHub Actions / XeLaTeX 已通过。

## 此前变化与边界

- 对照固定上游提交 `deekur/gaokaomath@08179f1fc0a3300787155d92800ac82b57ee4118`，新提交 1952、1953、1954—1957、1959—1965 年历史试卷共 **13 个 PDF**，及 **2011 上海春季高考 1 个 PDF**。文件路径及校验 SHA 见 [历史试卷核验记录](AUDIT_1952_1965.md)。
- 先前核验并补齐的 **2016 年四份缺失 PDF 已存在于 main 且 SHA 一致**；见 [2016 核验](AUDIT_2016_GAPS.md)。
- 修正 `mathpaper/Package/GKExam.sty` 的 Git 模式：原仓库是符号链接 `120000`，此前错误存为普通文件 `100644`。两者 Blob SHA 相同，但之前**不能算严格模式一致**；现已按原模式恢复。
- 其余 2023 年天津 PDF 尚未实体入库（固定上游 Blob `ba9c93b59d737d76c7fb165001b0bd2c7f78d91e`，上游大小 1,717,817 字节）。
- `mathpaper` 尚有两份较大 DOCX 未完整入库；`gaokaomath` 早年试卷及大型题库来源仍大量缺失，不能称为全库镜像完成。
- 历史试卷中存在标注“来源不明”“真实性不确定”的原始文件名；**哈希一致只证明镜像忠实，不证明试卷是真题**。
- [最近一次全量镜像 Actions 运行](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40165208999) 状态为失败，未获得可用的作业步骤记录；本次校验基于 Git 对象直接比对，并非 Actions 运行通过。
- **源文件 SHA/模式一致 ≠ LaTeX 编译通过 ≠ 数学解析正确 ≠ 已取得第三方内容再分发授权**。以上另行检查。

[机器可读状态](MIRROR_STATUS.json) · [镜像脚本](../scripts/mirror_all_upstream.sh)


## 可重复的镜像完整度审计

已经递归检出 11 个固定版本的上游子模块后，可用

```bash
python3 scripts/validate_pinned_sources.py
python3 scripts/audit_mirror_inventory.py --output mirror/MIRROR_STATUS.json
```

重新读取 **本仓库 HEAD 的实际 Git 对象**，计算逐来源的期望文件、SHA 与模式严格匹配的文件、缺失／模式不一致文件及多余文件。该命令只输出本地统计文件，不自动修改 GitHub；需审核差异再提交。单来源可加 `--source SOURCE_ID`。

该工具检测镜像完整度，而不是数学证明、PDF 排版或版权。自动质检没有获得正常 GitHub Runner 日志之前，不能声明 CI 通过。
