# 11 源仓库实体导入进展：2026-10-25

固定版源文件数 **7,222**；严格 Git Blob SHA + 文件模式均一致 **1,158**；剩余 **6,064**；完整来源仓库 **6/11**。

| 来源 | 应有 | 已严格匹配 | 仍待实体入库 |
|---|---:|---:|---:|
| `math-lecture-notes` | 373 | 133 | 240 |
| `gaokao-math-problems-compilation` | 5546 | 223 | 5323 |
| `gaokaomath` | 782 | 287 | 495 |
| `first-round-review` | 47 | 43 | 4 |
| `gaokao-math-corpus` | 207 | 207 | 0 |
| `2024-china-gaokao-math` | 7 | 7 | 0 |
| `gaokao-exam-template` | 18 | 18 | 0 |
| `mathpaper` | 39 | 37 | 2 |
| `daxmate-math` | 21 | 21 | 0 |
| `math-atlas` | 110 | 110 | 0 |
| `mathex` | 72 | 72 | 0 |

## 本轮已提交的文件

- `math-lecture-notes`：新增 25 个文件（包括原始 TeX 与 PDF），保持固定上游 Git SHA。
- `gaokao-math-problems-compilation`：新增 2020—2023 年 46 个高考试卷 TeX 文件（2024—2026 已在此前的镜像中）。
- 已将每批目标 Blob SHA 与固定上游 SHA 比对；已写入的文件均为原始 Git 数据对象，并非 Git 子模块链接。

## 后续批次：206 个实体文件（同日追加）

- 历史试卷 TeX：`gaokao-math-problems-compilation` 增加 **141** 份（含重试成功的 1992 全国文科卷）。
- 数学讲义／测试卷 TeX：`math-lecture-notes` 增加 **65** 份。
- 固定来源模式 + Blob SHA 对照结果：**1,158 / 7,222**；待补齐 **6,064**；剩余源 Blob 大小合计约 **582,105,389 字节**。
- 新增审计工具 `scripts/audit_mirror_inventory.py`，可从固定上游 Git 树重新生成本仓库 HEAD 的镜像覆盖率；并不代表试卷数学审核或 PDF 编译。

## 为什么不能在本连接内完成剩余文件

余下的 Blob 原始体积约 **582,105,389 字节**，其中 **46 个**单个文件不小于 1 MB（主要为历史 PDF、图片和 DOCX），超过当前 GitHub 连接读取二进制大文件的直接能力；单纯将上游 Blob SHA 添加到目标 Git 树会被 GitHub 拒绝，因为目标仓库并不存在该 Blob。Github Actions 的作业在未形成可用 steps/log 的情况下失败，不能代替实际传输。

完整复制的仓库现成入口：`bash scripts/mirror_all_upstream.sh`。它会按 `sources.json` 的固定提交克隆、复制并运行 `scripts/verify_pinned_mirror.py`，通过后分来源提交推送。需要可访问 GitHub 的 Git CLI 环境、写权限和足够磁盘空间；脚本未在当前受限环境执行，不能声称剩余文件已推送。

特别提醒：`SHA` 一致只验证忠实复制；不证明题目真伪、公式正确、图片清晰、PDF 可编译或第三方再分发许可。
