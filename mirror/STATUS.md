# 11 个上游仓库实体文件 SHA 质检进度

对 `main` 的实体文件逐个与 `sources.json` 固定提交中的 Git Blob SHA 对比；**不把子模块、索引或脚本算作文件实体**。

**793 / 7,222 个文件逐一 SHA 一致，6 / 11 个上游完整。** 尚缺 6,471 个，数学答案正确性和 LaTeX 可编译性需另行质检。

| 来源 | 上游文件 | 校验通过 | 尚缺 | 状态 |
|---|---:|---:|---:|---|
| math-lecture-notes | 373 | 44 | 329 | 未完整 |
| gaokao-math-problems-compilation | 5546 | 35 | 5511 | 未完整 |
| gaokaomath | 782 | 199 | 583 | 未完整 |
| first-round-review | 47 | 43 | 4 | 未完整 |
| gaokao-math-corpus | 207 | 207 | 0 | 已完整 |
| 2024-china-gaokao-math | 7 | 7 | 0 | 已完整 |
| gaokao-exam-template | 18 | 18 | 0 | 已完整 |
| mathpaper | 39 | 37 | 2 | 未完整 |
| daxmate-math | 21 | 21 | 0 | 已完整 |
| math-atlas | 110 | 110 | 0 | 已完整 |
| mathex | 72 | 72 | 0 | 已完整 |

## 本轮说明

- 2013 年 38 份 PDF 已分两批全部按固定提交 SHA 对照实体入库，逐个校验源与目标 Git Blob SHA。

- `gaokaomath` 已归档 125 个真实文件，2021—2026 年试卷年度文件除 2023 年天津卷（约 1.7 MB）外已按上游 SHA 完整；2020—2017 年度文件已进入仓库；2015 年普通高考 31 份与春季高考 1 份也已完成上游 SHA 对照和实体入库。2016 年原缺失的 4 份试卷本轮已按锁定上游 Git Blob SHA 实体补入。2013、2014、2015、2016 年度现在均按固定上游文件 Blob SHA 完整。
- 2016 年的 4 份先前缺失 PDF 改用 Base64 读取原始二进制，写入后逐个核对 Blob SHA；原先因文本解码失败导致的导入阻碍已排除。其他单个文件可能超过接口可可靠传输的大小限制。
- `mathpaper` 尚有两份超过普通 Contents API 读取能力的 DOCX 未完整归档。
- [GitHub Actions 全量镜像运行](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40103091319) 在分配 Runner 前失败，无法声称运行成功。
- 所有上游版权和第三方试题素材仍需按各自授权处理；数学证明正确性不是 Blob 完整性检验的结论。

[机器可读进度](MIRROR_STATUS.json) · [镜像脚本](../scripts/mirror_all_upstream.sh)
