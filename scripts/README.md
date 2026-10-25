# 同步和索引工具

运行 `bash scripts/sync_sources.sh` 更新 11 个 Git 子模块、生成文件级索引并执行一致性验证。此命令需要 Git 和 Python 3；GitHub Actions 可调用。

索引脚本只筛选文件名，不能证明文件内容是导数题，也不会做逐题数学核验。

固定版本核验：`python3 scripts/validate_pinned_sources.py --index-only`（仅 Git 索引，无须下载子模块）；克隆子模块后运行 `python3 scripts/validate_pinned_sources.py` 严格对比 HEAD。同步不再使用 `--remote`，更换上游版本须显式修改锁定 SHA 与 gitlink 后复核。

轻量离线质检：`.github/workflows/audit-archive.yml` 会运行单元测试、题目级索引及审核溯源校验。数学正确性与 XeLaTeX 编译另行验收。


重新核算固定版本镜像数量：`python3 scripts/audit_mirror_inventory.py --output mirror/MIRROR_STATUS.json`。需要先递归检出所有 11 个上游子模块。该脚本按 **HEAD Git SHA + mode** 统计，不把子模块 gitlink 或索引路径算作完整文件。运行后先审阅本地 JSON，再自行提交。独立单元测试在 `tests/test_audit_mirror_inventory.py`。

## 已入库镜像批次的离线验收（无须初始化上游子模块）

从完整 Git 历史的仓库检出运行：

```bash
python3 scripts/validate_import_batches.py
python3 -m unittest discover -s tests -v
```

此检查读取 `mirror/IMPORT_BATCH_*.json`，对每条记录分别比对基线提交、导入完成时提交和当前 HEAD 的 **Git Blob SHA、文件模式与原始对象大小**；并独立重算文件数、分组字节数及 `mirror/MIRROR_STATUS.json` 的汇总算术。若历史文件被修改、缺失，或导入数被虚报，命令以非零状态退出。CI 使用 `fetch-depth: 0` 保留所需历史提交，并对 `mirror/**` 改动触发验收。

**范围限制：**它只校验既有导入清单的 Git 对象及统计一致性，不能独立证明剩余上游文件总数、数学答案正确、图片可读、PDF 编译成功或再分发合法；这些仍需专门审核。
