# 仓库维护工具

精简主分支只保留发布产物、索引和维护脚本；11 个来源的固定原件保留在 full-source-archive 分支。

- `python3 scripts/check_published_names.py`：核对 775 份真题 PDF、142 组同名 TeX/PDF 及 Git Blob SHA。
- `python3 scripts/verify_source_snapshot.py`：从 full-source-archive 校验 11 个上游版本和 7,222 个原始文件。
- `python3 scripts/build_catalog_fast.py`：从完整快照生成可用的试卷与专题链接。
- `python3 -m unittest discover -s tests -v`：执行回归测试。

需编译上游原始多文件工程时，访问 [固定源代码快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，连同图片与各模块一起检出；不要把片段 `.tex` 误认作独立主文件。

历史导入与子模块管理命令仍可在 [旧版说明](README_FULL_IMPORT.md) 查阅，但旧日志中的 main/mirror 状态已过时。
