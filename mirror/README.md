# 十一个上游仓库的实体源码镜像

本目录用普通 Git 文件镜像 `sources.json` 中的全部 11 个上游项目。目标不仅包括 `.tex`，也包括编译所需的图片、样式文件、字体依赖、引用文件、构建脚本以及原仓库已公开的 PDF。保留原来的相对目录结构。

## 工作流程

- [镜像工作流](../.github/workflows/mirror-all-upstream.yml)：在 Actions 中选择 `all` 或一项上游来源。
- [增量可重试的镜像脚本](../scripts/mirror_all_upstream.sh)：检出 `sources.json` 规定的固定 SHA；复制源目录（排除 Git 元数据），每个来源独立提交和推送。支持重复运行。
- `mirror/<id>/` 为实体文件；`upstream/<id>/` 仍是 Git 子模块，**不能混淆**。GitHub ZIP 下载会包含前者的真实文件，但不会携带后者子模块的完整文件。

## 实际进度

只能将已提交到 GitHub `main` 分支 `mirror/<id>/` 的文件算作实体导入。编写工作流不代表文件已入库，原有 Actions 还存在运行器启动前失败的问题。

全部上游普通文件总计约 7,200 个，包括大量 PNG 与 PDF；大仓库可能造成 GitHub 容量和推送限制。建议优先逐个来源镜像，脚本每完成一个来源便做一次可恢复的 Git 提交。

**许可提示：**来源混有 MIT、GPL、CC、LPPL 与许可证不明确项目。保留各自许可和署名；原始真题与第三方插图的授权需单独处理，不因镜像而一概变更许可证。

已有配对资料见 [TeX 与 PDF 实体目录](../materials/README.md)。