# 11 个上游仓库的完整原始镜像

`mirror/<source-id>/` 下保存全部 **11 个固定版本原始 Git 树**，**7,222/7,222 个文件**与固定上游的路径、SHA 和 Git 模式一致。

- [当前完整性验收](STATUS.md) · [机器可读的 SHA 校验数据](MIRROR_STATUS.json)
- [合并后的历史专项审计和迁移记录](HISTORICAL_AUDITS.md)
- [GitHub Actions 自动镜像工作流](../.github/workflows/mirror-all-upstream.yml)
- [统一检索与去重目录](../catalog/README.md)

原始 `mirror/<source-id>/` 文件必须保留，特别是来源自带的 Markdown、TeX、PDF、图片与样式文件；本仓库不因内容相似而直接删改它们。文档精简和去重只发生在派生目录和历史报告层。上游子模块 `upstream/` 仍用于源版本对照，与真实镜像的文件区分。

固定版本镜像每 30 分钟检查一次，版本 SHA 不变时跳过；本机制**不会自动抓取上游后续新提交**。原始题目版权及第三方插图的再分发许可需要逐项审核，数学正确性和 PDF 可读性也不由 Git SHA 保证。
