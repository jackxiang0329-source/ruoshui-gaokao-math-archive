# 维护和自动化脚本

主分支为精简发布文件；上游完整版本在 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，不应向主分支回填原始 `mirror/`。

- `python3 scripts/check_published_names.py`：检查 775 份 PDF 的年代/年份/命名、143 对专题 TeX/PDF、映射 SHA、合订证明与图片依赖。
- `python3 scripts/validate_question_index.py`：只校验统一的 `index/derivative-problems-2010-2026.json/.csv`，分年份查询从总表动态筛选，无需维护 7 份旧分期数据。
- `python3 scripts/validate_review_traceability.py`：审核证明与题号的溯源一致性。
- `python3 scripts/build_catalog_fast.py`：从 `full-source-archive` 生成 `catalog/` 搜索索引，已发布资源指向 `papers/` 与 `topics/`。
- `python3 scripts/verify_source_snapshot.py`：严格核对固定来源的原始 Git Tree SHA。

GitHub Actions 每 30 分钟检查固定快照与索引，实际编译与数学内容核验是不同流程。旧全量导入/子模块脚本仅供历史恢复，当前 `main` 不再提供会重新写入旧索引和上游目录的手动同步工作流。不要在精简版主分支运行这些旧脚本；如需恢复原有工程，请从 `full-source-archive` 或 [整理前快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/snapshot-before-lean-metadata-20261027) 建立独立工作分支。

## 主分支瘦身约定

早期导入/候选的 `index/files.csv`、`index/gaokao-candidates.csv`、`index/derivative-candidates.csv`、`index/INDEX.md` 和 `index/stats.json` 已在 [整理前快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/snapshot-before-lean-metadata-20261027/index) 保留。旧版手工子模块同步可以临时生成这些清单用于本地核验，但不会自动提交回 `main`。当前检索请用 `catalog/documents.csv` 和统一题目级 JSON/CSV。

## 已归档的一次性工具

2026-10-27 起不再在精简主分支保留旧年份候选索引生成器、已完成的 Markdown/证明合并脚本和 2016 年特定 PDF 补录脚本。历史源码仍可从 Git 历史与 [整理前快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/snapshot-before-lean-metadata-20261027/scripts) 找回。现行年份目录由 `build_catalog_fast.py` 直接读取主分支 `papers/` Git 树生成，完整来源记录仍在 `catalog/documents.csv`。
