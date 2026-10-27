# 固定上游镜像：最终完整性状态

**已锁定的 11 个来源，共 7,222/7,222 个原始 Git 文件。完整 SHA 校验的对象是 [full-source-archive 分支](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，不是精简后的 main。**

2026-10-26 完成了原始 11 棵 Git 文件树的严格 SHA 比对；2026-10-27 将完整快照单独保存，并在主分支将 215 份上游 Markdown 合为一份。原快照的独立原件和目录树均仍完整保留。

| 位置 | 文件数量 | 说明 |
|---|---:|---|
| 完整快照 `full-source-archive/mirror/<source>` | **7,222** | 原始路径、SHA 和 Git 模式均与锁定版本一致 |
| 精简主分支 `main/mirror/<source>` | **7,007** | 原始非 Markdown 文件；镜像树不再与上游同 SHA |
| `main/archive/SOURCE_MARKDOWN.md` | **1 个合订本** | 汇集 215 个上游 Markdown 原文及 SHA、路径映射 |

[逐源机器审计记录](MIRROR_STATUS.json) · [源文合订本](../archive/SOURCE_MARKDOWN.md) · [历史审计](HISTORICAL_AUDITS.md)

原 [完全镜像成功运行](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/actions/runs/40354890353) · [完整快照的周期校验工作流](../.github/workflows/mirror-all-upstream.yml)。

完整快照校验不意味着高考卷真伪、第三方再分发权利、数学证明或 PDF 质量已经独立验证。
