# Data Format Draft

本文件是题目文件格式草案，当前主体只覆盖数据清洗阶段需要的客观字段。知识点、难度、解题方法等描述性字段不得进入题面主体。

## 基本原则

- Markdown、YAML 和图片文件是权威数据源。
- 题目正文使用中文，字段名、目录名和程序标识符使用英文。
- 题目正文、选项和说明文字统一使用西文风格标点符号；数学公式按 LaTeX 习惯处理。
- Markdown 正文中的 LaTeX 命令使用单反斜杠；YAML 中含 LaTeX 的选项优先使用单引号字符串，避免把 LaTeX 写成双反斜杠。
- 题面字段只保存可从试卷直接确认的内容。
- 分值不在题目文件中手工填写，由 `paper_scheme` 和题号推导。
- 无法确认的内容使用 `needs_confirmation` 和 `uncertain_notes` 标记。
- 描述性标注必须写在独立的 `annotation` 区域。

## 文件组织

采用“每题一个文件 + 每张试卷独立目录”的组织方式，避免不同试卷的题目混在一起。

建议路径：

```text
corpus/papers/{year}/{volume}/paper.yml
corpus/papers/{year}/{volume}/items/01.md
corpus/papers/{year}/{volume}/assets/01-fig-01.png
corpus/papers/{year}/{volume}/assets/01-table-01.png
```

示例：

```text
corpus/papers/2024/I/paper.yml
corpus/papers/2024/I/items/01.md
corpus/papers/2024/I/assets/01-fig-01.png
```

卷种使用官方写法 `I` 和 `II`。题目稳定 ID 使用 `年份-卷种-两位题号`，例如 `2024-I-01`。

## 试卷元数据

每张试卷使用一个 `paper.yml` 记录试卷级元数据：

```yaml
paper:
  id: "2024-I"
  year: 2024
  series: national_new_gaokao
  volume: I
  title: "2024年普通高等学校招生全国统一考试 数学 (I卷)"
  paper_scheme_id: "new_gaokao_current"
  status: draft
  needs_confirmation: false
  uncertain_notes: []
items:
  - id: "2024-I-01"
    number: 1
    path: "items/01.md"
```

字段说明：

- `id`：稳定试卷标识。
- `year`：试卷年份。
- `series`：试卷系列标识，当前为 `national_new_gaokao`。
- `volume`：卷种，使用 `I` 或 `II`。
- `title`：中文显示标题, 由年份和卷种按 `{year}年普通高等学校招生全国统一考试 数学 ({volume}卷)` 生成, 不从 OCR 或社区排版标题读取。
- `paper_scheme_id`：试卷结构与计分方案标识。
- `status`：试卷级题面流程状态, 同时表示转录和审核的当前状态。
- `needs_confirmation`：是否仍有待确认事项。
- `uncertain_notes`：待确认事项列表。

## Paper Scheme

当前确认两个新高考试卷方案：

```yaml
paper_schemes:
  - id: "new_gaokao_legacy"
    series: national_new_gaokao
    years: [2021, 2022, 2023]
    total_items: 22
    rules:
      - type: mcq_single_answer
        numbers: [1, 2, 3, 4, 5, 6, 7, 8]
        points: 5
      - type: mcq_multiple_answers
        numbers: [9, 10, 11, 12]
        points: 5
      - type: fill_blank
        numbers: [13, 14, 15, 16]
        points: 5
      - type: solution
        numbers: [17]
        points: 10
      - type: solution
        numbers: [18, 19, 20, 21, 22]
        points: 12
  - id: "new_gaokao_current"
    series: national_new_gaokao
    years: [2024, 2025, 2026]
    total_items: 19
    rules:
      - type: mcq_single_answer
        numbers: [1, 2, 3, 4, 5, 6, 7, 8]
        points: 5
      - type: mcq_multiple_answers
        numbers: [9, 10, 11]
        points: 6
      - type: fill_blank
        numbers: [12, 13, 14]
        points: 5
      - type: solution
        numbers: [15]
        points: 13
      - type: solution
        numbers: [16, 17]
        points: 15
      - type: solution
        numbers: [18, 19]
        points: 17
```

题目文件不手工填写 `points`。校验器和构建器以后根据 `paper_scheme_id` 与题号推导题型和分值。

## 题目文件

每题一个 Markdown 文件，使用 YAML front matter 保存结构化字段，正文保存题面文本。

```yaml
---
id: "2024-I-01"
paper_id: "2024-I"
number: 1
type: mcq_single_answer
status: draft
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---
```

## 选择题与多选题

选择题和多选题都保存题干与选项，不保存答案。

```yaml
type: mcq_single_answer
options:
  A: '选项 A 原文'
  B: '选项 B 原文'
  C: '选项 C 原文'
  D: '选项 D 原文'
```

多选题仅把 `type` 改为 `mcq_multiple_answers`。

不得根据题意或记忆补写正确选项。

## 填空题

填空题保存题干原文。空格使用 `[填空]` 表达，但注意：西文方括号不得与附近的符号冲突而导致markdown解析问题，必要时可在两边加空格。

```yaml
type: fill_blank
```

正文示例：

```markdown
题干原文, [填空].
```

## 解答题与小题

解答题保存总题干和各小题内容，不保存解答过程。

```yaml
type: solution
subquestions:
  - label: "(1)"
  - label: "(2)"
```

正文中按原卷编号保留小题：

```markdown
题干原文.

(1) 第 (1) 小题题目内容.

(2) 第 (2) 小题题目内容.
```

## 图片与表格

图片和表格暂时都使用原图裁剪。裁剪后的图片保存在该试卷目录的 `assets/` 下，并由题目文件引用。

裁剪时先定位图形或表格主体外接范围，再加入适中边距；不需要追求大白边或绝对居中。如果图形或表格贴近相邻文字，在保证图形或表格完整截取的同时尽量避免带入无关题干、选项或页眉页脚。

```yaml
assets:
  - id: "fig-01"
    type: figure
    path: "../assets/01-fig-01.png"
    needs_confirmation: false
    notes: []
  - id: "table-01"
    type: table
    path: "../assets/01-table-01.png"
    needs_confirmation: false
    notes: []
```

正文引用：

```markdown
![图 1](../assets/01-fig-01.png)

![表 1](../assets/01-table-01.png)
```

## 状态枚举

`status` 表示题面流程的唯一当前状态：

- `draft`：文件已创建, 尚未完成转录。
- `needs_review`：转录结果需要审核或存在待确认事项。
- `approved`：题面已经完成审核。

审核可以由人工或 Agent 执行, 不在数据中区分审核执行者。

`annotation.status`：

- `not_started`
- `draft`
- `needs_review`
- `approved`

待确认事项统一写入 `uncertain_notes`。必要时在文字中说明疑点类型，例如“文字”“公式”“图形”“表格”“跨页”。

## Annotation Area

题面审核完成后，才允许填写 `annotation` 区域。当前只做最粗略描述：

```yaml
annotation:
  status: draft
  problem_kind: "函数"
  primary_knowledge_point: "函数的性质"
  notes: []
```

当前不设计题目形式特征、能力维度、难度、解题方法、相似题关系或次要知识点。
