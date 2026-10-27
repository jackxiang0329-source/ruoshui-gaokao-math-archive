# 镜像目录说明：精简主分支 / 完整快照分支

**完整原件位于 [full-source-archive 分支](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive/mirror)**。该分支保留 11 个固定上游文件树，7,222/7,222 个原件（含 215 个独立 Markdown），Git Tree SHA 与固定提交全部一致。

主分支 `main` 中的 `mirror/` 为精简版本，只保留 **7,007 个非 Markdown** 原始文件。原始 Markdown 内容已合并入 [一个 Markdown 合订本](../archive/SOURCE_MARKDOWN.md)，并附有 [215 条原路径 / SHA 映射](../archive/source-markdown-paths.csv)。

**因此不能再声称主分支的镜像子目录 SHA 与原始上游完全相同。** 完整版本的精确 SHA 核验应针对 `full-source-archive`；想使用源仓库的原始 README、题目 Markdown 相对图片路径、工程构建和编译配置，也应进入完整快照分支。

- [完整来源校验说明](STATUS.md)
- [机器可读的原始来源锁定信息](MIRROR_STATUS.json)
- [合订的历史镜像审计](HISTORICAL_AUDITS.md)
- [新的统一资料目录](../catalog/README.md)

周期性 GitHub Actions 任务每 30 分钟验证完整快照，而不会回填已合并的 Markdown。该任务不自动更新上游版本。许可、数学内容及 PDF 视觉质量仍需分别审核。
