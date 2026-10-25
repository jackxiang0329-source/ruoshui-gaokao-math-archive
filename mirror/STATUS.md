# 11 个上游仓库实体文件 SHA 质检进度

对 `main` 的实体文件逐个与 `sources.json` 固定提交中的 Git Blob SHA 对比；**不把子模块、索引或脚本算作文件实体**。

**719 / 7,222 个文件逐一 SHA 一致，6 / 11 个上游完整。** 尚缺 6,503 个，数学答案正确性和 LaTeX 可编译性需另行质检。

| 来源 | 上游文件 | 校验通过 | 尚缺 | 状态 |
|---|---:|---:|---:|---|
| math-lecture-notes | 373 | 44 | 329 | 未完整 |
| gaokao-math-problems-compilation | 5546 | 35 | 5511 | 未完整 |
| gaokaomath | 782 | 125 | 657 | 未完整 |
| first-round-review | 47 | 43 | 4 | 未完整 |
| gaokao-math-corpus | 207 | 207 | 0 | 已完整 |
| 2024-china-gaokao-math | 7 | 7 | 0 | 已完整 |
| gaokao-exam-template | 18 | 18 | 0 | 已完整 |
| mathpaper | 39 | 37 | 2 | 未完整 |
| daxmate-math | 21 | 21 | 0 | 已完整 |
| math-atlas | 110 | 110 | 0 | 已完整 |
| mathex | 72 | 72 | 0 | 已完整 |

## 本轮说明

- `gaokaomath` 已归档 125 个真实文件，2021—2026 试卷年度文件在所固定的上游版本中已完整；2020—2017 年度文件已进入仓库。本轮另外通过 SHA 对照提交 4 份 2016 年试卷 PDF。
- 部分 2016 年 PDF 的文件读取请求遭接口安全拦截，未进行绕过，仍记为未导入。其他单个文件可能超过接口可可靠传输的大小限制。
- `mathpaper` 尚有两份超过普通 Contents API 读取能力的 DOCX 未完整归档。
- [GitHub Actions 全量镜像运行](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40103091319) 在分配 Runner 前失败，无法声称运行成功。
- 所有上游版权和第三方试题素材仍需按各自授权处理；数学证明正确性不是 Blob 完整性检验的结论。

[机器可读进度](MIRROR_STATUS.json) · [镜像脚本](../scripts/mirror_all_upstream.sh)
