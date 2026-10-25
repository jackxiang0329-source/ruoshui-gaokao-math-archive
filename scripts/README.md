# 同步和索引工具

运行 `bash scripts/sync_sources.sh` 更新 11 个 Git 子模块、生成文件级索引并执行一致性验证。此命令需要 Git 和 Python 3；GitHub Actions 可调用。

索引脚本只筛选文件名，不能证明文件内容是导数题，也不会做逐题数学核验。

固定版本核验：`python3 scripts/validate_pinned_sources.py --index-only`（仅 Git 索引，无须下载子模块）；克隆子模块后运行 `python3 scripts/validate_pinned_sources.py` 严格对比 HEAD。同步不再使用 `--remote`，更换上游版本须显式修改锁定 SHA 与 gitlink 后复核。

轻量离线质检：`.github/workflows/audit-archive.yml` 会运行单元测试、题目级索引及审核溯源校验。数学正确性与 XeLaTeX 编译另行验收。
