# 11 个上游仓库实体源码镜像：实际核验进度

本表依据 GitHub `main` 分支文件树及各上游固定版本的 Git Blob SHA 逐文件比较，**不把子模块、Git 索引或导入脚本当作源码实体**。

截至 2026-10-24 本轮实际提交，**265 / 7222 个普通文件已校验**；**4 / 11 个来源完整**。未入库 6957 个文件，不得声称全量完成。

| 上游 | 原始文件 | SHA 一致且已入库 | 缺失 | 状态 |
|---|---:|---:|---:|---|
| math-lecture-notes | 373 | 10 | 363 | 未完整 |
| gaokao-math-problems-compilation | 5546 | 20 | 5526 | 未完整 |
| gaokaomath | 782 | 0 | 782 | 未完整 |
| first-round-review | 47 | 43 | 4 | 未完整 |
| gaokao-math-corpus | 207 | 36 | 171 | 未完整 |
| 2024-china-gaokao-math | 7 | 7 | 0 | 已完整 |
| gaokao-exam-template | 18 | 18 | 0 | 已完整 |
| mathpaper | 39 | 31 | 8 | 未完整 |
| daxmate-math | 21 | 21 | 0 | 已完整 |
| math-atlas | 110 | 7 | 103 | 未完整 |
| mathex | 72 | 72 | 0 | 已完整 |

## 本轮新增实体文件

- `math-atlas`：7 个 Markdown 文件。
- `gaokao-math-corpus`：36 个结构化 Markdown/YAML 文件。
- `math-lecture-notes`：10 个原始 LaTeX 源文件。
- `gaokao-math-problems-compilation`：2024—2026 年 20 份 TeX 试卷源码。
- 各个源文件均以原固定提交 SHA 的 Git Blob 为校验基准；并未对其数学内容作独立正确性保证。

## 尚未完成的阻塞

- [全量镜像工作流](../.github/workflows/mirror-all-upstream.yml) 已加入推送触发并已运行，但 [GitHub Actions #40103091319](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40103091319) 在 Runner 分配前失败，无步骤日志，无法归因为代码本身。
- 当前连接方式可以安全提交并核验 UTF-8 文本，却无法可靠复制部分 PDF/PNG/JPG/DOCX 二进制文件；遇到 SHA 不一致或不可读取的内容会拒绝入库。完整镜像仍需要可运行的 GitHub Actions Runner 执行 `scripts/mirror_all_upstream.sh`，或其他能安全传输二进制数据的 Git 环境。
- 试题原作、图片以及许可证不明确的来源仍需分别核查；当前目标仓库保持私有。
- **编译依赖目前尚不齐全，不得宣称所有 TeX 可复编译。**

[机器可读进度](MIRROR_STATUS.json) · [执行脚本](../scripts/mirror_all_upstream.sh) · [来源固定 SHA](../sources.json)
