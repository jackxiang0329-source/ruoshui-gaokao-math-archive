# 同步和索引工具

运行 `bash scripts/sync_sources.sh` 更新 11 个 Git 子模块、生成文件级索引并执行一致性验证。此命令需要 Git 和 Python 3；GitHub Actions 可调用。

索引脚本只筛选文件名，不能证明文件内容是导数题，也不会做逐题数学核验。
