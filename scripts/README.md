# 维护和自动化脚本

主分支为精简发布文件；上游完整版本在 [full-source-archive](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive)，不应向主分支回填原始 `mirror/`。

- `python3 scripts/check_published_names.py`：检查 775 份 PDF 的年代/年份/命名、143 对专题 TeX/PDF、映射 SHA、合订证明与图片依赖。
- `python3 scripts/validate_question_index.py`：只校验统一的 `index/derivative-problems-2010-2026.json/.csv`，分年份查询从总表动态筛选，无需维护 7 份旧分期数据。
- `python3 scripts/validate_review_traceability.py`：审核证明与题号的溯源一致性。
- `python3 scripts/build_catalog_fast.py`：从 `full-source-archive` 生成 `catalog/` 搜索索引，已发布资源指向 `papers/` 与 `topics/`。
- `python3 scripts/verify_source_snapshot.py`：严格核对固定来源的原始 Git Tree SHA。

GitHub Actions 每 30 分钟检查固定快照与索引，实际编译与数学内容核验是不同流程。历史全量导入/子模块脚本仍保留以便需要时使用，但不能把它们产生的历史状态当作当前主分支状态。

## 主分支瘦身约定

早期导入/候选的 `index/files.csv`、`index/gaokao-candidates.csv`、`index/derivative-candidates.csv`、`index/INDEX.md` 和 `index/stats.json` 已在 [整理前快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/snapshot-before-lean-metadata-20261027/index) 保留。旧版手工子模块同步可以临时生成这些清单用于本地核验，但不会自动提交回 `main`。当前检索请用 `catalog/documents.csv` 和统一题目级 JSON/CSV。
