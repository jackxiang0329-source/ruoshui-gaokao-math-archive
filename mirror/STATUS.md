# 11 个上游仓库实体源码镜像：实际核验进度

根据 GitHub `main` 当前文件树与各原仓库在 `sources.json` 固定版本的 Git Blob SHA 逐项核对。**不把子模块、文件索引或脚本算成已导入文件**。

- SHA 验证通过：**539 / 7222** 个上游普通文件。
- 完整实体镜像：**6 / 11** 个仓库。
- 仍缺：**6683** 个文件，主要集中在大型 TeX+PNG 题库和 PDF 试卷库。

| 上游 | 原始文件 | SHA 一致并实体入库 | 缺失 | 结果 |
|---|---:|---:|---:|---|
| math-lecture-notes | 373 | 10 | 363 | 未完整 |
| gaokao-math-problems-compilation | 5546 | 20 | 5526 | 未完整 |
| gaokaomath | 782 | 0 | 782 | 未完整 |
| first-round-review | 47 | 43 | 4 | 未完整 |
| gaokao-math-corpus | 207 | 207 | 0 | 已完整 |
| 2024-china-gaokao-math | 7 | 7 | 0 | 已完整 |
| gaokao-exam-template | 18 | 18 | 0 | 已完整 |
| mathpaper | 39 | 31 | 8 | 未完整 |
| daxmate-math | 21 | 21 | 0 | 已完整 |
| math-atlas | 110 | 110 | 0 | 已完整 |
| mathex | 72 | 72 | 0 | 已完整 |

## 本轮（2026-10-24）实际新增与核验

- `math-atlas`：**110/110 完整**，Markdown、TypeScript/TSX、CSS、SVG、JPG、ICO、配置文件等均与原仓库一致。
- `gaokao-math-corpus`：**207/207 完整**，Markdown 题面、YAML 配置、18 张 PNG、JSON 模式、Python 工具及 `uv.lock` 等原文件均与原仓库一致。
- `gaokao-math-problems-compilation`：已补入 **2024—2026 年 20 份 TeX 试卷文件**，但该项目尚有大量 PNG 等依赖没有归档。
- `math-lecture-notes`：已补入 10 份上游 TeX 文件，其他源码、图片/PDF 未全部同步。

## 仍需处理的限制

- 自动全量镜像工作流 [#40103091319](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40103091319) 在 GitHub 分配 Runner 前失败，无法获得任何步骤日志。该工作流已支持通过修改其 YAML 自动触发，亦可在 Actions 页面手动执行。
- 连接器可用 Base64 逐文件同步并验证小型二进制素材，但部分 **大于 1 MiB** 的原文件在 Contents API 中返回空内容，必须使用具备 `git clone` 能力的远端环境完成，不能直接上传不完整文件。
- 数学正确性、版权许可与第三方试题的转录完整性并未因此自动通过独立审核；全部 TeX 的可复编译性仍待补齐依赖后验证。

[机器可读进度](MIRROR_STATUS.json) · [完整镜像脚本](../scripts/mirror_all_upstream.sh) · [固定版本清单](../sources.json)
