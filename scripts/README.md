# 同步和索引工具

运行 `bash scripts/sync_sources.sh` 更新 11 个 Git 子模块、生成文件级索引并执行一致性验证。此命令需要 Git 和 Python 3；GitHub Actions 可调用。

索引脚本只筛选文件名，不能证明文件内容是导数题，也不会做逐题数学核验。

固定版本核验：`python3 scripts/validate_pinned_sources.py --index-only`（仅 Git 索引，无须下载子模块）；克隆子模块后运行 `python3 scripts/validate_pinned_sources.py` 严格对比 HEAD。同步不再使用 `--remote`，更换上游版本须显式修改锁定 SHA 与 gitlink 后复核。

轻量离线质检：`.github/workflows/audit-archive.yml` 会运行单元测试、题目级索引及审核溯源校验。数学正确性与 XeLaTeX 编译另行验收。


重新核算固定版本镜像数量：`python3 scripts/audit_mirror_inventory.py --output mirror/MIRROR_STATUS.json`。需要先递归检出所有 11 个上游子模块。该脚本按 **HEAD Git SHA + mode** 统计，不把子模块 gitlink 或索引路径算作完整文件。运行后先审阅本地 JSON，再自行提交。独立单元测试在 `tests/test_audit_mirror_inventory.py`。


## 全量搬运全部 11 个固定版上游仓库

[详细用法：README_FULL_IMPORT.md](README_FULL_IMPORT.md)。

Windows 用户可以双击 [一键导入11个仓库.cmd](一键导入11个仓库.cmd)，使用 PowerShell、Python 和 Git for Windows 完成真实 Git Blob 导入，无须 rsync/WSL。Linux/macOS 运行：

    python3 scripts/import_pinned_git_trees.py --push

选择一个来源：

    python3 scripts/import_pinned_git_trees.py --source gaokaomath --push

与旧版 rsync 路径相比，新脚本完整抓取上游 Git 对象，通过临时 Git index 组装精确的 Git 树；只有当迁入目录的树 SHA 与上游固定树 SHA 完全一致时才快进推送。脚本不会修改工作目录；多次执行会跳过已经完整匹配的来源。镜像 Actions 的 shell 入口也已改为调用该版本；但远程 Runner 未正常执行前，不宣称自动导入完成。

有关准确进度，读取 [镜像状态](../mirror/STATUS.md)。最近独立核验为 2,007/7,222，仍需通过拥有 GitHub 网络访问的本地 Git 完整导入约 566.5 MB。
