# Repository Layout

本文件提出第一阶段的仓库结构。当前阶段只创建说明性文件和占位目录，不实现完整 CLI、数据库、索引或知识点体系。

## Layout

```text
.
├── AGENTS.md
├── pyproject.toml
├── .python-version
├── corpus/
│   └── papers/
│       └── {year}/
│           └── {volume}/
│               ├── paper.yml
│               ├── items/
│               │   ├── 01.md
│               └── assets/
│                   ├── 01-fig-01.png
│                   └── 01-table-01.png
├── config/
│   ├── scope.yml
│   ├── status.yml
│   ├── agents/
│   ├── paper_schemes/
│   └── taxonomy/
├── schemas/
├── docs/
├── src/
├── tests/
├── tools/
├── work/
├── build/
└── dist/
```

## Directories

### `corpus/`

题目语料目录，提交 Git。

采用“每题一个文件 + 每张试卷独立目录”的结构。题目全文、原图裁剪、表格裁剪和审阅状态以这里的数据为准。

### `config/`

项目配置目录，提交 Git。

用于保存收录范围、状态枚举、agent 任务配置、`paper_scheme` 和未来粗粒度知识点体系等配置。

### `schemas/`

数据格式目录，提交 Git。

用于保存后续 YAML、JSON 或 Markdown front matter 的 schema。schema 应服务于确定性校验。

### `docs/`

说明文档目录，提交 Git。

用于记录项目范围、数据层级、格式草案、转录规则、审阅流程、试卷方案与分值规则、仓库结构。

### `src/`

未来确定性 CLI 的源码目录，提交 Git。

CLI 用于校验、构建 SQLite、生成索引、统计和发布产物。正式 CLI 不调用 LLM，不依赖在线模型服务。

如需使用 Python，项目统一通过 `uv` 管理 Python 版本、虚拟环境和依赖。Python 版本记录在 `.python-version`，依赖声明在 `pyproject.toml`；维护者应使用 `uv run`、`uv add`、`uv sync` 等命令，不直接使用全局 `pip`。

### `tests/`

测试目录，提交 Git。

用于测试 schema、校验器、构建流程和未来 CLI。

### `tools/`

维护者辅助脚本目录，提交 Git。

agent transcription、review、annotation 和少量人工维护工具放在这里。允许维护者脚本批量调度 `codex exec`，但每次调用应保持独立会话，并遵守对应 agent 配置。

### `work/`

本地工作目录，不提交 Git。

用于保存原始 PDF、社区排版文件、页面截图、OCR 临时结果和处理中间文件。仓库配置中不得保存指向这些文件的本地绝对路径。

### `build/`

构建产物目录，不提交 Git。

用于保存 SQLite、全文索引、统计文件、校验报告和静态网页中间产物。

### `dist/`

发布产物目录，不提交 Git。

用于保存压缩包、发布快照、静态网站发布版本和面向下游使用者的导出文件。

## Git Ignore

`.gitignore` 保留 `work/`、`build/`、`dist/` 目录本身的占位文件，但忽略这些目录中的其他内容。
