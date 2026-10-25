# 11 个上游仓库固定版本镜像进度（2026-10-25）

按 `sources.json` 锁定的 11 个上游 Git 提交逐路径比对主仓库 `mirror/<id>/` 下的 **Git Blob SHA 与 Git 文件模式**；不把 `upstream/` 子模块或仅有索引的记录当作实体文件。

**严格一致：1,158 / 7,222**；缺失或模式不一致：**6,064**；来源完整：**6 / 11**。

| 来源 ID | 上游 Blob | SHA 与模式均一致 | 未一致 | 状态 |
|---|---:|---:|---:|---|
| math-lecture-notes | 373 | 133 | 240 | 未完整 |
| gaokao-math-problems-compilation | 5546 | 223 | 5323 | 未完整 |
| gaokaomath | 782 | 287 | 495 | 未完整 |
| first-round-review | 47 | 43 | 4 | 未完整 |
| gaokao-math-corpus | 207 | 207 | 0 | 完整 |
| 2024-china-gaokao-math | 7 | 7 | 0 | 完整 |
| gaokao-exam-template | 18 | 18 | 0 | 完整 |
| mathpaper | 39 | 37 | 2 | 未完整 |
| daxmate-math | 21 | 21 | 0 | 完整 |
| math-atlas | 110 | 110 | 0 | 完整 |
| mathex | 72 | 72 | 0 | 完整 |

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
