# 11 个上游仓库实体源码镜像：实际核验进度

本表从 **GitHub main 分支实际文件树** 与各上游仓库固定 SHA 的 Git Blob 逐路径校验，**不把 `upstream/` 子模块算作实体导入**。

当前共有 7222 个上游普通文件，**192 个**已核实为相同 Git Blob，**4 个来源**已完整实体入库。

| 上游 | 原始普通文件 | SHA 一致且已入库 | 仍缺失 | 状态 |
|---|---:|---:|---:|---|
| math-lecture-notes | 373 | 0 | 373 | 未完整 |
| gaokao-math-problems-compilation | 5546 | 0 | 5546 | 未完整 |
| gaokaomath | 782 | 0 | 782 | 未完整 |
| first-round-review | 47 | 43 | 4 | 未完整 |
| gaokao-math-corpus | 207 | 0 | 207 | 未完整 |
| 2024-china-gaokao-math | 7 | 7 | 0 | 已完整 |
| gaokao-exam-template | 18 | 18 | 0 | 已完整 |
| mathpaper | 39 | 31 | 8 | 未完整 |
| daxmate-math | 21 | 21 | 0 | 已完整 |
| math-atlas | 110 | 0 | 110 | 未完整 |
| mathex | 72 | 72 | 0 | 已完整 |

## 后续执行

- [远端同步工作流](../.github/workflows/mirror-all-upstream.yml) 与 [固定 SHA 实体镜像脚本](../scripts/mirror_all_upstream.sh) 已提交，但 GitHub Actions 先前工作流未能获得 Runner，不能声称已经运行完毕。
- 大型 PDF/PNG 在当前连接器直接上传时出现过 Git Blob SHA 与原文件不一致的情况，已拒绝把这些不匹配文件挂到主分支。
- 建议恢复 GitHub Actions 执行器后，逐个来源运行：完整 clone 固定版本，rsync 真实文件，分库提交。大型题库的成千图片与 TeX 应一并导入以保留编译依赖。
- 当前仅已存在于仓库 `mirror/` 的源码可视为已经交付。另有 [materials](../materials/README.md) 目录的 6 套 TeX/PDF 已实体入库，但它们不等于上游 11 仓库的完整镜像。

**许可证边界：**来源中有未明确授权项目。完整复制到可能公开的仓库前，还应分别核查原作者代码许可与题面、图片等第三方权利。

[机器可读进度 JSON](MIRROR_STATUS.json)