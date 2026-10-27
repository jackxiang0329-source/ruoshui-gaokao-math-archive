# 高考数学：固定上游镜像状态

## 当前验收（2026-10-26）

**11/11 个上游固定提交的实体镜像完整，7,222/7,222 个原始文件，缺失 0 个。**

已将 `sources.json` 中 11 个固定来源的 Git Tree SHA 与 `mirror/<source-id>/` 逐源比对，全部一致。源文件路径、内容和 Git 模式未被去重整理操作改变。

- [机器可读的全部来源审计](MIRROR_STATUS.json)
- [已成功运行的实体迁移工作流](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40354890353)
- [原始镜像说明](README.md)
- [历史审计与历次补档内容合订本](HISTORICAL_AUDITS.md)

**自动化：** `mirror-all-upstream.yml` 每 30 分钟检查固定 SHA，文件相同则跳过；不自动引入未经审查的新上游版本。

**限制：** Git Tree 一致仅代表复制完整，不等于数学正确性、原卷真实性、PDF 可读性、图片质量或版权已审查。
