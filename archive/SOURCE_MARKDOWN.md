# 上游 Markdown 原始正文合订本（215 个源文件）

这里只合并阅读入口，不更改题干。所有原件仍可在 [完整固定版本快照](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/tree/full-source-archive) 按原路径查看、下载和构建。

每节标注原始文件 Git Blob SHA；原文被封装为 Markdown 代码区块，避免 YAML front matter、相对图片和其它标记跨文件冲突。

原资料的许可状态和第三方作品权利不因合订而改变。

---

## 001 · mirror/2024-china-gaokao-math/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/2024-china-gaokao-math/README.md) · SHA c1f4cdff5c4c8ec9056cf86fa7831d7ca59ee6eb · mode 100644

``````markdown
# 2024-China-Gaokao-Math

## 1. 说明 Description

本仓库包含了 2024 年普通高等学校招生全国统一考试（以下简称 “高考”）的数学科目考试试卷。

*注意：本仓库中上传的是 新高考I卷*，该试卷覆盖了：广东、福建、湖南、湖北、浙江、江苏、山东、河北。

The repository includes the math paper of Chinese National College Entrance Exam (Gaokao). (hereinafter referred to as the "Gaokao"). The paper covers Guangdong, Fujian, Hunan, Hubei, Zhejiang, Jiangsu, Shandong, and Hebei. 

## 2. 包含 Include

main.tex -- 试卷的 $\LaTeX$ 源代码

main.pdf -- 试卷的 PDF 结果
``````

---

## 002 · mirror/daxmate-math/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/daxmate-math/README.md) · SHA 7329a0917fd7048106fada2a0b09328189988d60 · mode 100644

``````markdown
# Why
我在2024年突然间一个想法,想做点数学题来锻炼锻炼已经年久失修的脑子,正好也学习学习LaTeX的一些实际的写法,就在网上找数学题,中文网上很多垃圾,所以刚开始我是在国外的网站上找了一点题来练习.后来在B站上偶然发现了[这个视频](https://www.bilibili.com/video/BV1Sk4y1Z7jG/?spm_id_from=333.1387.favlist.content.click&vd_source=e45034e5fdc28a425d6b68ec04611379),里面有大量的习题可以用来练习.强烈推荐[这个网盘](https://docs.qq.com/sheet/DTkRSbGFZRWhnb1Z2?tab=sod4da)里面的内容.

# What
这个仓库会放我解题的经过，试卷会分别编译成不带答案和带答案的。相比起网上很多的Word版的数学试卷而言，内容会看起来更美观，图片都是用LaTeX绘制的。但是也可能会存在一些错误。

# Table of Contents
- 封面
![coverpage](./gaokao/imgs/coverpage.png)
这个是我用tikz随意画的，😄
- 试卷内容
  - 1977 年高考数学试卷及答案 (北京卷) 理科
  - 1977 年高考数学试卷及答案 (福建卷) 理科
  - 1977 年高考数学试卷及答案 (河北卷) 理科
  - 1977 年高考数学试卷及答案 (黑龙江) 理科
  - 1977 年高考数学试卷及答案 (江苏卷) 理科
  - 1977 年高考数学试卷及答案 (上海卷) 理科
  - 1977 年高考数学试卷及答案 (天津卷) 理科
  - 1978 年高考数学试卷及答案 (天津卷) 文理
  - 1997 年高考数学试卷及答案 (全国卷) 理科
  - 1998 年高考数学试卷及答案 (全国卷) 理科

# Copyleft

请随意分享

``````

---

## 003 · mirror/first-round-review/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/first-round-review/README.md) · SHA 239c2f4934d96cd7fd1d68f87aa7d98b6348e8c1 · mode 100644

``````markdown
# 北京高考高三数学一轮复习讲义

本项目是一份使用 LaTeX 编写的高三数学一轮复习讲义，主要面向北京高考数学复习。内容按专题分章编写，将基础知识、主要题型和历年试题进行整理，便于课堂讲解、学生练习和后续补充。

> 本项目仍在持续整理中，部分章节可能尚未完成。

## 主要内容

目前已经建立或正在整理的专题包括：

- 解析几何解答题；
- 导数；
- 三角函数与解三角形；
- 立体几何；
- 概率统计。

试题汇总文件中收录了部分北京各区期中、期末、一模、二模及高考题目，题目出处使用类似“2026海淀一模”的格式标注。

## 项目结构

```text
.
├── elegantbook-cn.tex       # 整本讲义的主文件
├── elegantbook.cls          # 根据讲义需求调整过的文档类
├── chapters/                # 各专题的 TeX 源文件
├── figure/ 和 image/       # 封面、标志和正文图片
├── tmp/                     # 单文件编译结果（Git 忽略）
└── Makefile                 # 整体及单文件编译命令
```

## 编译方法

建议使用 TeX Live 2026 和 XeLaTeX。

### 编译整个工程

```bash
make build
```

也可以直接运行：

```bash
xelatex -interaction=nonstopmode -halt-on-error elegantbook-cn.tex
```

修改了目录或交叉引用后，通常需要连续编译两次。

### 单独编译某个章节文件

```bash
make build chapters/导数/期中题目汇总.tex
```

上述命令的中间文件和 PDF 会保存到：

```text
tmp/导数/期中题目汇总/
```

也可以只传入文件名，但要求 `chapters` 中不存在同名文件：

```bash
make build 入题思路.tex
```

### 清理编译中间文件

```bash
make clean
```

## 致谢

本项目的排版模板来源于 [ElegantBook](https://github.com/ElegantLaTeX/ElegantBook)，并在其基础上根据高中数学讲义的实际需求进行了修改。

感谢 ElegantLaTeX 团队为社区提供 ElegantBook 这一美观、易用且具有良好可定制性的 LaTeX 书籍模板；感谢模板创建者 [Ethan Deng](https://github.com/EthanDeng) 和 [Liam Huang](https://github.com/Liam0205)，以及 [syvshc](https://github.com/syvshc)、[sikouhjw](https://github.com/sikouhjw)、[Osbert Wang](https://github.com/OsbertWang) 等维护者和所有贡献者的持续付出。没有他们的工作，本讲义的排版和维护将需要付出更多精力。

- ElegantBook GitHub：<https://github.com/ElegantLaTeX/ElegantBook>
- ElegantBook CTAN：<https://ctan.org/pkg/elegantbook>

本项目是基于 ElegantBook 的个人讲义项目，不是 ElegantLaTeX 团队的官方项目。

本讲义中的部分题目主要整理自 [组卷网](https://zujuan.xkw.com/) 和 [菁师帮](https://www.jingshibang.com/home/)。感谢两家平台长期以来为广大师生提供丰富的试题资源和教学参考，为本讲义的收集与整理提供了重要帮助，在此表示诚挚感谢！

## 许可协议

ElegantBook 模板依照 [LaTeX Project Public License 1.3c](https://www.latex-project.org/lppl/lppl-1-3c/) 或更高版本发布，本项目中由 ElegantBook 衍生的模板文件继续遵循该协议。详细内容见 [License](./License)。

讲义中引用的试题、图片及其他第三方内容，其权利归原作者或原出版方所有。

``````

---

## 004 · mirror/gaokao-exam-template/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-exam-template/README.md) · SHA 6aa8ebc3fe6022506f0a42c654f56771dee0d68a · mode 100644

``````markdown
# gaokao_exam
高考试卷LaTeX模板

#### 介绍
高考试卷LaTeX模板

#### GEEexam使用说明

1. GEEexam.sty(有分栏线) 示例 17quanguo3.tex
2. NEMT.sty(无分栏线) 示例 2017quanguo3.tex

``````

---

## 005 · mirror/gaokao-math-corpus/AGENTS.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/AGENTS.md) · SHA b6c0c750b4231a2d65a4dbc5b6e25cfec778703c · mode 100644

``````markdown
# Codex Rules

本仓库用于建设公开的“新高考数学试题知识库”。所有 Codex 任务必须遵守以下核心规则。

## Core Rules

- 不添加标准答案、题解、解题过程、推荐解法或任何变相解析。
- 数据清洗阶段只记录可从试卷直接确认的客观内容，以及按明确规则推导的基础元数据；不得添加知识点、板块、难度、解题方法、思维类型、教学用途、相似题关系等描述性内容。
- 忠实转录题面，只做必要的 Markdown 和 LaTeX 格式化，不自行改写题意。
- 题目正文、选项和说明文字统一使用西文风格标点符号；数学公式按 LaTeX 习惯处理。
- 无法确认的文字、公式、图形、表格或跨页关系必须明确标记，不得猜测或根据常识补全。
- 不识别、不转录、不手工填写试卷页面或社区版本中出现的题目分值；分值以后由 `paper_scheme` 和题号统一推导。
- 原始 PDF、社区排版文件、页面图片和处理中间文件不提交到仓库。
- 正式 CLI 和构建流程应保持确定性，不调用 LLM，不依赖在线模型服务。
- 建设阶段使用 Codex agent 时，应按任务选择刚好足够的模型和推理强度；页面转录/OCR 默认使用较小模型和较低推理强度，复杂审阅再按需升档。
- 自动化脚本可以读取环境变量或系统代理以减少超时重试，但不得把本地代理地址写入仓库配置。
- 如需使用 Python，必须通过 `uv` 管理 Python 版本、虚拟环境和依赖；不要直接使用全局 `pip` 或未声明依赖的临时环境。
- 修改后应执行与本次改动相称的检查，例如文档一致性检查、链接检查、格式检查或测试。
- 最终回复只报告修改文件、检查结果和待确认事项，不重复输出完整题目或大段文档正文。

## Detailed Documents

- 项目范围：`docs/PROJECT_SCOPE.md`
- 数据层级：`docs/DATA_LAYERS.md`
- 数据格式草案：`docs/DATA_FORMAT.md`
- 转录规则：`docs/TRANSCRIPTION_RULES.md`
- 审阅流程：`docs/REVIEW_WORKFLOW.md`
- 试卷方案与分值规则：`docs/SCORING_RULES.md`
- 仓库结构：`docs/REPOSITORY_LAYOUT.md`

``````

---

## 006 · mirror/gaokao-math-corpus/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/README.md) · SHA 397ec2fb7063ccbb0120525da522a4713d1e93d5 · mode 100644

``````markdown
# 新高考数学试题知识库

这是一个“新高考数学试题知识库”项目。项目的第一阶段收录 2021--2026 年新高考全国 I 卷和新高考全国 II 卷，保存经过整理和审核的题面语料，以及支撑转录、校验和发布的项目文档与工具。

本项目的目标是建立一份适合人类阅读、程序查询和未来 Agent 查询的结构化题面数据。仓库中的 Markdown、YAML 和图片文件是核心数据源，数据库、索引、统计文件、静态网页和发布压缩包均属于可以重新生成的衍生产物。

项目不保存标准答案、题解、解题过程、推荐解法或其他变相解析。数据清洗阶段只记录可以从试卷直接确认的题面内容，以及由明确规则推导的基础元数据。知识点等描述性标注在题面审核完成后单独进行。

## 项目归属与 AI 贡献

这个项目由我发起。我负责确定项目目标和收录范围, 做出关键设计决策, 审核并接受代码和数据变更, 维护仓库, 以及对公开内容承担最终责任。

但这不是一个主要由个人手工编写的项目。它也是一次使用大批量 vibe coding 敏捷构建数据集的尝试。项目中的文档 (包括你现在正在阅读的 `README.md` ) 、目录设计、数据格式、配置和脚本绝大多数由 OpenAI Codex 生成或在 Codex 的协作下形成。Codex 不只是一个偶尔使用的辅助工具, 而是本项目建设过程中的核心生产力和重要贡献来源。

因此, 本项目同时承认两件事:

- 人类维护者拥有项目方向、范围、接受标准和最终发布责任。
- Codex 参与了绝大多数工程设计、文档编写、脚本实现, 以及后续题面转录和数据整理工作。

AI 生成并不等于自动获得事实正确性。由 Codex 生成的文档、代码和题面都必须经过与其风险相称的检查。题面 review 和描述性标注 review 可以由人工或 Agent 执行, 两者具有同等效力。只有经过审核并达到项目规则要求的内容, 才能被视为已审核的语料。

## 当前范围

当前阶段包括:

- 2021-2026 年新高考全国 I 卷和新高考全国 II 卷。
- 题干、选项、填空内容、解答题小题、必要的图形和表格。
- 试卷年份、卷种、题号、题型、转录状态、审核状态和待确认事项等基础字段。

当前阶段不包括:

- 标准答案、题解、解题过程和推荐解法。
- 未经独立审核的知识点、难度、能力维度或教学用途判断。
- 原始 PDF、社区排版文件、页面图片和处理中间文件的 Git 提交。
- 依赖在线模型的正式 CLI、数据库或检索服务。

## 工作方式

题面转录可以使用 Codex 处理整份试卷的页面图片, 并将结果直接写入目标文件。遇到无法确认的文字、公式、图形、表格或跨页关系时, 必须保留明确的待确认标记, 不能猜测或根据常识补全。

当前 review 的基本流程是:

1. 使用 Codex 转录并生成题面文件。
2. 执行确定性的格式和结构检查。
3. 使用单文件 HTML 查看全部题目。
4. 人工逐题或按风险抽查, 对照原始页面修正错误。
5. 确认题面审核完成后, 再考虑粗粒度知识标注。

详细规则见 [`AGENTS.md`](AGENTS.md) 和 [`docs/`](docs/)。

## 目录概览

- `corpus/`: 题目语料。
- `config/`: 项目范围、试卷方案和 Agent 任务配置。
- `schemas/`: 数据格式约束。
- `docs/`: 项目规则和工作流程。
- `tools/`: 转录、review 和维护工具。
- `work/`: 本地页面图片和处理中间文件, 不提交 Git。
- `build/`: 可重新生成的构建产物, 不提交 Git。
- `dist/`: 可重新生成的发布包, 不提交 Git。

如果需要使用 Python, 请通过 `uv` 管理版本和依赖, 使用 `uv run` 执行项目命令。

## 贡献与责任

欢迎对题面错误、格式问题、脚本缺陷和文档规则提出修正建议。提交变更时请说明是否由 Codex 或其他 AI 生成, 并按照项目规则进行人工核对。任何自动生成内容都不能绕过题面审核直接进入已确认状态。

项目的具体边界和接受标准以仓库中的规则文件为准, 而不是以某一次模型输出或某个来源文件的排版为准。

``````

---

## 007 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/01.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/01.md) · SHA 8a7cd10b51df2b0e5d6dd48b4d5316d7d9a17fee · mode 100644

``````markdown
---
id: 2021-I-01
paper_id: 2021-I
number: 1
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\{2\}$
  B: $\{2,3\}$
  C: $\{3,4\}$
  D: $\{2,3,4\}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设集合 $A=\{x \mid -2<x<4\}$, $B=\{2,3,4,5\}$, 则 $A \cap B=$

``````

---

## 008 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/02.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/02.md) · SHA b2079879f1b36e82c645fbb79e5177e1420f1608 · mode 100644

``````markdown
---
id: 2021-I-02
paper_id: 2021-I
number: 2
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $6-2\mathrm{i}$
  B: $4-2\mathrm{i}$
  C: $6+2\mathrm{i}$
  D: $4+2\mathrm{i}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $z=2-\mathrm{i}$, 则 $z(\overline{z}+\mathrm{i})=$

``````

---

## 009 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/03.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/03.md) · SHA 49f44e6f1fba4d3e345ed2008dada04523b79fe8 · mode 100644

``````markdown
---
id: 2021-I-03
paper_id: 2021-I
number: 3
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $2$
  B: $2\sqrt{2}$
  C: $4$
  D: $4\sqrt{2}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知圆锥的底面半径为 $\sqrt{2}$, 其侧面展开图为一个半圆, 则该圆锥的母线长为

``````

---

## 010 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/04.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/04.md) · SHA d133d4e3d0fbcddf336fb08a09b951941e75e207 · mode 100644

``````markdown
---
id: 2021-I-04
paper_id: 2021-I
number: 4
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $(0,\dfrac{\pi}{2})$
  B: $(\dfrac{\pi}{2},\pi)$
  C: $(\pi,\dfrac{3\pi}{2})$
  D: $(\dfrac{3\pi}{2},2\pi)$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

下列区间中, 函数 $f(x)=7\sin(x-\dfrac{\pi}{6})$ 单调递增的区间是

``````

---

## 011 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/05.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/05.md) · SHA 72518c5cf9ed085184bf958817c4f335aef156af · mode 100644

``````markdown
---
id: 2021-I-05
paper_id: 2021-I
number: 5
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $13$
  B: $12$
  C: $9$
  D: $6$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $F_1$, $F_2$ 是椭圆 $C:\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$ 的两个焦点, 点 $M$ 在 $C$ 上, 则 $|MF_1|\cdot |MF_2|$ 的最大值为

``````

---

## 012 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/06.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/06.md) · SHA ce1e2b9c16b7873688df33500014a76be7decb16 · mode 100644

``````markdown
---
id: 2021-I-06
paper_id: 2021-I
number: 6
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-\dfrac{6}{5}$
  B: $-\dfrac{2}{5}$
  C: $\dfrac{2}{5}$
  D: $\dfrac{6}{5}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若 $\tan\theta=-2$, 则 $\dfrac{\sin\theta(1+\sin2\theta)}{\sin\theta+\cos\theta}=$

``````

---

## 013 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/07.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/07.md) · SHA cf20b4692f2c2639b7f093a0cd40b1b868e0baf4 · mode 100644

``````markdown
---
id: 2021-I-07
paper_id: 2021-I
number: 7
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $e^b<a$
  B: $e^a<b$
  C: $0<a<e^b$
  D: $0<b<e^a$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若过点 $(a,b)$ 可以作曲线 $y=e^x$ 的两条切线, 则

``````

---

## 014 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/08.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/08.md) · SHA b2630b6e3a41184b6f6cee1b52b7e0673297f472 · mode 100644

``````markdown
---
id: 2021-I-08
paper_id: 2021-I
number: 8
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 甲与丙相互独立
  B: 甲与丁相互独立
  C: 乙与丙相互独立
  D: 丙与丁相互独立
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

有 $6$ 个相同的球, 分别标有数字 $1$, $2$, $3$, $4$, $5$, $6$, 从中有放回的随机取两次, 每次取 $1$ 个球. 甲表示事件"第一次取出的球的数字是 $1$", 乙表示事件"第二次取出的球的数字是 $2$", 丙表示事件"两次取出的球的数字之和是 $8$", 丁表示事件"两次取出的球的数字之和是 $7$", 则

``````

---

## 015 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/09.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/09.md) · SHA 2da16cf93db3279bd46d51258ce20e9bb57de520 · mode 100644

``````markdown
---
id: 2021-I-09
paper_id: 2021-I
number: 9
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 两组样本数据的样本平均数相同
  B: 两组样本数据的样本中位数相同
  C: 两组样本数据的样本标准差相同
  D: 两组样本数据的样本极差相同
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

有一组样本数据 $x_1,x_2,\cdots,x_n$, 由这组数据得到新样本数据 $y_1,y_2,\cdots,y_n$, 其中 $y_i=x_i+c(i=1,2,\cdots,n)$, $c$ 为非零常数, 则

``````

---

## 016 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/10.md) · SHA 6f7fd228a04a981ed90be2540faeac4b3136f6f6 · mode 100644

``````markdown
---
id: 2021-I-10
paper_id: 2021-I
number: 10
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $|\overrightarrow{OP_1}|=|\overrightarrow{OP_2}|$
  B: $|\overrightarrow{AP_1}|=|\overrightarrow{AP_2}|$
  C: $\overrightarrow{OA}\cdot\overrightarrow{OP_3}=\overrightarrow{OP_1}\cdot\overrightarrow{OP_2}$
  D: $\overrightarrow{OA}\cdot\overrightarrow{OP_1}=\overrightarrow{OP_2}\cdot\overrightarrow{OP_3}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $O$ 为坐标原点, 点 $P_1(\cos\alpha,\sin\alpha)$, $P_2(\cos\beta,-\sin\beta)$, $P_3(\cos(\alpha+\beta),\sin(\alpha+\beta))$, $A(1,0)$, 则

``````

---

## 017 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/11.md) · SHA 92010819c3b0541e864ebce63723f7abed445b59 · mode 100644

``````markdown
---
id: 2021-I-11
paper_id: 2021-I
number: 11
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 点 $P$ 到直线 $AB$ 的距离小于 $10$
  B: 点 $P$ 到直线 $AB$ 的距离大于 $2$
  C: 当 $\angle PBA$ 最小时, $|PB|=3\sqrt{2}$
  D: 当 $\angle PBA$ 最大时, $|PB|=3\sqrt{2}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知点 $P$ 在圆 $(x-5)^2+(y-5)^2=16$ 上, 点 $A(4,0)$, $B(0,2)$, 则

``````

---

## 018 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/12.md) · SHA 8a70d019654f435b96c2e11c4216cecc30182fd6 · mode 100644

``````markdown
---
id: 2021-I-12
paper_id: 2021-I
number: 12
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 当 $\lambda=1$ 时, $\triangle AB_1P$ 的周长为定值
  B: 当 $\mu=1$ 时, 三棱锥 $P-A_1BC$ 的体积为定值
  C: 当 $\lambda=\dfrac{1}{2}$ 时, 有且仅有一个点 $P$, 使得 $A_1P\perp BP$
  D: 当 $\mu=\dfrac{1}{2}$ 时, 有且仅有一个点 $P$, 使得 $A_1B\perp$ 平面 $AB_1P$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在正三棱柱 $ABC-A_1B_1C_1$ 中, $AB=AA_1=1$, 点 $P$ 满足 $\overrightarrow{BP}=\lambda\overrightarrow{BC}+\mu\overrightarrow{BB_1}$, 其中 $\lambda\in[0,1]$, $\mu\in[0,1]$, 则

``````

---

## 019 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/13.md) · SHA dbabfd56046cca336e84df6b3bd9f5b722101c5b · mode 100644

``````markdown
---
id: 2021-I-13
paper_id: 2021-I
number: 13
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=x^3(a\cdot 2^x-2^{-x})$ 是偶函数, 则 $a=$ [填空].

``````

---

## 020 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/14.md) · SHA fb91689ed3de24dc5c5736b27970509060cdcdf0 · mode 100644

``````markdown
---
id: 2021-I-14
paper_id: 2021-I
number: 14
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $O$ 为坐标原点, 抛物线 $C:y^2=2px(p>0)$ 的焦点为 $F$, $P$ 为 $C$ 上一点, $PF$ 与 $x$ 轴垂直, $Q$ 为 $x$ 轴上一点, 且 $PQ\perp OP$. 若 $|FQ|=6$, 则 $C$ 的准线方程为 [填空].

``````

---

## 021 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/15.md) · SHA 28c51d7a5511ff57f3542cdf90654ebbd3ed04e6 · mode 100644

``````markdown
---
id: 2021-I-15
paper_id: 2021-I
number: 15
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

函数 $f(x)=|2x-1|-2\ln x$ 的最小值为 [填空].

``````

---

## 022 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/16.md) · SHA 2fb6261fc3b2995d66f529b9e00d587f32143026 · mode 100644

``````markdown
---
id: 2021-I-16
paper_id: 2021-I
number: 16
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

某校学生在研究民间剪纸艺术时, 发现剪纸时经常会沿纸的某条对称轴把纸对折. 规格为 $20\mathrm{dm}\times12\mathrm{dm}$ 的长方形纸, 对折 $1$ 次共可以得到 $10\mathrm{dm}\times12\mathrm{dm}$, $20\mathrm{dm}\times6\mathrm{dm}$ 两种规格的图形, 它们的面积之和 $S_1=240\mathrm{dm}^2$, 对折 $2$ 次共可以得到 $5\mathrm{dm}\times12\mathrm{dm}$, $10\mathrm{dm}\times6\mathrm{dm}$, $20\mathrm{dm}\times3\mathrm{dm}$ 三种规格的图形, 它们的面积之和 $S_2=180\mathrm{dm}^2$, 以此类推. 则对折 $4$ 次共可以得到不同规格图形的种数为 [填空]; 如果对折 $n$ 次, 那么 $\sum_{k=1}^{n}S_k=$ [填空] $\mathrm{dm}^2$.

``````

---

## 023 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/17.md) · SHA bafe4d7dc7e52f1128581880f445a514b8d72640 · mode 100644

``````markdown
---
id: 2021-I-17
paper_id: 2021-I
number: 17
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知数列 $\{a_n\}$ 满足 $a_1=1$, 
$$
a_{n+1}=
\begin{cases}
a_n + 1, & \text{$n$为奇数},\\
a_n + 2, & \text{$n$为偶数}.
\end{cases}
$$

(1) 记 $b_n=a_{2n}$, 写出 $b_1$, $b_2$, 并求数列 $\{b_n\}$ 的通项公式;

(2) 求 $\{a_n\}$ 的前 $20$ 项和.

``````

---

## 024 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/18.md) · SHA 49011e4ffda8adb431354ec793ada62537b470d2 · mode 100644

``````markdown
---
id: 2021-I-18
paper_id: 2021-I
number: 18
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

某学校组织"一带一路"知识竞赛, 有 $A$, $B$ 两类问题. 每位参加比赛的同学先在两类问题中选择一类并从中随机抽取一个问题回答, 若回答错误则该同学比赛结束; 若回答正确则从另一类问题中再随机抽取一个问题回答, 无论回答正确与否, 该同学比赛结束. $A$ 类问题中的每个问题回答正确得 $20$ 分, 否则得 $0$ 分; $B$ 类问题中的每个问题回答正确得 $80$ 分, 否则得 $0$ 分.

已知小明能正确回答 $A$ 类问题的概率为 $0.8$, 能正确回答 $B$ 类问题的概率为 $0.6$, 且能正确回答问题的概率与回答次序无关.

(1) 若小明先回答 $A$ 类问题, 记 $X$ 为小明的累计得分, 求 $X$ 的分布列;

(2) 为使累计得分的期望最大, 小明应选择先回答哪类问题? 并说明理由.

``````

---

## 025 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/19.md) · SHA 4eafb1d61585cd02d6595900fa4f97ddaf3ad881 · mode 100644

``````markdown
---
id: 2021-I-19
paper_id: 2021-I
number: 19
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $\triangle ABC$ 的内角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$. 已知 $b^2=ac$, 点 $D$ 在边 $AC$ 上, $BD\sin\angle ABC=a\sin C$.

(1) 证明: $BD=b$;

(2) 若 $AD=2DC$, 求 $\cos\angle ABC$.

``````

---

## 026 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/20.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/20.md) · SHA b7313357cd82820ca8ae5df02df7d384d7991666 · mode 100644

``````markdown
---
id: 2021-I-20
paper_id: 2021-I
number: 20
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/20-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, 在三棱锥 $A-BCD$ 中, 平面 $ABD\perp$ 平面 $BCD$, $AB=AD$, $O$ 为 $BD$ 的中点.

![图1](../assets/20-fig-01.png)

(1) 证明: $OA\perp CD$;

(2) 若 $\triangle OCD$ 是边长为 $1$ 的等边三角形, 点 $E$ 在棱 $AD$ 上, $DE=2EA$, 且二面角 $E-BC-D$ 的大小为 $45^\circ$, 求三棱锥 $A-BCD$ 的体积.

``````

---

## 027 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/21.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/21.md) · SHA 570beee801f5274e0c85335158d22da8e3c92229 · mode 100644

``````markdown
---
id: 2021-I-21
paper_id: 2021-I
number: 21
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在平面直角坐标系 $xOy$ 中, 已知点 $F_1(-\sqrt{17},0)$, $F_2(\sqrt{17},0)$, 点 $M$ 满足 $||MF_1|-|MF_2||=2$. 记 $M$ 的轨迹为 $C$.

(1) 求 $C$ 的方程;

(2) 设点 $T$ 在直线 $x=\dfrac{1}{2}$ 上, 过 $T$ 的两条直线分别交 $C$ 于 $A$, $B$ 两点和 $P$, $Q$ 两点, 且 $|TA|\cdot|TB|=|TP|\cdot|TQ|$, 求直线 $AB$ 的斜率与直线 $PQ$ 的斜率之和.

``````

---

## 028 · mirror/gaokao-math-corpus/corpus/papers/2021/I/items/22.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2021/I/items/22.md) · SHA 82111a94e306d3bf77197c7a9fc5f2d38acae1ab · mode 100644

``````markdown
---
id: 2021-I-22
paper_id: 2021-I
number: 22
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=x(1-\ln x)$.

(1) 讨论 $f(x)$ 的单调性;

(2) 设 $a$, $b$ 为两个不相等的正数, 且 $b\ln a-a\ln b=a-b$, 证明: $2<\dfrac{1}{a}+\dfrac{1}{b}<e$.

``````

---

## 029 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/01.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/01.md) · SHA 5309b69b5bf831494b34dfb52f981a1a11ef48dc · mode 100644

``````markdown
---
id: 2022-I-01
paper_id: 2022-I
number: 1
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\{x \mid 0 \le x < 2\}$
  B: $\{x \mid \dfrac{1}{3} \le x < 2\}$
  C: $\{x \mid 3 \le x < 16\}$
  D: $\{x \mid \dfrac{1}{3} \le x < 16\}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若集合 $M=\{x \mid \sqrt{x}<4\}$, $N=\{x \mid 3x \ge 1\}$, 则 $M \cap N=$

``````

---

## 030 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/02.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/02.md) · SHA ab2dd57d20dab51d64c10f5e683cce765cfc05ec · mode 100644

``````markdown
---
id: 2022-I-02
paper_id: 2022-I
number: 2
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-2$
  B: $-1$
  C: $1$
  D: $2$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若 $\mathrm{i}(1-z)=1$, 则 $z+\overline{z}=$

``````

---

## 031 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/03.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/03.md) · SHA 8b6b9faf7029d11768e50b4ceb0bd3dc27d74738 · mode 100644

``````markdown
---
id: 2022-I-03
paper_id: 2022-I
number: 3
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $3\boldsymbol m-2\boldsymbol n$
  B: $-2\boldsymbol m+3\boldsymbol n$
  C: $3\boldsymbol m+2\boldsymbol n$
  D: $2\boldsymbol m+3\boldsymbol n$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在 $\triangle ABC$ 中, 点 $D$ 在边 $AB$ 上, $BD=2DA$. 记 $\overrightarrow{CA}=\boldsymbol m$, $\overrightarrow{CD}=\boldsymbol n$, 则 $\overrightarrow{CB}=$

``````

---

## 032 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/04.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/04.md) · SHA ee4efa6158e56ceeb41a2f47ac2279afc36b6c00 · mode 100644

``````markdown
---
id: 2022-I-04
paper_id: 2022-I
number: 4
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $1.0 \times 10^9\ \mathrm{m}^3$
  B: $1.2 \times 10^9\ \mathrm{m}^3$
  C: $1.4 \times 10^9\ \mathrm{m}^3$
  D: $1.6 \times 10^9\ \mathrm{m}^3$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

南水北调工程缓解了北方一些地区水资源短缺问题, 其中一部分水蓄入某水库. 已知该水库水位为海拔 $148.5\ \mathrm{m}$ 时, 相应水面的面积为 $140.0\ \mathrm{km}^2$; 水位为海拔 $157.5\ \mathrm{m}$ 时, 相应水面的面积为 $180.0\ \mathrm{km}^2$. 将该水库在这两个水位间的形状看作一个棱台, 则该水库水位从海拔 $148.5\ \mathrm{m}$ 上升到 $157.5\ \mathrm{m}$ 时, 增加的水量约为($\sqrt{7}\approx 2.65$)

``````

---

## 033 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/05.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/05.md) · SHA 78d7d07a8a3ed11489042225ce5bf92e126d3fe4 · mode 100644

``````markdown
---
id: 2022-I-05
paper_id: 2022-I
number: 5
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{1}{6}$
  B: $\dfrac{1}{3}$
  C: $\dfrac{1}{2}$
  D: $\dfrac{2}{3}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

从 $2$ 至 $8$ 的 $7$ 个整数中随机取 $2$ 个不同的数, 则这 $2$ 个数互质的概率为

``````

---

## 034 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/06.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/06.md) · SHA 9e7c3da508eff714a142481e7219b4c2e4af790a · mode 100644

``````markdown
---
id: 2022-I-06
paper_id: 2022-I
number: 6
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $1$
  B: $\dfrac{3}{2}$
  C: $\dfrac{5}{2}$
  D: $3$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记函数 $f(x)=\sin(\omega x+\dfrac{\pi}{4})+b(\omega>0)$ 的最小正周期为 $T$, 若 $\dfrac{2\pi}{3}<T<\pi$, 且 $y=f(x)$ 的图像关于点 $(\dfrac{3\pi}{2},2)$ 中心对称, 则 $f(\dfrac{\pi}{2})=$

``````

---

## 035 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/07.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/07.md) · SHA 99c964b91a46c26d6043c748df5b7aebe99871c6 · mode 100644

``````markdown
---
id: 2022-I-07
paper_id: 2022-I
number: 7
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $a<b<c$
  B: $c<b<a$
  C: $c<a<b$
  D: $a<c<b$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设 $a=0.1e^{0.1}$, $b=\dfrac{1}{9}$, $c=-\ln 0.9$, 则

``````

---

## 036 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/08.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/08.md) · SHA aa7742a482171399b5fa52dd237b1c98381acb5d · mode 100644

``````markdown
---
id: 2022-I-08
paper_id: 2022-I
number: 8
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $[18,\dfrac{81}{4}]$
  B: $[\dfrac{27}{4},\dfrac{81}{4}]$
  C: $[\dfrac{27}{4},\dfrac{64}{3}]$
  D: $[18,27]$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知正四棱锥的侧棱长为 $l$, 其各顶点都在同一球面上. 若该球的体积为 $36\pi$, 且 $3 \le l \le 3\sqrt{3}$, 则该正四棱锥体积的取值范围是

``````

---

## 037 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/09.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/09.md) · SHA bd329c64b71077a752ac228b8c844da7bdcd8bec · mode 100644

``````markdown
---
id: 2022-I-09
paper_id: 2022-I
number: 9
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 直线 $BC_1$ 与 $DA_1$ 所成的角为 $90^\circ$
  B: 直线 $BC_1$ 与 $CA_1$ 所成的角为 $90^\circ$
  C: 直线 $BC_1$ 与平面 $BB_1D_1D$ 所成的角为 $45^\circ$
  D: 直线 $BC_1$ 与平面 $ABCD$ 所成的角为 $45^\circ$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知正方体 $ABCD-A_1B_1C_1D_1$, 则

``````

---

## 038 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/10.md) · SHA 99c64e9154f817aea87bdcd6571ee496dbf5ceae · mode 100644

``````markdown
---
id: 2022-I-10
paper_id: 2022-I
number: 10
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $f(x)$ 有两个极值点
  B: $f(x)$ 有三个零点
  C: 点 $(0,1)$ 是曲线 $y=f(x)$ 的对称中心
  D: 直线 $y=2x$ 是曲线 $y=f(x)$ 的切线
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=x^3-x+1$, 则

``````

---

## 039 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/11.md) · SHA 3b10b609ad2666a474c7551ad5472b7764a4c101 · mode 100644

``````markdown
---
id: 2022-I-11
paper_id: 2022-I
number: 11
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $C$ 的准线为 $y=-1$
  B: 直线 $AB$ 与 $C$ 相切
  C: $|OP|\cdot|OQ|>|OA|^2$
  D: $|BP|\cdot|BQ|>|BA|^2$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $O$ 为坐标原点, 点 $A(1,1)$ 在抛物线 $C:x^2=2py(p>0)$ 上, 过点 $B(0,-1)$ 的直线交 $C$ 于 $P$, $Q$ 两点, 则

``````

---

## 040 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/12.md) · SHA e469b1b0e54d24562443bed0e21d5027beaeed06 · mode 100644

``````markdown
---
id: 2022-I-12
paper_id: 2022-I
number: 12
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $f(0)=0$
  B: $g(-\dfrac{1}{2})=0$
  C: $f(-1)=f(4)$
  D: $g(-1)=g(2)$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)$ 及其导函数 $f'(x)$ 的定义域均为 $\mathbb{R}$, 记 $g(x)=f'(x)$. 若 $f(\dfrac{3}{2}-2x)$, $g(2+x)$ 均为偶函数, 则

``````

---

## 041 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/13.md) · SHA a1548a15202040a78e3c09768ffec7e884473a6b · mode 100644

``````markdown
---
id: 2022-I-13
paper_id: 2022-I
number: 13
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

$(1-\dfrac{y}{x})(x+y)^8$ 的展开式中 $x^2y^6$ 的系数为 [填空] (用数字作答).

``````

---

## 042 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/14.md) · SHA 4c3eba275d1810e61528175757c38d59f522f4f0 · mode 100644

``````markdown
---
id: 2022-I-14
paper_id: 2022-I
number: 14
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

写出与圆 $x^2+y^2=1$ 和 $(x-3)^2+(y-4)^2=16$ 都相切的一条直线的方程[填空].

``````

---

## 043 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/15.md) · SHA 66ab7ba9cc542f4ab4314f8aa65106cd3afaec85 · mode 100644

``````markdown
---
id: 2022-I-15
paper_id: 2022-I
number: 15
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若曲线 $y=(x+a)e^x$ 有两条过坐标原点的切线, 则 $a$ 的取值范围是[填空].

``````

---

## 044 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/16.md) · SHA 5cff7d2ecb0764c80a6f1c9191afe60962dd64ef · mode 100644

``````markdown
---
id: 2022-I-16
paper_id: 2022-I
number: 16
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1(a>b>0)$, $C$ 的上顶点为 $A$, 两个焦点为 $F_1$, $F_2$, 离心率为 $\dfrac{1}{2}$. 过 $F_1$ 且垂直于 $AF_2$ 的直线交 $C$ 于 $D$, $E$ 两点, $|DE|=6$, 则 $\triangle ADE$ 的周长是[填空].

``````

---

## 045 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/17.md) · SHA b9970d4b28c6884637386d88f6a4a0367746e6a8 · mode 100644

``````markdown
---
id: 2022-I-17
paper_id: 2022-I
number: 17
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $S_n$ 为数列 $\{a_n\}$ 的前 $n$ 项和, 已知 $a_1=1$, $\{\dfrac{S_n}{a_n}\}$ 是公差为 $\dfrac{1}{3}$ 的等差数列.

(1) 求 $\{a_n\}$ 的通项公式;

(2) 证明: $\dfrac{1}{a_1}+\dfrac{1}{a_2}+\cdots+\dfrac{1}{a_n}<2$.

``````

---

## 046 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/18.md) · SHA d3c62c0ede26a1b5287737645d2121b7c44f3210 · mode 100644

``````markdown
---
id: 2022-I-18
paper_id: 2022-I
number: 18
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $\triangle ABC$ 的内角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$, 已知 $\dfrac{\cos A}{1+\sin A}=\dfrac{\sin 2B}{1+\cos 2B}$.

(1) 若 $C=\dfrac{2\pi}{3}$, 求 $B$.

(2) 求 $\dfrac{a^2+b^2}{c^2}$ 的最小值.

``````

---

## 047 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/19.md) · SHA b020c296c88c8e26bcbf20b0d34ac9a4e79afc00 · mode 100644

``````markdown
---
id: 2022-I-19
paper_id: 2022-I
number: 19
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/19-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, 直三棱柱 $ABC-A_1B_1C_1$ 的体积为 $4$, $\triangle A_1BC$ 的面积为 $2\sqrt{2}$.

![图 1](../assets/19-fig-01.png)

(1) 求 $A$ 到平面 $A_1BC$ 的距离;

(2) 设 $D$ 为 $A_1C$ 的中点, $AA_1=AB$, 平面 $A_1BC \perp$ 平面 $ABB_1A_1$, 求二面角 $A-BD-C$ 的正弦值.

``````

---

## 048 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/20.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/20.md) · SHA 15350b2decb68db7c953e0b63fa1b91274245aa2 · mode 100644

``````markdown
---
id: 2022-I-20
paper_id: 2022-I
number: 20
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: table-01
  type: table
  path: ../assets/20-table-01.png
  needs_confirmation: false
  notes: []
- id: table-02
  type: table
  path: ../assets/20-table-02.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

一医疗团队为研究某地的一种地方性疾病与当地居民的卫生习惯(卫生习惯分为良好和不够良好两类)的关系, 在已患该疾病的病例中随机调查了 $100$ 例(称为病例组), 同时在未患该疾病的人群中随机调查了 $100$ 人(称为对照组), 得到如下数据:

![表 1](../assets/20-table-01.png)

(1) 能否有 $99\%$ 的把握认为患该疾病群体与未患该疾病群体的卫生习惯有差异?

(2) 从该地的人群中任选一人, $A$ 表示事件 "选到的人卫生习惯不够良好", $B$ 表示事件 "选到的人患有该疾病", $\dfrac{P(B \mid A)}{P(\overline{B} \mid A)}$ 与 $\dfrac{P(B \mid \overline{A})}{P(\overline{B} \mid \overline{A})}$ 的比值是卫生习惯不够良好对患该疾病风险程度的一项度量指标, 记该指标为 $R$.

(i) 证明: $R=\dfrac{P(A \mid B)}{P(\overline{A} \mid B)}\cdot\dfrac{P(\overline{A} \mid \overline{B})}{P(A \mid \overline{B})}$;

(ii) 利用该调查数据, 给出 $P(A \mid B)$, $P(A \mid \overline{B})$ 的估计值, 并利用 (i) 的结果给出 $R$ 的估计值.

附: $K^2=\dfrac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}$,

![表 2](../assets/20-table-02.png)

``````

---

## 049 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/21.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/21.md) · SHA afb127c2390e071d6e1cc47d068580e9b06a593d · mode 100644

``````markdown
---
id: 2022-I-21
paper_id: 2022-I
number: 21
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知点 $A(2,1)$ 在双曲线 $C:\dfrac{x^2}{a^2}-\dfrac{y^2}{a^2-1}=1(a>1)$ 上, 直线 $l$ 交 $C$ 于 $P$, $Q$ 两点, 直线 $AP$, $AQ$ 的斜率之和为 $0$.

(1) 求 $l$ 的斜率;

(2) 若 $\tan \angle PAQ=2\sqrt{2}$, 求 $\triangle PAQ$ 的面积.

``````

---

## 050 · mirror/gaokao-math-corpus/corpus/papers/2022/I/items/22.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/I/items/22.md) · SHA 73ee1313ade0ed2c1fc35720b92e4f30564e7343 · mode 100644

``````markdown
---
id: 2022-I-22
paper_id: 2022-I
number: 22
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=e^x-ax$ 和 $g(x)=ax-\ln x$ 有相同的最小值.

(1) 求 $a$;

(2) 证明: 存在直线 $y=b$, 其与两条曲线 $y=f(x)$ 和 $y=g(x)$ 共有三个不同的交点, 并且从左到右的三个交点的横坐标成等差数列.

``````

---

## 051 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/01.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/01.md) · SHA affce189cdd68628d3de6c0a7b8b4a13c2d5e52d · mode 100644

``````markdown
---
id: 2022-II-01
paper_id: 2022-II
number: 1
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\{-1,2\}$
  B: $\{1,2\}$
  C: $\{1,4\}$
  D: $\{-1,4\}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知集合 $A=\{-1,1,2,4\}$, $B=\{x\mid |x-1|\leq 1\}$, 则 $A\cap B=$

``````

---

## 052 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/02.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/02.md) · SHA 052840be4d84e59d786f7e2e291b86157720d0ce · mode 100644

``````markdown
---
id: 2022-II-02
paper_id: 2022-II
number: 2
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-2+4\mathrm{i}$
  B: $-2-4\mathrm{i}$
  C: $6+2\mathrm{i}$
  D: $6-2\mathrm{i}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

$(2+2\mathrm{i})(1-2\mathrm{i})=$

``````

---

## 053 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/03.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/03.md) · SHA b1687d341622488ad9d5b2decda60db50564c2c2 · mode 100644

``````markdown
---
id: 2022-II-03
paper_id: 2022-II
number: 3
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/03-fig-01.png
  needs_confirmation: false
  notes: []
options:
  A: $0.75$
  B: $0.8$
  C: $0.85$
  D: $0.9$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

图 1 是中国古代建筑中的举架结构, $AA'$, $BB'$, $CC'$, $DD'$ 是桁, 相邻桁的水平距离称为步, 垂直距离称为举. 图 2 是某古代建筑屋顶截面的示意图, 其中 $DD_1$, $CC_1$, $BB_1$, $AA_1$ 是举, $OD_1$, $DC_1$, $CB_1$, $BA_1$ 是相等的步, 相邻桁的举步之比分别为 $\dfrac{DD_1}{OD_1}=0.5$, $\dfrac{CC_1}{DC_1}=k_1$, $\dfrac{BB_1}{CB_1}=k_2$, $\dfrac{AA_1}{BA_1}=k_3$. 已知 $k_1$, $k_2$, $k_3$ 成公差为 $0.1$ 的等差数列, 且直线 $OA$ 的斜率为 $0.725$, 则 $k_3=$

![图 1 与图 2](../assets/03-fig-01.png)

``````

---

## 054 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/04.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/04.md) · SHA e1f1327bfeb2d6bf35b4ec18605ac15ba75d4049 · mode 100644

``````markdown
---
id: 2022-II-04
paper_id: 2022-II
number: 4
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-6$
  B: $-5$
  C: $5$
  D: $6$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知向量 $\boldsymbol{a}=(3,4)$, $\boldsymbol{b}=(1,0)$, $\boldsymbol{c}=\boldsymbol{a}+t\boldsymbol{b}$, 若 $\langle \boldsymbol{a},\boldsymbol{c}\rangle=\langle \boldsymbol{b},\boldsymbol{c}\rangle$, 则 $t=$

``````

---

## 055 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/05.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/05.md) · SHA 52ff9a2b9fc6414b470817dc65e6751073aa5c91 · mode 100644

``````markdown
---
id: 2022-II-05
paper_id: 2022-II
number: 5
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $12$ 种
  B: $24$ 种
  C: $36$ 种
  D: $48$ 种
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

甲, 乙, 丙, 丁, 戊 $5$ 名同学站成一排参加文艺汇演, 若甲不站在两端, 丙和丁相邻, 则不同排列方式共有

``````

---

## 056 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/06.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/06.md) · SHA 634858431e37262100996957ace7373486bcb20e · mode 100644

``````markdown
---
id: 2022-II-06
paper_id: 2022-II
number: 6
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\tan(\alpha-\beta)=1$
  B: $\tan(\alpha+\beta)=1$
  C: $\tan(\alpha-\beta)=-1$
  D: $\tan(\alpha+\beta)=-1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若 $\sin(\alpha+\beta)+\cos(\alpha+\beta)=2\sqrt{2}\cos(\alpha+\dfrac{\pi}{4})\sin\beta$, 则

``````

---

## 057 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/07.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/07.md) · SHA a977f632e6df39821fea6e8539c5da178eb5992f · mode 100644

``````markdown
---
id: 2022-II-07
paper_id: 2022-II
number: 7
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $100\pi$
  B: $128\pi$
  C: $144\pi$
  D: $192\pi$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知正三棱台的高为 $1$, 上, 下底面边长分别为 $3\sqrt{3}$ 和 $4\sqrt{3}$, 其顶点都在同一球面上, 则该球的表面积为

``````

---

## 058 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/08.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/08.md) · SHA a41f9d000b99906437d28b1dc567a4328cd72b99 · mode 100644

``````markdown
---
id: 2022-II-08
paper_id: 2022-II
number: 8
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-3$
  B: $-2$
  C: $0$
  D: $1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)$ 的定义域为 $\mathbb{R}$, 且 $f(x+y)+f(x-y)=f(x)f(y)$, $f(1)=1$, 则 $\sum_{k=1}^{22}f(k)=$

``````

---

## 059 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/09.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/09.md) · SHA af80871f7f8f30b015b97d48d930eaa7ffd8e519 · mode 100644

``````markdown
---
id: 2022-II-09
paper_id: 2022-II
number: 9
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $f(x)$ 在区间 $(0,\dfrac{5\pi}{12})$ 单调递减
  B: $f(x)$ 在区间 $(-\dfrac{\pi}{12},\dfrac{11\pi}{12})$ 有两个极值点
  C: 直线 $x=\dfrac{7\pi}{6}$ 是曲线 $y=f(x)$ 的对称轴
  D: 直线 $y=\dfrac{\sqrt{3}}{2}-x$ 是曲线 $y=f(x)$ 的切线
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=\sin(2x+\varphi)(0<\varphi<\pi)$ 的图像关于点 $(\dfrac{2\pi}{3},0)$ 中心对称, 则

``````

---

## 060 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/10.md) · SHA 3199edaa563e7305e314074c3966886f7ad6b721 · mode 100644

``````markdown
---
id: 2022-II-10
paper_id: 2022-II
number: 10
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 直线 $AB$ 的斜率为 $2\sqrt{6}$
  B: $|OB|=|OF|$
  C: $|AB|>4|OF|$
  D: $\angle OAM+\angle OBM<180^\circ$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $O$ 为坐标原点, 过抛物线 $C:y^2=2px(p>0)$ 焦点 $F$ 的直线与 $C$ 交于 $A$, $B$ 两点, 其中 $A$ 在第一象限, 点 $M(p,0)$. 若 $|AF|=|AM|$, 则

``````

---

## 061 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/11.md) · SHA c99ed95cd9a38430b392844d1eb3eae49ff50e6e · mode 100644

``````markdown
---
id: 2022-II-11
paper_id: 2022-II
number: 11
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/11-fig-01.png
  needs_confirmation: false
  notes: []
options:
  A: $V_1=2V_2$
  B: $V_3=V_1$
  C: $V_3=V_1+V_2$
  D: $2V_3=3V_1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, 四边形 $ABCD$ 为正方形, $ED\perp$ 平面 $ABCD$, $FB\parallel ED$, $AB=ED=2FB$, 记棱锥 $E-ACD$, $F-ABC$, $F-ACE$ 的体积分别为 $V_1$, $V_2$, $V_3$, 则

![图](../assets/11-fig-01.png)

``````

---

## 062 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/12.md) · SHA eb41b2462e85ae6d2d3fe3d3e7a8f4aa1b664f4c · mode 100644

``````markdown
---
id: 2022-II-12
paper_id: 2022-II
number: 12
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $x+y\leq 1$
  B: $x+y\geq -2$
  C: $x^2+y^2\leq 2$
  D: $x^2+y^2\geq 1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若 $x$, $y$ 满足 $x^2+y^2-xy=1$, 则

``````

---

## 063 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/13.md) · SHA 7e66b7da78f4aa0d3ef08a6c68e98265395c8b98 · mode 100644

``````markdown
---
id: 2022-II-13
paper_id: 2022-II
number: 13
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知随机变量 $X$ 服从正态分布 $N(2,\sigma^2)$, 且 $P(2<X\leq 2.5)=0.36$, 则 $P(X>2.5)=$ [填空].

``````

---

## 064 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/14.md) · SHA 782dbe8d288a2adc71c037967763c9e370aad91a · mode 100644

``````markdown
---
id: 2022-II-14
paper_id: 2022-II
number: 14
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

曲线 $y=\ln|x|$ 过坐标原点的两条切线的方程为 [填空], [填空].

``````

---

## 065 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/15.md) · SHA 4a3f1f051ac42548b3bcd7b1d703ce62e819e4b7 · mode 100644

``````markdown
---
id: 2022-II-15
paper_id: 2022-II
number: 15
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设点 $A(-2,3)$, $B(0,a)$, 若直线 $AB$ 关于 $y=a$ 对称的直线与圆 $(x+3)^2+(y+2)^2=1$ 有公共点, 则 $a$ 的取值范围是 [填空].

``````

---

## 066 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/16.md) · SHA ec92a5bccec301fd67673e3e5a63b297da668ae5 · mode 100644

``````markdown
---
id: 2022-II-16
paper_id: 2022-II
number: 16
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知直线 $l$ 与椭圆 $C:\dfrac{x^2}{6}+\dfrac{y^2}{3}=1$ 在第一象限交于 $A$, $B$ 两点, $l$ 与 $x$ 轴, $y$ 轴分别交于 $M$, $N$ 两点, 且 $|MA|=|NB|$, $|MN|=2\sqrt{3}$, 则 $l$ 的方程为 [填空].

``````

---

## 067 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/17.md) · SHA c538a5021e1426ad8b95f0adedd9808b1b1e465b · mode 100644

``````markdown
---
id: 2022-II-17
paper_id: 2022-II
number: 17
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $\{a_n\}$ 为等差数列, $\{b_n\}$ 是公比为 $2$ 的等比数列, 且 $a_2-b_2=a_3-b_3=b_4-a_4$.

(1) 证明: $a_1=b_1$;

(2) 求集合 $\{k\mid b_k=a_m+a_1,1\leq m\leq 500\}$ 中元素的个数.

``````

---

## 068 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/18.md) · SHA 9b2a5443a41e1ec8093f8351cd598621a63087df · mode 100644

``````markdown
---
id: 2022-II-18
paper_id: 2022-II
number: 18
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $\triangle ABC$ 的内角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$, 分别以 $a$, $b$, $c$ 为边长的三个正三角形的面积依次为 $S_1$, $S_2$, $S_3$, 已知 $S_1-S_2+S_3=\dfrac{\sqrt{3}}{2}$, $\sin B=\dfrac{1}{3}$.

(1) 求 $\triangle ABC$ 的面积;

(2) 若 $\sin A\sin C=\dfrac{\sqrt{2}}{3}$, 求 $b$.

``````

---

## 069 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/19.md) · SHA 751a82c9b38a9765e71f113295a4997e01337214 · mode 100644

``````markdown
---
id: 2022-II-19
paper_id: 2022-II
number: 19
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/19-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
- label: (3)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在某地区进行流行病学调查, 随机调查了 $100$ 位某种疾病患者的年龄, 得到如下的样本数据的频率分布直方图:

![频率分布直方图](../assets/19-fig-01.png)

(1) 估计该地区这种疾病患者的平均年龄 (同一组中的数据用该组区间的中点值为代表);

(2) 估计该地区一位这种疾病患者的年龄位于区间 $[20,70)$ 的概率;

(3) 已知该地区这种疾病的患病率为 $0.1\%$, 该地区年龄位于区间 $[40,50)$ 的人口占该地区总人口的 $16\%$. 从该地区中任选一人, 若此人的年龄位于区间 $[40,50)$, 求此人患这种疾病的概率 (以样本数据中患者的年龄位于各区间的频率作为患者的年龄位于该区间的概率, 精确到 $0.0001$).

``````

---

## 070 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/20.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/20.md) · SHA ca2c5ec41124c0f808f2dcc08989207f5e1e9ad2 · mode 100644

``````markdown
---
id: 2022-II-20
paper_id: 2022-II
number: 20
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/20-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, $PO$ 是三棱锥 $P-ABC$ 的高, $PA=PB$, $AB\perp AC$, $E$ 是 $PB$ 的中点.

![图](../assets/20-fig-01.png)

(1) 证明: $OE\parallel$ 平面 $PAC$;

(2) 若 $\angle ABO=\angle CBO=30^\circ$, $PO=3$, $PA=5$, 求二面角 $C-AE-B$ 的正弦值.

``````

---

## 071 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/21.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/21.md) · SHA 9da56e49175e2d65a7eee14e0c7956185ff25ea6 · mode 100644

``````markdown
---
id: 2022-II-21
paper_id: 2022-II
number: 21
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知双曲线 $C:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1(a>0,b>0)$ 的右焦点为 $F(2,0)$, 渐近线方程为 $y=\pm\sqrt{3}x$.

(1) 求 $C$ 的方程;

(2) 过 $F$ 的直线与 $C$ 的两条渐近线分别交于 $A$, $B$ 两点, 点 $P(x_1,y_1)$, $Q(x_2,y_2)$ 在 $C$ 上, 且 $x_1>x_2>0$, $y_1>0$. 过 $P$ 且斜率为 $-\sqrt{3}$ 的直线与过 $Q$ 且斜率为 $\sqrt{3}$ 的直线交于点 $M$. 从下面①②③中选取两个作为条件, 证明另外一个成立.

① $M$ 在 $AB$ 上; ② $PQ\parallel AB$; ③ $|MA|=|MB|$.

注: 若选择不同的组合分别解答, 则按第一个解答计分.

``````

---

## 072 · mirror/gaokao-math-corpus/corpus/papers/2022/II/items/22.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2022/II/items/22.md) · SHA acfe43c7712bd06ff1f1b7b8ec89f0e74f737f28 · mode 100644

``````markdown
---
id: 2022-II-22
paper_id: 2022-II
number: 22
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
- label: (3)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=x\mathrm{e}^{ax}-\mathrm{e}^x$.

(1) 当 $a=1$ 时, 讨论 $f(x)$ 的单调性;

(2) 当 $x>0$ 时, $f(x)<-1$, 求 $a$ 的取值范围;

(3) 设 $n\in\mathbb{N}^*$, 证明 $\dfrac{1}{\sqrt{1^2+1}}+\dfrac{1}{\sqrt{2^2+2}}+\cdots+\dfrac{1}{\sqrt{n^2+n}}>\ln(n+1)$.

``````

---

## 073 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/01.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/01.md) · SHA 2b473749658ba895868b2b6aeb63d26c11771671 · mode 100644

``````markdown
---
id: 2023-I-01
paper_id: 2023-I
number: 1
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\{-2,-1,0,1\}$
  B: $\{0,1,2\}$
  C: $\{-2\}$
  D: $\{2\}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知集合 $M=\{-2,-1,0,1,2\}$, $N=\{x\mid x^2-x-6\geqslant0\}$, 则 $M\cap N=$

``````

---

## 074 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/02.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/02.md) · SHA d358b58e7611dee64b80fa6a10865ed29dd824b8 · mode 100644

``````markdown
---
id: 2023-I-02
paper_id: 2023-I
number: 2
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-\mathrm{i}$
  B: $\mathrm{i}$
  C: $0$
  D: $1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $z=\dfrac{1-\mathrm{i}}{2+2\mathrm{i}}$, 则 $z-\bar z=$

``````

---

## 075 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/03.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/03.md) · SHA dce14d4234011b4421e947859502b2938c458bfc · mode 100644

``````markdown
---
id: 2023-I-03
paper_id: 2023-I
number: 3
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\lambda+\mu=1$
  B: $\lambda+\mu=-1$
  C: $\lambda\mu=1$
  D: $\lambda\mu=-1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知向量 $\boldsymbol a=(1,1)$, $\boldsymbol b=(1,-1)$. 若 $(\boldsymbol a+\lambda\boldsymbol b)\perp(\boldsymbol a+\mu\boldsymbol b)$, 则

``````

---

## 076 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/04.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/04.md) · SHA f36ae53e8fa4177c494ca258a3e414d7cc831be5 · mode 100644

``````markdown
---
id: 2023-I-04
paper_id: 2023-I
number: 4
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $(-\infty,-2]$
  B: $[-2,0)$
  C: $(0,2]$
  D: $[2,+\infty)$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设函数 $f(x)=2^{x(x-a)}$ 在区间 $(0,1)$ 单调递减, 则 $a$ 的取值范围是

``````

---

## 077 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/05.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/05.md) · SHA 3ac2ed56f34210f598f04680d68360068d48fdf0 · mode 100644

``````markdown
---
id: 2023-I-05
paper_id: 2023-I
number: 5
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{2\sqrt3}{3}$
  B: $\sqrt2$
  C: $\sqrt3$
  D: $\sqrt6$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设椭圆 $C_1:\dfrac{x^2}{a^2}+y^2=1(a>1)$, $C_2:\dfrac{x^2}{4}+y^2=1$ 的离心率分别为 $e_1$, $e_2$. 若 $e_2=\sqrt3 e_1$, 则 $a=$

``````

---

## 078 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/06.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/06.md) · SHA b3fbd0f3b85fbe8efc25280dd3aae2b7fe34bb03 · mode 100644

``````markdown
---
id: 2023-I-06
paper_id: 2023-I
number: 6
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $1$
  B: $\dfrac{\sqrt{15}}{4}$
  C: $\dfrac{\sqrt{10}}{4}$
  D: $\dfrac{\sqrt6}{4}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

过 $(0,-2)$ 与圆 $x^2+y^2-4x-1=0$ 相切的两条直线的夹角为 $\alpha$, 则 $\sin\alpha=$

``````

---

## 079 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/07.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/07.md) · SHA 67e8908664f139aad8fd4bd411ee89091fa027cb · mode 100644

``````markdown
---
id: 2023-I-07
paper_id: 2023-I
number: 7
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 甲是乙的充分条件但不是必要条件
  B: 甲是乙的必要条件但不是充分条件
  C: 甲是乙的充要条件
  D: 甲既不是乙的充分条件也不是乙的必要条件
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $S_n$ 为数列 $\{a_n\}$ 的前 $n$ 项和, 设甲: $\{a_n\}$ 为等差数列; 乙: $\left\{\dfrac{S_n}{n}\right\}$ 为等差数列, 则

``````

---

## 080 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/08.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/08.md) · SHA 4bded8faedee1de8f27dd024523d242147673a5a · mode 100644

``````markdown
---
id: 2023-I-08
paper_id: 2023-I
number: 8
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{7}{9}$
  B: $\dfrac{1}{9}$
  C: $-\dfrac{1}{9}$
  D: $-\dfrac{7}{9}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $\sin(\alpha-\beta)=\dfrac{1}{3}$, $\cos\alpha\sin\beta=\dfrac{1}{6}$, 则 $\cos(2\alpha+2\beta)=$

``````

---

## 081 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/09.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/09.md) · SHA 480f7cf52c3db9790c68bef93d5e38de70b162ba · mode 100644

``````markdown
---
id: 2023-I-09
paper_id: 2023-I
number: 9
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $x_2,x_3,x_4,x_5$ 的平均数等于 $x_1,x_2,\cdots,x_6$ 的平均数
  B: $x_2,x_3,x_4,x_5$ 的中位数等于 $x_1,x_2,\cdots,x_6$ 的中位数
  C: $x_2,x_3,x_4,x_5$ 的标准差不小于 $x_1,x_2,\cdots,x_6$ 的标准差
  D: $x_2,x_3,x_4,x_5$ 的极差不大于 $x_1,x_2,\cdots,x_6$ 的极差
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

有一组样本数据 $x_1,x_2,\cdots,x_6$, 其中 $x_1$ 是最小值, $x_6$ 是最大值, 则

``````

---

## 082 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/10.md) · SHA 263fc44ba67fed3326c505e6649911dd54904044 · mode 100644

``````markdown
---
id: 2023-I-10
paper_id: 2023-I
number: 10
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: table-01
  type: table
  path: ../assets/10-table-01.png
  needs_confirmation: false
  notes: []
options:
  A: $p_1\geqslant p_2$
  B: $p_2>10p_3$
  C: $p_3=100p_0$
  D: $p_1\leqslant100p_2$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

噪声污染问题越来越受到重视. 用声压级来度量声音的强弱, 定义声压级 $L_p=20\times\lg\dfrac{p}{p_0}$, 其中常数 $p_0(p_0>0)$ 是听觉下限阈值, $p$ 是实际声压. 下表为不同声源的声压级:

![表 1](../assets/10-table-01.png)

已知在距离燃油汽车, 混合动力汽车, 电动汽车 $10\ \mathrm{m}$ 处测得实际声压分别为 $p_1$, $p_2$, $p_3$, 则

``````

---

## 083 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/11.md) · SHA 677fd624463186f5a471830466e4961103c65ca3 · mode 100644

``````markdown
---
id: 2023-I-11
paper_id: 2023-I
number: 11
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $f(0)=0$
  B: $f(1)=0$
  C: $f(x)$ 是偶函数
  D: $x=0$ 为 $f(x)$ 的极小值点
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)$ 的定义域为 $\mathbb R$, $f(xy)=y^2f(x)+x^2f(y)$, 则

``````

---

## 084 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/12.md) · SHA 83d4b0e07ed70a649077530aa34f752511935725 · mode 100644

``````markdown
---
id: 2023-I-12
paper_id: 2023-I
number: 12
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 直径为 $0.99\ \mathrm{m}$ 的球体
  B: 所有棱长均为 $1.4\ \mathrm{m}$ 的四面体
  C: 底面直径为 $0.01\ \mathrm{m}$, 高为 $1.8\ \mathrm{m}$ 的圆柱体
  D: 底面直径为 $1.2\ \mathrm{m}$, 高为 $0.01\ \mathrm{m}$ 的圆柱体
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

下列物体中, 能被整体放入棱长为 $1$ (单位: $\mathrm{m}$) 的正方体容器 (容器壁厚度忽略不计) 内的有

``````

---

## 085 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/13.md) · SHA b06a3ed60f222dc54c7c1e17b4cdb00f0f5a0281 · mode 100644

``````markdown
---
id: 2023-I-13
paper_id: 2023-I
number: 13
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

某学校开设了 $4$ 门体育类选修课和 $4$ 门艺术类选修课, 学生需从这 $8$ 门课中选 $2$ 门或 $3$ 门课, 并且每类选修课至少选修 $1$ 门, 则不同的选课方案共有[填空]种 (用数字作答).

``````

---

## 086 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/14.md) · SHA 2f8c728f010d037db9efd37987bce0add550051b · mode 100644

``````markdown
---
id: 2023-I-14
paper_id: 2023-I
number: 14
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在正四棱台 $ABCD-A_1B_1C_1D_1$ 中, $AB=2$, $A_1B_1=1$, $AA_1=\sqrt2$, 则该棱台的体积为[填空].

``````

---

## 087 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/15.md) · SHA 21452921bb2b1ce07ad6ca69738abf99657c8e2f · mode 100644

``````markdown
---
id: 2023-I-15
paper_id: 2023-I
number: 15
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=\cos\omega x-1(\omega>0)$ 在区间 $[0,2\pi]$, 有且仅有 $3$ 个零点, 则 $\omega$ 的取值范围是[填空].

``````

---

## 088 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/16.md) · SHA 2ae275d045119f82c00468750400bb1a3f8ddec9 · mode 100644

``````markdown
---
id: 2023-I-16
paper_id: 2023-I
number: 16
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知双曲线 $C:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1(a>0,b>0)$ 的左, 右焦点分别为 $F_1$, $F_2$. 点 $A$ 在 $C$ 上, 点 $B$ 在 $y$ 轴上, $\overrightarrow{F_1A}\perp\overrightarrow{F_1B}$, $\overrightarrow{F_2A}=-\dfrac{2}{3}\overrightarrow{F_2B}$, 则 $C$ 的离心率为[填空].

``````

---

## 089 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/17.md) · SHA 0693cd24fd33ca08948454901db026e4d13fefa2 · mode 100644

``````markdown
---
id: 2023-I-17
paper_id: 2023-I
number: 17
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知在 $\triangle ABC$ 中, $A+B=3C$, $2\sin(A-C)=\sin B$.

(1) 求 $\sin A$;

(2) 设 $AB=5$, 求 $AB$ 边上的高.

``````

---

## 090 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/18.md) · SHA 509bc25d503c7ef0610fbc8995dd733552a04926 · mode 100644

``````markdown
---
id: 2023-I-18
paper_id: 2023-I
number: 18
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/18-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, 在正四棱柱 $ABCD-A_1B_1C_1D_1$ 中, $AB=2$, $AA_1=4$. 点 $A_2$, $B_2$, $C_2$, $D_2$ 分别在棱 $AA_1$, $BB_1$, $CC_1$, $DD_1$ 上, $AA_2=1$, $BB_2=DD_2=2$, $CC_2=3$.

![图 1](../assets/18-fig-01.png)

(1) 证明: $B_2C_2//A_2D_2$;

(2) 点 $P$ 在棱 $BB_1$ 上, 当二面角 $P-A_2C_2-D_2$ 为 $150^\circ$ 时, 求 $B_2P$.

``````

---

## 091 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/19.md) · SHA bf6622c2b20054e8dfbcd075b59a6845906c3b74 · mode 100644

``````markdown
---
id: 2023-I-19
paper_id: 2023-I
number: 19
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=a(e^x+a)-x$.

(1) 讨论 $f(x)$ 的单调性;

(2) 证明: 当 $a>0$ 时, $f(x)>2\ln a+\dfrac{3}{2}$.

``````

---

## 092 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/20.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/20.md) · SHA 55fc5159b3615adba2cafebb9ec14a8c61869b97 · mode 100644

``````markdown
---
id: 2023-I-20
paper_id: 2023-I
number: 20
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设等差数列 $\{a_n\}$ 的公差为 $d$, 且 $d>1$. 令 $b_n=\dfrac{n^2+n}{a_n}$, 记 $S_n$, $T_n$ 分别为数列 $\{a_n\}$, $\{b_n\}$ 的前 $n$ 项和.

(1) 若 $3a_2=3a_1+a_3$, $S_3+T_3=21$, 求 $\{a_n\}$ 的通项公式;

(2) 若 $\{b_n\}$ 为等差数列, 且 $S_{99}-T_{99}=99$, 求 $d$.

``````

---

## 093 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/21.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/21.md) · SHA 674e5b15046607f4bffb23b27f13375a39df71f1 · mode 100644

``````markdown
---
id: 2023-I-21
paper_id: 2023-I
number: 21
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
- label: (3)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

甲乙两人投篮, 每次由其中一人投篮, 规则如下: 若命中则此人继续投篮, 若未命中则换为对方投篮. 无论之前投篮情况如何, 甲每次投篮的命中率均为 $0.6$, 乙每次投篮的命中率均为 $0.8$, 由抽签决定第一次投篮的人选, 第一次投篮的人是甲, 乙的概率各为 $0.5$.

(1) 求第 $2$ 次投篮的人是乙的概率;

(2) 求第 $i$ 次投篮的人是甲的概率;

(3) 已知: 若随机变量 $X_i$ 服从两点分布, 且 $P(X_i=1)=1-P(X_i=0)=q_i$, $i=1,2,\cdots,n$, 则 $E\left(\sum_{i=1}^n X_i\right)=\sum_{i=1}^n q_i$. 记前 $n$ 次 (即从第 $1$ 次到第 $n$ 次投篮) 中甲投篮的次数为 $Y$, 求 $E(Y)$.

``````

---

## 094 · mirror/gaokao-math-corpus/corpus/papers/2023/I/items/22.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/I/items/22.md) · SHA 6151395c9eaa924ded37d7250ee6fa95b6d6ba1b · mode 100644

``````markdown
---
id: 2023-I-22
paper_id: 2023-I
number: 22
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在直角坐标系 $xOy$ 中, 点 $P$ 到 $x$ 轴的距离等于点 $P$ 到点 $\left(0,\dfrac{1}{2}\right)$ 的距离, 记动点 $P$ 的轨迹为 $W$.

(1) 求 $W$ 的方程;

(2) 已知矩形 $ABCD$ 有三个顶点在 $W$ 上, 证明: 矩形 $ABCD$ 的周长大于 $3\sqrt3$.

``````

---

## 095 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/01.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/01.md) · SHA 98d83bb0e5b3d813377fc59d47c96d933ccb84f5 · mode 100644

``````markdown
---
id: 2023-II-01
paper_id: 2023-II
number: 1
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 第一象限
  B: 第二象限
  C: 第三象限
  D: 第四象限
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在复平面内, $(1+3\mathrm{i})(3-\mathrm{i})$ 对应的点位于

``````

---

## 096 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/02.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/02.md) · SHA 06eccb4da571fa950971af3483ed13effc6b8425 · mode 100644

``````markdown
---
id: 2023-II-02
paper_id: 2023-II
number: 2
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $2$
  B: $1$
  C: $\dfrac{2}{3}$
  D: $-1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设集合 $A=\{0,-a\}$, $B=\{1,a-2,2a-2\}$, 若 $A\subseteq B$, 则 $a=$

``````

---

## 097 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/03.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/03.md) · SHA a092ed5dd50458b15cc8e28661beb6c9193fb12c · mode 100644

``````markdown
---
id: 2023-II-03
paper_id: 2023-II
number: 3
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\text{C}_{400}^{45}\cdot \text{C}_{200}^{15}$ 种
  B: $\text{C}_{400}^{20}\cdot \text{C}_{200}^{40}$ 种
  C: $\text{C}_{400}^{30}\cdot \text{C}_{200}^{30}$ 种
  D: $\text{C}_{400}^{40}\cdot \text{C}_{200}^{20}$ 种
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

某学校为了解学生参加体育运动的情况, 用比例分配的分层随机抽样方法作抽样调查, 拟从初中部和高中部两层共抽取 $60$ 名学生, 已知该校初中部和高中部分别有 $400$ 名和 $200$ 名学生, 则不同的抽样结果共有

``````

---

## 098 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/04.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/04.md) · SHA cacf34c530db9c8551a798cd4f9fabb9a011f571 · mode 100644

``````markdown
---
id: 2023-II-04
paper_id: 2023-II
number: 4
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-1$
  B: $0$
  C: $\dfrac{1}{2}$
  D: $1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若 $f(x)=(x+a)\ln\dfrac{2x-1}{2x+1}$ 为偶函数, 则 $a=$

``````

---

## 099 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/05.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/05.md) · SHA 018381bf2fcf4c544b7a0825b512bba531992698 · mode 100644

``````markdown
---
id: 2023-II-05
paper_id: 2023-II
number: 5
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{2}{3}$
  B: $\dfrac{\sqrt{2}}{3}$
  C: $-\dfrac{\sqrt{2}}{3}$
  D: $-\dfrac{2}{3}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知椭圆 $C:\dfrac{x^2}{3}+y^2=1$ 的左, 右焦点分别为 $F_1$, $F_2$, 直线 $y=x+m$ 与 $C$ 交于 $A$, $B$ 两点, 若 $\triangle F_1AB$ 面积是 $\triangle F_2AB$ 面积的 $2$ 倍, 则 $m=$

``````

---

## 100 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/06.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/06.md) · SHA bce2baf1f157a10ea687ac5ce5fbb14746000112 · mode 100644

``````markdown
---
id: 2023-II-06
paper_id: 2023-II
number: 6
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\mathrm{e}^2$
  B: $\mathrm{e}$
  C: $\mathrm{e}^{-1}$
  D: $\mathrm{e}^{-2}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=a\mathrm{e}^x-\ln x$ 在区间 $(1,2)$ 上单调递增, 则 $a$ 的最小值为

``````

---

## 101 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/07.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/07.md) · SHA a2d123c3fbf61b7a68d536844ed99bb608ab1ddf · mode 100644

``````markdown
---
id: 2023-II-07
paper_id: 2023-II
number: 7
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{3-\sqrt{5}}{8}$
  B: $\dfrac{-1+\sqrt{5}}{8}$
  C: $\dfrac{3-\sqrt{5}}{4}$
  D: $\dfrac{-1+\sqrt{5}}{4}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $\alpha$ 为锐角, $\cos\alpha=\dfrac{1+\sqrt{5}}{4}$, 则 $\sin\dfrac{\alpha}{2}=$

``````

---

## 102 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/08.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/08.md) · SHA 2b4900b81343c9a6bf83aa7ee35885f4ee57a4f6 · mode 100644

``````markdown
---
id: 2023-II-08
paper_id: 2023-II
number: 8
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $120$
  B: $85$
  C: $-85$
  D: $-120$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $S_n$ 为等比数列 $\{a_n\}$ 的前 $n$ 项和, 若 $S_4=-5$, $S_6=21S_2$, 则 $S_8=$

``````

---

## 103 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/09.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/09.md) · SHA 0a6664edeea960d468b651a44f2c44ce8edf54fb · mode 100644

``````markdown
---
id: 2023-II-09
paper_id: 2023-II
number: 9
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 该圆锥的体积为 $\pi$
  B: 该圆锥的侧面积为 $4\sqrt{3}\pi$
  C: $AC=2\sqrt{2}$
  D: $\triangle PAC$ 的面积为 $\sqrt{3}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知圆锥的顶点为 $P$, 底面圆心为 $O$, $AB$ 为底面直径, $\angle APB=120^\circ$, $PA=2$, 点 $C$ 在底面圆周上, 且二面角 $P-AC-O$ 为 $45^\circ$, 则

``````

---

## 104 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/10.md) · SHA 57b6b6e9e16c3cfc770e56dbaac330578fa03af2 · mode 100644

``````markdown
---
id: 2023-II-10
paper_id: 2023-II
number: 10
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $p=2$
  B: $|MN|=\dfrac{8}{3}$
  C: 以 $MN$ 为直径的圆与 $l$ 相切
  D: $\triangle OMN$ 为等腰三角形
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设 $O$ 为坐标原点, 直线 $y=-\sqrt{3}(x-1)$ 过抛物线 $C:y^2=2px(p>0)$ 的焦点, 且与 $C$ 交于 $M$, $N$ 两点, $l$ 为 $C$ 的准线, 则

``````

---

## 105 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/11.md) · SHA 8c147b2cdff1c194ec2e87247c71bc119a7ddd1d · mode 100644

``````markdown
---
id: 2023-II-11
paper_id: 2023-II
number: 11
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $bc>0$
  B: $ab>0$
  C: $b^2+8ac>0$
  D: $ac<0$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若函数 $f(x)=a\ln x+\dfrac{b}{x}+\dfrac{c}{x^2}(a\ne0)$ 既有极大值也有极小值, 则

``````

---

## 106 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/12.md) · SHA 7d4cb29544e61b3c6c46cfe3b9192cb9bac2a607 · mode 100644

``````markdown
---
id: 2023-II-12
paper_id: 2023-II
number: 12
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 采用单次传输方案, 若依次发送 $1$, $0$, $1$, 则依次收到 $1$, $0$, $1$ 的概率为 $(1-\alpha)(1-\beta)^2$
  B: 采用三次传输方案, 若发送 $1$, 则依次收到 $1$, $0$, $1$ 的概率为 $\beta(1-\beta)^2$
  C: 采用三次传输方案, 若发送 $1$, 则译码为 $1$ 的概率为 $\beta(1-\beta)^2+(1-\beta)^3$
  D: 当 $0<\alpha<0.5$ 时, 若发送 $0$, 则采用三次传输方案译码为 $0$ 的概率大于采用单次传输方案译码为 $0$ 的概率
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在信道内传输 $0$, $1$ 信号, 信号的传输相互独立. 发送 $0$ 时, 收到 $1$ 的概率为 $\alpha(0<\alpha<1)$, 收到 $0$ 的概率为 $1-\alpha$; 发送 $1$ 时, 收到 $0$ 的概率为 $\beta(0<\beta<1)$, 收到 $1$ 的概率为 $1-\beta$. 考虑两种传输方案: 单次传输和三次传输. 单次传输是指每个信号只发送 $1$ 次, 三次传输是指每个信号重复发送 $3$ 次. 收到的信号需要译码, 译码规则如下: 单次传输时, 收到的信号即为译码; 三次传输时, 收到的信号中出现次数多的即为译码(例如, 若依次收到 $1$, $0$, $1$, 则译码为 $1$).

``````

---

## 107 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/13.md) · SHA d45e0027ccacad6e8a95e030d02062a311241eac · mode 100644

``````markdown
---
id: 2023-II-13
paper_id: 2023-II
number: 13
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知向量 $\boldsymbol{a}$, $\boldsymbol{b}$ 满足 $|\boldsymbol{a}-\boldsymbol{b}|=\sqrt{3}$, $|\boldsymbol{a}+\boldsymbol{b}|=|2\boldsymbol{a}-\boldsymbol{b}|$, 则 $|\boldsymbol{b}|=$ [填空].

``````

---

## 108 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/14.md) · SHA eafecfa560a4ecdc9ec9c17ed029e80180dcc565 · mode 100644

``````markdown
---
id: 2023-II-14
paper_id: 2023-II
number: 14
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

底面边长为 $4$ 的正四棱锥被平行于其底面的平面所截, 截去一个底面边长为 $2$, 高为 $3$ 的正四棱锥, 所得棱台的体积为 [填空].

``````

---

## 109 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/15.md) · SHA c92763e18353d85347e1845a48c28785511440f6 · mode 100644

``````markdown
---
id: 2023-II-15
paper_id: 2023-II
number: 15
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知直线 $l:x-my+1=0$ 与 $\odot C:(x-1)^2+y^2=4$ 交于 $A$, $B$ 两点, 写出满足 "$\triangle ABC$ 面积为 $\dfrac{8}{5}$" 的 $m$ 的一个值 [填空].

``````

---

## 110 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/16.md) · SHA 1e0b10fbd99981057c1f699a76e56dac962164ef · mode 100644

``````markdown
---
id: 2023-II-16
paper_id: 2023-II
number: 16
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/16-fig-01.png
  needs_confirmation: false
  notes: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=\sin(\omega x+\varphi)$, 如图, $A$, $B$ 是直线 $y=\dfrac{1}{2}$ 与曲线 $y=f(x)$ 的两个交点, 若 $|AB|=\dfrac{\pi}{6}$, 则 $f(\pi)=$ [填空].

![图 1](../assets/16-fig-01.png)

``````

---

## 111 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/17.md) · SHA e029682293fc96c5509031eeeb88a68930449402 · mode 100644

``````markdown
---
id: 2023-II-17
paper_id: 2023-II
number: 17
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $\triangle ABC$ 的内角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$, 已知 $\triangle ABC$ 的面积为 $\sqrt{3}$, $D$ 为 $BC$ 中点, 且 $AD=1$.

(1) 若 $\angle ADC=\dfrac{\pi}{3}$, 求 $\tan B$;

(2) 若 $b^2+c^2=8$, 求 $b$, $c$.

``````

---

## 112 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/18.md) · SHA 6e3428f8ae4155555bebff66d44d84686651d0ff · mode 100644

``````markdown
---
id: 2023-II-18
paper_id: 2023-II
number: 18
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $\{a_n\}$ 为等差数列, $b_n=\begin{cases}a_n-6, & n\text{为奇数},\\ 2a_n, & n\text{为偶数},\end{cases}$ 记 $S_n$, $T_n$ 分别为数列 $\{a_n\}$, $\{b_n\}$ 的前 $n$ 项和, $S_4=32$, $T_3=16$.

(1) 求 $\{a_n\}$ 的通项公式;

(2) 证明: 当 $n>5$ 时, $T_n>S_n$.

``````

---

## 113 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/19.md) · SHA de1bb5829dd650f05178fb3e43f2d246e69692e0 · mode 100644

``````markdown
---
id: 2023-II-19
paper_id: 2023-II
number: 19
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/19-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

某研究小组经过研究发现某种疾病的患病者与未患病者的某项医学指标有明显差异, 经过大量调查, 得到如下的患病者和未患病者该指标的频率分布直方图:

![图 1](../assets/19-fig-01.png)

利用该指标制定一个检测标准, 需要确定临界值 $c$, 将该指标大于 $c$ 的人判定为阳性, 小于或等于 $c$ 的人判定为阴性. 此检测标准的漏诊率是将患病者判定为阴性的概率, 记为 $p(c)$; 误诊率是将未患病者判定为阳性的概率, 记为 $q(c)$. 假设数据在组内均匀分布, 以事件发生的频率作为相应事件发生的概率.

(1) 当漏诊率 $p(c)=0.5\%$ 时, 求临界值 $c$ 和误诊率 $q(c)$;

(2) 设函数 $f(c)=p(c)+q(c)$, 当 $c\in[95,105]$ 时, 求 $f(c)$ 的解析式, 并求 $f(c)$ 在区间 $[95,105]$ 的最小值.

``````

---

## 114 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/20.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/20.md) · SHA e4312d7eef9858ba52e87344b3d2f6cfe1e77da4 · mode 100644

``````markdown
---
id: 2023-II-20
paper_id: 2023-II
number: 20
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/20-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, 三棱锥 $A-BCD$ 中, $DA=DB=DC$, $BD\perp CD$, $\angle ADB=\angle ADC=60^\circ$, $E$ 为 $BC$ 的中点.

![图 1](../assets/20-fig-01.png)

(1) 证明: $BC\perp DA$;

(2) 点 $F$ 满足 $\overrightarrow{EF}=\overrightarrow{DA}$, 求二面角 $D-AB-F$ 的正弦值.

``````

---

## 115 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/21.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/21.md) · SHA cda6028846bf220c3cdf18812d9a67d48a7a5a07 · mode 100644

``````markdown
---
id: 2023-II-21
paper_id: 2023-II
number: 21
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知双曲线 $C$ 的中心为坐标原点, 左焦点为 $(-2\sqrt{5},0)$, 离心率为 $\sqrt{5}$.

(1) 求 $C$ 的方程;

(2) 记 $C$ 的左, 右顶点分别为 $A_1$, $A_2$, 过点 $(-4,0)$ 的直线与 $C$ 的左支交于 $M$, $N$ 两点, $M$ 在第二象限, 直线 $MA_1$ 与 $NA_2$ 交于点 $P$, 证明: 点 $P$ 在定直线上.

``````

---

## 116 · mirror/gaokao-math-corpus/corpus/papers/2023/II/items/22.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2023/II/items/22.md) · SHA c24f77be8bb0b257598061f711634589088ecfc6 · mode 100644

``````markdown
---
id: 2023-II-22
paper_id: 2023-II
number: 22
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

(1) 证明: 当 $0<x<1$ 时, $x-x^2<\sin x<x$;

(2) 已知函数 $f(x)=\cos ax-\ln(1-x^2)$, 若 $x=0$ 是 $f(x)$ 的极大值点, 求 $a$ 的取值范围.

``````

---

## 117 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/01.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/01.md) · SHA 98cb24be1bc795cb2fd42b715513193e21fa396d · mode 100644

``````markdown
---
id: 2024-I-01
paper_id: 2024-I
number: 1
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\{-1,0\}$
  B: $\{2,3\}$
  C: $\{-3,-1,0\}$
  D: $\{-1,0,2\}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知集合 $A=\{x|-5<x^3<5\}$, $B=\{-3,-1,0,2,3\}$, 则 $A\cap B=$

``````

---

## 118 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/02.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/02.md) · SHA f0609dc91048345818d1a545bbde4c0351b84a60 · mode 100644

``````markdown
---
id: 2024-I-02
paper_id: 2024-I
number: 2
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-1-i$
  B: $-1+i$
  C: $1-i$
  D: $1+i$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若 $\dfrac{z}{z-1}=1+i$, 则 $z=$

``````

---

## 119 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/03.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/03.md) · SHA c095a185fb38cdf5c4b408fa251173caa1f70b5d · mode 100644

``````markdown
---
id: 2024-I-03
paper_id: 2024-I
number: 3
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-2$
  B: $-1$
  C: $1$
  D: $2$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知向量 $\boldsymbol{a}=(0,1)$, $\boldsymbol{b}=(2,x)$, 若 $\boldsymbol{b}\perp(\boldsymbol{b}-4\boldsymbol{a})$, 则 $x=$

``````

---

## 120 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/04.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/04.md) · SHA e4c4f870f6e495a7c6b374d4ead409a00f9c9647 · mode 100644

``````markdown
---
id: 2024-I-04
paper_id: 2024-I
number: 4
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-3m$
  B: $-\dfrac{m}{3}$
  C: $\dfrac{m}{3}$
  D: $3m$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $\cos(\alpha+\beta)=m$, $\tan\alpha\tan\beta=2$, 则 $\cos(\alpha-\beta)=$

``````

---

## 121 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/05.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/05.md) · SHA 148540bf24d78e083f7354b28424aa751c44f135 · mode 100644

``````markdown
---
id: 2024-I-05
paper_id: 2024-I
number: 5
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $2\sqrt{3}\pi$
  B: $3\sqrt{3}\pi$
  C: $6\sqrt{3}\pi$
  D: $9\sqrt{3}\pi$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知圆柱和圆锥的底面半径相等, 侧面积相等, 且它们的高均为 $\sqrt{3}$, 则圆锥的体积为

``````

---

## 122 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/06.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/06.md) · SHA 09d59b8d2ae74d818c94146f3376d82f8c7181fa · mode 100644

``````markdown
---
id: 2024-I-06
paper_id: 2024-I
number: 6
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $(-\infty,0]$
  B: $[-1,0]$
  C: $[-1,1]$
  D: $[0,+\infty)$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数
$$
f(x)=
\begin{cases}
-x^2-2ax-a, & x<0,\\
e^x+\ln(x+1), & x\ge 0
\end{cases}
$$
在 $\mathbb{R}$ 上单调递增, 则 $a$ 的取值范围是

``````

---

## 123 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/07.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/07.md) · SHA 74082719e69a5340fe92252c3e2de0b134d26f8c · mode 100644

``````markdown
---
id: 2024-I-07
paper_id: 2024-I
number: 7
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $3$
  B: $4$
  C: $6$
  D: $8$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

当 $x\in[0,2\pi]$ 时, 曲线 $y=\sin x$ 与 $y=2\sin\left(3x-\dfrac{\pi}{6}\right)$ 的交点个数为

``````

---

## 124 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/08.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/08.md) · SHA 775d55ad2275d28a3fd5e4cef43b436d58cd1eb3 · mode 100644

``````markdown
---
id: 2024-I-08
paper_id: 2024-I
number: 8
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $f(10)>100$
  B: $f(20)>1000$
  C: $f(10)<1000$
  D: $f(20)<10000$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)$ 的定义域为 $\mathbb{R}$, $f(x)>f(x-1)+f(x-2)$, 且当 $x<3$ 时 $f(x)=x$, 则下列结论中一定正确的是

``````

---

## 125 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/09.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/09.md) · SHA 0c5feeb1ca1ed3e0392c81e2a376b83618070881 · mode 100644

``````markdown
---
id: 2024-I-09
paper_id: 2024-I
number: 9
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $P(X>2)>0.2$
  B: $P(X>2)<0.2$
  C: $P(Y>2)>0.5$
  D: $P(Y>2)<0.8$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

随着“一带一路”国际合作的深入, 某茶叶种植区多措并举推动茶叶出口. 为了解推动出口后的亩收入(单位: 万元)情况, 从该种植区抽取样本, 得到推动出口后亩收入的样本均值 $\bar{x}=2.1$, 样本方差 $s^2=0.01$. 已知该种植区以往的亩收入 $X$ 服从正态分布 $N(1.8,0.1^2)$, 假设推动出口后的亩收入 $Y$ 服从正态分布 $N(\bar{x},s^2)$, 则

(若随机变量 $Z$ 服从正态分布 $N(\mu,\sigma^2)$, 则 $P(Z<\mu+\sigma)\approx0.8413$)

``````

---

## 126 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/10.md) · SHA 01a382e33c798b6f58c638c1a7a35af242b30209 · mode 100644

``````markdown
---
id: 2024-I-10
paper_id: 2024-I
number: 10
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $x=3$ 是 $f(x)$ 的极小值点
  B: 当 $0<x<1$ 时, $f(x)<f(x^2)$
  C: 当 $1<x<2$ 时, $-4<f(2x-1)<0$
  D: 当 $-1<x<0$ 时, $f(2-x)>f(x)$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设函数 $f(x)=(x-1)^2(x-4)$, 则

``````

---

## 127 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/11.md) · SHA 7b1a92120927c5392fae24fa04c2db3c1fbaad6c · mode 100644

``````markdown
---
id: 2024-I-11
paper_id: 2024-I
number: 11
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/11-fig-01.png
  needs_confirmation: false
  notes: []
options:
  A: $a=-2$
  B: 点 $(2\sqrt{2},0)$ 在 $C$ 上
  C: $C$ 在第一象限的点的纵坐标的最大值为 $1$
  D: 当点 $(x_0,y_0)$ 在 $C$ 上时, $y_0\le \dfrac{4}{x_0+2}$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设计一条美丽的丝带, 其造型可以看作图中的曲线 $C$ 的一部分.

![图 1](../assets/11-fig-01.png)

已知 $C$ 过坐标原点 $O$, 且 $C$ 上的点满足: 横坐标大于 $-2$; 到点 $F(2,0)$ 的距离与到定直线 $x=a(a<0)$ 的距离之积为 $4$. 则

``````

---

## 128 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/12.md) · SHA 36a745c7cc2f3e235a0ac6339d4205c4e1247b97 · mode 100644

``````markdown
---
id: 2024-I-12
paper_id: 2024-I
number: 12
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设双曲线 $C:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1(a>0,b>0)$ 的左、右焦点分别为 $F_1$, $F_2$. 过 $F_2$ 作平行于 $y$ 轴的直线交 $C$ 于 $A$, $B$ 两点. 若 $|F_1A|=13$, $|AB|=10$, 则 $C$ 的离心率为[填空].

``````

---

## 129 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/13.md) · SHA 958f0b0263d358fc8a20b1a2fd11256a9e29d701 · mode 100644

``````markdown
---
id: 2024-I-13
paper_id: 2024-I
number: 13
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

若曲线 $y=e^x+x$ 在点 $(0,1)$ 处的切线也是曲线 $y=\ln(x+1)+a$ 的切线, 则 $a=$[填空].

``````

---

## 130 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/14.md) · SHA 7956d01765783f76b673b2ac9496ad25b8ad4271 · mode 100644

``````markdown
---
id: 2024-I-14
paper_id: 2024-I
number: 14
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

甲、乙两人各有四张卡片, 每张卡片上标有一个数字, 甲的卡片上分别标有数字 $1,3,5,7$, 乙的卡片上分别标有数字 $2,4,6,8$. 两人进行四轮比赛. 在每轮比赛中, 两人各自从自己持有的卡片中随机选一张, 并比较所选卡片上数字的大小, 数字大的人得 $1$ 分, 数字小的人得 $0$ 分, 然后各自弃置此轮所选的卡片(弃置的卡片在此后的轮次中不能使用). 则四轮比赛后, 甲的总得分不小于 $2$ 的概率为[填空].

``````

---

## 131 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/15.md) · SHA 17e676266e96fc012cf2e1df611cbf75f71ba005 · mode 100644

``````markdown
---
id: 2024-I-15
paper_id: 2024-I
number: 15
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $\triangle ABC$ 的内角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$. 已知 $\sin C=\sqrt{2}\cos B$, $a^2+b^2-c^2=\sqrt{2}ab$.

(1) 求 $B$;

(2) 若 $\triangle ABC$ 的面积为 $3+\sqrt{3}$, 求 $c$.

``````

---

## 132 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/16.md) · SHA ce006dbdd808652f3225c3342f1de0372c191057 · mode 100644

``````markdown
---
id: 2024-I-16
paper_id: 2024-I
number: 16
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $A(0,3)$ 和 $P(3,\dfrac{3}{2})$ 为椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1(a>b>0)$ 上两点.

(1) 求 $C$ 的离心率;

(2) 若过 $P$ 的直线 $l$ 交 $C$ 于另一点 $B$, 且 $\triangle APB$ 的面积为 $9$, 求 $l$ 的方程.

``````

---

## 133 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/17.md) · SHA f89d178ecb43d6ea1374b8b1408680e992cdaedd · mode 100644

``````markdown
---
id: 2024-I-17
paper_id: 2024-I
number: 17
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/17-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, 四棱锥 $P-ABCD$ 中, $PA\perp$ 平面 $ABCD$, $PA=AC=2$, $BC=1$, $AB=\sqrt{3}$.

![图 1](../assets/17-fig-01.png)

(1) 若 $AD\perp PB$, 证明: $AD//$ 平面 $PBC$;

(2) 若 $AD\perp DC$, 且二面角 $A-CP-D$ 的正弦值为 $\dfrac{\sqrt{42}}{7}$, 求 $AD$.

``````

---

## 134 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/18.md) · SHA 19328d8a6a642f90275247594ec102e7d4c35326 · mode 100644

``````markdown
---
id: 2024-I-18
paper_id: 2024-I
number: 18
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
- label: (3)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=\ln\dfrac{x}{2-x}+ax+b(x-1)^3$.

(1) 若 $b=0$, 且 $f'(x)\ge0$, 求 $a$ 的最小值;

(2) 证明: 曲线 $y=f(x)$ 是中心对称图形;

(3) 若 $f(x)>-2$ 当且仅当 $1<x<2$, 求 $b$ 的取值范围.

``````

---

## 135 · mirror/gaokao-math-corpus/corpus/papers/2024/I/items/19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/I/items/19.md) · SHA 03f3729b37f848acc11c804d8edc89b17e09daf0 · mode 100644

``````markdown
---
id: 2024-I-19
paper_id: 2024-I
number: 19
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
- label: (3)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设 $m$ 为正整数, 数列 $a_1,a_2,\cdots,a_{4m+2}$ 是公差不为 $0$ 的等差数列, 若从中删去两项 $a_i$ 和 $a_j(i<j)$ 后剩余的 $4m$ 项可被平均分为 $m$ 组, 且每组的 $4$ 个数都能构成等差数列, 则称数列 $a_1,a_2,\cdots,a_{4m+2}$ 是 $(i,j)$-可分数列.

(1) 写出所有的 $(i,j)$, $1\le i<j\le6$, 使得数列 $a_1,a_2,\cdots,a_6$ 是 $(i,j)$-可分数列;

(2) 当 $m\ge3$ 时, 证明: 数列 $a_1,a_2,\cdots,a_{4m+2}$ 是 $(2,13)$-可分数列;

(3) 从 $1,2,\cdots,4m+2$ 中一次任取两个数 $i$ 和 $j(i<j)$, 记数列 $a_1,a_2,\cdots,a_{4m+2}$ 是 $(i,j)$-可分数列的概率为 $P_m$, 证明: $P_m>\dfrac{1}{8}$.

``````

---

## 136 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/01.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/01.md) · SHA 504ad966f0fd3e0a1e8adc4b92e7a909a23acf83 · mode 100644

``````markdown
---
id: 2024-II-01
paper_id: 2024-II
number: 1
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $0$
  B: $1$
  C: $\sqrt{2}$
  D: $2$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $z=-1-\mathrm{i}$, 则 $|z|=$

``````

---

## 137 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/02.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/02.md) · SHA 06aabd56b9c61fc0861a589f259a216fefd4433a · mode 100644

``````markdown
---
id: 2024-II-02
paper_id: 2024-II
number: 2
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $p$ 和 $q$ 都是真命题
  B: $\neg p$ 和 $q$ 都是真命题
  C: $p$ 和 $\neg q$ 都是真命题
  D: $\neg p$ 和 $\neg q$ 都是真命题
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知命题 $p:\forall x\in \mathbb{R}$, $|x+1|>1$; 命题 $q:\exists x>0$, $x^3=x$. 则

``````

---

## 138 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/03.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/03.md) · SHA 7a06b4fc16bc426487c735366a83a2c0e9f62b34 · mode 100644

``````markdown
---
id: 2024-II-03
paper_id: 2024-II
number: 3
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{1}{2}$
  B: $\dfrac{\sqrt{2}}{2}$
  C: $\dfrac{\sqrt{3}}{2}$
  D: $1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知向量 $\boldsymbol{a}$, $\boldsymbol{b}$ 满足 $|\boldsymbol{a}|=1$, $|\boldsymbol{a}+2\boldsymbol{b}|=2$, 且 $(\boldsymbol{b}-2\boldsymbol{a})\perp \boldsymbol{b}$, 则 $|\boldsymbol{b}|=$

``````

---

## 139 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/04.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/04.md) · SHA 0ed080e325e9a92468eac06e54b9e221e7f6e132 · mode 100644

``````markdown
---
id: 2024-II-04
paper_id: 2024-II
number: 4
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: table-01
  type: table
  path: ../assets/04-table-01.png
  needs_confirmation: false
  notes: []
options:
  A: $100$ 块稻田亩产量的中位数小于 $1050\ \mathrm{kg}$
  B: $100$ 块稻田中亩产量低于 $1100\ \mathrm{kg}$ 的稻田所占比例超过 $80\%$
  C: $100$ 块稻田亩产量的极差介于 $200\ \mathrm{kg}$ 至 $300\ \mathrm{kg}$ 之间
  D: $100$ 块稻田亩产量的平均值介于 $900\ \mathrm{kg}$ 至 $1000\ \mathrm{kg}$ 之间
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

某农业研究部门在面积相等的 $100$ 块稻田上种植一种新型水稻, 得到各块稻田的亩产量 (单位: $\mathrm{kg}$) 并整理得下表:

![表 1](../assets/04-table-01.png)

根据表中数据, 下列结论中正确的是

``````

---

## 140 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/05.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/05.md) · SHA c47594c0f8c22330b0043d5c54e0c9c4925e1f46 · mode 100644

``````markdown
---
id: 2024-II-05
paper_id: 2024-II
number: 5
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{x^2}{16}+\dfrac{y^2}{4}=1\ (y>0)$
  B: $\dfrac{x^2}{16}+\dfrac{y^2}{8}=1\ (y>0)$
  C: $\dfrac{y^2}{16}+\dfrac{x^2}{4}=1\ (y>0)$
  D: $\dfrac{y^2}{16}+\dfrac{x^2}{8}=1\ (y>0)$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知曲线 $C:x^2+y^2=16\ (y>0)$, 从 $C$ 上任意一点 $P$ 向 $x$ 轴作垂线段 $PP'$, $P'$ 为垂足, 则线段 $PP'$ 的中点 $M$ 的轨迹方程为

``````

---

## 141 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/06.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/06.md) · SHA fcddab924950f78bda0e225399870f4cae921096 · mode 100644

``````markdown
---
id: 2024-II-06
paper_id: 2024-II
number: 6
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $-1$
  B: $\dfrac{1}{2}$
  C: $1$
  D: $2$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设函数 $f(x)=a(x+1)^2-1$, $g(x)=\cos x+2ax$. 当 $x\in(-1,1)$ 时, 曲线 $y=f(x)$ 与 $y=g(x)$ 恰有一个交点. 则 $a=$

``````

---

## 142 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/07.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/07.md) · SHA f2be8aea9b26813932bd167679dda00992eeefda · mode 100644

``````markdown
---
id: 2024-II-07
paper_id: 2024-II
number: 7
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{1}{2}$
  B: $1$
  C: $2$
  D: $3$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知正三棱台 $ABC-A_1B_1C_1$ 的体积为 $\dfrac{52}{3}$, $AB=6$, $A_1B_1=2$, 则 $A_1A$ 与平面 $ABC$ 所成角的正切值为

``````

---

## 143 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/08.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/08.md) · SHA e04a60df90ee175a0ff1128cfe6fa09bebc3b506 · mode 100644

``````markdown
---
id: 2024-II-08
paper_id: 2024-II
number: 8
type: mcq_single_answer
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $\dfrac{1}{8}$
  B: $\dfrac{1}{4}$
  C: $\dfrac{1}{2}$
  D: $1$
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设函数 $f(x)=(x+a)\ln(x+b)$. 若 $f(x)\geqslant 0$, 则 $a^2+b^2$ 的最小值为

``````

---

## 144 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/09.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/09.md) · SHA 675af501c47463246d468becec261acd4892d0f6 · mode 100644

``````markdown
---
id: 2024-II-09
paper_id: 2024-II
number: 9
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $f(x)$ 与 $g(x)$ 有相同的零点
  B: $f(x)$ 与 $g(x)$ 有相同的最大值
  C: $f(x)$ 与 $g(x)$ 有相同的最小正周期
  D: $f(x)$ 与 $g(x)$ 的图象有相同的对称轴
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

对于函数 $f(x)=\sin 2x$ 和 $g(x)=\sin(2x-\dfrac{\pi}{4})$, 下列说法中正确的有

``````

---

## 145 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/10.md) · SHA 3623b9b14b53ef9932a1024dace27aa7b3a7cb10 · mode 100644

``````markdown
---
id: 2024-II-10
paper_id: 2024-II
number: 10
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: $l$ 与 $\odot A$ 相切
  B: 当 $P$, $A$, $B$ 三点共线时, $|PQ|=\sqrt{15}$
  C: 当 $|PB|=2$ 时, $PA\perp AB$
  D: 满足 $|PA|=|PB|$ 的点 $P$ 有且仅有 $2$ 个
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

抛物线 $C:y^2=4x$ 的准线为 $l$, $P$ 为 $C$ 上动点. 过 $P$ 作 $\odot A:x^2+(y-4)^2=1$ 的一条切线, $Q$ 为切点. 过 $P$ 作 $l$ 的垂线, 垂足为 $B$. 则

``````

---

## 146 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/11.md) · SHA 44be278b6513c5ecd856cf6f8fb8b8491ecc5020 · mode 100644

``````markdown
---
id: 2024-II-11
paper_id: 2024-II
number: 11
type: mcq_multiple_answers
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
options:
  A: 当 $a>1$ 时, $f(x)$ 有三个零点
  B: 当 $a<0$ 时, $x=0$ 是 $f(x)$ 的极大值点
  C: 存在 $a$, $b$, 使得 $x=b$ 为曲线 $y=f(x)$ 的对称轴
  D: 存在 $a$, 使得点 $(1,f(1))$ 为曲线 $y=f(x)$ 的对称中心
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

设函数 $f(x)=2x^3-3ax^2+1$, 则

``````

---

## 147 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/12.md) · SHA 5ec68a5817049ed89fc97e69145a5457e52b647b · mode 100644

``````markdown
---
id: 2024-II-12
paper_id: 2024-II
number: 12
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $S_n$ 为等差数列 $\{a_n\}$ 的前 $n$ 项和. 若 $a_3+a_4=7$, $3a_2+a_5=5$, 则 $S_{10}=$ [填空].

``````

---

## 148 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/13.md) · SHA 3fca875eeca761454ae198610c15a590fae96bad · mode 100644

``````markdown
---
id: 2024-II-13
paper_id: 2024-II
number: 13
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知 $\alpha$ 为第一象限角, $\beta$ 为第三象限角, $\tan\alpha+\tan\beta=4$, $\tan\alpha\tan\beta=\sqrt{2}+1$, 则 $\sin(\alpha+\beta)=$ [填空].

``````

---

## 149 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/14.md) · SHA c468f1b060f61b1035f0d3606997393169a46765 · mode 100644

``````markdown
---
id: 2024-II-14
paper_id: 2024-II
number: 14
type: fill_blank
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: table-01
  type: table
  path: ../assets/14-table-01.png
  needs_confirmation: false
  notes: []
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

在右图的 $4\times 4$ 的方格表中选 $4$ 个方格, 要求每行和每列均恰有一个方格被选中, 则共有 [填空] 种选法. 在所有符合上述要求的选法中, 选中方格中的 $4$ 个数之和的最大值是 [填空].

![表 1](../assets/14-table-01.png)

``````

---

## 150 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/15.md) · SHA a4a6ebc83a5d3ed0925a2612994e3cee193339ff · mode 100644

``````markdown
---
id: 2024-II-15
paper_id: 2024-II
number: 15
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

记 $\triangle ABC$ 的内角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$, 已知 $\sin A+\sqrt{3}\cos A=2$.

(1) 求 $A$;

(2) 若 $a=2$, $\sqrt{2}b\sin C=c\sin 2B$, 求 $\triangle ABC$ 的周长.

``````

---

## 151 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/16.md) · SHA f96166058dcf78b3496bf6a6dda7bcb61878c439 · mode 100644

``````markdown
---
id: 2024-II-16
paper_id: 2024-II
number: 16
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知函数 $f(x)=e^x-ax-a^3$.

(1) 当 $a=1$ 时, 求曲线 $y=f(x)$ 在点 $(1,f(1))$ 处的切线方程;

(2) 若 $f(x)$ 有极小值, 且极小值小于 $0$, 求 $a$ 的取值范围.

``````

---

## 152 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/17.md) · SHA 428ae570bbed12f91c1851821b168175aa45381e · mode 100644

``````markdown
---
id: 2024-II-17
paper_id: 2024-II
number: 17
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets:
- id: fig-01
  type: figure
  path: ../assets/17-fig-01.png
  needs_confirmation: false
  notes: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

如图, 平面四边形 $ABCD$ 中, $AB=8$, $CD=3$, $AD=5\sqrt{3}$, $\angle ADC=90^\circ$, $\angle BAD=30^\circ$, 点 $E$, $F$ 满足 $\overrightarrow{AE}=\dfrac{2}{5}\overrightarrow{AD}$, $\overrightarrow{AF}=\dfrac{1}{2}\overrightarrow{AB}$. 将 $\triangle AEF$ 沿 $EF$ 翻折至 $\triangle PEF$, 使得 $PC=4\sqrt{3}$.

![图 1](../assets/17-fig-01.png)

(1) 证明: $EF\perp PD$;

(2) 求面 $PCD$ 与面 $PBF$ 所成的二面角的正弦值.

``````

---

## 153 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/18.md) · SHA 81244967a118640173ff6863f6016970d7327f02 · mode 100644

``````markdown
---
id: 2024-II-18
paper_id: 2024-II
number: 18
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

某投篮比赛分为两个阶段, 每个参赛队由两名队员组成. 比赛具体规则如下: 第一阶段由参赛队中一名队员投篮 $3$ 次, 若 $3$ 次都未投中, 则该队被淘汰, 比赛成绩为 $0$ 分; 若至少投中 $1$ 次, 则该队进入第二阶段. 第二阶段由该队的另一名队员投篮 $3$ 次, 每次投篮投中得 $5$ 分, 未投中得 $0$ 分, 该队的比赛成绩为第二阶段的得分总和.

某参赛队由甲, 乙两名队员组成, 设甲每次投中的概率为 $p$, 乙每次投中的概率为 $q$, 各次投中与否相互独立.

(1) 若 $p=0.4$, $q=0.5$, 甲参加第一阶段比赛, 求甲, 乙所在队的比赛成绩不少于 $5$ 分的概率;

(2) 假设 $0<p<q$.

(i) 为使得甲, 乙所在队的比赛成绩为 $15$ 分的概率最大, 应该由谁参加第一阶段比赛?

(ii) 为使得甲, 乙所在队的比赛成绩的数学期望最大, 应该由谁参加第一阶段比赛?

``````

---

## 154 · mirror/gaokao-math-corpus/corpus/papers/2024/II/items/19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/corpus/papers/2024/II/items/19.md) · SHA 2a5b685a4d8127850691fde49c24521190c6b6b9 · mode 100644

``````markdown
---
id: 2024-II-19
paper_id: 2024-II
number: 19
type: solution
status: approved
needs_confirmation: false
uncertain_notes: []
assets: []
subquestions:
- label: (1)
- label: (2)
- label: (3)
annotation:
  status: not_started
  problem_kind: null
  primary_knowledge_point: null
  notes: []
---

已知双曲线 $C:x^2-y^2=m\ (m>0)$, 点 $P_1(5,4)$ 在 $C$ 上, $k$ 为常数, $0<k<1$. 按照如下方式依次构造点 $P_n(n=2,3,\cdots)$: 过 $P_{n-1}$ 作斜率为 $k$ 的直线与 $C$ 的左支交于点 $Q_{n-1}$, 令 $P_n$ 为 $Q_{n-1}$ 关于 $y$ 轴的对称点. 记 $P_n$ 的坐标为 $(x_n,y_n)$.

(1) 若 $k=\dfrac{1}{2}$, 求 $x_2$, $y_2$;

(2) 证明: 数列 $\{x_n-y_n\}$ 是公比为 $\dfrac{1+k}{1-k}$ 的等比数列;

(3) 设 $S_n$ 为 $\triangle P_nP_{n+1}P_{n+2}$ 的面积. 证明: 对任意正整数 $n$, $S_n=S_{n+1}$.

``````

---

## 155 · mirror/gaokao-math-corpus/docs/DATA_FORMAT.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/docs/DATA_FORMAT.md) · SHA b9f42b628f7b25e7cd4b57125e55ddf35e4bf3b8 · mode 100644

``````markdown
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

``````

---

## 156 · mirror/gaokao-math-corpus/docs/DATA_LAYERS.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/docs/DATA_LAYERS.md) · SHA 90c315e26865201099948f87a78cec497d3ca514 · mode 100644

``````markdown
# Data Layers

本项目把数据分为五层。仓库中的 Markdown、YAML 和图片文件是权威数据源；数据库、索引、统计和发布包都是可重新生成的衍生产物。

## 1. 原始输入

原始输入包括：

- 官方或社区来源的试卷 PDF
- 社区排版文件
- 页面截图或页面图片
- OCR 临时结果
- 转录过程中的中间文件

是否提交 Git：不提交。

是否可重新生成：不一定。放入工作目录用于处理的来源默认已经过维护者检查，项目不区分官方来源、社区排版来源和人工校对来源。

建议位置：`work/` 或仓库外部本地目录。仓库配置中不得保存本地绝对路径。

## 2. 数据清洗后的权威语料

权威语料只保存可从试卷直接确认的客观内容，以及项目根据明确规则推导的基础元数据。

包括：

- 试卷年份、卷种和试卷类别
- `paper_scheme_id`
- 题号和题型
- 题干原文
- 选择题或多选题选项
- 填空内容
- 解答题各小题的题目内容
- 题目中的原图裁剪、表格裁剪和必要说明
- 转录状态和待确认事项

不包括：

- 答案、解析和解法
- 知识点、板块、难度、教学用途、相似题关系等描述性内容
- 手工识别的页面分值

是否提交 Git：提交。

是否可重新生成：不可完全自动重新生成。它是人工转录、审阅和修订后的权威数据源。

建议位置：`corpus/`。

## 3. 审阅与描述性标注

审阅与描述性标注在题面转录完成并通过审核后进行。审核可以由人工或 Agent 执行, 两者具有同等效力。

题面审核关注：

- 转录是否忠实于原卷
- 公式、选项、原图裁剪和表格裁剪是否准确
- 模糊内容是否被正确标记
- 禁止字段是否未进入数据清洗层

描述性标注当前只保留最粗略范围：

- 题目种类
- 主要知识点

是否提交 Git：提交，但必须写在题目文件的独立 `annotation` 区域，并记录标注状态。

是否可重新生成：不可视为完全可重新生成。题面审核和描述性标注都需要依据原始输入进行审核, 但不在数据中区分人工 review 与 Agent review。

## 4. 构建产物

构建产物由权威语料和配置文件确定性生成。

包括：

- SQLite 数据库
- 全文索引
- 统计文件
- 校验报告
- 静态网页中间产物

是否提交 Git：不提交。

是否可重新生成：可以。正式 CLI 应确定性生成，不调用 LLM，不依赖在线模型服务。

建议位置：`build/`。

## 5. 发布产物

发布产物用于对外分发。

包括：

- 静态网站发布版本
- 压缩包
- 数据快照
- 面向下游使用者的导出文件

是否提交 Git：通常不提交，必要时通过 release 或发布系统分发。

是否可重新生成：可以。发布产物应从已提交的语料、配置、schema 和确定性构建流程生成。

建议位置：`dist/`。

``````

---

## 157 · mirror/gaokao-math-corpus/docs/PROJECT_SCOPE.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/docs/PROJECT_SCOPE.md) · SHA 89eaa3a615c5faec09d857e6f285acd69e6f999a · mode 100644

``````markdown
# Project Scope

## 项目目标

本项目建设一个公开的“新高考数学试题知识库”，以 Markdown、YAML 和图片文件保存可人工审阅、可版本管理、可由程序重新构建的题目语料。

项目首先关注题面语料本身：把试卷中的题干、选项、填空、解答题小题、图形、表格和必要说明整理成结构化文本。完成题面转录和审核后，再进入独立的描述性标注阶段。

## 当前收录范围

第一阶段收录 2021--2026 年的新高考数学全国卷：

- 新高考全国 I 卷
- 新高考全国 II 卷

试卷类别必须在开始录入时明确标记。当前使用两个新高考结构版本：

- `new_gaokao_legacy`：2021--2023 年结构，共 22 题。单项选择题 8 道，多项选择题 4 道，填空题 4 道，均为每题 5 分；解答题 6 道，第 17 题 10 分，第 18--22 题每题 12 分。
- `new_gaokao_current`：2024--2026 年结构，共 19 题。单项选择题 8 道，每题 5 分；多项选择题 3 道，每题 6 分；填空题 3 道，每题 5 分；第 15 题 13 分，第 16--17 题每题 15 分，第 18--19 题每题 17 分。

结构标识保留 `new_gaokao`，为以后扩展老高考试卷或其他系列预留空间。

## 暂不收录的内容

当前阶段暂不收录或不设计以下内容：

- 标准答案
- 题解、解析、解题过程和推荐解法
- 真实试题的大规模转录
- 完整知识点分类体系
- 难度、思维类型、教学用途、相似题关系
- SQLite 数据库、全文索引、向量索引
- 静态网站、发布压缩包和 MCP 服务
- 完整自动化转录流水线
- 依赖外部 LLM API 的流程

## 原始试卷与整理后语料

原始 PDF、社区排版文件、页面截图、OCR 结果和处理中间文件属于原始输入或工作文件，不提交到 Git 仓库。

整理后的题目全文、必要的原图裁剪文件、数据格式、配置和说明文档可以公开提交到 Git 仓库。仓库中的 Markdown、YAML 和图片文件是权威数据源。

不区分不同来源类别。放入工作目录用于处理的来源默认已经过维护者检查。整理过程应记录转录状态和待确认事项，但不得把本地绝对路径写入仓库配置。

## 预期用途

本项目面向三类查询和使用场景：

- 人类查询：教师、学生或维护者可以直接阅读 Markdown 题面和审阅记录。
- 程序查询：确定性 CLI 可以从权威文件生成 SQLite、全文索引、统计文件、静态网页和发布包。
- 未来 Agent 查询：Agent 可以基于明确的数据格式和审阅状态检索题面、定位疑点。当前 Agent review 和 Agent annotation 尚未实现，描述性标注仍由人工完成；未来引入 Agent 时，也不得把未经确认的生成内容写入题面字段。

## Agent 使用原则

建设阶段可以使用 Codex agent 辅助转录、初步整理、代码生成和审阅。agent 任务应按工作类型选择刚好足够的模型和推理强度：页面转录/OCR 默认使用较小模型和较低推理强度，只有复杂图形、密集公式或审阅争议需要时再升档。

批量调度脚本可以继承环境变量中的代理设置，或读取 Windows 系统代理以减少超时重试。仓库配置不得保存本地代理地址、认证信息或其他机器专属网络设置。

``````

---

## 158 · mirror/gaokao-math-corpus/docs/REPOSITORY_LAYOUT.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/docs/REPOSITORY_LAYOUT.md) · SHA 779ce8f3ed310442f73e6893305659861229729a · mode 100644

``````markdown
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

``````

---

## 159 · mirror/gaokao-math-corpus/docs/REVIEW_WORKFLOW.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/docs/REVIEW_WORKFLOW.md) · SHA 946e44031ffff8c084f61539a012f6606f321d78 · mode 100644

``````markdown
# Review Workflow

本项目把题面审核和知识标注审核分开。题面流程使用一个统一的 `status` 字段表示转录和审核状态。

本文件描述的是 Agent review 的流程，本项目也支持人工 review 。不区分人工 review 与 Agent review 的效力。

## Overall Workflow

1. 整份试卷一次性转录。
2. 自动格式检查。
3. 使用新的独立会话对照原图检查。
4. 汇总疑点。
5. 修正错误。
6. 人工抽样复核或必要时逐题确认。
7. 完成题面审核。
8. 再进入粗粒度知识标注阶段。

## 1. 整份试卷一次性转录

一份试卷的页面数量较少，默认通过一个独立的 `codex exec` 会话提交该试卷的全部页面图片。这样可以减少会话启动开销，并让跨页题目、题号连续性和试卷级元数据在同一上下文中处理。

维护者脚本可以对每份试卷调度一个独立会话。只有在维护者显式指定页面范围进行局部重跑时，才提交页面子集。

批量调度应默认使用刚好足够的模型和较低推理强度；页面 OCR 不应默认使用高推理强度。脚本可以继承环境变量或系统代理，降低超时重试概率，但代理地址不得写入仓库配置。

转录会话只负责：

- 识别页面中可直接确认的题面内容。
- 修改目标 Markdown、YAML 和必要原图裁剪文件。
- 标记模糊文字、公式、图形和表格。
- 在已提交的同一份试卷页面之间处理跨页题目；不得根据未提交页面或题型习惯补全内容。
- 题目正文、选项和说明文字使用西文风格标点符号。
- 不添加答案、解析、知识点、难度或解题方法。

Codex 应直接修改目标文件，不在最终回复中重复输出完整题目。

## 2. 自动格式检查

转录后执行与当前文件格式相称的确定性检查，例如：

- YAML front matter 是否可解析。
- 必需字段是否存在。
- 题号是否重复。
- 题号与 `paper_scheme_id` 是否匹配。
- 图片引用是否指向同一试卷目录下的 `assets/`。
- 是否出现禁止字段，如答案、解析、手工分值、难度或解题方法。
- 题面审核完成前，`annotation` 是否仍为 `not_started`。

正式 CLI 应保持确定性，不调用 LLM，不依赖在线模型服务。

## 3. 独立会话对照原图检查

题面审阅任务应与转录任务分开。审阅可以由人工或 Agent 执行, 两者具有同等效力, 结果都更新同一个 `status` 字段。

审阅会话对照原图或页面截图检查：

- 题干文字是否完整。
- 公式和符号是否准确。
- 选项顺序和内容是否准确。
- 小题编号和内容是否准确。
- 原图裁剪和表格裁剪是否完整、清晰、对应正确。
- 待确认标记是否充分。

审阅图形或表格资产时，应确认裁剪范围没有包含整页、相邻题目或大段无关留白，并确认所有必要标注仍可辨认。

## 4. 汇总疑点

所有无法确认的问题应集中记录在题目级 `uncertain_notes` 或试卷级 `uncertain_notes` 中。

疑点应具体说明位置和原因，例如：

- 某页某题某个公式上标不清。
- 图形中某条辅助线是否存在待确认。
- 表格某个单元格数字模糊。
- 页面疑似跨页，需要相关页面一并处理。

## 5. 修正错误

应直接修正题面文件，并保留必要的审阅状态更新。

不得用未确认的猜测替代待确认标记。无法确认的问题应继续保留。

## 6. 人工抽样复核或逐题确认

维护者会手动抽样复核；对于高风险题目，可逐题确认。

建议逐题确认的情况：

- 公式密集。
- 图形或表格复杂。
- 曾触发跨页错误。
- OCR 或页面质量较差。

## 7. 完成题面审核

题面审核完成表示：

- 题面字段已对照原卷核对。
- 禁止字段未进入数据清洗层。
- 待确认事项要么已解决，要么已明确保留。
- 图片和表格裁剪可追溯。
- 自动检查通过。

题面审核完成不表示知识点已经审核。

## 8. 描述性标注阶段

题面审核完成后，才进入粗粒度知识标注阶段。

该阶段只加入：

- 题目种类
- 主要知识点

描述性标注必须写在题目文件的 `annotation` 区域，并记录标注状态。暂不设计题目形式特征、能力维度、难度、解题方法、相似题关系或次要知识点。

## 题面审核与知识标注审核

题面审核回答的问题是：题目是否被忠实、完整、可追溯地转录。

知识标注审核回答的问题是：`annotation.problem_kind` 和 `annotation.primary_knowledge_point` 是否符合项目定义、是否一致、是否经过审核。审核执行者不作为状态字段或数据层级的一部分。

两类审核不得混用。未经题面审核的题目不应进入正式知识标注。

``````

---

## 160 · mirror/gaokao-math-corpus/docs/SCORING_RULES.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/docs/SCORING_RULES.md) · SHA 026a2e847a6cc3e3c65f1c5061a5983345787a12 · mode 100644

``````markdown
# Paper Scheme And Scoring Rules

本项目不从试卷页面或社区排版文件中识别题目分值。分值由试卷采用的 `paper_scheme` 和题号统一推导。

## Core Principles

- 不从页面 OCR 分值。
- 不转录社区试卷页面中的分值。
- 不在题目文件中手工填写分值。
- 每张试卷在开始录入时必须显式标记 `paper_scheme_id`。
- `paper_scheme` 同时描述题号覆盖、题型和计分规则。
- 2021--2023 与 2024--2026 使用两套不同的 `paper_scheme`。
- 校验器以后需要检查总分、题号覆盖和规则冲突。

## Confirmed Paper Schemes

当前录入的试卷包含两种新高考方案。

### `new_gaokao_legacy`

适用年份：2021--2023。

总题数：22。

规则：

- 第 1--8 题：单项选择题，每题 5 分。
- 第 9--12 题：多项选择题，每题 5 分。
- 第 13--16 题：填空题，每题 5 分。
- 第 17 题：解答题，10 分。
- 第 18--22 题：解答题，每题 12 分。

### `new_gaokao_current`

适用年份：2024--2026，并作为当前新高考结构继续使用。

总题数：19。

规则：

- 第 1--8 题：单项选择题，每题 5 分。
- 第 9--11 题：多项选择题，每题 6 分。
- 第 12--14 题：填空题，每题 5 分。
- 第 15 题：解答题，13 分。
- 第 16--17 题：解答题，每题 15 分。
- 第 18--19 题：解答题，每题 17 分。

## Paper Reference

每张试卷通过 `paper_scheme_id` 引用一个方案：

```yaml
paper:
  year: 2024
  volume: I
  paper_scheme_id: "new_gaokao_current"
```

## Validation Requirements

未来校验器需要检查：

- 每张试卷是否引用了合法 `paper_scheme`。
- `paper_scheme` 是否覆盖全部题号。
- 题号区间是否重叠或冲突。
- 推导出的总分是否符合已确认规则。
- 题目文件中的 `type` 是否与 `paper_scheme` 推导结果一致。
- 是否出现手工填写的题目分值。

校验器必须是确定性的，不调用 LLM，不依赖在线模型服务。

``````

---

## 161 · mirror/gaokao-math-corpus/docs/TRANSCRIPTION_RULES.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-corpus/docs/TRANSCRIPTION_RULES.md) · SHA 1f4145da99c1d9b04fbb4597fa917f5ca4818fd5 · mode 100644

``````markdown
# Transcription Rules

本文件规定从试卷页面转录为 Markdown 和 LaTeX 的基本规则。当前阶段只处理题面，不添加答案、解析、知识点、难度或解题方法。

## 忠实转录

- 保留中文原文、题干结构和必要说明。
- 只做必要的 Markdown 和 LaTeX 格式化。
- 题目正文、选项和说明文字统一使用西文风格标点符号，例如 `, . ; : ? ! ( )`；数学公式按 LaTeX 习惯处理。
- 不自行改写题意，不把口语化说明改成解释性文字。
- 发现无法确认的文字、公式、图形或表格时，必须标记为 `待确认` 。
- 注意观察原文的向量字母是否使用粗体，保持与原文一致，粗体使用`\boldsymbol`处理。
- 表示排列数和组合数的大写`A`和`C`需要写成直体，使用`\text`处理；但表示几何对象和表示数列和的大写字母等不需要使用`\text`处理。

## 数学公式

- 行内公式使用 `$...$`。
- 独立公式使用 `$$...$$`。
- 分段函数要使用 `cases` 环境
- Markdown 正文中的 LaTeX 命令使用单反斜杠, 例如 `\dfrac`, `\sqrt`, `\mathbb`; 不得写成 `\\dfrac`, `\\sqrt`, `\\mathbb`。
- YAML front matter 中含 LaTeX 的选项或字段优先使用单引号字符串。
- 尽量保留原卷符号、变量、上下标、括号和排列顺序。
- 不把原卷没有给出的推导步骤、等价变形或答案写入题面。
- 公式中无法确认的字符使用明确占位并记录疑点，例如 `[待确认：上标]`。

## 选项格式

选择题和多选题选项按 `A`、`B`、`C`、`D` 等原有顺序记录，例如：

```yaml
options:
  A: "选项 A 原文"
  B: "选项 B 原文"
  C: "选项 C 原文"
  D: "选项 D 原文"
```

不得标记正确选项。

## 小题格式

解答题小题按原卷编号保留，例如：

```markdown
(1) 小题原文。

(2) 小题原文。
```

结构化字段中使用 `label: "(1)"`、`label: "(2)"`。不得补写解答过程。

## 图形引用

- 题目中出现图形时，应在题面中保留图形引用。
- 图形暂时使用原图裁剪，不重绘。
- 如果图片是由多张子图片构成的，占据一整行，可以将多张子图片截在一个图片文件中，不必对每张子图片分别裁切，但截在同一张图片里时会包含题目文本等额外信息的情况除外。
- 裁剪后的图片提交到对应试卷目录的 `assets/`。
- 图形裁剪范围、编号或内容无法确认时，必须在题目疑点中标记，后续交给review处理。
- 裁剪范围应先定位图形主体外接范围，再加入适中边距。
- 统一使用 `uv run python tools/crop_asset.py SOURCE OUTPUT --box LEFT TOP RIGHT BOTTOM`, 坐标单位为源页面图片像素, 顺序为左、上、右、下。应先确定一个裁剪框, 再调用固定工具执行; 不得寻找其他裁剪方法。
- 裁剪后的图片应保留坐标轴、刻度、点名、线段标注、图例、单位和理解图形所必需的说明文字。
- 裁剪图形时避免包含整页、大段无关留白或页眉页脚，但为了尽可能保留图形信息可以适当包含。
- 裁剪后至多只检查两次图形是否清晰完整，在review阶段可调整，但必须检查是否与题号对应、是否被正文正确引用。

建议引用：

```markdown
![图 1](../assets/01-fig-01.png)
```

## 表格处理

- 表格使用原图裁剪，不转写为 Markdown 表格。
- 裁剪后的表格图片提交到对应试卷目录的 `assets/`。
- 表格裁剪范围或内容无法确认时，必须在题目疑点中标记，后续交给 review 处理。
- 表格同样使用 `tools/crop_asset.py` 按源图像像素坐标裁剪, 不得寻找其他截图方法。
- 裁剪范围应完整包含表头、行列标签、表内文字、数字、单位和边框关系，并在外侧保留适中边距。必须包含完整的表格外框线。
- 裁剪表格时避免包含相邻题干、大段无关留白或页眉页脚，但为了尽可能保留表格要素时可以包含。
- 裁剪后只检查一次清晰度、完整性，重点检查是否保留表格外框线。
- 必须检查编号对应关系和正文引用路径。

建议引用：

```markdown
![表 1](../assets/01-table-01.png)
```

## 模糊字符处理

遇到无法辨认的内容时：

- 在题面中使用明确占位，例如 `[待确认：字符]`、`[待确认：公式]`、`[待确认：图形]`、`[待确认：表格]`。
- 在 `uncertain_notes` 中说明位置和原因。
- 不用相似字、常见公式或题目经验替代原文。

## 分值处理

- 忽略页面或社区排版文件中出现的题目分值。
- 不从页面 OCR 分值。
- 不在题目文件中手工填写分值。
- 分值以后由 `paper_scheme` 和题号统一推导。

## Agent 模型与代理

- 页面转录/OCR 默认使用刚好足够的模型和较低推理强度，避免为常规识别任务消耗过多 token。
- 转录脚本可以继承 `HTTPS_PROXY`、`HTTP_PROXY`、`ALL_PROXY` 等环境变量，或读取 Windows/WinINET 系统代理；不得把本地代理地址写入仓库文件。
- 如果 Windows/WinINET 设置没有暴露可读取的代理字符串，应在运行脚本时显式传入 `--proxy`。

``````

---

## 162 · mirror/gaokao-math-problems-compilation/CONTRIBUTORS.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-problems-compilation/CONTRIBUTORS.md) · SHA 9702f991528bc1f08362f9e82346ec04d9f8f1d7 · mode 100644

``````markdown
# Contributors

- [iwaxi](https://github.com/iwaxi)

``````

---

## 163 · mirror/gaokao-math-problems-compilation/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokao-math-problems-compilation/README.md) · SHA 9c34dd949390af4cbdc68c1fc298eb7965e7d0a9 · mode 100644

``````markdown
# 高考数学题库

本代码库包含生成题目版和答案版 PDF 所需的 LaTeX 源文件、索引、题图、重绘图源和布局表。

Git 仓库仅收录源码和必要题图；成品 PDF 可从 [Releases](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/releases) 下载，也可按以下说明自行编译。

## 当前版本：答案与解析补全（2026-10-04）

- 同步开发仓已完成的答案回填成果，补充详细解析，并修正相关题干、题图和排版。
- 新增 1994 年旧科目组文科、理科试卷，各 25 题；与已有新科目组试卷一并收录。
- 重写 2024 年上海春考解析，补回第 16 题遗漏命题；第 11 题采用补充相切条件的修订题面，原题条件差异在解析中说明。
- 补回 1987 年广东理科第 22 题选项图、1990 年广东理科第 12 题原图，修正 2023 年全国甲卷理科解析的嵌套编号排版。

答案回填完成不代表重新独立审核了全书每一道题。原题版本冲突、条件修订或选项不匹配等情况，以对应题目的说明与解析为准。

## 仓库内容

仅发布 `content/` 正文、`index/` 索引、`img/` 必要题图、`img_repaint/` 重绘 TeX，以及根目录编译和排版文件。`tools/` 中仅保留编译直接读取的两份 TeX 图片布局表，不包含开发脚本、任务队列或状态文件。

Git 仓库不收录成品 PDF、原始试卷 PDF、压缩包、开发资料、临时文件或缓存；必要题图随源码提供。Release 单独提供 `Compilation.pdf`（试题版）和 `Compilation-answer.pdf`（答案与解析版）。

## 试题来源与致谢

本仓库中**大部分试题的源头来自 [deekur/gaokaomath](https://github.com/deekur/gaokaomath)**，在此向原仓库作者及贡献者表示感谢。

本项目在其基础上进行了重新整理、排版、校订、索引、题图处理、重绘以及答案整理等工作。对于来源于其他资料或由本项目进一步整理、补充的内容，其权利仍归相应权利人所有。

## 【特别提醒】许可与转载要求

除另有注明的第三方内容外，本仓库中由本项目整理、编写和制作的内容采用 **Creative Commons Attribution-ShareAlike 4.0 International（CC BY-SA 4.0）** 协议发布：

<https://creativecommons.org/licenses/by-sa/4.0/>

这意味着你可以复制、转载、分发、修改和再创作本仓库中的受许可内容，也可以将其用于商业用途，但必须遵守以下要求：

1. **署名（BY）**：转载、分发或改编时必须给予适当署名，保留本项目名称及仓库链接，并保留适用的原作者、贡献者和来源信息。
2. **注明修改**：如果对内容进行了修改、整理、删减或再创作，应明确说明内容已经被修改。
3. **相同方式共享（SA）**：如果发布基于本仓库内容制作的改编或衍生作品，必须以 **CC BY-SA 4.0** 或该协议允许的兼容许可继续发布，不得将衍生作品改为禁止他人继续共享和改编的封闭许可。
4. **保留上游来源**：对于来源于 [deekur/gaokaomath](https://github.com/deekur/gaokaomath) 的试题或整理成果，转载或改编时应同时保留该上游仓库的来源说明及链接。
5. **不得附加额外限制**：不得通过法律条款或技术措施，额外限制其他人在 CC BY-SA 4.0 已允许范围内使用这些内容。

简而言之：**可以转载、修改、再发布，甚至商业使用，但必须署名；改编后继续公开发布时，也必须允许后来者按照相同规则继续使用。**

完整许可说明见仓库根目录的 [`LICENSE`](./LICENSE) 文件及 Creative Commons 官方页面。

## 构建

环境需要：

- TeX Live（含 XeLaTeX、latexmk 及 `styles.tex` 引用的宏包）
- `SimSun`、`SimHei`、`KaiTi`、`Times New Roman` 字体
- `STIX` 字体（用于希腊字母字体）

生成：

```bash
make pdf
```

- `Compilation.pdf`
- `Compilation-answer.pdf`

清理构建产物：

```bash
make clean
```

``````

---

## 164 · mirror/gaokaomath/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokaomath/README.md) · SHA 195f00cde1bc7288d8d441e276a1b476f9030400 · mode 100644

``````markdown
# 高考：普通*高*等学校招生全国统一*考*试

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_JA.md">日本語</a>
</p>

*（自1991年起，国家教委——教育部的前身——出版的高考相关书籍统一使用此全称）*

 ***（以下均特指数学科目）***

<details>
  <summary><b>1. 高考改革史</b></summary>

  - 1952：统一高考制度建立
  - 1952-1957：统一高考下分省与统一的争论
  - 1958：分省命题
  - 1959-1965：全国统一试卷
  - 1966-1976：高考停止
  - 1977：高考恢复，*因故*分省命题
  - 1978-1984：全国统一试卷
  - 1985：上海自主命题，广东启动***标准化***改革
  - 1986-1990：标准化改革继续推广
  - 1991：广东回归全国卷，三南试验启动
  - 1992：三南试验继续
  - 1993：三南试验结束，3+2方案开始实行
  - 1994：3+2方案继续推广
  - 1995：3+2方案推广完成
  - 1996：3+2方案与上海方案并存
  - 1997：天津，山西，江西启动***新课程***改革
  - 1998：新课程改革继续
  - 1999：广东启动3+X改革
  - 2000-2001：3+X改革推进
  - 2002：北京自主命题，3+X改革完成
  - 2003：新课程改革推进
  - 2004：重庆，福建，广东，湖北，湖南，江苏，辽宁，天津，浙江自主命题，***新课标***改革启动
  - 2005：山东，江西自主命题，新课程改革完成
  - 2006：安徽，四川，陕西自主命题
  - 2007-2009：教育部为海南，宁夏单独命题，新课标改革继续
  - 2010：海南，宁夏卷结束，并入新课标卷
  - 2011-2013：新课标改革继续
  - 2014：新课标改革继续，***新高考***改革启动
  - 2015：新课标改革完成，江西，辽宁停止自主命题
  - 2016：重庆，福建，广东，湖北，湖南，安徽，陕西停止自主命题
  - 2017：四川停止自主命题
  - 2018：山东停止自主命题
  - 2019：新高考改革继续
  - 2020：新高考全国卷出现
  - 2021：江苏停止自主命题
  - 2022：新高考改革继续
  - 2023：浙江停止自主命题
  - 2024：新高考改革继续
  - 2025：新高考改革完成

</details>

<details>
  <summary><b>2. 分年试卷详细情况</b></summary>

  - 1952-1957：全国卷
  - 1958：国家下放命题权，试卷总数量不明，目前收集到的有12套：
    - 北京，上海，福建，安徽（来源网络，真实性存疑），黑吉辽，湖北，湖南，江苏，四川，云南，河北，广东，另有一套地区不明
  - 1959-1965：全国卷
  - 1966-1976：——
  - 1977：因时间仓促，命题权下放，试卷总数量不明，收集到的有：
    - 29省级行政区卷，湖南株洲卷，广西百色卷，江苏南通卷，部分地区初试：黑龙江和江苏各行政区卷
  - 1978-1984：全国卷
  - 1985-1990：上海卷，广东卷，全国卷
  - 1991-1992：上海卷，全国卷，湖南、海南、云南卷
  - 1993-1994：上海卷，新旧科目组卷
  - 1995-1998：上海卷，全国卷
  - 1999：广东卷，上海卷，全国卷
  - 2000：广东卷，上海卷，新旧课程卷
  - 2001：广东河南卷，上海卷，全国新旧课程卷
  - 2002：北京卷，广东、河南、江苏、广西卷，上海卷，全国新旧课程卷
  - 2003：辽宁卷，江苏卷，广东广西卷，河南卷，北京卷，上海卷，全国新旧课程卷
  - 2004：重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，全国124卷，旧课程卷（又名全国3卷）
  - 2005：江西卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，大纲123卷
  - 2006：安徽卷，陕西卷，四川卷，江西卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，大纲12卷
  - 2007：安徽卷，陕西卷，四川卷，江西卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，新课标卷，大纲12卷
  - 2008：安徽卷，陕西卷，四川卷，延考区卷，江西卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，新课标卷，大纲12卷
  - 2009-2010：安徽卷，陕西卷，四川卷，江西卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，新课标卷，大纲12卷
  - 2011-2012：安徽卷，陕西卷，四川卷，江西卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，新课标卷，大纲卷
  - 2013-2014：安徽卷，陕西卷，四川卷，江西卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，辽宁卷，天津卷，浙江卷，北京卷，上海卷，新课标12卷，大纲卷
  - 2015：安徽卷，陕西卷，四川卷，山东卷，重庆卷，福建卷，广东卷，湖北卷，湖南卷，江苏卷，天津卷，浙江卷，北京卷，上海卷，全国12卷
  - 2016：四川卷，山东卷，江苏卷，天津卷，浙江卷，北京卷，上海卷，全国123卷
  - 2017：山东卷，江苏卷，天津卷，浙江卷，北京卷，上海卷，全国123卷
  - 2018-2019：江苏卷，天津卷，浙江卷，北京卷，上海卷，全国123卷
  - 2020：江苏卷，天津卷，浙江卷，北京卷，上海卷，全国123卷，新高考12卷
  - 2021-2022：天津卷，浙江卷，北京卷，上海卷，全国甲乙卷，新高考12卷
  - 2023：天津卷，北京卷，上海卷，全国甲乙卷，新高考12卷
  - 2024：天津卷，北京卷，上海卷，全国卷，新高考12卷
  - 2025-2026：天津卷，北京卷，上海卷，全国12卷

***名词解释：***
- **全国卷**：存在两套课程标准时，年份较早的对应的*统一*高考试题，只存在一套时，指*统一*高考试题
- **新课程卷/大纲卷**：依照1996版课标（大纲）命制的统一高考试题  
  - 2000-2004 相对旧课程叫新课程卷  
  - 2005-2014 相对新课标叫大纲卷
- **旧课程卷**：存在新课程卷时，其余的统一高考试题，依照1986版课标命制
- **新课标卷**：依照2003版课标命制的统一高考试题
- **新高考卷**：依照2017版课标命制的统一高考试题

</details>

<details>
  <summary><b>3. 历年各地文理数学试卷是否相同</b></summary>

  *（同卷不同要求也算同卷，比如1978；地名之间不加逗号代表共用一套试题）*

  - 1952-1957：同卷
  - 1958：收集到的全部同卷
  - 1959-1965：同卷
  - 1977：安徽，北京，福建，广西，广西百色，内蒙古，上海，新疆分卷，其余同卷
  - 1978：同卷
  - 1979-1986：全部文理分卷
  - 1987-1990：全国卷分卷，上海同卷
  - 1991-1992：全国卷分卷，上海、三南同卷
  - 1993：上海同卷，其余分卷
  - 1994：上海旧教材同卷，其余分卷
  - 1995-1998：分卷
  - 1999-2000：广东同卷，其余分卷
  - 2001：广东河南同卷，其余分卷
  - 2002：广东河南江苏广西同卷，其余分卷
  - 2003：广东广西，河南，江苏，辽宁同卷，其余分卷
  - 2004-2005：广东，江苏，辽宁同卷，其余分卷
  - 2006：广东，江苏同卷，其余分卷
  - 2007-2016：江苏同卷，其余分卷
  - 2017-2019：江苏，上海，浙江同卷，其余分卷
  - 2020-2024：全国卷分卷，其余同卷
  - 2025-2026：全部同卷

</details>

<details>
  <summary><b>4. 统一高考制度建立以来课程标准、大纲演变</b></summary>

  1. 1952 中学数学教学大纲（草案，1954、1956修订）
  2. 1963 全日制中学数学教学大纲（草案）
  3. 1978 全日制十年制学校中学数学教学大纲（试行草案）
  4. 1982 全日制六年制重点中学数学教学大纲（征求意见稿）
  5. 1983 高中数学教学纲要（草案）
  6. 1986 全日制中学数学教学大纲（1990、1994修订）
  7. 1996 全日制普通高级中学数学教学大纲（供试验用，2000、2002修订）
  8. 2003 普通高中数学课程标准（实验）
  9. 2017 普通高中数学课程标准（2020、2025修订[未出版]）

</details>

<details>
  <summary><b>5. 部分题目和考试信息来源</b></summary>

<details>
  <summary><b>1. 出版物（isbn10转为isbn13）</b></summary>

<ul>
<li>《上海市高考试卷集 数学 1990-2003》 ISBN：9787208049062</li>
<li>《1950-1965高考数学题解 —附数学竞赛题解（1978）》 保定一中三中数学组 无ISBN</li>
<li>《2000~2003年 全国及各省市高考数学试题及解答》 ISBN：9787560399911</li>
<li>《1977年各省、市、自治区 高考数学题解汇编》 梧州市教学研究室 无ISBN</li>
<li>《1977年全国各省市自治区高等学校招生 数学试题解答汇编》 江苏省邳县文教局数学资料编写组 无ISBN</li>
<li>《1951-1979 全国历届高考数学题解》 河北人民出版社 无ISBN</li>
<li>《全国高等学校招生数学试题及解答 1977年、1950年-1965年》 昆明师范学院数学系 无ISBN</li>
<li>《1977年各省市高考数学题解》 江西省南昌市第十九中学编著 无ISBN</li>
<li>《1949-1979 全国历届高考试题及解答（数学）》 新蕾出版社 无ISBN</li>
<li>《数学试题解 1978》 山西大学 无ISBN</li>
<li>《'78-'91 中国高考数学试题汇析》 ISBN：9787532027613</li>
<li>《高考文献 上》ISBN：9787040126716</li>
<li>《高考文献 下》ISBN：9787040126723</li>
<li>《中国高考史论述》ISBN：9787216048873</li>
<li>《新中国高考史》ISBN：9787211058914</li>
<li>《历史拐点 广东高考30年》ISBN：9787536135765</li>
<li>《中国高考事略》ISBN：9787574801875</li>
<li>《中国高考真题全编》，《全国及各省市高考试题全解》《中国教育考试年鉴》系列</li>
<li>《数学通报》 ISSN：05831458</li>
<li>《数学教学》 ISSN：04887387</li>
<li>《数学教学通讯》 ISSN：10018875</li>
<li>《数学通讯》 ISSN：04887395</li>
<li>《中学数学教学参考》 ISSN：10022171</li>
<li>《数学教学研究》 ISSN：16710452</li>
<li>《教学与研究（数学）》 ISSN：10036407</li>
<li>《上海中学数学》 ISSN：16727495</li>
<li>《中国考试》 ISSN：10058427</li>
</ul>

</details>

<details>
  <summary><b>2. 电子资料</b></summary>

<ul>
<li><a href="https://www.zxxk.com">学科网</a></li>
<li><a href="http://www.trgroup.com.cn">天仁报业集团</a></li>
<li><a href="https://www.zqy.com">正确教育云</a></li>
<li><a href="https://edu.sina.com.cn">新浪教育</a></li>
<li><a href="https://www.eol.cn">中国教育在线</a></li>
<li><a href="https://www.edu.cn">中国教育和科研计算机网</a></li>
<li><a href="https://fz.wanfangdata.com.cn/">万方中国地方志数据库</a></li>
</ul>

</details>

<details>
  <summary><b>3. 个人整理</b></summary>

<ul>
<li>刘威整理的《1977—2025高考数学真题全编》（主要参考对象，微信公众号：劢思数学，微信号：gh_e0ffa704d298）</li>
<li>周应业整理的1958年安徽高考试卷</li>
<li>张瑞兵整理的2020年上海春考试卷</li>
</ul>

</details>

**未能确定来源的也一并表示感谢**

</details>

<details>
  <summary><b>6. 内容说明</b></summary>

  <br>

  **1. 试卷收录标准**

  - 普通本科院校可参与招生且非院校直接招生 
  - **普通高中**学生均可参加
  - 春季高考加一条：难度与**当年**普通高考相当

  据此，部分年份、省份的大专招生专用试卷，大学单独、联合招生试卷，近年山东，广东，天津，福建等省所谓~~春季高考~~试卷不收录

  **2. 已知缺失试题**

  **普通高考**
  - 1958剩余地区
  - 1977浙江预选试题（见6.4）
  - 1977不确定是否还有地区独立命题

  **春季高考**
  - 春季2003安徽文（内蒙古可能同卷）
  - 春季2002内蒙古（可能与北京同卷）

  **3. 关于副题**

  本仓库不收录**副题**，**无论是否启用过**，值得注意的是，2003未启用副题，2008四川45区、市的延考区卷不是副题，副题又叫**备用卷**、**付题**（“付”为“副”的二简字）

  **4. 关于预考题**

  本仓库不收录预考试题，但1977除外，因为只有1977预考和高考均由省级及以下单位命题；关于1977的黑龙江初试，江苏初考，浙江预选是否算作预考，这里采用[此观点](https://doi.org/10.13397/j.cnki.fef.2023.05.010)

</details>

<details>
  <summary><b>7. 反馈与说明</b></summary>

  <br>

  **1. 反馈：**

  - 补充试题请联系 [deekur114514@gmail.com](mailto:deekur114514@gmail.com)，需确保试题来源无误并可靠，在没有其他来源的情况下可适当放宽条件
  - 补充答案同上，只接收教育部或**省级**教育考试单位出版、印发的试题分析或答案，2009及以后的全国卷不需要
  - **如您所提供的内容包含您的原创或整理汇编成果，我方接收之时即视为您已同意采用CC BY 4.0协议进行授权**
  - 其他问题（包括勘误）请提issues

  **2. 文件说明：**

  - 全部文件格式均为pdf，已移除所有元数据和水印
  - 小部分文件为docx转换而来，可能会有公式显示不完整的情况，后续会修复
  - 文件命名方式：(春季)+年份+卷种（+文理）（+初试）+(适用省份).pdf
  - 批量下载教程：Code→Download ZIP，详见下图
  ![批量下载教程](https://files.seeusercontent.com/2026/04/08/v3jX/1000085612.jpg)

  **3. 版权声明**

  - 试题来源于网络公开资料与已出版资料，版权归命题方或出版方所有。
  - 排版基于公开版本，本仓库仅进行汇编整理与必要的注释说明。
  - 本仓库仅对整理方式、目录结构、命名规则及说明性内容保留权利。
  - 本仓库采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可协议，转载时须提供指向原始仓库的链接，且不得删除License，如有修改须注明。

</details>

<details>
  <summary><b>8. 延伸阅读</b></summary>

  - 如果你对高考的政策演变与历史背景感兴趣，欢迎关注我的另一个项目：
  [**gaokao-system**](https://github.com/deekur/gaokao-system)
  
  - 此外，社区中也有基于本仓库数据使用latex重排整合的文件，并提供源码：
[**DxAThing/Gaokao-Math-Problems-Compilation**](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation)
</details>

**最后更新时间：2026年10月12日，以最新版本为准，历史版本仅供参考**

``````

---

## 165 · mirror/gaokaomath/README_EN.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokaomath/README_EN.md) · SHA a95446d2d75255dc5bf9f6e23c9ed4d93c131f3c · mode 100644

``````markdown
# Gaokao: National Unified *Examination* for Admissions to General *Higher* Education Institutions

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_JA.md">日本語</a>
</p>

*(Since 1991, books about the Gaokao published by the State Education Commission—the predecessor of the Ministry of Education—have consistently used this full official name.)*

***(Everything below refers specifically to mathematics.)***

<details>
  <summary><b>1. History of Gaokao Reform</b></summary>

  - 1952: The unified Gaokao system was established
  - 1952–1957: Debate over provincial versus national examinations under the unified Gaokao system
  - 1958: Provinces set their own examinations
  - 1959–1965: Nationally unified papers
  - 1966–1976: The Gaokao was suspended
  - 1977: The Gaokao was reinstated; provinces set their own examinations *because of exceptional circumstances*
  - 1978–1984: Nationally unified papers
  - 1985: Shanghai began setting its own papers, and Guangdong launched the ***standardization*** reform
  - 1986–1990: The standardization reform continued to expand
  - 1991: Guangdong returned to the national paper, and the Three-South Pilot began
  - 1992: The Three-South Pilot continued
  - 1993: The Three-South Pilot ended, and the 3+2 model began
  - 1994: The 3+2 model continued to expand
  - 1995: Nationwide adoption of the 3+2 model was completed
  - 1996: The 3+2 model and the Shanghai model coexisted
  - 1997: Tianjin, Shanxi, and Jiangxi launched the ***new curriculum*** reform
  - 1998: The new curriculum reform continued
  - 1999: Guangdong launched the 3+X reform
  - 2000-2001: The 3+X reform was expanded
  - 2002: Beijing began setting their own papers; the 3+X reform was completed
  - 2003: New curriculum reform was expanded
  - 2004: Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, and Zhejiang began setting their own papers; the ***new curriculum standards*** reform began
  - 2005: Shandong and Jiangxi began setting their own papers; the new curriculum reform was completed
  - 2006: Anhui, Sichuan, and Shaanxi began setting their own papers
  - 2007–2009: The Ministry of Education set separate papers for Hainan and Ningxia; the new curriculum standards reform continued
  - 2010: The Hainan and Ningxia papers ended and were incorporated into the New Curriculum Standards paper
  - 2011–2013: The new curriculum standards reform continued
  - 2014: The new curriculum standards reform continued, and the ***New Gaokao*** reform began
  - 2015: The new curriculum standards reform was completed; Jiangxi and Liaoning stopped setting their own papers
  - 2016: Chongqing, Fujian, Guangdong, Hubei, Hunan, Anhui, and Shaanxi stopped setting their own papers
  - 2017: Sichuan stopped setting its own papers
  - 2018: Shandong stopped setting its own papers
  - 2019: The New Gaokao reform continued
  - 2020: The national New Gaokao papers appeared
  - 2021: Jiangsu stopped setting its own papers
  - 2022: The New Gaokao reform continued
  - 2023: Zhejiang stopped setting its own papers
  - 2024: The New Gaokao reform continued
  - 2025: The New Gaokao reform was completed

</details>

<details>
  <summary><b>2. Detailed Papers by Year</b></summary>

  - 1952–1957: National paper
  - 1958: The central government delegated examination-setting authority. The total number of papers is unknown; 12 sets have currently been collected:
    - Beijing, Shanghai, Fujian, and Anhui (sourced online; authenticity uncertain); Heilongjiang-Jilin-Liaoning, Hubei, Hunan, Jiangsu, Sichuan, Yunnan, Hebei, and Guangdong; plus one paper from an unidentified region
  - 1959–1965: National paper
  - 1966–1976: —
  - 1977: Because time was limited, examination-setting authority was delegated. The total number of papers is unknown; the collection currently includes:
    - Papers from 29 provincial-level administrative regions; Zhuzhou, Hunan; Baise, Guangxi; Nantong, Jiangsu; and some regional preliminary examinations, including papers from administrative regions in Heilongjiang and Jiangsu
  - 1978–1984: National paper
  - 1985–1990: Shanghai paper, Guangdong paper, and national paper
  - 1991–1992: Shanghai paper, national paper, and the Hunan-Hainan-Yunnan paper
  - 1993-1994: Shanghai paper and papers for the new and old subject groups
  - 1995–1998: Shanghai paper and national paper
  - 1999: Guangdong paper, Shanghai paper, and national paper
  - 2000: Guangdong paper, Shanghai paper, and new/old curriculum papers
  - 2001: Guangdong-Henan paper, Shanghai paper, and national new/old curriculum papers
  - 2002: Beijing paper; Guangdong-Henan-Jiangsu-Guangxi paper; Shanghai paper; and national new/old curriculum papers
  - 2003: Liaoning, Jiangsu, Guangdong-Guangxi, Henan, Beijing, and Shanghai papers; and national new/old curriculum papers
  - 2004: Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; National Papers I, II, and IV; and the Old Curriculum paper (also known as National Paper III)
  - 2005: Jiangxi, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; and Syllabus Papers I, II, and III
  - 2006: Anhui, Shaanxi, Sichuan, Jiangxi, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; and Syllabus Papers I and II
  - 2007: Anhui, Shaanxi, Sichuan, Jiangxi, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; New Curriculum Standards paper; and Syllabus Papers I and II
  - 2008: Anhui, Shaanxi, Sichuan, Postponed Examination Region, Jiangxi, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; New Curriculum Standards paper; and Syllabus Papers I and II
  - 2009–2010: Anhui, Shaanxi, Sichuan, Jiangxi, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; New Curriculum Standards paper; and Syllabus Papers I and II
  - 2011–2012: Anhui, Shaanxi, Sichuan, Jiangxi, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; New Curriculum Standards paper; and Syllabus paper
  - 2013–2014: Anhui, Shaanxi, Sichuan, Jiangxi, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Liaoning, Tianjin, Zhejiang, Beijing, and Shanghai papers; New Curriculum Standards Papers I and II; and Syllabus paper
  - 2015: Anhui, Shaanxi, Sichuan, Shandong, Chongqing, Fujian, Guangdong, Hubei, Hunan, Jiangsu, Tianjin, Zhejiang, Beijing, and Shanghai papers; and National Papers I and II
  - 2016: Sichuan, Shandong, Jiangsu, Tianjin, Zhejiang, Beijing, and Shanghai papers; and National Papers I, II, and III
  - 2017: Shandong, Jiangsu, Tianjin, Zhejiang, Beijing, and Shanghai papers; and National Papers I, II, and III
  - 2018–2019: Jiangsu, Tianjin, Zhejiang, Beijing, and Shanghai papers; and National Papers I, II, and III
  - 2020: Jiangsu, Tianjin, Zhejiang, Beijing, and Shanghai papers; National Papers I, II, and III; and New Gaokao Papers I and II
  - 2021–2022: Tianjin, Zhejiang, Beijing, and Shanghai papers; National Papers A and B; and New Gaokao Papers I and II
  - 2023: Tianjin, Beijing, and Shanghai papers; National Papers A and B; and New Gaokao Papers I and II
  - 2024: Tianjin, Beijing, and Shanghai papers; national paper; and New Gaokao Papers I and II
  - 2025–2026: Tianjin, Beijing, and Shanghai papers; National Papers I and II

***Terminology (for consistency, these names may differ from mainstream usage and from *Test Paper Analysis*):***
- **National paper**: When two curriculum standards coexisted, the earlier set of *unified* Gaokao questions; when only one standard existed, the *unified* Gaokao questions
- **New Curriculum paper / Syllabus paper**: Unified Gaokao questions based on the 1996 curriculum standards (syllabus)
  - From 2000 to 2004, it was called the New Curriculum paper in contrast with the Old Curriculum
  - From 2005 to 2014, it was called the Syllabus paper in contrast with the New Curriculum Standards paper
- **Old Curriculum paper**: When a New Curriculum paper existed, the other unified Gaokao questions, based on the 1986 curriculum standards
- **New Curriculum Standards paper**: Unified Gaokao questions based on the 2003 curriculum standards
- **New Gaokao paper**: Unified Gaokao questions based on the 2017 curriculum standards
</details>


<details>
  <summary><b>3. Whether Liberal-Arts and Science Mathematics Papers Were Identical by Region and Year</b></summary>

  *(Papers with different requirements are still counted as the same paper, as in 1978. Place names without commas shared one paper.)*

  - 1952–1957: Same paper
  - 1958: All collected papers used the same paper for both tracks
  - 1959–1965: Same paper
  - 1977: Anhui, Beijing, Fujian, Guangxi, Baise in Guangxi, Inner Mongolia, Shanghai, and Xinjiang used separate papers; all others used the same paper
  - 1978: Same paper
  - 1979–1986: All used separate liberal-arts and science papers
  - 1987–1990: The national paper was split; Shanghai used the same paper
  - 1991–1992: The national paper was split; Shanghai and the Three-South regions used the same paper
  - 1993: Shanghai used the same paper; all others were split
  - 1994: Shanghai's old-textbook paper was the same; all others were split
  - 1995–1998: Separate papers
  - 1999–2000: Guangdong used the same paper; all others were split
  - 2001: Guangdong and Henan shared the same paper; all others were split
  - 2002: Guangdong, Henan, Jiangsu, and Guangxi shared the same paper; all others were split
  - 2003: Guangdong-Guangxi, Henan, Jiangsu, and Liaoning each used the same paper for both tracks; all others were split
  - 2004–2005: Guangdong, Jiangsu, and Liaoning used the same paper; all others were split
  - 2006: Guangdong and Jiangsu used the same paper; all others were split
  - 2007–2016: Jiangsu used the same paper; all others were split
  - 2017–2019: Jiangsu, Shanghai, and Zhejiang used the same paper; all others were split
  - 2020–2024: The national paper was split; all others used the same paper
  - 2025–2026: All used the same paper

</details>

<details>
  <summary><b>4. Evolution of Curriculum Standards and Syllabi Since the Unified Gaokao System Was Established</b></summary>

  1. 1952 *Secondary School Mathematics Teaching Syllabus* (draft; revised in 1954 and 1956)
  2. 1963 *Mathematics Teaching Syllabus for Full-Time Secondary Schools* (draft)
  3. 1978 *Secondary School Mathematics Teaching Syllabus for Full-Time Ten-Year Schools* (trial draft)
  4. 1982 *Mathematics Teaching Syllabus for Full-Time Six-Year Key Secondary Schools* (consultation draft)
  5. 1983 *Senior High School Mathematics Teaching Outline* (draft)
  6. 1986 *Mathematics Teaching Syllabus for Full-Time Secondary Schools* (revised in 1990 and 1994)
  7. 1996 *Mathematics Teaching Syllabus for Full-Time General Senior High Schools* (for trial use; revised in 2000 and 2002)
  8. 2003 *General Senior High School Mathematics Curriculum Standards* (experimental)
  9. 2017 *General Senior High School Mathematics Curriculum Standards* (revised in 2020 and 2025 [unpublished])

</details>

<details>
  <summary><b>5. Sources for Selected Questions and Examination Information</b></summary>

<details>
  <summary><b>1. Publications (ISBN-10 converted to ISBN-13)</b></summary>

<ul>
<li>《上海市高考试卷集 数学 1990-2003》 ISBN: 9787208049062</li>
<li>《1950-1965高考数学题解 —附数学竞赛题解（1978）》, mathematics groups of Baoding No. 1 and No. 3 Middle Schools, no ISBN</li>
<li>《2000~2003年 全国及各省市高考数学试题及解答》 ISBN: 9787560399911</li>
<li>《1977年各省、市、自治区 高考数学题解汇编》, Wuzhou Teaching Research Office, no ISBN</li>
<li>《1977年全国各省市自治区高等学校招生 数学试题解答汇编》, mathematics-materials editorial group of the Education Bureau of Pixian County, Jiangsu, no ISBN</li>
<li>《1951-1979 全国历届高考数学题解》, Hebei People's Publishing House, no ISBN</li>
<li>《全国高等学校招生数学试题及解答 1977年、1950年-1965年》, Department of Mathematics, Kunming Normal College, no ISBN</li>
<li>《1977年各省市高考数学题解》, Nanchang No. 19 Middle School, Jiangxi, no ISBN</li>
<li>《1949-1979 全国历届高考试题及解答（数学）》, Xinlei Publishing House, no ISBN</li>
<li>《数学试题解 1978》, Shanxi University, no ISBN</li>
<li>《'78-'91 中国高考数学试题汇析》 ISBN: 9787532027613</li>
<li>《高考文献 上》 ISBN: 9787040126716</li>
<li>《高考文献 下》 ISBN: 9787040126723</li>
<li>《中国高考史论述》 ISBN: 9787216048873</li>
<li>《新中国高考史》 ISBN: 9787211058914</li>
<li>《历史拐点 广东高考30年》 ISBN: 9787536135765</li>
<li>《中国高考事略》 ISBN: 9787574801875</li>
<li>The 《中国高考真题全编》, 《全国及各省市高考试题全解》, and 《中国教育考试年鉴》 series</li>
<li>《数学通报》 ISSN: 05831458</li>
<li>《数学教学》 ISSN: 04887387</li>
<li>《数学教学通讯》 ISSN: 10018875</li>
<li>《数学通讯》 ISSN: 04887395</li>
<li>《中学数学教学参考》 ISSN: 10022171</li>
<li>《数学教学研究》 ISSN: 16710452</li>
<li>《教学与研究（数学）》 ISSN: 10036407</li>
<li>《上海中学数学》 ISSN: 16727495</li>
<li>《中国考试》 ISSN: 10058427</li>
</ul>

</details>

<details>
  <summary><b>2. Electronic Resources</b></summary>

<ul>
<li><a href="https://www.zxxk.com">ZXXK</a></li>
<li><a href="http://www.trgroup.com.cn">Tianren Newspaper Group</a></li>
<li><a href="https://www.zqy.com">Zhengque Education Cloud</a></li>
<li><a href="https://edu.sina.com.cn">Sina Education</a></li>
<li><a href="https://www.eol.cn">China Education Online</a></li>
<li><a href="https://www.edu.cn">China Education and Research Network</a></li>
<li><a href="https://fz.wanfangdata.com.cn/">Wanfang Database of Chinese Local Gazetteers</a></li>
</ul>

</details>

<details>
  <summary><b>3. Individual Compilations</b></summary>

<ul>
<li>Liu Wei's 《1977—2025高考数学真题全编》 (the primary reference; WeChat official account: 劢思数学; WeChat ID: gh_e0ffa704d298)</li>
<li>The 1958 Anhui Gaokao paper compiled by Zhou Yingye</li>
<li>The 2020 Shanghai Spring Examination paper compiled by Zhang Ruibing</li>
</ul>

</details>

**Thanks Also Go to Sources That Could Not Be Identified**

</details>

<details>
  <summary><b>6. Notes on the Collection</b></summary>

  <br>

  **1. Inclusion Criteria for Papers**

  - General undergraduate institutions could participate in admissions, and admission was not conducted directly by individual institutions
  - All **general senior high school** students could participate
  - One additional criterion for spring examinations: difficulty comparable to the **same year's** regular Gaokao

  Accordingly, the collection excludes papers used solely for junior-college admissions in some years or provinces, papers for independent or joint admissions by universities, and the so-called ~~Spring Gaokao~~ papers used in recent years by Shandong, Guangdong, Tianjin, Fujian, and other provinces.

  **2. Known Missing Papers**

  **Regular Gaokao**
  - Remaining regions from 1958
  - Zhejiang's 1977 preliminary paper (see Section 6.4)
  - It is uncertain whether other regions independently set papers in 1977

  **Spring Gaokao**
  - 2003 Anhui liberal-arts spring paper (Inner Mongolia may have used the same paper)
  - 2002 Inner Mongolia spring paper (may have been the same as Beijing's)

  **3. Alternative Papers**

  This repository does not include **alternative papers**, **whether or not they were ever used**. Note that the 2003 alternative paper was not used, and that the papers for the postponed-examination regions in 45 districts and cities of Sichuan in 2008 were not alternative papers. Alternative papers are also called **backup papers** and **付题** (“付” is the Second Simplified Chinese form of “副”).

  **4. Preliminary Examination Papers**

  This repository does not include preliminary examination papers, except those from 1977, because only in 1977 were both preliminary examinations and the Gaokao set by units at or below the provincial level. As for whether Heilongjiang's first-round examination, Jiangsu's preliminary examination, and Zhejiang's selection examination in 1977 count as preliminary examinations, this repository follows [this view](https://doi.org/10.13397/j.cnki.fef.2023.05.010).

</details>

<details>
  <summary><b>7. Feedback and Notes</b></summary>

  <br>

  **1. Feedback**

  - To contribute missing papers, contact [deekur114514@gmail.com](mailto:deekur114514@gmail.com). Sources must be accurate and reliable; the requirements may be relaxed appropriately when no other source exists
  - The same contact applies to supplemental answers. Only test analyses or answers published or issued by the Ministry of Education or **provincial-level** education and examination authorities are accepted; answers for national papers from 2009 onward are not needed
  - **If the material you provide contains your original work or your own compiled work, it will be deemed licensed under CC BY 4.0 when we accept it**
  - For other matters, including corrections, please open an issue

  **2. File Notes**

  - All files are PDFs, with all metadata and watermarks removed
  - A small number of files were converted from DOCX and may have incomplete formula rendering; this will be fixed later
  - File naming format: (Spring)+year+paper type+(liberal arts/science)+(preliminary examination)+(applicable province).pdf
  - Bulk download instructions: Code → Download ZIP; see the image below
  ![Bulk download instructions](https://files.seeusercontent.com/2026/04/08/v3jX/1000085612.jpg)

  **3. Copyright Notice**

  - Examination questions come from publicly available online and published sources; copyright belongs to the examination setters or publishers.
  - Typesetting is based on public editions. This repository only compiles and organizes the materials and adds necessary annotations.
  - This repository reserves rights only to its method of compilation, directory structure, naming rules, and explanatory content.
  - This repository is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Reuse must include a link to the original repository, must not remove the License, and must identify any modifications.

</details>

<details>
  <summary><b>8. Further Reading</b></summary>

  - If you are interested in the policy evolution and historical background of the Gaokao, feel free to check out my other project:
  [**gaokao-system**](https://github.com/deekur/gaokao-system)
  
  - Additionally, there is a community project that uses LaTeX to retype and compile the data from this repository, providing both the generated PDFs and the source code:
[**DxAThing/Gaokao-Math-Problems-Compilation**](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation)
</details>

**Last updated: October 12, 2026. The latest version prevails; historical versions are for reference only.**

``````

---

## 166 · mirror/gaokaomath/README_JA.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/gaokaomath/README_JA.md) · SHA ba19c019989c1a1b9e699af3f29771cc2823522c · mode 100644

``````markdown
# 高考：中国普通*高等*学校招生全国統一*試験*

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_JA.md">日本語</a>
</p>

*（1991 年以降、国家教育委員会——教育部の前身——が出版した高考関連書籍では、この正式名称が一貫して使用されています。）*

***（以下はすべて数学科目を指します。）***

<details>
  <summary><b>1. 高考改革の歴史</b></summary>

  - 1952：統一高考制度を確立
  - 1952～1957：統一高考制度下で、省別出題と全国統一出題をめぐる議論
  - 1958：各省が独自に出題
  - 1959～1965：全国統一試験
  - 1966～1976：高考を停止
  - 1977：高考を再開し、*やむを得ない事情により*各省が独自に出題
  - 1978～1984：全国統一試験
  - 1985：上海が独自出題を開始し、広東が***標準化***改革を開始
  - 1986～1990：標準化改革を引き続き拡大
  - 1991：広東が全国統一試験へ復帰し、「三南」試行を開始
  - 1992：「三南」試行を継続
  - 1993：「三南」試行を終了し、3+2 方式を開始
  - 1994：3+2 方式を引き続き拡大
  - 1995：3+2 方式の全国展開が完了
  - 1996：3+2 方式と上海方式が併存
  - 1997：天津、山西、江西が***新課程***改革を開始
  - 1998：新課程改革を継続
  - 1999：広東が 3+X 改革を開始
  - 2000-2001：3+X改革が進む
  - 2002：北京が独自出題を開始し、3+X 改革が完了
  - 2003：新課程改革が進む
  - 2004：重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江が独自出題を開始し、***新課程標準***改革を開始
  - 2005：山東と江西が独自出題を開始し、新課程改革が完了
  - 2006：安徽、四川、陝西が独自出題を開始
  - 2007～2009：教育部が海南と寧夏向けに個別出題し、新課程標準改革を継続
  - 2010：海南・寧夏試験を終了し、新課程標準試験へ統合
  - 2011～2013：新課程標準改革を継続
  - 2014：新課程標準改革を継続し、***新高考***改革を開始
  - 2015：新課程標準改革が完了し、江西と遼寧が独自出題を終了
  - 2016：重慶、福建、広東、湖北、湖南、安徽、陝西が独自出題を終了
  - 2017：四川が独自出題を終了
  - 2018：山東が独自出題を終了
  - 2019：新高考改革を継続
  - 2020：新高考全国試験が登場
  - 2021：江蘇が独自出題を終了
  - 2022：新高考改革を継続
  - 2023：浙江が独自出題を終了
  - 2024：新高考改革を継続
  - 2025：新高考改革が完了

</details>

<details>
  <summary><b>2. 年別試験問題の詳細</b></summary>

  - 1952～1957：全国試験
  - 1958：国が出題権を地方へ移譲。試験の総数は不明で、現在 12 組を収集：
    - 北京、上海、福建、安徽（インターネット由来で真正性に疑義あり）、黒竜江・吉林・遼寧、湖北、湖南、江蘇、四川、雲南、河北、広東、および地域不明の 1 組
  - 1959～1965：全国試験
  - 1966～1976：—
  - 1977：準備期間が短かったため出題権を地方へ移譲。試験の総数は不明で、現在の収集内容は次のとおり：
    - 29 の省級行政区の試験、湖南株洲、広西百色、江蘇南通の試験、および一部地域の一次試験（黒竜江と江蘇の各行政区試験）
  - 1978～1984：全国試験
  - 1985～1990：上海試験、広東試験、全国試験
  - 1991～1992：上海試験、全国試験、湖南・海南・雲南試験
  - 1993-1994：上海試験、新旧科目群試験
  - 1995～1998：上海試験、全国試験
  - 1999：広東試験、上海試験、全国試験
  - 2000：広東試験、上海試験、新旧課程試験
  - 2001：広東・河南試験、上海試験、全国新旧課程試験
  - 2002：北京試験、広東・河南・江蘇・広西試験、上海試験、全国新旧課程試験
  - 2003：遼寧、江蘇、広東・広西、河南、北京、上海の各試験、全国新旧課程試験
  - 2004：重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、全国 I・II・IV 試験、旧課程試験（全国 III 試験とも呼ばれる）
  - 2005：江西、山東、重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、大綱 I・II・III 試験
  - 2006：安徽、陝西、四川、江西、山東、重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、大綱 I・II 試験
  - 2007：安徽、陝西、四川、江西、山東、重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、新課程標準試験、大綱 I・II 試験
  - 2008：安徽、陝西、四川、延期試験地域、江西、山東、重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、新課程標準試験、大綱 I・II 試験
  - 2009～2010：安徽、陝西、四川、江西、山東、重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、新課程標準試験、大綱 I・II 試験
  - 2011～2012：安徽、陝西、四川、江西、山東、重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、新課程標準試験、大綱試験
  - 2013～2014：安徽、陝西、四川、江西、山東、重慶、福建、広東、湖北、湖南、江蘇、遼寧、天津、浙江、北京、上海の各試験、新課程標準 I・II 試験、大綱試験
  - 2015：安徽、陝西、四川、山東、重慶、福建、広東、湖北、湖南、江蘇、天津、浙江、北京、上海の各試験、全国 I・II 試験
  - 2016：四川、山東、江蘇、天津、浙江、北京、上海の各試験、全国 I・II・III 試験
  - 2017：山東、江蘇、天津、浙江、北京、上海の各試験、全国 I・II・III 試験
  - 2018～2019：江蘇、天津、浙江、北京、上海の各試験、全国 I・II・III 試験
  - 2020：江蘇、天津、浙江、北京、上海の各試験、全国 I・II・III 試験、新高考 I・II 試験
  - 2021～2022：天津、浙江、北京、上海の各試験、全国甲・乙試験、新高考 I・II 試験
  - 2023：天津、北京、上海の各試験、全国甲・乙試験、新高考 I・II 試験
  - 2024：天津、北京、上海の各試験、全国試験、新高考 I・II 試験
  - 2025～2026：天津、北京、上海の各試験、全国 I・II 試験

***用語の説明（基準を統一するため、名称は一般的な呼称や『試題分析』と異なる場合があります。）：***
- **全国試験**：2 種類の課程標準が併存する場合は、より古い課程に対応する*統一*高考试験問題を指し、1 種類のみの場合は*統一*高考试験問題を指す
- **新課程試験／大綱試験**：1996 年版課程標準（大綱）に基づく統一高考试験問題
  - 2000～2004 年は旧課程との対比で新課程試験と呼ぶ
  - 2005～2014 年は新課程標準との対比で大綱試験と呼ぶ
- **旧課程試験**：新課程試験が存在する場合のもう一方の統一高考试験問題で、1986 年版課程標準に基づく
- **新課程標準試験**：2003 年版課程標準に基づく統一高考试験問題
- **新高考试験**：2017 年版課程標準に基づく統一高考试験問題

</details>

<details>
  <summary><b>3. 年・地域別の文系数学と理系数学の試験が同一だったか</b></summary>

  *（要求が異なっても同じ問題なら同一試験と数えます。1978 年がその例です。地名の間に読点がない場合は、同じ試験問題を共有したことを示します。）*

  - 1952～1957：同一試験
  - 1958：収集済みの試験はすべて同一
  - 1959～1965：同一試験
  - 1977：安徽、北京、福建、広西、広西百色、内モンゴル、上海、新疆は別試験、その他は同一
  - 1978：同一試験
  - 1979～1986：すべて文系・理系別試験
  - 1987～1990：全国試験は別試験、上海は同一
  - 1991～1992：全国試験は別試験、上海と「三南」は同一
  - 1993：上海は同一、その他は別試験
  - 1994：上海の旧教材試験は同一、その他は別試験
  - 1995～1998：別試験
  - 1999～2000：広東は同一、その他は別試験
  - 2001：広東・河南は同一、その他は別試験
  - 2002：広東・河南・江蘇・広西は同一、その他は別試験
  - 2003：広東・広西、河南、江蘇、遼寧はそれぞれ文理同一、その他は別試験
  - 2004～2005：広東、江蘇、遼寧は同一、その他は別試験
  - 2006：広東と江蘇は同一、その他は別試験
  - 2007～2016：江蘇は同一、その他は別試験
  - 2017～2019：江蘇、上海、浙江は同一、その他は別試験
  - 2020～2024：全国試験は別試験、その他は同一
  - 2025～2026：すべて同一試験

</details>

<details>
  <summary><b>4. 統一高考制度確立後の課程標準・大綱の変遷</b></summary>

  1. 1952 『中学数学教学大纲』（草案、1954・1956 年改訂）
  2. 1963 『全日制中学数学教学大纲』（草案）
  3. 1978 『全日制十年制学校中学数学教学大纲』（試行草案）
  4. 1982 『全日制六年制重点中学数学教学大纲』（意見募集稿）
  5. 1983 『高中数学教学纲要』（草案）
  6. 1986 『全日制中学数学教学大纲』（1990・1994 年改訂）
  7. 1996 『全日制普通高级中学数学教学大纲』（試行用、2000・2002 年改訂）
  8. 2003 『普通高中数学课程标准』（実験版）
  9. 2017 『普通高中数学课程标准』（2020・2025 年改訂［未出版］）

</details>

<details>
  <summary><b>5. 一部の問題および試験情報の出典</b></summary>

<details>
  <summary><b>1. 出版物（ISBN-10 を ISBN-13 に変換）</b></summary>

<ul>
<li>《上海市高考试卷集 数学 1990-2003》 ISBN：9787208049062</li>
<li>《1950-1965高考数学题解 —附数学竞赛题解（1978）》 保定第一・第三中学校数学グループ、ISBN なし</li>
<li>《2000~2003年 全国及各省市高考数学试题及解答》 ISBN：9787560399911</li>
<li>《1977年各省、市、自治区 高考数学题解汇编》 梧州市教学研究室、ISBN なし</li>
<li>《1977年全国各省市自治区高等学校招生 数学试题解答汇编》 江蘇省邳県文教局数学資料編集グループ、ISBN なし</li>
<li>《1951-1979 全国历届高考数学题解》 河北人民出版社、ISBN なし</li>
<li>《全国高等学校招生数学试题及解答 1977年、1950年-1965年》 昆明師範学院数学系、ISBN なし</li>
<li>《1977年各省市高考数学题解》 江西省南昌市第十九中学校、ISBN なし</li>
<li>《1949-1979 全国历届高考试题及解答（数学）》 新蕾出版社、ISBN なし</li>
<li>《数学试题解 1978》 山西大学、ISBN なし</li>
<li>《'78-'91 中国高考数学试题汇析》 ISBN：9787532027613</li>
<li>《高考文献 上》ISBN：9787040126716</li>
<li>《高考文献 下》ISBN：9787040126723</li>
<li>《中国高考史论述》ISBN：9787216048873</li>
<li>《新中国高考史》ISBN：9787211058914</li>
<li>《历史拐点 广东高考30年》ISBN：9787536135765</li>
<li>《中国高考事略》ISBN：9787574801875</li>
<li>《中国高考真题全编》、《全国及各省市高考试题全解》、《中国教育考试年鉴》シリーズ</li>
<li>《数学通报》 ISSN：05831458</li>
<li>《数学教学》 ISSN：04887387</li>
<li>《数学教学通讯》 ISSN：10018875</li>
<li>《数学通讯》 ISSN：04887395</li>
<li>《中学数学教学参考》 ISSN：10022171</li>
<li>《数学教学研究》 ISSN：16710452</li>
<li>《教学与研究（数学）》 ISSN：10036407</li>
<li>《上海中学数学》 ISSN：16727495</li>
<li>《中国考试》 ISSN：10058427</li>
</ul>

</details>

<details>
  <summary><b>2. 電子資料</b></summary>

<ul>
<li><a href="https://www.zxxk.com">学科网</a></li>
<li><a href="http://www.trgroup.com.cn">天仁报业集团</a></li>
<li><a href="https://www.zqy.com">正确教育云</a></li>
<li><a href="https://edu.sina.com.cn">新浪教育</a></li>
<li><a href="https://www.eol.cn">中国教育在线</a></li>
<li><a href="https://www.edu.cn">中国教育和科研计算机网</a></li>
<li><a href="https://fz.wanfangdata.com.cn/">万方中国地方志数据库</a></li>
</ul>

</details>

<details>
  <summary><b>3. 個人による整理</b></summary>

<ul>
<li>劉威が整理した《1977—2025高考数学真题全编》（主な参照資料、WeChat 公式アカウント：劢思数学、WeChat ID：gh_e0ffa704d298）</li>
<li>周応業が整理した 1958 年安徽高考试験</li>
<li>張瑞兵が整理した 2020 年上海春季試験</li>
</ul>

</details>

**出典を特定できなかった資料にも感謝します**

</details>

<details>
  <summary><b>6. 内容に関する説明</b></summary>

  <br>

  **1. 試験問題の収録基準**

  - 一般本科大学が入試に参加でき、大学による直接募集ではないこと
  - **普通高校**のすべての生徒が参加できること
  - 春季高考には追加条件として、難易度が**同年**の通常高考と同程度であること

  以上に基づき、一部の年度・省における専科大学募集専用試験、大学の単独・共同募集試験、近年の山東、広東、天津、福建などでいわゆる~~春季高考~~と呼ばれる試験は収録しません。

  **2. 既知の未収録問題**

  **通常高考**
  - 1958 年の残りの地域
  - 1977 年浙江の予備選抜問題（6.4 参照）
  - 1977 年にほかの地域でも独自出題があったかは不明

  **春季高考**
  - 2003 年春季安徽文系（内モンゴルも同一試験だった可能性あり）
  - 2002 年春季内モンゴル（北京と同一試験だった可能性あり）

  **3. 副題について**

  本リポジトリは**副題**を、**実際に使用されたかどうかにかかわらず**収録しません。なお、2003 年の副題は使用されておらず、2008 年に四川の 45 区市で実施された延期試験地域の試験は副題ではありません。副題は**予備試験**、**付题**とも呼ばれます（「付」は「副」の第二次簡体字）。

  **4. 予備試験問題について**

  本リポジトリは 1977 年を除き予備試験問題を収録しません。1977 年だけは、予備試験と高考の双方が省級以下の機関によって出題されたためです。1977 年の黒竜江の初試、江蘇の初考、浙江の予選を予備試験とみなすかについては、[こちらの見解](https://doi.org/10.13397/j.cnki.fef.2023.05.010)を採用しています。

</details>

<details>
  <summary><b>7. フィードバックと説明</b></summary>

  <br>

  **1. フィードバック**

  - 試験問題を追加する場合は [deekur114514@gmail.com](mailto:deekur114514@gmail.com) までご連絡ください。出典が正確かつ信頼できることが必要ですが、ほかに出典がない場合は条件を適切に緩和できます
  - 解答の追加も同じ連絡先です。教育部または**省級**の教育・試験機関が出版・発行した試題分析または解答のみ受け付けます。2009 年以降の全国試験の解答は不要です
  - **提供された内容にご自身の創作または整理・編集成果が含まれる場合、当方が受領した時点で CC BY 4.0 による使用許諾に同意したものとみなします**
  - その他の問題（誤記の訂正を含む）は issue を作成してください

  **2. ファイルについて**

  - すべてのファイルは PDF 形式で、メタデータと透かしはすべて削除済みです
  - 一部のファイルは DOCX から変換されており、数式が完全に表示されない場合があります。今後修正予定です
  - ファイル名の形式：(春季)+年+試験種別+(文理)+(初試)+(適用省份).pdf
  - 一括ダウンロード手順：Code → Download ZIP。下図を参照してください
  ![一括ダウンロード手順](https://files.seeusercontent.com/2026/04/08/v3jX/1000085612.jpg)

  **3. 著作権表示**

  - 試験問題はインターネット上で公開された資料および出版物に由来し、著作権は出題者または出版社に帰属します。
  - 組版は公開版に基づき、本リポジトリは資料の収集・整理と必要な注釈のみを行います。
  - 本リポジトリは、整理方法、ディレクトリ構成、命名規則、および説明文についてのみ権利を留保します。
  - 本リポジトリは [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) でライセンスされています。転載時は元のリポジトリへのリンクを記載し、License を削除せず、変更がある場合はその旨を明記する必要があります。

</details>

<details>
  <summary><b>8. 関連プロジェクト</b></summary>

  - 中国の高考政策の変遷や歴史的背景に興味がある方は、こちらの関連プロジェクトもぜひご覧ください：
  [**gaokao-system**](https://github.com/deekur/gaokao-system)
  
  - また、コミュニティには、このリポジトリのデータを基に LaTeX で組版・統合したプロジェクトがあり、生成された PDF とソースコードも提供されています：
[**DxAThing/Gaokao-Math-Problems-Compilation**](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation)

</details>

**最終更新：2026 年 10 月 12 日。最新バージョンを優先し、過去のバージョンは参考用です。**

``````

---

## 167 · mirror/math-atlas/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/README.md) · SHA 54afa8066a59088663e887fbfbc0e89a51bc440f · mode 100644

``````markdown
:

# MathAtlas

一个轻量的高中数学题库浏览与讲义导出工具。基于 Next.js，以 Obsidian Vault 作为数据源。

---

## 准备工作

电脑上需要装有 **Node.js 18+**：

- 访问 [nodejs.org](https://nodejs.org) 下载 LTS 版本
- 下载后双击安装，默认选项一路下一步即可

Pandoc（可选，用于 Word 导出）

Pandoc 用于生成高质量的 Word 文档。如不安装，程序将使用浏览器端生成（latex公式无法转换）。

- 访问 [pandoc](https://github.com/jgm/pandoc/releases/tag/3.10) 下载
- pandoc-3.10-windows-x86_64.zip
- zip或msi都可以
- 下载后解压到该项目的tool目录下

## 安装与启动

1. 下载本项目代码，解压到本地
2. 在项目文件夹里打开终端（在文件夹地址栏输入 `cmd` 回车即可），依次执行：

```bash
# (网络顺畅就跳过这一步)切换到国内镜像
npm config set registry https://registry.npmmirror.com

# 安装依赖
npm install

# 启动
npm run dev
```

3. 浏览器打开 **http://localhost:3000**
4. 想用「在 Obsidian 中打开」跳转功能的话，用 Obsidian 打开 `demo-vault` 文件夹作为 Vault 即可

项目自带两套示例试卷（2025 全国一卷、二卷），不配置也能直接体验。

---

## 配置自己的题库（可选）

> **注意**：Obsidian Vault 中必须有 `题库` 文件夹，程序只读这个文件夹。配置时填 Vault 根目录即可，程序会自动拼接 `\题库` 和 `\images`。

例如 Vault 结构像这样：

```
高中数学/          ← 填这个路径
├── 题库/          ← 名字不能改
│   ├── 2025全国一卷/
│   └── 2025全国二卷/
└── images/        ← 题目用到的图片
```

复制 `.env.local.example` 为 `.env.local`，用记事本打开，改成你的 Vault 路径：

```
# 复制此文件并重命名为 .env.local，然后修改为你电脑上的实际路径
# 不配置则默认使用 ./demo-vault 示例题库
VAULT_PATH=./demo-vault
NEXT_PUBLIC_VAULT_PATH=./demo-vault

# 默认学段：小学/初中/高中
NEXT_PUBLIC_DEFAULT_GRADE=初中
# 可选学段下拉列表，逗号分隔
NEXT_PUBLIC_GRADE_LIST=初中,高中
# 默认分类后缀（匹配你代码里的「高中数学」）
NEXT_PUBLIC_DEFAULT_SUBJECT_SUFFIX=数学
# Pandoc 路径（可选，不配置会自动检测项目内的 pandoc）
# PANDOC_PATH=D:\桌面\math-atlas\src\tool\pandoc-3.10\pandoc.exe
```

更多细节参见 `demo-vault/` 目录。

---

## 功能

- 按年级、来源、题型、难度、知识点筛选题目
- 勾选题目生成讲义（Markdown / LaTeX 打包下载，含图片）
- 深色/浅色模式切换
- Obsidian 一键跳转
- 试题篮功能
- word导出功能，适配ee

``````

---

## 168 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T1.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T1.md) · SHA c4f3fb433d95ef48d2f5791800caf3f6d0bcab3c · mode 100644

``````markdown
---
qid: 1781356597883061
grade: 高三
source: 25全国1
number: T1
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 求复数的实部与虚部
  - 复数代数形式的乘法运算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
$(1 + 5\mathrm{i})\mathrm{i}$ 的虚部为 [选]

## 选项
A．$-1$
B．$0$
C．$1$
D．$6$

## 备注

### 我的备注

### AI备注


## 答案
C

## 解析
因为 $(1+5i)i=i+5i^{2}=-5+i$ ，所以其虚部为1，故选：C.

``````

---

## 169 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T10.md) · SHA 0e6b66436478b75548dae5695b006a6edca2c810 · mode 100644

``````markdown
---
qid: 1781356597886900
grade: 高三
source: 25全国1
number: T10
type: 多选题
difficulty: 0.4
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 抛物线定义的理解
  - 求直线与抛物线相交所得弦的弦长
  - 与抛物线焦点弦有关的几何性质
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知抛物线 $C: y^{2} = 6x$ 的焦点为 $F$ , 过 $F$ 的一条直线交 $C$ 于 $A, B$ 两点, 过 $A$ 作直线 $l: x = -\dfrac{3}{2}$ 的垂线, 垂足为 $D$ , 过 $F$ 且与直线 $AB$ 垂直的直线交 $l$ 于点 $E$ , 则 [选]

## 选项
A．$\left|AD\right|=\left|AF\right|$
B．$|AE|=|AB|$
C．$|AB| \geq 6$
D．$|AE|\cdot|BE|\geq18$

## 备注

### 我的备注

### AI备注


## 答案
ACD

## 解析
法一：对于 A，对于抛物线 $C: y^{2} = 6x$ ，则 $p = 3$ ，其准线方程为 $x = -\dfrac{3}{2}$ ，焦点 $F\left(\dfrac{3}{2},0\right)$ ，则 $|AD|$ 为抛物线上点到准线的距离， $|AF|$ 为抛物线上点到焦点的距离，

![](images/46eb6054be64910ae3d3ac25defd9f2bb124b7363caf5e03c559cacf52cfdcb2.jpg)

由抛物线的定义可知， $|AD|=|AF|$ ，故 A 正确；

对于 B，过点 B 作准线 l 的垂线，交于点 P，由题意可知 $AD \perp l, EF \perp AB$ ，则 $\angle ADE = \angle AFE = 90^{\circ}$ ，又 $|AD|=|AF|$ ， $|AE|=|AE|$ ，所以 $\triangle ADE\cong\triangle AFE$ ，所以 $\angle AED = \angle AEF$ ，同理 $\angle BEP = \angle BEF$ ，又 $\angle AED + \angle AEF + \angle BEP + \angle BEF = 180^{\circ}$ ，所以 $\angle AEF + \angle BEF = 90^{\circ}$ ，即 $\angle AEB = 90^{\circ}$ ，显然 AB 为 $\triangle ABE$ 的斜边，则 $|AE| < |AB|$ ，故 B 错误；

对于 C，易知直线 AB 的斜率不为 0，设直线 AB 的方程为 $x = my + \dfrac{3}{2}$ ， $A(x_{1}, y_{1}), B(x_{2}, y_{2})$ ，联立 $\left\{\begin{aligned}x&=my+\dfrac{3}{2},\\ y^{2}&=6x\end{aligned}\right.$ ，得 $y^{2}-6my-9=0$ ，易知 $\Delta > 0$ ，则 $y_{1} + y_{2} = 6m, y_{1}y_{2} = -9$ ，又 $x_{1} = my_{1} + \dfrac{3}{2}, x_{2} = my_{2} + \dfrac{3}{2}$ ，所以 $|AB|=x_{1}+x_{2}+p=m(y_{1}+y_{2})+3+3=6m^{2}+6\geq6$ ，当且仅当 m=0 时取等号，故 C 正确；

对于 D，在 Rt△ABE 与 Rt△AEF 中，∠BAE = ∠EAF，所以 $\mathrm{Rt}_{\triangle}ABE\sim \mathrm{Rt}_{\triangle}AEF$ ，则 $\dfrac{|AE|}{|AB|} = \dfrac{|AF|}{|AE|}$ ，即 $|AE|^2 = |AF|\cdot |AB|$ ，同理 $\left|BE\right|^{2}=\left|BF\right|\cdot\left|AB\right|$ ，又 $\left|AF\right|\cdot\left|BF\right|=\left(x_{1}+\dfrac{3}{2}\right)\left(x_{2}+\dfrac{3}{2}\right)=\left(my_{1}+3\right)\left(my_{2}+3\right)$

$$
= m^{2} y_{1} y_{2} + 3m\left(y_{1} + y_{2}\right) + 9 = -9m^{2} + 18m^{2} + 9 = 9\left(m^{2} + 1\right),
$$

$$
\left|AB\right| = 6m^{2} + 6 = 6(m^{2} + 1),
$$

所以 $\left|AE\right|^{2}\cdot\left|BE\right|^{2}=\left|BF\right|\cdot\left|AF\right|\cdot\left|AB\right|^{2}=9(m^{2}+1)\times36(m^{2}+1)^{2}$ ，则 $|AE|\cdot|BE|=3(m^{2}+1)^{\frac{1}{2}}\times6(m^{2}+1)=18(m^{2}+1)^{\frac{3}{2}}\geq18$ ，故D正确. 故选：ACD.

法二：对于 A，对于抛物线 $C: y^{2} = 6x$ ，则 p=3，其准线方程为 $x=-\dfrac{3}{2}$ ，焦点 $F\left(\dfrac{3}{2},0\right)$ ，则 $|AD|$ 为抛物线上点到准线的距离， $|AF|$ 为抛物线上点到焦点的距离，

![](images/8e12874f576033f685a2e790b6a2674ac0b9dfc4fb27a017389bd20cd9978b1a.jpg)

由抛物线的定义可知， $|AD|=|AF|$ ，故 A 正确；

对于 B，过点 B 作准线 l 的垂线，交于点 P，由题意可知 $AD \perp l, EF \perp AB$ ，则 $\angle ADE = \angle AFE = 90^{\circ}$ ，又 $|AD|=|AF|$ ， $|AE|=|AE|$ ，所以 $\triangle ADE\cong\triangle AFE$ ，所以 $\angle AED = \angle AEF$ ，同理 $\angle BEP = \angle BEF$ ，又 $\angle AED + \angle AEF + \angle BEP + \angle BEF = 180^{\circ}$ ，所以 $\angle AEF + \angle BEF = 90^{\circ}$ ，即 $\angle AEB = 90^{\circ}$ ，显然 AB 为 $\triangle ABE$ 的斜边，则 $|AE| < |AB|$ ，故 B 错误；

对于 C，当直线 AB 的斜率不存在时， $|AB|=2p=6$ ；当直线 AB 的斜率存在时，设直线 AB 方程为 $y = k \left( x - \dfrac{3}{2} \right)$ ，联立 $\left\{\begin{aligned}y&=k\left(x-\dfrac{3}{2}\right),\\ y^{2}&=6x\end{aligned}\right.$ ，消去y，得 $k^{2}x^{2}-\left(3k^{2}+6\right)x+\dfrac{9}{4}k^{2}=0$ ，易知 $\Delta > 0$ ，则 $x_{1} + x_{2} = 3 + \dfrac{6}{k^{2}}, x_{1}x_{2} = \dfrac{9}{4}$ ，所以 $\left|AB\right|=\sqrt{1+k^{2}}\left|x_{1}-x_{2}\right|=\sqrt{1+k^{2}}\times\sqrt{\left(x_{1}+x_{2}\right)^{2}-4x_{1}x_{2}}$

$$
= \sqrt{1 + k^{2}} \times \sqrt{\left(3 + \dfrac{6}{k^{2}}\right)^{2} - 9} = 6\left(1 + \dfrac{1}{k^{2}}\right) > 6,
$$

综上， $|AB|\geq6$ ，故C正确；

对于 D，在 Rt△ABE 与 Rt△AEF 中，∠BAE = ∠EAF，所以 $\mathrm{Rt}_{\triangle}ABE\sim \mathrm{Rt}_{\triangle}AEF$ ，则 $\dfrac{|AE|}{|AB|} = \dfrac{|AF|}{|AE|}$ ，即 $\left|AE\right|^2 = \left|AF\right|\cdot \left|AB\right|$ ，同理 $\left|BE\right|^{2}=\left|BF\right|\cdot\left|AB\right|$ ，当直线 $AB$ 的斜率不存在时， $|AB| = 6$ ， $|AF| = |BF| = \dfrac{1}{2} |AB| = 3$ ；所以 $\left|AE\right|^{2}\cdot\left|BE\right|^{2}=\left|BF\right|\cdot\left|AF\right|\cdot\left|AB\right|^{2}=3\times3\times6^{2}$ ，即 $\left|AE\right|\cdot\left|BE\right|=18$ ；当直线 AB 的斜率存在时， $\left|AB\right|=6\left(1+\dfrac{1}{k^{2}}\right)$ ，

$$
\left|AF\right|\cdot\left|BF\right| = \left(x_{1} + \dfrac{3}{2}\right)\left(x_{2} + \dfrac{3}{2}\right) = x_{1}x_{2} + \dfrac{3}{2}\left(x_{1} + x_{2}\right) + \dfrac{9}{4}
$$

$$
= \dfrac{9}{4} + \dfrac{3}{2}\left(3 + \dfrac{6}{k^{2}}\right) + \dfrac{9}{4} = 9\left(1 + \dfrac{1}{k^{2}}\right),
$$

所以 $\left|AE\right|^{2}\cdot\left|BE\right|^{2}=\left|BF\right|\cdot\left|AF\right|\cdot\left|AB\right|^{2}=9\left(1+\dfrac{1}{k^{2}}\right)\times36\left(1+\dfrac{1}{k^{2}}\right)^{2}$ ，则 $|AE|\cdot|BE|=3\left(1+\dfrac{1}{k^{2}}\right)^{\frac{1}{2}}\times6\left(1+\dfrac{1}{k^{2}}\right)=18\left(1+\dfrac{1}{k^{2}}\right)^{\frac{3}{2}}>18$ ；综上， $|AE|\cdot|BE|\geq18$ ，故D正确. 故选：ACD.

``````

---

## 170 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T11.md) · SHA ba8ec0f4d7946796cafee68d3e62ba1923b92b52 · mode 100644

``````markdown
---
qid: 1781356597886622
grade: 高三
source: 25全国1
number: T11
type: 多选题
difficulty: 0.4
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 比较正弦值的大小
  - 二倍角的余弦公式
  - 三角恒等变换的化简问题
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知 $\triangle ABC$ 的面积为 $\dfrac{1}{4}$ , 若 $\cos 2A + \cos 2B + 2\sin C = 2$, $\cos A\cos B\sin C = \dfrac{1}{4}$ , 则 [选]

## 选项
A．$\sin C = \sin^2 A + \sin^2 B$
B．$AB = \sqrt{2}$
C．$\sin A + \sin B = \dfrac{\sqrt{6}}{2}$
D．$AC^2 + BC^2 = 3$

## 备注

### 我的备注

### AI备注


## 答案
ABC

## 解析
$\cos 2A + \cos 2B + 2\sin C = 2$ ，由二倍角公式， $1 - 2\sin^2 A + 1 - 2\sin^2 B + 2\sin C = 2$ ，整理可得， $\sin C = \sin^2 A + \sin^2 B$ ，A选项正确；

由诱导公式， $\sin (A + B) = \sin (\pi -C) = \sin C$ ，展开可得 $\sin A \cos B + \sin B \cos A = \sin^{2} A + \sin^{2} B$ ，即 $\sin A(\sin A - \cos B) + \sin B(\sin B - \cos A) = 0$ ，下证 $C = \dfrac{\pi}{2}$

## 方法一：分类讨论

若 $A + B = \dfrac{\pi}{2}$ ，则 $\sin A = \cos B, \sin B = \cos A$ 可知等式成立；

若 $A + B < \dfrac{\pi}{2}$ ，即 $A < \dfrac{\pi}{2} - B$ ，由诱导公式和正弦函数的单调性可知， $\sin A < \cos B$ ，同理 $\sin B < \cos A$ ，又 $\sin A > 0, \sin B > 0$ ，于是 $\sin A(\sin A - \cos B) + \sin B(\sin B - \cos A) < 0$ ，与条件不符，则 $A + B < \dfrac{\pi}{2}$ 不成立；

若 $A + B > \dfrac{\pi}{2}$ ，类似可推导出 $\sin A(\sin A - \cos B) + \sin B(\sin B - \cos A) > 0$ ，则 $A + B > \dfrac{\pi}{2}$ 不成立。综上讨论可知， $A + B = \dfrac{\pi}{2}$ ，即 $C = \dfrac{\pi}{2}$ 。

## 方法二：边角转化

$\sin C = \sin^{2} A + \sin^{2} B$ 时，由 $C \in (0, \pi)$ ，则 $\sin C \in (0, 1]$ ，于是 $1\times\sin C=\sin^{2}A+\sin^{2}B\geq\sin^{2}C$ ，由正弦定理， $a^2 + b^2 \geq c^2$ ，由余弦定理可知， $\cos C \geq 0$ ，则 $C \in (0, \dfrac{\pi}{2}]$ ，若 $C \in (0, \dfrac{\pi}{2})$ ，则 $A + B > \dfrac{\pi}{2}$ ，注意到 $\cos A \cos B \sin C = \dfrac{1}{4}$ ，则 $\cos A \cos B > 0$ ，于是 $\cos A > 0, \cos B > 0$ （两者同负会有两个钝角，不成立），于是 $A, B \in \left(0, \dfrac{\pi}{2}\right)$ ，结合 $A + B > \dfrac{\pi}{2} \Leftrightarrow A > \dfrac{\pi}{2} - B$ ，而 $A, \dfrac{\pi}{2} - B$ 都是锐角，则 $\sin A > \sin \left( \dfrac{\pi}{2} - B \right) = \cos B > 0$ ，于是 $\sin C = \sin^2 A + \sin^2 B > \cos^2 B + \sin^2 B = 1$ ，这和 $\sin C \leq 1$ 相矛盾，故 $C \in (0, \dfrac{\pi}{2})$ 不成立，则 $C = \dfrac{\pi}{2}$

## 方法三：结合射影定理（方法一改进）

由 $\sin C = \sin^{2} A + \sin^{2} B$ ，结合正弦定理可得， $c = a \sin A + b \sin B$ ，由射影定理可得 $c=a\cos B+b\cos A$ ，于是 $a\sin A+b\sin B=a\cos B+b\cos A$ ，则 $a(\sin A - \cos B) + b(\sin B - \cos A) = 0$ ，可同方法一种讨论的角度，推出 $A + B = \dfrac{\pi}{2}$ ，

## 方法四：和差化积（方法一改进）

续法三： $a(\sin A - \cos B) + b(\sin B - \cos A) = 0$ ，可知 $\sin A - \cos B, \sin B - \cos A$ 同时为0或者异号，即 $(\sin A - \cos B)(\sin B - \cos A) \leq 0$ ，展开可得， $\sin A\sin B-\sin A\cos A-\cos B\sin B+\cos A\cos B\leq0,$ 即 $\cos(A-B)-\dfrac{1}{2}\left(\sin2A+\sin2B\right)\leq0$ ，结合和差化积， $\cos(A-B)\left(1-\sin(A+B)\right)\leq0$ ，由上述分析， $A,B\in\left(0,\dfrac{\pi}{2}\right)$ ，则 $A-B\in\left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)$ ，则 $\cos(A-B)\geq0$ ，则 $1-\sin(A+B)\leq0$ ，即 $\sin C\geq1$ ，于是 $\sin C=1$ ，可知 $C=\dfrac{\pi}{2}$ .

由 $\cos A\cos B\sin C = \dfrac{1}{4} = \cos A\cos B$ ，由 $A + B = \dfrac{\pi}{2}$ ，则 $\cos B = \sin A$ ，即 $\sin A\cos A = \dfrac{1}{4}$ ，则 $\sin 2A = \dfrac{1}{2}$ ，同理 $\sin 2B = \dfrac{1}{2}$ ，由上述推导， $A, B \in \left(0, \dfrac{\pi}{2}\right)$ ，则 $2A, 2B \in (0, \pi)$ ，不妨设 A < B，则 $2A = \dfrac{\pi}{6}, 2B = \dfrac{5\pi}{6}$ ，即 $A = \dfrac{\pi}{12}, B = \dfrac{5\pi}{12}$ ，由两角和差的正弦公式可知 $\sin \dfrac{\pi}{12} +\sin \dfrac{5\pi}{12} = \dfrac{\sqrt{6} - \sqrt{2}}{4} +\dfrac{\sqrt{6} + \sqrt{2}}{4} = \dfrac{\sqrt{6}}{2}$ ，C选项正确

由两角和的正切公式可得， $\tan \dfrac{5\pi}{12} = 2 + \sqrt{3}$ ，设 $BC = t, AC = (2 + \sqrt{3})t$ ，则 $AB = (\sqrt{2} + \sqrt{6})t$ ，由 $S_{\triangle ABC} = \dfrac{1}{2} (2 + \sqrt{3})t^2 = \dfrac{1}{4}$ ，则 $t^2 = \dfrac{4 - 2\sqrt{3}}{4} = \left(\dfrac{\sqrt{3} - 1}{2}\right)^2$ ，则 $t = \dfrac{\sqrt{3} - 1}{2}$ ，于是 $AB = (\sqrt{6} +\sqrt{2})t = \sqrt{2}$ ，B选项正确，由勾股定理可知， $AC^2 +BC^2 = 2$ ，D选项错误

![](images/377af0ea35a51fe20840b568c60e4a63d25f773ab3520853d1ff9454907dec53.jpg)

故选：ABC

``````

---

## 171 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T12.md) · SHA 2a5e700ce07a338d82105968a5c057a939b5e6f7 · mode 100644

``````markdown
---
qid: 1781356597887022
grade: 高三
source: 25全国1
number: T12
type: 填空题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 已知切线（斜率）求参数
  - 导数的加减法
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
若直线 $y = 2x + 5$ 是曲线 $y = e^{x} + x + a$ 的一条切线，则 $a =$ [填]

## 备注

### 我的备注

### AI备注


## 答案
$4$

## 解析
法一：对于 $y=e^{x}+x+a$ ，其导数为 $y'=e^{x}+1$ ，因为直线 $y=2x+5$ 是曲线的切线，直线的斜率为 2，令 $y' = e^{x} + 1 = 2$ ，即 $e^{x} = 1$ ，解得 x = 0，将 x=0 代入切线方程 $y=2x+5$ ，可得 $y=2\times0+5=5$ ，所以切点坐标为(0,5)，因为切点(0,5)在曲线 $y=e^{x}+x+a$ 上，所以 $5 = e^{0} + 0 + a$ ，即 $5 = 1 + a$ ，解得 a = 4。故答案为：4.

法二：对于 $y=e^{x}+x+a$ ，其导数为 $y' = e^{x} + 1$ ，假设 $y=2x+5$ 与 $y=e^{x}+x+a$ 的切点为 $(x_{0},y_{0})$ , 则 $\left\{ \begin{array}{l} \mathrm{e}^{x_0} + 1 = 2 \\ y_0 = 2x_0 + 5 \\ y_0 = \mathrm{e}^{x_0} + x_0 + a \end{array} \right.$ ，解得 $a = 4$ . 故答案为：4.

``````

---

## 172 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T13.md) · SHA 4d99a855d68e2e28a7940b8e5d6bcc947c348bec · mode 100644

``````markdown
---
qid: 1781356597888856
grade: 高三
source: 25全国1
number: T13
type: 填空题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 等比数列通项公式的基本量计算
  - 等比数列前 n 项和的基本量计算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
若一个等比数列的各项均为正数，且前 4 项的和等于 4，前 8 项的和等于 68，则这个数列的公比等于 [填]

## 备注

### 我的备注

### AI备注


## 答案
$2$

## 解析
法一：设该等比数列为 $\left\{a_{n}\right\}$ ， $S_{n}$ 是其前n项和，则 $S_{4}=4,S_{8}=68$ ，设 $\left\{a_{n}\right\}$ 的公比为 $q(q>0)$ ，当 q=1 时， $S_{4}=4a_{1}=4$ ，即 $a_{1}=1$ ，则 $S_{8}=8a_{1}=8\neq68$ ，显然不成立，舍去；当 $q \neq 1$ 时，则 $S_{4} = \dfrac{a_{1}(1 - q^{4})}{1 - q} = 4, S_{8} = \dfrac{a_{1}(1 - q^{8})}{1 - q} = 68$ ，两式相除得 $\dfrac{1 - q^8}{1 - q^4} = \dfrac{68}{4}$ ，即 $\dfrac{(1 - q^4)(1 + q^4)}{1 - q^4} = 17$ ，则 $1+q^{4}=17$ ，所以q=2，所以该等比数列公比为 2. 故答案为：2.

法二：设该等比数列为 $\left\{a_{n}\right\}$ ， $S_{n}$ 是其前n项和，则 $S_{4}=4,S_{8}=68$ ，设 $\left\{a_{n}\right\}$ 的公比为 $q(q>0)$ ，所以 $S_{4}=a_{1}+a_{2}+a_{3}+a_{4}=4$

$$
S_{8} = a_{1} + a_{2} + a_{3} + a_{4} + a_{5} + a_{6} + a_{7} + a_{8}
$$

$$
= a_{1} + a_{2} + a_{3} + a_{4} + a_{1} q^{4} + a_{2} q^{4} + a_{3} q^{4} + a_{4} q^{4}
$$

$$
= \left(a_{1} + a_{2} + a_{3} + a_{4}\right) \left(1 + q^{4}\right) = 68,
$$

所以 $4\left(1 + q^4\right) = 68$ ，则 $1 + q^4 = 17$ ，所以 $q = 2$ ，所以该等比数列公比为 2. 故答案为：2.

法三：设该等比数列为 $\left\{a_{n}\right\}$ ， $S_{n}$ 是其前n项和，则 $S_{4}=4,S_{8}=68$ ，设 $\left\{a_{n}\right\}$ 的公比为 $q(q>0)$ ，因为 $S_{8} - S_{4} = a_{5} + a_{6} + a_{7} + a_{8} = (a_{1} + a_{2} + a_{3} + a_{4})q^{4} = 68 - 4 = 64$ ，又 $S_{4} = a_{1} + a_{2} + a_{3} + a_{4} = 4$ ，所以 $\dfrac{S_8 - S_4}{S_4} = q^4 = \dfrac{64}{4} = 16$ ，所以 $q = 2$ ，所以该等比数列公比为2. 故答案为：2.

``````

---

## 173 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T14.md) · SHA 9f0d046cbbf636cc899ef4d6ec5cda3d3406220e · mode 100644

``````markdown
---
qid: 1781356597888832
grade: 高三
source: 25全国1
number: T14
type: 填空题
difficulty: 0.4
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 写出简单离散型随机变量分布列
  - 求离散型随机变量的均值
  - 均值的性质
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
有 5 个相同的球, 分别标有数字 1, 2, 3, 4, 5, 从中有放回地随机取 3 次, 每次取 1 个球. 记 $X$ 为这 5 个球中至少被取出 1 次的球的个数, 则 $X$ 的数学期望 $E(X) =$ [填]

## 备注

### 我的备注

### AI备注


## 答案
$\dfrac{61}{25} / 2.44$

## 解析
法一：依题意，X 的可能取值为 1、2、3，总的选取可能数为 $5^{3}=125$ ，其中 X=1：三次抽取同一球，选择球的编号有 5 种方式，故 $P(X=1)=\dfrac{5}{125}=\dfrac{1}{25}$ , X=2：恰好两种不同球被取出（即一球出现两次，另一球出现一次），选取出现两次的球有 5 种方式，选取出现一次的球有 4 种方式，其中选取出现一次球的位置有 3 种可能，故事件 X=2 的可能情况有 $5 \times 4 \times 3 = 60$ 种，故 $P(X=2)=\dfrac{60}{125}=\dfrac{12}{25}$ , $X = 3$ ：三种不同球被取出，由排列数可知事件 X=3 的可能情有况 $5 \times 4 \times 3 = 60$ 种，故 $P(X=3)=\dfrac{60}{125}=\dfrac{12}{25}$ , 所以 $E(X)=1\times P(X=1)+2\times P(X=2)+3\times P(X=3)$

$$
= 1 \times \dfrac{5}{125} + 2 \times \dfrac{12}{25} + 3 \times \dfrac{12}{25} = \dfrac{61}{25}.
$$

故答案为： $\dfrac{61}{25}$

法二：依题意，假设随机变量 $X_{i}$ ，其中i=1,2,3,4,5：其中 $X_{i}=\left\{\begin{aligned}&1,\\ &0,\\ &\end{aligned}\right.$ 这3次选取中,球i至少被取出一次，则 $X=\sum_{i=1}^{5}X_{i}$ ，由于球的对称性，易知所有 $E[X_i]$ 相等，则由期望的线性性质，得 $E[X] = E\left[\sum_{i=1}^{5} X_i\right] = \sum_{i=1}^{5} E[X_i] = 5E[X_i]$ ，由题意可知，球i在单次抽取中未被取出的概率为 $\dfrac{4}{5}$ ，由于抽取独立，三次均未取出球 $i$ 的概率为 $P(X_{i} = 0) = \left(\dfrac{4}{5}\right)^{3} = \dfrac{64}{125}$ ，因此球 $i$ 至少被取出一次的概率为： $P(X_{i} = 1) = 1 - \dfrac{64}{125} = \dfrac{61}{125}$ ，故 $E[X_{i}]=\dfrac{61}{125}$ , 所以 $E[X]=5E\left[X_{i}\right]=5\times\dfrac{61}{125}=\dfrac{61}{25}$ . 故答案为： $\dfrac{61}{25}$

``````

---

## 174 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T15.md) · SHA 08779ad4fab1b5eb07a71fe246ad718c01dc0b69 · mode 100644

``````markdown
---
qid: 1781356597889395
grade: 高三
source: 25全国1
number: T15
type: 解答题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 独立性检验解决实际问题
  - 计算古典概型问题的概率
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
为研究某疾病与超声波检查结果的关系，从做过超声波检查的人群中随机调查了 1000 人，得到如下列联表：

<table><tr><td>超声波检查结果组别</td><td>正常</td><td>不正常</td><td>合计</td></tr><tr><td>患该疾病</td><td>20</td><td>180</td><td>200</td></tr><tr><td>未患该疾病</td><td>780</td><td>20</td><td>800</td></tr><tr><td>合计</td><td>800</td><td>200</td><td>1000</td></tr></table>

(1)记超声波检查结果不正常者患该疾病的概率为 p，求 p 的估计值；

(2)根据小概率值 $\alpha = 0.001$ 的独立性检验，分析超声波检查结果是否与患该疾病有关.

附 $\chi^{2}=\dfrac{n(ad-bc)^{2}}{(a+b)(c+d)(a+c)(b+d)}$ ,

<table><tr><td>$P(\chi^{2} \geq k)$</td><td>0.050</td><td>0.010</td><td>0.001</td></tr><tr><td>$k$</td><td>3.841</td><td>6.635</td><td>10.828</td></tr></table>

## 备注

### 我的备注

### AI备注


## 答案
(1) $\dfrac{9}{10}$

(2)有关

## 解析
（1）根据表格可知，检查结果不正常的200人中有180人患病，所以 $p$ 的估计值为 $\dfrac{180}{200} = \dfrac{9}{10}$ ;

(2) 零假设为 $H_{0}$ : 超声波检查结果与患病无关, 根据表中数据可得， $\chi^{2}=\dfrac{1000\times(20\times20-780\times180)^{2}}{800\times200\times800\times200}=765.625>10.828=x_{0.001}$ ，根据小概率值 $\alpha = 0.001$ 的 $\chi^{2}$ 独立性检验，我们推断 $H_{0}$ 不成立，即认为超声波检查结果与患该病有关，该推断犯错误的概率不超过 0.001.

``````

---

## 175 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T16.md) · SHA 650e14ec70bf28947fdf15215f52ff6f42bd5b16 · mode 100644

``````markdown
---
qid: 1781356597890269
grade: 高三
source: 25全国1
number: T16
type: 解答题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 导数的运算法则
  - 由递推关系证明数列是等差数列
  - 求等比数列前 n 项和
  - 错位相减法求和
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知数列 $\{a_{n}\}$ 中， $a_{1} = 3$ ， $\dfrac{a_{n+1}}{n} = \dfrac{a_{n}}{n+1} + \dfrac{1}{n(n+1)}$ .

(1)证明：数列 $\{na_{n}\}$ 是等差数列；

(2)给定正整数 $m$，设函数 $f(x)=a_{1}x+a_{2}x^{2}+\cdots+a_{m}x^{m}$ ，求 $f'(-2)$ .

## 备注

### 我的备注

### AI备注


## 答案
(1)证明见解析;

(2) $f^{\prime}(-2)=\dfrac{7}{9}-\dfrac{(3m+7)(-2)^{m}}{9}$

## 解析
（1）由题意证明如下， $n \in N^{*}$ ，在数列 $\{a_{n}\}$ 中， $a_1 = 3$ ， $\dfrac{a_{n + 1}}{n} = \dfrac{a_n}{n + 1} +\dfrac{1}{n(n + 1)}$ ， $\therefore (n+1)a_{n+1}=na_{n}+1$ ，即 $(n+1)a_{n+1}-na_{n}=1$ ，∴ $\left\{na_{n}\right\}$ 是以 $a_{1}=3$ 为首项，1 为公差的等差数列.

（2）由题意及（1）得， $n \in N^{*}$ ，在数列 $\left\{na_{n}\right\}$ 中，首项为3，公差为1，∴ $na_{n}=3+1\times(n-1)$ ，即 $a_{n}=1+\dfrac{2}{n}$ ,在 $f(x)=a_{1}x+a_{2}x^{2}+\cdots+a_{m}x^{m}$ 中，

$$
f(x) = 3x + 2x^{2} + \dots + \left(1 + \dfrac{2}{m}\right) x^{m}, f^{\prime}(x) = 3 + 4x + \dots + (m + 2) x^{m - 1}
$$

$$
\therefore \left\{ \begin{array}{l} f^{\prime}(x) = 3 + 4x + \dots + (m + 2) x^{m - 1} \\ x f^{\prime}(x) = 3x + 4x^{2} + \dots + (m + 2) x^{m} \end{array} , \right.
$$

当 $x \neq 1$ 且 $x \neq 0$ 时，

$$
\therefore (1 - x) f^{\prime}(x) = 3 + x + x^{2} + \dots + x^{m - 1} - (m + 2) x^{m} = 3 + \dfrac{x (1 - x^{m - 1})}{1 - x} - (m + 2) x^{m},
$$

$$
\therefore f^{\prime}(x) = \dfrac{3}{1 - x} + \dfrac{x (1 - x^{m - 1})}{(1 - x)^{2}} - \dfrac{(m + 2) x^{m}}{1 - x}
$$

$$
\begin{array}{l} \therefore f^{\prime}(-2) = \dfrac{3}{1 - (-2)} + \dfrac{-2 [1 - (-2)^{m - 1}]}{[1 - (-2)]^{2}} - \dfrac{(m + 2) (-2)^{m}}{1 - (-2)} \\ = 1 + \dfrac{(-2) [1 - (-2)^{m - 1}]}{9} - \dfrac{(m + 2) (-2)^{m}}{3} \\ = 1 - \dfrac{2}{9} - \dfrac{(-2)^{m}}{9} - \dfrac{(m + 2) (-2)^{m}}{3} \\ = \dfrac{7}{9} - \dfrac{(3m + 7) (-2)^{m}}{9}. \\ \end{array}
$$

``````

---

## 176 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T17.md) · SHA 848b2c0dd99cfaa552df1bdd44e15d006adcb3e3 · mode 100644

``````markdown
---
qid: 1781356597890427
grade: 高三
source: 25全国1
number: T17
type: 解答题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 多面体与球体内切外接问题
  - 求异面直线所成的角
  - 证明面面垂直
  - 异面直线夹角的向量求法
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
如图,在四棱锥 P-ABCD 中， $PA \perp$ 底面 ABCD， $AB \perp AD, BC \parallel AD$ .

![](images/cd63147719c298e52e8a388bac13a762ebe352f374be57f63c1a0d50255d9d55.jpg)

(1)证明：平面 $PAB \perp$ 平面 $PAD$ ；

(2)设 $PA = AB = \sqrt{2}$ , $BC = 2$ , $AD = 1 + \sqrt{3}$ ，且点 $P$ , $B$ , $C$ , $D$ 均在球 $O$ 的球面上.

(i) 证明：点 O 在平面 ABCD 内；

（ii）求直线 AC 与 PO 所成角的余弦值.

## 备注

### 我的备注

### AI备注


## 答案
(1)证明：由题意证明如下，在四棱锥 P-ABCD 中， $PA \perp$ 平面 ABCD， $AB \perp AD$ ， $AB \subset$ 平面 ABCD， $AD \subset$ 平面 ABCD， $\therefore AP \perp AB, AP \perp AD$ ，∵ $AP \subset$ 平面 PAD， $AD \subset$ 平面 PAD， $AP \cap AD = A$ ，∴ $AB \perp$ 平面 PAD，∵ $AB \subset$ 平面 PAB，∴平面 $PAB \perp$ 平面 PAD.

(2) (i) 证明: 由题意及 (1) 证明如下, 在四棱锥 P-ABCD 中， $AP \perp AB$ ， $AP \perp AD$ ， $AB \perp AD$ ， $BC \parallel AD$ ， $PA = AB = \sqrt{2}, \quad AD = 1 + \sqrt{3}$ , 建立空间直角坐标系如下图所示，

![](images/156027def48bf21289d87dc8f6bcde5fe88420a925daa51c3beddf5220261988.jpg)

$\therefore A(0,0,0), B(\sqrt{2},0,0), C(\sqrt{2},2,0), D(0,1+\sqrt{3},0), P(0,0,\sqrt{2})$ , 若 $P$ ， $B$ ， $C$ ， $D$ 在同一个球面上，则 $\left|OP\right|=\left|OB\right|=\left|OC\right|=\left|OD\right|$ , 在平面 $xAy$ 中，

![](images/e24c8950a00f714b738fdd6a696490d2174c3e6478e900b9924b1baff02477cc.jpg)

$\therefore A(0,0), B(\sqrt{2},0), C(\sqrt{2},2), D(0,1+\sqrt{3})$ , ∴线段 CD 中点坐标 $F\left(\dfrac{\sqrt{2}}{2}, \dfrac{\sqrt{3} + 3}{2}\right)$ , 直线 $CD$ 的斜率： $k_{1} = \dfrac{1 + \sqrt{3} - 2}{0 - \sqrt{2}} = -\dfrac{\sqrt{3} - 1}{\sqrt{2}}$ ，直线 $CD$ 的垂直平分线 $EF$ 斜率： $k_{2} = \dfrac{\sqrt{2}}{\sqrt{3} - 1} = \dfrac{\sqrt{6} + \sqrt{2}}{2}$ ，∴直线 EF 的方程： $y-\dfrac{\sqrt{3}+3}{2}=\dfrac{\sqrt{6}+\sqrt{2}}{2}\left(x-\dfrac{\sqrt{2}}{2}\right)$ , 即 $y=\dfrac{\sqrt{6}+\sqrt{2}}{2}\left(x-\dfrac{\sqrt{2}}{2}\right)+\dfrac{\sqrt{3}+3}{2}$ , 当 $y = 1$ 时， $1 = \dfrac{\sqrt{6} + \sqrt{2}}{2}\left(x_{O} - \dfrac{\sqrt{2}}{2}\right) + \dfrac{\sqrt{3} + 3}{2}$ ，解得： $x_{O} = 0$ ， $\therefore O(0,1)$ ，在立体几何中， $O(0,1,0)$ ，

$$
\because \left\{ \begin{array}{l} |OP| = \sqrt{0^{2} + 1^{2} + (0 - \sqrt{2})^{2}} \\ |OB| = \sqrt{(0 - \sqrt{2})^{2} + 1^{2} + 0^{2}} \\ |OC| = \sqrt{(0 - \sqrt{2})^{2} + (1 - 2)^{2} + 0^{2}} \\ |OD| = \sqrt{0^{2} + (1 - 1 - \sqrt{3})^{2} + 0^{2}} \end{array} \right.
$$

解得： $\left|OP\right|=\left|OB\right|=\left|OC\right|=\left|OD\right|=\sqrt{3}$ ∴点O在平面ABCD上.

(ii) $\dfrac{\sqrt{2}}{3}$ .

## 解析
（1）略

(2) (i) 略

（ii）由题意，（1）（2）（ii）及图得，

![](images/e149fac76ec45f091049650779ab2493fca02696eea6e7ce16cfa65e576afd40.jpg)

$$
\overrightarrow{AC} = (\sqrt{2}, 2, 0), \overrightarrow{PO} = (0, 1, -\sqrt{2}),
$$

设直线 AC 与直线 PO 所成角为 $\theta$ ，

$$
\therefore \cos \theta = \dfrac{\left| \overrightarrow{AC} \cdot \overrightarrow{PO} \right|}{\left| \overrightarrow{AC} \right| \left| \overrightarrow{PO} \right|} = \dfrac{\left| 0 + 2 \times 1 + 0 \right|}{\sqrt{(\sqrt{2})^{2} + 2^{2} + 0} \times \sqrt{0 + 1^{2} + (-\sqrt{2})^{2}}} = \dfrac{\sqrt{2}}{3}.
$$

法 2: 由几何知识得， $PO = \sqrt{3}$ ， $AB \perp AD, BC \parallel AD$ ， $\therefore AB \perp BC$ ，在 Rt△ABC 中， $AB=\sqrt{2}$ ，BC=2，由勾股定理得， $AC = \sqrt{AB^{2} + BC^{2}} = \sqrt{(\sqrt{2})^{2} + 2^{2}} = \sqrt{6}$ ，过点 O 作 AC 的平行线，交 BC 的延长线为 $C_{1}$ ，连接 $AC_{1}$ ， $PC_{1}$ ，

![](images/265fb7f8512d7bc91141a6fa2a5d4a2489d5993d9789a33a4df03c4f8a3afcaf.jpg)

则 $OC_{1}=AC=\sqrt{6}$ ，直线 AC 与直线 PO 所成角即为 $\triangle POC_{1}$ 中 $\angle POC_{1}$ 或其补角. ∵ PA ⊥ 平面 ABCD， $AC_{1} \subset$ 平面 ABCD， $PA \cap AC_{1} = A$ ， $\therefore PA \perp AC_{1}$ ，在 Rt△ABC₁ 中， $AB=\sqrt{2}$ ， $BC_{1}=BC+CC_{1}=2+1=3$ ，由勾股定理得， $AC_{1} = \sqrt{AB^{2} + BC_{1}^{2}} = \sqrt{(\sqrt{2})^{2} + 3^{2}} = \sqrt{11}$ ，在 Rt△APC₁ 中， $PA = \sqrt{2}$ ，由勾股定理得， $PC_{1} = \sqrt{PA^{2} + AC_{1}^{2}} = \sqrt{(\sqrt{2})^{2} + (\sqrt{11})^{2}} = \sqrt{13}$ ，在 $\triangle POC_{1}$ 中，由余弦定理得， $PC_{1}^{2} = PO^{2} + OC_{1}^{2} - 2 PO \cdot OC_{1} \cos \angle POC_{1}$ ，即： $(\sqrt{13})^{2} = (\sqrt{3})^{2} + (\sqrt{6})^{2} - 2\sqrt{3} \times \sqrt{6} \cos \angle POC_{1}$ ，解得： $\cos \angle POC_{1} = -\dfrac{\sqrt{2}}{3}$ ，∴直线 AC 与直线 PO 所成角的余弦值为： $\left|\cos\angle POC_{1}\right|=\dfrac{\sqrt{2}}{3}$ .

``````

---

## 177 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T18.md) · SHA 9e6946529341dcace8cdd9de8da3859bb7dfdb7d · mode 100644

``````markdown
---
qid: 1781356597890783
grade: 高三
source: 25全国1
number: T18
type: 解答题
difficulty: 0.4
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 根据 a、b、c 求椭圆标准方程
  - 求椭圆中的最值问题
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知椭圆 $C: \dfrac{x^{2}}{a^{2}} + \dfrac{y^{2}}{b^{2}} = 1 (a > b > 0)$ 的离心率为 $\dfrac{2\sqrt{2}}{3}$ ，下顶点为 $A$ ，右顶点为 $B$, $|AB| = \sqrt{10}$ .

(1)求 C 的方程;

(2)已知动点 $P$ 不在 $y$ 轴上，点 $R$ 在射线 $AP$ 上，且满足 $\left|AP\right|\cdot \left|AR\right| = 3$

(i) 设 $P(m, n)$ ，求 $R$ 的坐标（用 $m$，$n$ 表示）；

(ii) 设 $O$ 为坐标原点, $Q$ 是 $C$ 上的动点, 直线 $OR$ 的斜率为直线 $OP$ 的斜率的 3 倍, 求 $|PQ|$ 的最大值.

## 备注

### 我的备注

### AI备注


## 答案
(1) $\dfrac{x^{2}}{9}+y^{2}=1$

(2)(i) $\left(\dfrac{3m}{m^{2} + (n + 1)^{2}}, \dfrac{n + 2 - m^{2} - n^{2}}{m^{2} + (n + 1)^{2}}\right)$ (ii) $3\left(\sqrt{3} + \sqrt{2}\right)$

## 解析
（1）由题可知， $A(0,-b),B(a,0)$ ，所以 $\left\{\begin{aligned}\sqrt{a^{2}+b^{2}}&=\sqrt{10}\\ e=\dfrac{c}{a}&=\dfrac{2\sqrt{2}}{3}\\ c^{2}&=a^{2}-b^{2}\end{aligned}\right.$ ，解得 $a^{2}=9,b^{2}=1,c^{2}=8$ ，故椭圆 C 的标准方程为 $\dfrac{x^{2}}{9} + y^{2} = 1$ ;

(2) (i) 设 $R(x_{0}, y_{0})$ ，易知 $m \neq 0$ ，法一：所以 $k_{AP} = \dfrac{n + 1}{m}$ ，故 $\dfrac{y_0 + 1}{x_0} = \dfrac{n + 1}{m}$ ，且 $mx_0 > 0$ ：因为 $A(0, - 1)$ ， $\left|AR\right|\left|AP\right| = 3$ ，所以 $\sqrt{x_0^{2} + (y_0 + 1)^{2}}\times \sqrt{m^{2} + (n + 1)^{2}} = 3$ ，即 $\left[1 + \left(\dfrac{n + 1}{m}\right)^{2}\right]x_0m = 3$ ，解得 $x_0 = \dfrac{3m}{m^{2} + (n + 1)^{2}}$ ，所以 $y_{0} = \dfrac{n + 2 - m^{2} - n^{2}}{m^{2} + (n + 1)^{2}}$ ，所以点 $R$ 的坐标为 $\left(\dfrac{3m}{m^{2} + (n + 1)^{2}}, \dfrac{n + 2 - m^{2} - n^{2}}{m^{2} + (n + 1)^{2}}\right)$ .

法二：设 $\overrightarrow{AR} = \lambda \overrightarrow{AP},\lambda >0$ ，则 $\left|AR\right|\left|AP\right| = 3\Rightarrow \lambda \left[m^{2} +(n + 1)^{2}\right] = 3$ ，所以

$$
\lambda = \dfrac{3}{m^{2} + (n + 1)^{2}}, \overrightarrow{AR} = \lambda \overrightarrow{AP} = \lambda (m, n + 1) = \left(\dfrac{3m}{m^{2} + (n + 1)^{2}}, \dfrac{3(n + 1)}{m^{2} + (n + 1)^{2}}\right), \text{故}
$$

点 $R$ 的坐标为 $\left(\dfrac{3m}{m^{2} + (n + 1)^{2}}, \dfrac{n + 2 - m^{2} - n^{2}}{m^{2} + (n + 1)^{2}}\right)$ .

(ii)因为 $k_{OR} = \dfrac{\dfrac{n + 2 - m^{2} - n^{2}}{m^{2} + (n + 1)^{2}}}{\dfrac{3m}{m^{2} + (n + 1)^{2}}} = \dfrac{n + 2 - m^{2} - n^{2}}{3m}, k_{OP} = \dfrac{n}{m}$ , 由 $k_{OR} = 3k_{OP}$ , 可得 $\dfrac{3n}{m} = \dfrac{n + 2 - m^{2} - n^{2}}{3m}$ , 化简得 $m^{2} + n^{2} + 8n - 2 = 0$ , 即 $m^{2} + (n + 4)^{2} = 18(m \neq 0)$ , 所以点 P 在以 $N(0,-4)$ 为圆心, $3\sqrt{2}$ 为半径的圆上（除去两个点）， $\left|PQ\right|_{\max}$ 为 Q 到圆心 N 的距离加上半径,

法一：设 $Q(3\cos \theta ,\sin \theta)$ ，所以

$$
\left| QN \right|^{2} = (3\cos \theta)^{2} + (\sin \theta + 4)^{2} = 9\cos^{2} \theta + \sin^{2} \theta + 8\sin \theta + 16
$$

$$
= 8\cos^{2} \theta + 1 + 8\sin \theta + 16
$$

$$
= 8\left(1 - \sin^{2} \theta\right) + 8\sin \theta + 17
$$

$$
= -8\sin^{2} \theta + 8\sin \theta + 25
$$

$= -8\left(\sin \theta -\dfrac{1}{2}\right)^{2} + 27\leq 27$ ，当且仅当 $\sin \theta = \dfrac{1}{2}$ 时取等号，所以 $\left|PQ\right|_{\max}=\sqrt{27}+3\sqrt{2}=3\left(\sqrt{3}+\sqrt{2}\right)$ .

法二：设 $Q\left(x_{Q},y_{Q}\right)$ ，则 $\dfrac{x_Q^{2}}{9} +y_Q^{2} = 1$

$$
\left| QN \right|^{2} = x_{Q}^{2} + \left(y_{Q} + 4\right)^{2} = 9 - 9y_{Q}^{2} + y_{Q}^{2} + 8y_{Q} + 16 = -8y_{Q}^{2} + 8y_{Q} + 25
$$

$= -8\left(y_{Q} - \dfrac{1}{2}\right)^{2} + 27 \leq 27$ ，当且仅当 $y_{Q} = \dfrac{1}{2}$ 时取等号，故 $\left|PQ\right|_{\max}=\sqrt{27}+3\sqrt{2}=3\left(\sqrt{3}+\sqrt{2}\right)$ .

``````

---

## 178 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T19.md) · SHA 934fcc9d34b10ad4333fa3e100fdea600035fb03 · mode 100644

``````markdown
---
qid: 1781356597891224
grade: 高三
source: 25全国1
number: T19
type: 解答题
difficulty: 0.15
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 由导数求函数的最值（不含参）
  - 解余弦不等式
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
（1）求函数 $f(x) = 5\cos x - \cos 5x$ 在区间 $\left[0, \dfrac{\pi}{4}\right]$ 的最大值；

（2）给定 $\theta\in(0,\pi)$ 和 $a\in R$ ，证明：存在 $y\in[a-\theta,a+\theta]$ 使得 $\cos y\leq\cos\theta$ ;

（3）设 $b \in \mathbf{R}$ ，若存在 $\varphi \in \mathbf{R}$ 使得 $5\cos x - \cos (5x + \varphi) \leq b$ 对 $x \in \mathbf{R}$ 恒成立，求 $b$ 的最小值.

## 备注

### 我的备注

### AI备注


## 答案
(1) $3\sqrt{3}$
(2)证明见解析
(3) $3\sqrt{3}$

## 解析
（1）法 1: $f'(x) = -5\sin x + 5\sin 5x = 10\cos 3x\sin 2x$ , 因为 $x \in \left[0, \dfrac{\pi}{4}\right]$ ，故 $2x \in \left[0, \dfrac{\pi}{2}\right]$ ，故 $\sin 2x \geq 0$ ，当 $0 < x < \dfrac{\pi}{6}$ 时， $\cos 3x > 0$ 即 $f'(x) > 0$ ，当 $\dfrac{\pi}{6}<x<\dfrac{\pi}{4}$ 时， $\cos3x<0$ 即 $f'(x)<0$ ，故 $f(x)$ 在 $\left(0, \dfrac{\pi}{6}\right)$ 上为增函数，在 $\left(\dfrac{\pi}{6}, \dfrac{\pi}{4}\right)$ 为减函数，故 $f(x)$ 在 $\left[0, \dfrac{\pi}{4}\right]$ 上的最大值为 $f\left(\dfrac{\pi}{6}\right)=5\cos\dfrac{\pi}{6}-\cos\dfrac{5\pi}{6}=3\sqrt{3}$ .

法2：我们有 $\cos 5x = \cos (x + 4x) = \cos x\cos 4x - \sin x\sin 4x$

$$
\begin{array}{l} = \cos x (2 \cos^{2} 2x - 1) - \sin x \cdot 2 \sin 2x \cos 2x \\ = \cos x \left(2 (2 \cos^{2} x - 1)^{2} - 1\right) - \sin x \cdot 2 \cdot 2 \sin x \cos x \cos 2x \\ = \cos x (8 \cos^{4} x - 8 \cos^{2} x + 1) - 4 \cos x \cos 2x \sin^{2} x \\ = 8 \cos^{5} x - 8 \cos^{3} x + \cos x - 4 \cos x (2 \cos^{2} x - 1) (1 - \cos^{2} x) \\ = 16 \cos^{5} x - 20 \cos^{3} x + 5 \cos x. \\ \end{array}
$$

所以：

$$
\begin{array}{l} f(x) = 5 \cos x - \cos 5x = 5 \cos x - \left(16 \cos^{5} x - 20 \cos^{3} x + 5 \cos x\right) = 20 \cos^{3} x - 16 \cos^{5} x \\ = 4 \cos^{3} x (5 - 4 \cos^{2} x) \leq 4 | \cos x |^{3} (5 - 4 | \cos x |^{2}) = 4 | \cos x |^{3} (\sqrt{5} - 2 | \cos x |) (\sqrt{5} + 2 | \cos x |) \\ = \dfrac{32}{3} \left(\left| \cos x \right| \cdot \left| \cos x \right| \cdot \left| \cos x \right| \cdot \dfrac{\sqrt{15} + 3}{4} (\sqrt{5} - 2 | \cos x |) \cdot \dfrac{\sqrt{15} - 3}{4} (\sqrt{5} + 2 | \cos x |)\right) \\ \leq \dfrac{32}{3} \left(\dfrac{1}{5} \left(\left| \cos x \right| + \left| \cos x \right| + \left| \cos x \right| + \dfrac{\sqrt{15} + 3}{4} (\sqrt{5} - 2 | \cos x |) + \dfrac{\sqrt{15} - 3}{4} (\sqrt{5} + 2 | \cos x |)\right)\right)^{5} \\ = \dfrac{32}{3} \left(\dfrac{\sqrt{3}}{2}\right)^{5} = 3\sqrt{3}. \\ \end{array}
$$

这得到 $f(x) \leq 3\sqrt{3}$ ，同时又有 $f\left(\dfrac{\pi}{6}\right) = 5\cos \dfrac{\pi}{6} - \cos \dfrac{5\pi}{6} = 3\sqrt{3}$ ，故 $f(x)$ 在 $\left[0, \dfrac{\pi}{4}\right]$ 上的最大值为 $3\sqrt{3}$ ，在R上的最大值也是 $3\sqrt{3}$ .

（2）法1：由余弦函数的性质得 $\cos x \leq \cos \theta$ 的解为 $[2k\pi + \theta, 2k\pi + 2\pi - \theta]$ ， $k \in \mathbb{Z}$ ，若任意 $[2k\pi + \theta, 2k\pi + 2\pi - \theta], k \in \mathbb{Z}$ 与 $[a - \theta, a + \theta]$ 交集为空，则 $a - \theta > 2k\pi + 2\pi - \theta$ 且 $a + \theta < 2k\pi + 2\pi + \theta$ ，此时 $a$ 无解，矛盾，故无解；故存在 $k \in \mathbb{Z}$ ，使得 $[2k\pi - \theta, 2k\pi + \theta] \cap (a - \theta, a + \theta) \neq \emptyset$

法2：由余弦函数的性质知 $\cos y\leq \cos \theta$ 的解为 $\left[2k\pi +\theta ,2(k + 1)\pi -\theta \right](k\in \mathbf{Z})$ ，若每个 $\left[2k\pi +\theta ,2(k + 1)\pi -\theta \right]$ 与 $[a - \theta ,a + \theta ]$ 交集都为空，则对每个 $k \in Z$ ，必有 $2(k+1)\pi - \theta < a - \theta$ 或 $2k\pi + \theta > a + \theta$ 之一成立. 此即 $k < \dfrac{a}{2\pi} - 1$ 或 $k > \dfrac{a}{2\pi}$ ，但长度为1的闭区间 $\left[\dfrac{a}{2\pi} - 1, \dfrac{a}{2\pi}\right]$ 上必有一整数 $k$ ，该整数 $k$ 不满足条件，矛盾. 故存在 $y \in [a - \theta, a + \theta]$ ，使得 $\cos y \leq \cos \theta$ 成立.

（3）法1：记 $h(x)=5\cos x-\cos(5x+\varphi)$ , 因为 $h(x+2\pi)=5\cos(x+2\pi)-\cos(5x+10\pi+\varphi)=h(x)$ , 故 $h(x)$ 为周期函数且周期为 $2\pi$ ，故只需讨论 $x \in [0, 2\pi]$ ， $\varphi \in [0, \pi]$ 的情况. 当 $\varphi = \pi$ 时， $h(x) = 5\cos x - \cos(5x + \pi) = 5\cos x + \cos 5x \leq 6$ ，当 $\varphi = 0$ 时， $h(x) = 5\cos x - \cos 5x$ ，此时 $h'(x) = -5 \sin x + 5 \sin 5x = 10 \cos 3x \sin 2x, x \in (0, 2\pi)$ , 令 $h'(x)=0$ ，则 $x=\dfrac{\pi}{6},\dfrac{\pi}{2},\dfrac{5\pi}{6},\pi,\dfrac{7\pi}{6},\dfrac{3\pi}{2},\dfrac{11\pi}{6}$ ，而 $h(\dfrac{\pi}{6}) = h(\dfrac{11\pi}{6}) = 3\sqrt{3}, h(\dfrac{\pi}{2}) = h(\dfrac{3\pi}{2}) = 0, h(\dfrac{5\pi}{6}) = h(\dfrac{7\pi}{6}) = -3\sqrt{3}, h(\pi) = -4$ ， $h(0)=h(2\pi)=4$ ，故 $h(x)_{\max}=h(\dfrac{\pi}{6})=h(\dfrac{11\pi}{6})=3\sqrt{3}$ ，

当 $\varphi \in (0, \pi)$ ，在（2）中取 $\varphi = a$ ，则存在 $y \in [\varphi - \theta, \varphi + \theta]$ ，使得 $\cos y \leq \cos \theta$ ，取 $\theta = \dfrac{5\pi}{6}$ ，则 $\cos y\leq -\dfrac{\sqrt{3}}{2}$ ，取 $x = \dfrac{y - \varphi}{5}\in \left[-\dfrac{\theta}{5},\dfrac{\theta}{5}\right]$ 即 $x = \dfrac{y - \varphi}{5}\in \left[-\dfrac{\pi}{6},\dfrac{\pi}{6}\right],$ 故 $5\cos x \geq \dfrac{5\sqrt{3}}{2}$ ，故 $5\cos x - \cos(5x + \varphi) \geq 3\sqrt{3}$ ，

综上 $b\geq3\sqrt{3}$ ，可取 $x=\dfrac{\pi}{6}$ ， $\varphi=0$ 使得等号成立. 综上， $b_{\mathrm{min}} = 3\sqrt{3}$

法2：设 $g_{\varphi}(x) = 5\cos x - \cos (5x + \varphi)$

①一方面，若存在 $\varphi$ ，使得 $g_{\varphi}(x)=5\cos x-\cos(5x+\varphi)\leq b$ 对任意 x 恒成立，则对这样的 $\varphi$ ，同样有 $g_{\varphi}(x) = -g_{\varphi}(x + \pi)\geq -b$ ，所以 $\left|g_{\varphi}(x)\right|\leq b$ 对任意x恒成立，这直接得到 $b\geq0$ . 设 $\dfrac{\varphi}{6} -\dfrac{\pi}{6} = m$ ，则根据 $\left|g_{\varphi}(x)\right|\leq b$ 恒成立，有

$$
b \geq \left| g_{\varphi}\left(-\dfrac{\varphi}{6} + \dfrac{\pi}{6}\right) \right| = \left| 5 \cos \left(-\dfrac{\varphi}{6} + \dfrac{\pi}{6}\right) - \cos \left(\dfrac{\varphi}{6} + \dfrac{5\pi}{6}\right) \right| = \left| 5 \cos \left(\dfrac{\varphi}{6} - \dfrac{\pi}{6}\right) + \cos \left(\dfrac{\varphi}{6} - \dfrac{\pi}{6}\right) \right| = \left| 6 \cos \left(\dfrac{\varphi}{6} - \dfrac{\pi}{6}\right) \right| = 6 | \cos m |
$$

$$
b \geq \left| g_{\varphi}\left(-\dfrac{\varphi}{6} - \dfrac{\pi}{6}\right) \right| = \left| 5 \cos \left(-\dfrac{\varphi}{6} - \dfrac{\pi}{6}\right) - \cos \left(\dfrac{\varphi}{6} - \dfrac{5\pi}{6}\right) \right| = \left| 5 \cos \left(\dfrac{\varphi}{6} + \dfrac{\pi}{6}\right) + \cos \left(\dfrac{\varphi}{6} + \dfrac{\pi}{6}\right) \right| = \left| 6 \cos \left(\dfrac{\varphi}{6} + \dfrac{\pi}{6}\right) \right| = 6 \left| \cos \left(m + \dfrac{\pi}{3}\right) \right|
$$

$$
b \geq \left| g_{\varphi}\left(-\dfrac{\varphi}{6} + \dfrac{\pi}{2}\right) \right| = \left| 5 \cos \left(-\dfrac{\varphi}{6} + \dfrac{\pi}{2}\right) - \cos \left(\dfrac{\varphi}{6} + \dfrac{5\pi}{2}\right) \right| = \left| 5 \cos \left(\dfrac{\varphi}{6} - \dfrac{\pi}{2}\right) + \cos \left(\dfrac{\varphi}{6} - \dfrac{\pi}{2}\right) \right| = \left| 6 \cos \left(\dfrac{\varphi}{6} - \dfrac{\pi}{2}\right) \right| = 6 \left| \cos \left(m - \dfrac{\pi}{3}\right) \right|
$$

所以 $\left|\cos m\right|,\left|\cos\left(m+\dfrac{\pi}{3}\right)\right|,\left|\cos\left(m-\dfrac{\pi}{3}\right)\right|$ 均不超过 $\dfrac{b}{6}$ , 再结合 $\cos 2x = 2|\cos x|^2 -1$ 就得到 $\cos 2m, \cos \left(2m + \dfrac{2\pi}{3}\right), \cos \left(2m - \dfrac{2\pi}{3}\right)$ 均不超过 $2\left(\dfrac{b}{6}\right)^2 - 1 = \dfrac{b^2}{18} - 1$ . 假设 $b < 3\sqrt{3}$ ，则 $\dfrac{b^2}{18} - 1 < \dfrac{(3\sqrt{3})^2}{18} - 1 = \dfrac{1}{2}$ ，故 $\cos 2m, \cos \left(2m + \dfrac{2\pi}{3}\right), \cos \left(2m - \dfrac{2\pi}{3}\right) \in \left[-1, \dfrac{1}{2}\right)$ . 但这是不可能的，因为三个角 $2m, 2m + \dfrac{2\pi}{3}, 2m - \dfrac{2\pi}{3}$ 和单位圆的交点将单位圆三等分，这三个点不可能都在直线 $x = \dfrac{1}{2}$ 左侧. 所以假设不成立，这意味着 $b \geq 3\sqrt{3}$ .

②另一方面，若 $b=3\sqrt{3}$ ，则由（1）中已经证明 $f(x)\leq3\sqrt{3}$ ，知存在 $\varphi = 0$ ，使得 $5\cos x - \cos (5x + \varphi) = 5\cos x - \cos 5x = f(x)\leq 3\sqrt{3} = b.$ 从而 $b = 3\sqrt{3}$ 满足题目要求. 综合上述两个方面，可知 $b$ 的最小值是 $3\sqrt{3}$ .

``````

---

## 179 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T2.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T2.md) · SHA 404f7189ce1fa607fbca6e55e7b20063f353fd09 · mode 100644

``````markdown
---
qid: 1781356597884662
grade: 高三
source: 25全国1
number: T2
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 补集的概念及运算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知集合 $U = \{x \mid x$ 是小于 $9$ 的正整数$\}$，$A = \{1,3,5\}$，则 $C_U A$ 中元素个数为 [选]

## 选项
A．$0$
B．$3$
C．$5$
D．$8$

## 备注

### 我的备注

### AI备注


## 答案
C

## 解析
因为 $U=\{1,2,3,4,5,6,7,8\}$ ，所以 $\complement_{U}A=\{2,4,6,7,8\}$ ， $\complement_{U}A$ 中的元素个数为5，故选：C.

``````

---

## 180 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T3.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T3.md) · SHA 7e9155e1b883b0025a638a31459f9b4ced7a040a · mode 100644

``````markdown
---
qid: 1781356597884245
grade: 高三
source: 25全国1
number: T3
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 求双曲线的离心率或离心率的取值范围
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知双曲线 $C$ 的虚轴长是实轴长的 $\sqrt{7}$ 倍，则 $C$ 的离心率为 [选]

## 选项
A．$\sqrt{2}$
B．$2$
C．$\sqrt{7}$
D．$2\sqrt{2}$

## 备注

### 我的备注

### AI备注


## 答案
D

## 解析
设双曲线的实轴，虚轴，焦距分别为2a,2b,2c，由题知， $b=\sqrt{7}a$ ，于是 $a^2 + b^2 = c^2 = a^2 + 7a^2 = 8a^2$ ，则 $c = 2\sqrt{2} a$ ，即 $e = \dfrac{c}{a} = 2\sqrt{2}$ ，故选：D.

``````

---

## 181 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T4.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T4.md) · SHA 952f315ab2c2763980e58ecb1044250891082cbf · mode 100644

``````markdown
---
qid: 1781356597884399
grade: 高三
source: 25全国1
number: T4
type: 单选题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 求正切（型）函数的对称中心
  - 正切函数对称性的应用
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知点 $(a,0)(a > 0)$ 是函数 $y = 2\tan \left(x - \dfrac{\pi}{3}\right)$ 的图象的一个对称中心，则 $a$ 的最小值为 [选]

## 选项
A．$\dfrac{\pi}{6}$
B．$\dfrac{\pi}{3}$
C．$\dfrac{\pi}{2}$
D．$\dfrac{4\pi}{3}$

## 备注

### 我的备注

### AI备注


## 答案
B

## 解析
根据正切函数的性质， $y=2\tan(x-\dfrac{\pi}{3})$ 的对称中心横坐标满足 $x-\dfrac{\pi}{3}=\dfrac{k\pi}{2},k\in\mathbf{Z}$ ，即 $y=2\tan(x-\dfrac{\pi}{3})$ 的对称中心是 $\left(\dfrac{\pi}{3}+\dfrac{k\pi}{2},0\right),k\in\mathbf{Z}$ ，即 $a = \dfrac{\pi}{3} +\dfrac{k\pi}{2},k\in \mathbf{Z}$ ，又 $a > 0$ ，则 $k = 0$ 时 $a$ 最小，最小值是 $\dfrac{\pi}{3}$ ，即 $a = \dfrac{\pi}{3}$ ，故选：B.

``````

---

## 182 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T5.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T5.md) · SHA aa4b87e29e142d90f4f740d9bffe495687d1ef31 · mode 100644

``````markdown
---
qid: 1781356597884393
grade: 高三
source: 25全国1
number: T5
type: 单选题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 函数奇偶性的应用
  - 由函数的周期性求函数值
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知 $f(x)$ 是定义在 $\mathbf{R}$ 上且周期为 2 的偶函数，当 $2 \leq x \leq 3$ 时， $f(x) = 5 - 2x$ ，则 $f\left(-\dfrac{3}{4}\right) =$ [选]

## 选项
A．$-\dfrac{1}{2}$
B．$-\dfrac{1}{4}$
C．$\dfrac{1}{4}$
D．$\dfrac{1}{2}$

## 备注

### 我的备注

### AI备注


## 答案
A

## 解析
由题知 $f(x)=f(-x)$ , $f(x+2)=f(x)$ 对一切 $x\in R$ 成立，于是 $f(-\dfrac{3}{4}) = f(\dfrac{3}{4}) = f(\dfrac{11}{4}) = 5 - 2 \times \dfrac{11}{4} = -\dfrac{1}{2}$ . 故选：A.

``````

---

## 183 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T6.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T6.md) · SHA 9f683488546081efea4cbd8fdc3fef54c6d49c9d · mode 100644

``````markdown
---
qid: 1781356597885845
grade: 高三
source: 25全国1
number: T6
type: 单选题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 平面向量线性运算的坐标表示
  - 向量坐标的线性运算解决几何问题
  - 坐标计算向量的模
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
帆船比赛中，运动员可借助风力计测定风速的大小与方向，测出的结果在航海学中称为 视风风速.视风风速对应的向量是真风风速对应的向量与船行风风速对应的向量之和，其中船行风风速对应的向量与船速对应的向量大小相等、方向相反.图1给出了部分风力等级、名称与风速大小的对应关系.已知某帆船运动员在某时刻测得的视风风速对应的向量与船速对应的向量如图2所示（线段长度代表速度大小，单位：m/s），则该时刻的真风为 [选]

<table><tr><td>级数</td><td>名称</td><td>风速大小(单位:m/s)</td></tr><tr><td>2</td><td>轻风</td><td>1.6~3.3</td></tr><tr><td>3</td><td>微风</td><td>3.4~5.4</td></tr><tr><td>4</td><td>和风</td><td>5.5~7.9</td></tr><tr><td>5</td><td>劲风</td><td>8.0~10.7</td></tr></table>

![](images/019435e37ff80cb5590da08958c28cb78815793ffb2dfcd534bce229d6d798dc.jpg)

## 选项
A．轻风
B．微风
C．和风
D．劲风

## 备注

### 我的备注

### AI备注


## 答案
A

## 解析
由题意及图得，视风风速对应的向量为： $\vec{n}=(0,2)-(3,3)=(-3,-1)$ ，视风风速对应的向量，是真风风速对应的向量与船行风速对应的向量之和，船速方向和船行风速的向量方向相反，设真风风速对应的向量为 $\overrightarrow{n_{1}}$ ，船行风速对应的向量为 $\overrightarrow{n_{2}}$ ，∴ $\vec{n}=\vec{n}_{1}+\vec{n}_{2}$ ，船行风速： $\vec{n}_{2}=-\left[\left(3,3\right)-\left(2,0\right)\right]=\left(-1,-3\right)$ ，

$$
\therefore \overrightarrow {n _ {1}} = \overrightarrow {n} - \overrightarrow {n _ {2}} = (- 3, - 1) - (- 1, - 3) = (- 2, 2),
$$

$$
\left| \overrightarrow {n _ {1}} \right| = \sqrt {(- 2) ^ {2} + 2 ^ {2}} = 2 \sqrt {2} \approx 2. 8 2 8,
$$

∴由表得，真风风速为轻风，故选：A.

``````

---

## 184 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T7.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T7.md) · SHA 43274fae89ea5ad172c488c498517eafa89101c2 · mode 100644

``````markdown
---
qid: 1781356597885947
grade: 高三
source: 25全国1
number: T7
type: 单选题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 求点到直线的距离
  - 圆上点到定直线（图形）上的最值（范围）
  - 坐标法的应用——直线与圆的位置关系
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知圆 $x^{2} + (y + 2)^{2} = r^{2}(r > 0)$ 上到直线 $y = \sqrt{3} x + 2$ 的距离为$1$的点有且仅有$2$个，则 $r$ 的取值范围是 [选]

## 选项
A．$(0,1)$
B．$(1,3)$
C．$(3,+\infty)$
D．$(0,+\infty)$

## 备注

### 我的备注

### AI备注


## 答案
B

## 解析
由题意，在圆 $x^{2} + (y + 2)^{2} = r^{2}(r > 0)$ 中，圆心 $E(0, - 2)$ ，半径为 $r$ ，到直线 $y = \sqrt{3} x + 2$ 的距离为1的点有且仅有2个，∵圆心 $E(0,-2)$ 到直线 $y=\sqrt{3}x+2$ 的距离为： $d=\dfrac{\left|0\times\sqrt{3}-(-2)\times1+2\right|}{\sqrt{(\sqrt{3})^{2}+(-1)^{2}}}=2$ ，

![](images/90a4064b7aa3fd33028b4ebb48fb506d850c7bf05c0a759311e8423121295b83.jpg)

故由图可知，当 $r = 1$ 时，圆 $x^{2}+(y+2)^{2}=r^{2}(r>0)$ 上有且仅有一个点（A 点）到直线 $y=\sqrt{3}x+2$ 的距离等于 1；当 $r = 3$ 时，圆 $x^{2}+(y+2)^{2}=r^{2}(r>0)$ 上有且仅有三个点（B,C,D点）到直线 $y=\sqrt{3}x+2$ 的距离等于1；当则 r 的取值范围为 $(1,3)$ 时，圆 $x^{2} + (y + 2)^{2} = r^{2}(r > 0)$ 上有且仅有两个点到直线 $y = \sqrt{3} x + 2$ 的距离等于1. 故选：B.

``````

---

## 185 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T8.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T8.md) · SHA 9df57230b270cfb9c9e9c09802aa340db9750e70 · mode 100644

``````markdown
---
qid: 1781356597885831
grade: 高三
source: 25全国1
number: T8
type: 单选题
difficulty: 0.4
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 对数的运算性质的应用
  - 对数函数单调性的应用
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知 $2 + \log_2 x = 3 + \log_3 y = 5 + \log_5 z$ ，则 $x, y, z$ 的大小关系不可能是 [选]

## 选项
A．$x > y > z$
B．$x > z > y$
C．$y > x > z$
D．$y > z > x$

## 备注

### 我的备注

### AI备注


## 答案
B

## 解析
法一：设 $2 + \log_2x = 3 + \log_3y = 5 + \log_5z = m$ ，所以令 $m = 2$ ，则 $x = 1, y = 3^{-1} = \dfrac{1}{3}, z = 5^{-3} = \dfrac{1}{125}$ ，此时 $x > y > z$ ，A有可能；令 m=5，则 x=8, y=9, z=1，此时 y>x>z，C 有可能；令 m=8，则 $x=2^{6}=64, y=3^{5}=243, z=5^{3}=125$ ，此时 y>z>x，D 有可能；故选：B.

法二：设 $2 + \log_2x = 3 + \log_3y = 5 + \log_5z = m$ ，所以， $x = 2^{m - 2},y = 3^{m - 3},z = 5^{m - 5}$ ，根据指数函数的单调性，易知各方程只有唯一的根，作出函数 $y=2^{x-2}, y=3^{x-3}, y=5^{x-5}$ 的图象，以上方程的根分别是函数 $y=2^{x-2}, y=3^{x-3}, y=5^{x-5}$ 的图象与直线 x=m 的交点纵坐标，如图所示：

![](images/0ef823f5dd67fe31ab9a6d71ff239fd251b413ed2dd890ea01ef29a350d1dbf5.jpg)

易知，随着 $m$ 的变化可能出现： $x > y > z$ ， $y > x > z$ ， $y > z > x$ ， $z > y > x$ ，故选：B.

``````

---

## 186 · mirror/math-atlas/demo-vault/题库/25全国1/25全国1-T9.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD1/25%E5%85%A8%E5%9B%BD1-T9.md) · SHA bb325628f9f3f836c4d560d943732f0b65979a2c · mode 100644

``````markdown
---
qid: 1781356597885761
grade: 高三
source: 25全国1
number: T9
type: 多选题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 证明线面平行
  - 证明线面垂直
  - 空间位置关系的向量证明
  - 求平面的法向量
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
在正三棱柱 $ABC - A_{1}B_{1}C_{1}$ 中， $D$ 为 $BC$ 的中点，则 [选]

## 选项
A．$AD \perp A_{1}C$
B．$B_{1}C_{1}\perp$ 平面 $AA_{1}D$
C．$AD \parallel A_{1}B_{1}$
D．$CC_{1} / /$ 平面 $AA_{1}D$

## 备注

### 我的备注

### AI备注


## 答案
BD

## 解析
法一：对于 A，在正三棱柱 $ABC-A_{1}B_{1}C_{1}$ 中， $AA_{1}\perp$ 平面 ABC，

![](images/ace670d058802f1547660e9cfe94a73905115e31be7a91ea1144eb8cef7712cd.jpg)

又 $AD \subset$ 平面 ABC，则 $AA_{1} \perp AD$ ，则 $\overrightarrow{A_{1}A} \cdot \overrightarrow{AD} = 0$ ，因为 $\triangle ABC$ 是正三角形， $D$ 为 $BC$ 中点，则 $AD\perp BC$ ，则 $\overrightarrow{DC}\cdot \overrightarrow{AD} = 0$ ，又 $\overrightarrow{A_1C} = \overrightarrow{A_1A} +\overrightarrow{AD} +\overrightarrow{DC}$ ，所以 $\overrightarrow{A_1C} \cdot \overrightarrow{AD} = (\overrightarrow{A_1A} + \overrightarrow{AD} + \overrightarrow{DC}) \cdot \overrightarrow{AD} = \overrightarrow{A_1A} \cdot \overrightarrow{AD} + \overrightarrow{AD}^2 + \overrightarrow{DC} \cdot \overrightarrow{AD} = \overrightarrow{AD}^2 \neq 0$ ，则 $AD \perp A_{1}C$ 不成立，故 A 错误；

对于 B，因为在正三棱柱 $ABC-A_{1}B_{1}C_{1}$ 中， $AA_{1}\perp$ 平面 $A_{1}B_{1}C_{1}$ ，又 $B_{1}C_{1}\subset$ 平面 $A_{1}B_{1}C_{1}$ ，则 $AA_{1}\perp B_{1}C_{1}$ ，因为 $\triangle ABC$ 是正三角形，D为BC中点，则 $AD\perp BC$ ， $AD\perp B_{1}C_{1}$ ，又 $AA_{1} \cap AD = A, AA_{1}, AD \subset$ 平面 $AA_{1}D$ ，所以 $B_{1}C_{1} \perp$ 平面 $AA_{1}D$ ，故 B 正确；

对于 D，因为在正三棱柱 $ABC-A_{1}B_{1}C_{1}$ 中， $CC_{1}//AA_{1}$ ，又 $AA_{1} \subset$ 平面 $AA_{1}D, CC_{1} \notin$ 平面 $AA_{1}D$ ，所以 $CC_{1} //$ 平面 $AA_{1}D$ ，故 D 正确；

对于 C，因为在正三棱柱 $ABC-A_{1}B_{1}C_{1}$ 中， $A_{1}B_{1}//AB$ ，假设 $AD \parallel A_{1}B_{1}$ ，则 $AD \parallel AB$ ，这与 $AD \cap AB = A$ 矛盾，所以 $AD // A_{1}B_{1}$ 不成立，故 C 错误；故选：BD.

法二：如图，建立空间直角坐标系，设该正三棱柱的底边为2，高为h，

![](images/d12921a27ec068cbd03e2f9e5ead01ff1324e95560c64ec6c32f52bfba795e9a.jpg)

则 $D(0,0,0), A(\sqrt{3}, 0, 0), A_1(\sqrt{3}, 0, h), C(0, -1, 0), C_1(0, -1, h), B(0, 1, 0), B_1(0, 1, h)$

对于 A, $\overrightarrow{AD} = (-\sqrt{3}, 0, 0)$ , $\overrightarrow{A_{1}C} = (-\sqrt{3}, -1, -h)$ ，则 $\overrightarrow{AD} \cdot \overrightarrow{A_1C} = (-\sqrt{3}) \times (-\sqrt{3}) + 0 = 3 \neq 0$ ，则 $AD \perp A_{1}C$ 不成立，故A错误；

对于 BD， $\overrightarrow{BC}=(0,-2,0),\overrightarrow{CC_{1}}=(0,0,h),\overrightarrow{AA_{1}}=(0,0,h),\overrightarrow{AD}=(-\sqrt{3},0,0)$ ，设平面 $AA_{1}D$ 的法向量为 $\vec{n}=(x,y,z)$ ，则 $\left\{\begin{aligned}\overrightarrow{AA_{1}}\cdot\vec{n}&=hz=0\\\overrightarrow{AD}\cdot\vec{n}&=-\sqrt{3}x=0\end{aligned}\right.$ ，得x=z=0，令y=1，则 $\vec{n}=(0,1,0)$ ，所以 $\overrightarrow{BC}=(0,-2,0)=-2\vec{n}$ ， $\overrightarrow{CC_{1}}\cdot\vec{n}=0$ ，则 $BC \perp$ 平面 $AA_{1}D$ ， $CC_{1} //$ 平面 $AA_{1}D$ ，故 BD 正确；

对于 C， $\overrightarrow{AD}=\left(-\sqrt{3},0,0\right),\overrightarrow{A_{1}B_{1}}=\left(-\sqrt{3},1,0\right)$ ，则 $\dfrac{-\sqrt{3}}{-\sqrt{3}} \neq \dfrac{0}{1}$ ，显然 $AD // A_1 B_1$ 不成立，故 C 错误；故选：BD.

``````

---

## 187 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T1.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T1.md) · SHA 698ff6ba4ad631f4b448faaf5ba76ce1371164c7 · mode 100644

``````markdown
---
qid: 1781356597963319
grade: 高三
source: 25全国2
number: T1
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 计算几个数的平均数
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
样本数据 2, 8, 14, 16, 20 的平均数为 [选]

## 选项
A．8
B．9
C．12
D．18

## 备注

### 我的备注

### AI备注


## 答案
C

## 解析
样本数据2,8,14,16,20的平均数为 $\dfrac{2 + 8 + 14 + 16 + 20}{5} = \dfrac{60}{5} = 12$ .

``````

---

## 188 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T10.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T10.md) · SHA ed957892d03dac83b39ff4b14939e240b5fd9f4c · mode 100644

``````markdown
---
qid: 1781356597965120
grade: 高三
source: 25全国2
number: T10
type: 多选题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 由奇偶性求函数解析式
  - 函数奇偶性的应用
  - 求已知函数的极值点
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知 $f(x)$ 是定义在 $\mathbf{R}$ 上的奇函数，且当 $x > 0$ 时， $f(x) = (x^2 - 3)e^x + 2$ ，则 [选]

## 选项
A．$f(0) = 0$
B．当 $x < 0$ 时， $f(x) = -\left(x^2 - 3\right)\mathrm{e}^{-x} - 2$
C．$f(x)\geq 2$ 当且仅当 $x\geq \sqrt{3}$
D．$x = -1$ 是 $f(x)$ 的极大值点

## 备注

### 我的备注

### AI备注


## 答案
ABD

## 解析
对 A，因为 $f(x)$ 定义在 R 上奇函数，则 $f(0)=0$ ，故 A 正确；

对 B，当 $x<0$ 时，$-x>0$，则 $f(x)=-f(-x)=-\left[\left((-x)^{2}-3\right)\mathrm{e}^{-x}+2\right]=-\left(x^{2}-3\right)\mathrm{e}^{-x}-2$ ，故 B 正确；

对 C， $f(-1)=-(1-3)e-2=2(e-1)>2$ ，故 C 错误；

对 D，当 $x<0$ 时， $f(x)=\left(3-x^{2}\right)\mathrm{e}^{-x}-2$ ，则 $f'(x)=-\left(3-x^{2}\right)\mathrm{e}^{-x}-2x\mathrm{e}^{-x}=\left(x^{2}-2x-3\right)\mathrm{e}^{-x}$ 令 $f'(x)=0$ ，解得 $x=-1$ 或 $3$（舍去），

当 $x \in (-\infty, -1)$ 时， $f'(x) > 0$ ，此时 $f(x)$ 单调递增，

当 $x\in(-1,0)$ 时， $f'(x)<0$ ，此时 $f(x)$ 单调递减，

则 $x = -1$ 是 $f(x)$ 极大值点，故 D 正确；

``````

---

## 189 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T11.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T11.md) · SHA b18c058c73ed8d13c97e96105ab6936a5df39ddd · mode 100644

``````markdown
---
qid: 1781356597965777
grade: 高三
source: 25全国2
number: T11
type: 多选题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 用定义求向量的数量积
  - 已知数量积求模
  - 双曲线的对称性
  - 求双曲线的离心率或离心率的取值范围
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
双曲线 $C: \dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1 (a > 0, b > 0)$ 的左、右焦点分别为 $F_1$ 、 $F_2$ ，左、右顶点分别为 $A_1$ ， $A_2$ ，以 $F_1 F_2$ 为直径的圆与 $C$ 的一条渐近线交于 $M$ ， $N$ 两点，且 $\angle NA_1 M = \dfrac{5\pi}{6}$ ，则 [选]

## 选项
A．$\angle A_{1}MA_{2} = \dfrac{\pi}{6}$
B．$|MA_{1}|=2|MA_{2}|$
C．$C$ 的离心率为 $\sqrt{13}$
D．当 $a = \sqrt{2}$ 时，四边形 $NA_{1}MA_{2}$ 的面积为 $8\sqrt{3}$

## 备注

### 我的备注

### AI备注


## 答案
ACD

## 解析
不妨设渐近线为 $y=\dfrac{b}{a}x$ ，M 在第一象限，N 在第三象限，

对于 A，由双曲线的对称性可得 $A_{1}MA_{2}N$ 为平行四边形，故 $\angle A_{1}MA_{2} = \pi - \dfrac{5\pi}{6} = \dfrac{\pi}{6}$ ，故 A 正确；

对于 B，方法一：因为 M 在以 $F_{1}F_{2}$ 为直径的圆上，故 $F_{1}M \perp F_{2}M$ 且 $|MO| = c$ ，

设 $M\left(x_0,y_0\right)$ ，则 $\left\{ \begin{array}{l}x_0^2 +y_0^2 = c^2\\ \dfrac{y_0}{x_0} = \dfrac{b}{a} \end{array} \right.$ ，故 $\left\{ \begin{array}{l}x_0 = a\\ y_0 = b \end{array} \right.$ ，故 $MA_{2}\perp A_{1}A_{2}$

由 A 得 $\angle A_{1}MA_{2} = \dfrac{\pi}{6}$ ，故 $|MA_2| = |MA_1|\times \dfrac{\sqrt{3}}{2}$ 即 $|MA_1| = \dfrac{2\sqrt{3}}{3}|MA_2|$ ，故 B 错误；

方法二：因为 $\tan \angle MOA_{2} = \dfrac{b}{a}$ ，因为双曲线中， $c^2 = a^2 +b^2$

则 $\cos \angle MOA_{2} = \dfrac{a}{c}$ ，又因为以 $F_{1}F_{2}$ 为直径的圆与 $C$ 的一条渐近线交于 $M$ 、 $N$ ，则 $OM = c$ 则若过点 $M$ 往 $x$ 轴作垂线，垂足为 $H$ ，则 $|OH| = c\cdot \dfrac{a}{c} = a = |OA_2|$ ，则点 $H$ 与 $A_{2}(H)$ 重合，则 $MA_{2}\perp x$ 轴，则 $|MA_2| = \sqrt{c^2 - a^2} = b$ ，则 $\triangle A_1HM$ 为直角三角形，且 $\angle A_1MH = \dfrac{\pi}{6}$ ，则 $2|MA_2| = \sqrt{3}|MA_1|$

方法三：在 $\triangle OMA_{2}$ 利用余弦定理知， $|MA_2|^2 = |OM|^2 +|OA_2|^2 -2|OM||OA_2|\cos \angle MOA_2$

即 $|MA_2|^2 = c^2 + a^2 - 2ac \cdot \dfrac{a}{c} = b^2$ ，则 $|MA_2| = b$ ，

则 $\triangle A_{1}A_{2}M$ 为直角三角形，且 $\angle A_{1}MA_{2} = \dfrac{\pi}{6}$ ，则 $2|MA_2| = \sqrt{3}|MA_1|$ ，故 B 错误；

对于 C，方法一：因为 $\overrightarrow{MO}=\dfrac{1}{2}\left(\overrightarrow{MA_{1}}+\overrightarrow{MA_{2}}\right)$ ，故 $4\overrightarrow{MO}^{2}=\overrightarrow{MA_{1}}^{2}+2\overrightarrow{MA_{1}}\cdot\overrightarrow{MA_{2}}+\overrightarrow{MA_{2}}^{2}$

由 B 可知 $|MA_{2}|=b,|MA_{1}|=\dfrac{2\sqrt{3}}{3}b$

故 $4c^{2}=b^{2}+\dfrac{4}{3}b^{2}+2\times b\times\dfrac{2\sqrt{3}}{3}b\times\dfrac{\sqrt{3}}{2}=\dfrac{13}{3}b^{2}=\dfrac{13}{3}\left(c^{2}-a^{2}\right)$ 即 $c^{2}=13a^{2}$ ,

故离心率 $e=\sqrt{13}$ ，故 C 正确；

方法二：因为 $\dfrac{|MA_2|}{|A_1A_2|} = \dfrac{b}{2a} = \sqrt{3}$ ，则 $\dfrac{b}{a} = 2\sqrt{3}$ ，则 $e = \dfrac{c}{a} = \sqrt{1 + \dfrac{b^2}{a^2}} = \sqrt{1 + (2\sqrt{3})^2} = \sqrt{13}$ ，故 C 正确；

对于 D，当 $a = \sqrt{2}$ 时，由 C 可知 $e = \sqrt{13}$ ，故 $c = \sqrt{26}$

故 $b=2\sqrt{6}$ ，故四边形 $NA_{1}MA_{2}$ 为 $2S_{\triangle MA_{1}A_{2}}=2\times\dfrac{1}{2}\times2\sqrt{6}\times2\sqrt{2}=8\sqrt{3}$ ，

故 D 正确，

![](images/a9c604228dae808d8f105eed82c9ec571c354df526bf1aff1d26b436be4fec52.jpg)

![](images/70e9a2746a9cc7198ac077c7ae073af77134ec00477fc00c22e9b23be17a60ae.jpg)

``````

---

## 190 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T12.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T12.md) · SHA db05e2d384c623d4d90ca11e3058b1e5d26edf9d · mode 100644

``````markdown
---
qid: 1781356597965425
grade: 高三
source: 25全国2
number: T12
type: 填空题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 平面向量线性运算的坐标表示
  - 坐标计算向量的模
  - 向量垂直的坐标表示
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知平面向量 $\vec{a} = (x, 1), \vec{b} = (x - 1, 2x)$ , 若 $\vec{a} \perp (\vec{a} - \vec{b})$ , 则 $|\vec{a}| =$ [填]

## 备注

### 我的备注

### AI备注


## 答案
$\sqrt{2}$

## 解析
$\vec{a}-\vec{b}=(1,1-2x)$ ，因为 $\vec{a}\perp(\vec{a}-\vec{b})$ ，则 $\vec{a}\cdot(\vec{a}-\vec{b})=0$ ，

则 $x+1-2x=0$ ，解得 $x=1$。

则 $\vec{a} = (1,1)$ ，则 $|\vec{a}| = \sqrt{2}$

``````

---

## 191 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T13.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T13.md) · SHA bf34e217f8e625c7f04a41eedc8caf63bf29f3c2 · mode 100644

``````markdown
---
qid: 1781356597965078
grade: 高三
source: 25全国2
number: T13
type: 填空题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 求函数值
  - 导数的运算法则
  - 根据极值点求参数
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
若 $x = 2$ 是函数 $f(x) = (x - 1)(x - 2)(x - a)$ 的极值点，则 $f(0) =$ [填]

## 备注

### 我的备注

### AI备注


## 答案
-4

## 解析
由题意有 $f(x)=(x-1)(x-2)(x-a)$ ,

所以 $f'(x)=(x-a)(x-1)+(x-1)(x-2)+(x-a)(x-2)$ ,

因为 $2$ 是函数 $f(x)$ 极值点，所以 $f'(2)=2-a=0$ ，得 $a=2$，

当 $a = 2$ 时， $f'(x) = 2(x - 2)(x - 1) + (x - 2)^2 = (x - 2)(3x - 4)$ ，

当 $x \in \left(-\infty, \dfrac{4}{3}\right), f'(x) > 0, f(x)$ 单调递增，当 $x \in \left(\dfrac{4}{3}, 2\right), f'(x) < 0, f(x)$ 单调递减，

当 $x\in(2,+\infty),f'(x)>0,f(x)$ 单调递增，

所以 $x=2$ 是函数 $f(x)=(x-1)(x-2)(x-a)$ 的极小值点，符合题意；

所以 $f(0) = -1 \times (-2) \times (-a) = -2a = -4$ .

``````

---

## 192 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T14.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T14.md) · SHA 1ff939dc2dcf755272d9afd787edaa6d9d89715b · mode 100644

``````markdown
---
qid: 1781356597966766
grade: 高三
source: 25全国2
number: T14
type: 填空题
difficulty: 0.4
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 圆柱的结构特征辨析
  - 球的截面的性质及计算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
一个底面半径为 $4 \mathrm{~cm}$ , 高为 $9 \mathrm{~cm}$ 的封闭圆柱形容器 (容器壁厚度忽略不计) 内有两个半径相等的铁球, 则铁球半径的最大值为 [填] cm

## 备注

### 我的备注

### AI备注


## 答案
2.5

## 解析

![](images/d7230dd448ced08ce80e978181a29181d814f7f8c62aaf5f20f4357954d535fb.jpg)

圆柱的底面半径为 $4 \mathrm{~cm}$ , 设铁球的半径为 $r$ , 且 $r < 4$ ,

由圆柱与球的性质知 $AB^{2}=(2r)^{2}=(8-2r)^{2}+(9-2r)^{2}$

即 $4r^{2} - 68r + 145 = (2r - 5)(2r - 29) = 0$ ， $\because r < 4$

$$
\therefore r = 2.5.
$$

``````

---

## 193 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T15.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T15.md) · SHA 653d7fab217abff414c22739980bcd1c09f04a3f · mode 100644

``````markdown
---
qid: 1781356597966433
grade: 高三
source: 25全国2
number: T15
type: 解答题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 求含cosx的函数的单调性
  - 利用余弦函数的单调性求参数
  - 求cosx(型)函数的值域
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知函数 $f(x) = \cos (2x + \varphi)(0 \leq \varphi < \pi), f(0) = \dfrac{1}{2}$ .

(1)求 $\varphi$ ;

(2)设函数 $g(x) = f(x) + f\left(x - \dfrac{\pi}{6}\right)$ ，求 $g(x)$ 的值域和单调区间.

## 备注

### 我的备注

### AI备注


## 答案
(1) $\varphi=\dfrac{\pi}{3}$

(2)值域为 $\left[-\sqrt{3},\sqrt{3}\right]$ ，单调递减区间为 $\left[-\dfrac{\pi}{12} +k\pi ,\dfrac{5\pi}{12} +k\pi \right],k\in Z$ ，单调递增区间为 $\left[\dfrac{5\pi}{12} + k\pi , \dfrac{11\pi}{12} + k\pi \right], k \in Z.$

## 解析
（1）由题意 $f(0)=\cos\varphi=\dfrac{1}{2},(0\leq\varphi<\pi)$ ，所以 $\varphi=\dfrac{\pi}{3}$ ;

（2）由（1）可知 $f(x) = \cos \left(2x + \dfrac{\pi}{3}\right)$

所以 $g(x)=f(x)+f\left(x-\dfrac{\pi}{6}\right)=\cos\left(2x+\dfrac{\pi}{3}\right)+\cos2x$

$$
= \dfrac{1}{2} \cos 2x - \dfrac{\sqrt{3}}{2} \sin 2x + \cos 2x = \dfrac{3}{2} \cos 2x - \dfrac{\sqrt{3}}{2} \sin 2x = \sqrt{3} \cos \left(2x + \dfrac{\pi}{6}\right),
$$

所以函数 $g(x)$ 的值域为 $\left[-\sqrt{3},\sqrt{3}\right]$

令 $2k\pi \leq 2x + \dfrac{\pi}{6} \leq \pi + 2k\pi, k \in \mathbb{Z}$ ，解得 $-\dfrac{\pi}{12} + k\pi \leq x \leq \dfrac{5\pi}{12} + k\pi, k \in \mathbb{Z}$ ，

令 $\pi + 2k\pi \leq 2x + \dfrac{\pi}{6} \leq 2\pi + 2k\pi, k \in \mathbb{Z}$ ，解得 $\dfrac{5\pi}{12} + k\pi \leq x \leq \dfrac{11\pi}{12} + k\pi, k \in \mathbb{Z}$ ，

所以函数 $g(x)$ 的单调递减区间为 $\left[-\dfrac{\pi}{12}+k\pi,\dfrac{5\pi}{12}+k\pi\right], k\in Z$ ,

函数 $g(x)$ 的单调递增区间为 $\left[\dfrac{5\pi}{12} + k\pi, \dfrac{11\pi}{12} + k\pi\right], k \in \mathbf{Z}$ .

``````

---

## 194 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T16.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T16.md) · SHA b01198fbe2ec5e25cc52a99086834bb56967353b · mode 100644

``````markdown
---
qid: 1781356597966196
grade: 高三
source: 25全国2
number: T16
type: 解答题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 根据a、b、c求椭圆标准方程
  - 根据离心率求椭圆的标准方程
  - 椭圆中三角形（四边形）的面积
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知椭圆 $C: \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1 (a > b > 0)$ 的离心率为 $\dfrac{\sqrt{2}}{2}$ ，长轴长为4.

(1)求 C 的方程;

(2)过点 $(0, -2)$ 的直线 $l$ 交 $C$ 于 $A,B$ 两点， $O$ 为坐标原点.若 $\triangle OAB$ 的面积为 $\sqrt{2}$ ，求 $|AB|$

## 备注

### 我的备注

### AI备注


## 答案
(1) $\dfrac{x^{2}}{4}+\dfrac{y^{2}}{2}=1$

(2) $\sqrt{5}$

## 解析
（1）因为长轴长为4，故 $a=2$，而离心率为 $\dfrac{\sqrt{2}}{2}$ ，故 $c=\sqrt{2}$ ，

故 $b=\sqrt{2}$ ，故椭圆方程为： $\dfrac{x^{2}}{4}+\dfrac{y^{2}}{2}=1$ .

(2)

![](images/b2d6d6e61f9fc379a78c5b76a7e0a7328ca5cbb6798082e6256f19ed838d1796.jpg)

由题设直线 AB 的斜率不为 0，故设直线 $l: x = t(y + 2)$ ， $A(x_{1}, y_{1})$ ， $B(x_{2}, y_{2})$ ，

由 $\left\{\begin{aligned}x=t(y+2)\\ x^{2}+2y^{2}=4\end{aligned}\right.$ 可得 $(t^{2}+2)y^{2}+4t^{2}y+4t^{2}-4=0$ ,

故 $\Delta = 16t^4 - 4(t^2 + 2)(4t^2 - 4) = 4(8 - 4t^2) > 0$ 即 $-\sqrt{2} < t < \sqrt{2}$ ，

且 $y_{1} + y_{2} = -\dfrac{4t^{2}}{t^{2} + 2}, y_{1}y_{2} = \dfrac{4t^{2} - 4}{t^{2} + 2}$ ,

故 $S_{\triangle OAB} = \dfrac{1}{2}\times |2t|\times |y_1 - y_2| = |t|\sqrt{(y_1 + y_2)^2 - 4y_1y_2} = \dfrac{|t|\sqrt{32 - 16t^2}}{t^2 + 2} = \sqrt{2}$

解得 $t = \pm \dfrac{\sqrt{6}}{3}$

故 $|AB|=\sqrt{1+t^{2}}|y_{1}-y_{2}|=\sqrt{1+\dfrac{2}{3}}\times\sqrt{\left(y_{1}+y_{2}\right)^{2}-4y_{1}y_{2}}=\sqrt{\dfrac{5}{3}}\times\dfrac{\sqrt{32-16\times\dfrac{2}{3}}}{\dfrac{2}{3}+2}=\sqrt{5}$

``````

---

## 195 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T17.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T17.md) · SHA fc0f87365083d1371c64ff263b1987805d6e86bd · mode 100644

``````markdown
---
qid: 1781356597966368
grade: 高三
source: 25全国2
number: T17
type: 解答题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 证明线面平行
  - 求二面角
  - 面面角的向量求法
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
如图, 在四边形 $ABCD$ 中, $AB // CD$ , $\angle DAB = 90^\circ$ , $F$ 为 $CD$ 的中点, 点 $E$ 在 $AB$ 上, $EF // AD$ , $AB = 3AD$ , $CD = 2AD$ . 将四边形 $EFDA$ 沿 $EF$ 翻折至四边形 $EFD'A'$ , 使得面 $EFD'A'$ 与面 $EFCB$ 所成的二面角为 $60^\circ$ .

![](images/317a9b401a5ec1866f19d60daf4fd5b476928480cb6d45bbf4e1fe4940b2f94c.jpg)

(1)证明： $A'B //$ 平面 $CD'F$ ；

(2)求面 $BCD'$ 与面 $EFD'A'$ 所成的二面角的正弦值.

## 备注

### 我的备注

### AI备注


## 答案
(1)证明见解析

(2) $\dfrac{\sqrt{42}}{7}$

## 解析
(1) 设 AD = 1，所以 AB = 3, CD = 2，因为 F 为 CD 中点，所以 DF = 1，因为 EF // AD，AB // CD，所以 AEFD 是平行四边形，所以 AE // DF，所以 A'E // D'F，因为 D'F ⊂ 平面 CD'F, A'E ≠ 平面 CD'F，所以 A'E // 平面 CD'F，因为 FC // EB, FC ⊂ 平面 CD'F, EB ≠ 平面 CD'F，所以 EB // 平面 CD'F，又 EB ∩ A'E = E，EB, A'E ⊂ 平面 A'EB，所以平面 A'EB // 平面 CD'F，又 A'B ⊂ 平面 A'EB，所以 A'B // 平面 CD'F。

(2)

![](images/431e38df5ff7962c86bdcc1dc5e89dea56ec708bd6058c68c4fbd7dcda8fd801.jpg)

因为 $\angle DAB = 90^{\circ}$ ，所以 $AD\perp AB$ ，又因为 $AB / / FC,EF / / AD$ ，所以 $EF\perp FC$

以 $F$ 为原点， $FE,FC$ 以及垂直于平面 $BECF$ 的直线分别为 $x,y,z$ 轴，建立空间直角坐标系.

因为 $D^{\prime}F \perp EF, CF \perp EF$ ，平面 $EFD'A'$ 与平面 EFCB 所成二面角为 $60^{\circ}$ ，

所以 $\angle D'FC = 60^{\circ}$

则 $B(1,2,0)$ ， $C(0,1,0)$ ， $D^{\prime}\left(0,\dfrac{1}{2},\dfrac{\sqrt{3}}{2}\right)$ ， $E(1,0,0)$ ， $F(0,0,0)$ .

所以 $\overrightarrow{BC} = (-1, -1,0),\overrightarrow{CD'} = \left(0, -\dfrac{1}{2},\dfrac{\sqrt{3}}{2}\right),\overrightarrow{FE} = (1,0,0),\overrightarrow{FD'} = \left(0,\dfrac{1}{2},\dfrac{\sqrt{3}}{2}\right).$

设平面 $BCD'$ 的法向量为 $\vec{n} = (x, y, z)$ ，则

$\left\{ \begin{array}{l} \overrightarrow{BC} \cdot \vec{n} = 0 \\ \overrightarrow{CD'} \cdot \vec{n} = 0 \end{array} \right.$ ，所以 $\left\{ \begin{array}{l} -\dfrac{1}{2} y + \dfrac{\sqrt{3}}{2} z = 0 \\ -x - y = 0 \end{array} \right.$ ，令 $y = \sqrt{3}$ ，则 $z = 1, x = -\sqrt{3}$ ，则 $\vec{n} = (-\sqrt{3}, \sqrt{3}, 1)$ .

设平面 $EFD'A'$ 的法向量为 $\vec{m}=(x_{1},y_{1},z_{1})$ ,

则 $\left\{\begin{aligned}\overrightarrow{FE}\cdot\vec{m}&=0\\\overrightarrow{FD^{\prime}}\cdot\vec{m}&=0\end{aligned}\right.$ ，所以 $\left\{\begin{aligned}\dfrac{1}{2}y_{1}+\dfrac{\sqrt{3}}{2}z_{1}&=0\\x_{1}&=0\end{aligned}\right.$

令 $y_{1} = \sqrt{3}$ ，则 $z_{1} = -1, x_{1} = 0$ ，所以 $\vec{m} = (0, \sqrt{3}, -1)$ .

所以 $\cos\left\langle\vec{m},\vec{n}\right\rangle=\dfrac{\vec{m}\cdot\vec{n}}{|\vec{m}||\vec{n}|}=\dfrac{0+3-1}{\sqrt{3+3+1}\times\sqrt{1+3}}=\dfrac{1}{\sqrt{7}}$

所以平面 $BCD'$ 与平面 $EFD'A'$ 夹角的正弦值为 $\sqrt{1 - \left(\dfrac{1}{\sqrt{7}}\right)^2} = \dfrac{\sqrt{42}}{7}$ .

``````

---

## 196 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T18.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T18.md) · SHA 331ccbeb3676baaafe5a69c468fb1a1bbb00a019 · mode 100644

``````markdown
---
qid: 1781356597966613
grade: 高三
source: 25全国2
number: T18
type: 解答题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 用导数判断或证明已知函数的单调性
  - 利用导数证明不等式
  - 利用导数研究函数的零点
  - 求已知函数的极值点
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知函数 $f(x) = \ln (1 + x) - x + \dfrac{1}{2} x^2 - kx^3$ ，其中 $0 < k < \dfrac{1}{3}$ .

(1)证明： $f(x)$ 在区间 $(0,+\infty)$ 存在唯一的极值点和唯一的零点；

(2)设 $x_{1},x_{2}$ 分别为 $f(x)$ 在区间 $(0,+\infty)$ 的极值点和零点.

(i) 设函数 $g(t)=f(x_{1}+t)-f(x_{1}-t)$ . 证明： $g(t)$ 在区间 $(0,x_{1})$ 单调递减；

(ii) 比较 $2x_{1}$ 与 $x_{2}$ 的大小，并证明你的结论.

## 备注

### 我的备注

### AI备注


## 答案
(1)证明：由题得 $f'(x)=\dfrac{1}{1+x}-1+x-3kx^{2}=\dfrac{x^{2}}{1+x}-3kx^{2}=x^{2}\left(\dfrac{1}{1+x}-3k\right)$ ,

因为 $x \in (0, +\infty)$ ，所以 $x^2 > 0$ ，设 $g(x) = \dfrac{1}{1 + x} - 3k, x > 0$

则 $g^{\prime}(x) = -\dfrac{1}{(1 + x)^{2}} < 0$ 在 $(0, + \infty)$ 上恒成立，所以 $g(x)$ 在 $(0, + \infty)$ 上单调递减，

$g(0)=1-3k>0$ ，令 $g(x_{0})=0\Rightarrow x_{0}=\dfrac{1}{3k}-1$ ，

所以当 $x\in(0,x_{0})$ 时， $g(x)>0$ ，则 $f'(x)>0$ ；当 $x\in(x_{0},+\infty)$ 时， $g(x)<0$ ，则 $f'(x)<0$ ，

所以 $f(x)$ 在 $(0, x_{0})$ 上单调递增，在 $(x_{0}, +\infty)$ 上单调递减，

所以 $f(x)$ 在 $(0,+\infty)$ 上存在唯一极值点，

对函数 $y=\ln(1+x)-x$ 有 $y'=\dfrac{1}{1+x}-1=-\dfrac{x}{1+x}<0$ 在 $(0,+\infty)$ 上恒成立，

所以 $y = \ln (1 + x) - x$ 在 $(0, +\infty)$ 上单调递减，

所以 $y = \ln (1 + x) - x < y|_{x=0} = 0$ 在 $(0, +\infty)$ 上恒成立，

又因为 $f(0) = 0$ ， $x \to +\infty$ 时 $\dfrac{1}{2} x^2 - kx^3 = \dfrac{1}{2} x^2 (1 - 2kx) < 0$ ，

所以 $x \to +\infty$ 时 $f(x) < 0$

所以存在唯一 $x_{2} \in (0, +\infty)$ 使得 $f(x_{2}) = 0$ ，即 $f(x)$ 在 $(0, +\infty)$ 上存在唯一零点.

(2)（i）证明：由（1）知 $x_{1} = \dfrac{1}{3k} - 1$ ，则 $x_{1} + 1 = \dfrac{1}{3k}$ ， $f'(x) = x^{2}\left(\dfrac{1}{1 + x} - \dfrac{1}{1 + x_{1}}\right)$ ，

$$
\because g (t) = f \left(x _ {1} + t\right) - f \left(x _ {1} - t\right),
$$

则 $g'(t)=\left(x_{1}+t\right)^{2}\left(\dfrac{1}{x_{1}+t+1}-\dfrac{1}{1+x_{1}}\right)+\left(x_{1}-t\right)^{2}\left(\dfrac{1}{x_{1}-t+1}-\dfrac{1}{1+x_{1}}\right)$

$$
= \dfrac{- t (x _ {1} + t) ^ {2}}{(x _ {1} + t + 1) (x _ {1} + 1)} + \dfrac{t (x _ {1} - t) ^ {2}}{(x _ {1} - t + 1) (x _ {1} + 1)} = 3 k t \left[ - \dfrac{(x _ {1} + t) ^ {2}}{x _ {1} + t + 1} + \dfrac{(x _ {1} - t) ^ {2}}{x _ {1} - t + 1} \right]
$$

$$
= \dfrac{6 k t ^ {2} \left(t ^ {2} - x _ {1} ^ {2} - 2 x _ {1}\right)}{\left(1 + x _ {1}\right) ^ {2} - t ^ {2}},
$$

$$
\because k > 0, t \in (0, x _ {1}), \therefore t ^ {2} - x _ {1} ^ {2} - 2 x _ {1} < 0, (1 + x _ {1}) ^ {2} - t ^ {2} > 0,
$$

$$
\therefore g ^ {\prime} (t) = \dfrac{6 k t ^ {2} \left(t ^ {2} - x _ {1} ^ {2} - 2 x _ {1}\right)}{\left(1 + x _ {1}\right) ^ {2} - t ^ {2}} < 0,
$$

即 $g(t)$ 在 $t \in (0, x_{1})$ 上单调递减.

(ii) $2x_{1} > x_{2}$ ，证明如下：

由（i）知：函数 $g(t)$ 在区间 $(0, x_1)$ 上单调递减，

所以 $g(0) > g(x_{1})$ 即 $0 > f(2x_{1})$ ，又 $f(x_{2}) = 0$ ，

由（1）可知 $f(x)$ 在 $(x_0, +\infty)$ 上单调递减， $x_2 \in (x_0, +\infty)$ ，且对任意 $x \in (0, x_2) f(x) > 0$ ，所以 $2x_1 > x_2$ .

## 解析
（1）略

(2) (i) 略

(ii) 略

``````

---

## 197 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T19.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T19.md) · SHA 75c333b44e37a0f2f1d2ae7b0da22520491aa660 · mode 100644

``````markdown
---
qid: 1781356597967307
grade: 高三
source: 25全国2
number: T19
type: 解答题
difficulty: 0.15
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 计算古典概型问题的概率
  - 服从二项分布的随机变量概率最大问题
  - 建立二项分布模型解决实际问题
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
甲、乙两人进行乒乓球练习，每个球胜者得 1 分，负者得 0 分．设每个球甲胜的概率为 $p\left(\dfrac{1}{2}<p<1\right)$ ，乙胜的概率为 $q$ ， $p+q=1$ ，且各球的胜负相互独立．对正整数 $k\geq2$ ，记 $p_k$ 为打完 $k$ 个球后甲比乙至少多得 2 分的概率， $q_k$ 为打完 $k$ 个球后乙比甲至少多得 2 分的概率．

(1)求 $p_{3},p_{4}$ （用p表示）.

(2)若 $\dfrac{p_4 - p_3}{q_4 - q_3} = 4$ ，求 $p$

(3)证明：对任意正整数 m， $p_{2m+1}-q_{2m+1}<p_{2m}-q_{2m}<p_{2m+2}-q_{2m+2}$

## 备注

### 我的备注

### AI备注


## 答案
(1) $p_{3}=p^{3}$ ， $p_{4}=p^{3}(4-3p)$

(2) $p=\dfrac{2}{3}$

(3)证明过程见解析

## 解析
（1） $p_{3}$ 为打完 3 个球后甲比乙至少多得两分的概率，故只能甲胜三场，

故所求为 $p_{3}=\mathrm{C}_{3}^{3}(1-p)^{0}p^{3}=p^{3}$ ,

$p_{4}$ 为打完 4 个球后甲比乙至少多得两分的概率，故甲胜三场或四场，

故所求为 $p_4 = \mathrm{C}_4^3 (1 - p)^1 p^3 +\mathrm{C}_4^4 (1 - p)^0 p^4 = 4p^3 (1 - p) + p^4 = p^3 (4 - 3p)$

（2）由（1）得 $p_3 = p^3$ ， $p_4 = p^3(4 - 3p)$ ，同理 $q_{3} = q^{3},q_{4} = q^{3}(4 - 3q)$

若 $\dfrac{p_4 - p_3}{q_4 - q_3} = 4$ ， $p + q = 1$

则 $\dfrac{p_4 - p_3}{q_4 - q_3} = \dfrac{p^3(4 - 3p) - p^3}{q^3(4 - 3q) - q^3} = \dfrac{3p^3(1 - p)}{3q^3(1 - q)} = \dfrac{p^3q}{q^3p} = \left(\dfrac{p}{q}\right)^2 = 4,$

由于 $0 < p, q < 1$，所以 $p = 2q = 2(1 - p) > 0$ ，解得 $p = \dfrac{2}{3}$ ;

（3）设打完 $k$ 个球，甲的得分为 $X_{k}$ ，乙的得分为 $Y_{k}$ ， $X_{k} + Y_{k} = k$ ，

所以 $p_{2m}=P(X_{2m}\geq m+1)$ ， $p_{2m+1}=P(X_{2m+1}\geq m+2)$ ， $p_{2m+2}=P(X_{2m+2}\geq m+2)$ ，

$$
q _ {2 m} = P \left(Y _ {2 m} \geq m + 1\right), \quad q _ {2 m + 1} = P \left(Y _ {2 m + 1} \geq m + 2\right), \quad q _ {2 m + 2} = P \left(Y _ {2 m + 2} \geq m + 2\right),
$$

要证明 $p_{2m + 1} - q_{2m + 1} < p_{2m} - q_{2m} < p_{2m + 2} - q_{2m + 2}$

即证明① $p_{2m+1}-p_{2m}<q_{2m+1}-q_{2m}$ ，② $p_{2m+2}-p_{2m}>q_{2m+2}-q_{2m}$

先证明① $p_{2m+1}-p_{2m}<q_{2m+1}-q_{2m}$ ，

$$
p _ {2 m + 1} - p _ {2 m} = P \left(X _ {2 m + 1} \geq m + 2\right) - P \left(X _ {2 m} \geq m + 1\right)
$$

$$
= P \left(X _ {2 m} \geq m + 2\right) + P \left(X _ {2 m} = m + 1\right) p - P \left(X _ {2 m} \geq m + 1\right)
$$

$$
= P \left(X _ {2 m} = m + 1\right) p - P \left(X _ {2 m} = m + 1\right)
$$

$$
= (p - 1) C _ {2 m} ^ {m + 1} p ^ {m + 1} q ^ {m - 1},
$$

同理可得 $q_{2m + 1} - q_{2m} = (q - 1)C_{2m}^{m + 1}q^{m + 1}p^{m - 1}$

所以

①

$$
\Leftrightarrow (p - 1) C _ {2 m} ^ {m + 1} p ^ {m + 1} q ^ {m - 1} < (q - 1) C _ {2 m} ^ {m + 1} q ^ {m + 1} p ^ {m - 1} \Leftrightarrow p ^ {2} (p - 1) < q ^ {2} (q - 1) \Leftrightarrow - p ^ {2} q < - q ^ {2} p \Leftrightarrow - p < - q \Leftrightarrow p > q
$$

，故成立；

证明② $p_{2m+2}-p_{2m}>q_{2m+2}-q_{2m}$ :

$$
p _ {2 m + 2} - p _ {2 m} = P \left(X _ {2 m + 2} \geq m + 2\right) - P \left(X _ {2 m} \geq m + 1\right)
$$

$$
\begin{array}{l} = P \left(X _ {2 m} = m\right) p ^ {2} + P \left(X _ {2 m} = m + 1\right) \left[ 1 - (1 - p) ^ {2} \right] + P \left(X _ {2 m} \geq m + 2\right) - P \left(X _ {2 m} \geq m + 1\right) \\ = P \left(X _ {2 m} = m\right) p ^ {2} + P \left(X _ {2 m} = m + 1\right) \left[ 1 - (1 - p) ^ {2} \right] + P \left(X _ {2 m} \geq m + 1\right) - P \left(X _ {2 m} = m + 1\right) - P \left(X _ {2 m} \geq m + 1\right) \\ = P \left(X _ {2 m} = m\right) p ^ {2} + P \left(X _ {2 m} = m + 1\right) \left(1 - q ^ {2}\right) - P \left(X _ {2 m} = m + 1\right) \\ = C _ {2 m} ^ {m} p ^ {m} q ^ {m} p ^ {2} - q ^ {2} C _ {2 m} ^ {m + 1} p ^ {m + 1} q ^ {m - 1} \\ = C _ {2 m} ^ {m} p ^ {m + 2} q ^ {m} - C _ {2 m} ^ {m + 1} p ^ {m + 1} q ^ {m + 1}, \\ \end{array}
$$

同理可得 $q_{2m + 2} - q_{2m} = C_{2m}^{m}q^{m + 2}p^{m} - C_{2m}^{m + 1}q^{m + 1}p^{m + 1}$

所以

②

$$
\Leftrightarrow C _ {2 m} ^ {m} p ^ {m + 2} q ^ {m} - C _ {2 m} ^ {m + 1} p ^ {m + 1} q ^ {m + 1} > C _ {2 m} ^ {m} q ^ {m + 2} p ^ {m} - C _ {2 m} ^ {m + 1} q ^ {m + 1} p ^ {m + 1} \Leftrightarrow C _ {2 m} ^ {m} p ^ {m + 2} q ^ {m} > C _ {2 m} ^ {m} q ^ {m + 2} p ^ {m} \Leftrightarrow p ^ {2} > q ^ {2} \Leftrightarrow p > q
$$

，故成立；

综上，不等式 $p_{2m + 1} - q_{2m + 1} < p_{2m} - q_{2m} < p_{2m + 2} - q_{2m + 2}$ 成立.

``````

---

## 198 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T2.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T2.md) · SHA 15d7c8b0121863bbe5b49d9b36ab8a7500fb3ac9 · mode 100644

``````markdown
---
qid: 1781356597963099
grade: 高三
source: 25全国2
number: T2
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 复数的除法运算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知 $z = 1 + \mathrm{i}$ ，则 $\dfrac{1}{z - 1} =$ [选]

## 选项
A．$-i$
B．$i$
C．$-1$
D．$1$

## 备注

### 我的备注

### AI备注


## 答案
A

## 解析
因为 $z = 1 + \mathrm{i}$ ，所以 $\dfrac{1}{z - 1} = \dfrac{1}{1 + \mathrm{i} - 1} = \dfrac{1}{\mathrm{i}} = \dfrac{\mathrm{i}}{\mathrm{i}^2} = -\mathrm{i}.$

``````

---

## 199 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T3.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T3.md) · SHA 3a6a157a00ab9bdfb467dac3a4a55997a382daa1 · mode 100644

``````markdown
---
qid: 1781356597963434
grade: 高三
source: 25全国2
number: T3
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 交集的概念及运算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知集合 $A = \{-4, 0, 1, 2, 8\}$ , $B = \{x \mid x^3 = x\}$ , 则 $A \cap B =$ [选]

## 选项
A．$\{0,1,2\}$
B．$\{1,2,8\}$
C．$\{2,8\}$
D．$\{0,1\}$

## 备注

### 我的备注

### AI备注


## 答案
D

## 解析
$B=\left\{x\mid x^{3}=x\right\}=\left\{0,-1,1\right\}$ ，故 $A\cap B=\left\{0,1\right\}$

``````

---

## 200 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T4.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T4.md) · SHA 30fa0a6071b48b2b50f8c65e82bc398701952ce7 · mode 100644

``````markdown
---
qid: 1781356597963644
grade: 高三
source: 25全国2
number: T4
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 分式不等式
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
不等式 $\dfrac{x - 4}{x - 1} \geq 2$ 的解集是 [选]

## 选项
A．$\{x\mid -2\leq x\leq 1\}$
B．$\{x \mid x \leq -2\}$
C．$\{x\mid-2\leq x<1\}$
D．$\{x \mid x > 1\}$

## 备注

### 我的备注

### AI备注


## 答案
C

## 解析
$\dfrac{x-4}{x-1}\geq2$ 即为 $\dfrac{x+2}{x-1}\leq0$ 即 $\left\{\begin{aligned}(x+2)(x-1)\leq0\\ x-1\neq0\end{aligned}\right.$ ，故 $-2\leq x<1$ ，

故解集为 $\{x\mid-2\leq x<1\}$ .

``````

---

## 201 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T5.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T5.md) · SHA 6cbc12b5f14dda9af18990c279ab80538be2d0bf · mode 100644

``````markdown
---
qid: 1781356597964627
grade: 高三
source: 25全国2
number: T5
type: 单选题
difficulty: 0.94
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 余弦定理解三角形
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
在 $\triangle ABC$ 中， $BC = 2$ ， $AC = 1 + \sqrt{3}$ ， $AB = \sqrt{6}$ ，则 $A =$ [选]

## 选项
A．$45^{\circ}$
B．$60^{\circ}$
C．$120^{\circ}$
D．$135^{\circ}$

## 备注

### 我的备注

### AI备注


## 答案
A

## 解析
由题意得 $\cos A=\dfrac{AB^{2}+AC^{2}-BC^{2}}{2AB\cdot AC}=\dfrac{\left(\sqrt{6}\right)^{2}+\left(1+\sqrt{3}\right)^{2}-2^{2}}{2\times\sqrt{6}\times\left(1+\sqrt{3}\right)}=\dfrac{\sqrt{2}}{2}$

又 $0^{\circ}<A<180^{\circ}$ ，所以 $A=45^{\circ}$ .

``````

---

## 202 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T6.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T6.md) · SHA 255944898fc8e2c60034d8937c6812171cbd9c68 · mode 100644

``````markdown
---
qid: 1781356597964431
grade: 高三
source: 25全国2
number: T6
type: 单选题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 根据抛物线方程求焦点或准线
  - 抛物线的焦半径公式
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
设抛物线 $C: y^{2} = 2px (p > 0)$ 的焦点为 $F$ , 点 $A$ 在 $C$ 上, 过 $A$ 作 $C$ 的准线的垂线, 垂足为 $B$ . 若直线 $BF$ 的方程为 $y = -2x + 2$ , 则 $|AF| =$ [选]

## 选项
A．3
B．4
C．5
D．6

## 备注

### 我的备注

### AI备注


## 答案
C

## 解析
对 $l_{BF}:y=-2x+2$ ，令 $y=0$ ，则 $x=1$ ，

所以 $F(1,0)$ ，$p=2$ 即抛物线 $C: y^{2}=4x$ ，故抛物线的准线方程为 $x=-1$，

故 $B(-1,4)$ ，则 $y_{A}=4$ ，代入抛物线 $C:y^{2}=4x$ 得 $x_{A}=4$ .

所以 $|AF|=|AB|=x_{A}+\dfrac{p}{2}=4+1=5$ .

![](images/697b3758e89a572e0792f013557804c5ac13f15346a465ed350a30875aeeea13.jpg)

``````

---

## 203 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T7.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T7.md) · SHA ba95fd4fe03410034b651e045f15263edef429b7 · mode 100644

``````markdown
---
qid: 1781356597964781
grade: 高三
source: 25全国2
number: T7
type: 单选题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 求等差数列前n项和
  - 等差数列前n项和的基本量计算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
记 $S_{n}$ 为等差数列 $\{a_{n}\}$ 的前 $n$ 项和. 若 $S_{3} = 6, S_{5} = -5$ , 则 $S_{6} =$ [选]

## 选项
A．$-20$
B．$-15$
C．$-10$
D．$-5$

## 备注

### 我的备注

### AI备注


## 答案
B

## 解析
设等差数列 $\left\{a_{n}\right\}$ 的公差为 $d$ ，则由题可得 $\left\{\begin{aligned}&3a_{1}+3d=6\\ &5a_{1}+10d=-5\end{aligned}\right.\Rightarrow\left\{\begin{aligned}d=-3\\ &a_{1}=5\end{aligned}\right.$ 所以 $S_{6}=6a_{1}+15d=6\times5+15\times(-3)=-15$ .

``````

---

## 204 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T8.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T8.md) · SHA 2b5e6d4ff02da4a39efcbb74b16b8adbecb4dea7 · mode 100644

``````markdown
---
qid: 1781356597964927
grade: 高三
source: 25全国2
number: T8
type: 单选题
difficulty: 0.65
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 已知正（余）弦求余（正）弦
  - 用和、差角的正弦公式化简、求值
  - 二倍角的余弦公式
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
已知 $0 < \alpha < \pi$ ， $\cos \dfrac{\alpha}{2} = \dfrac{\sqrt{5}}{5}$ ，则 $\sin \left(\alpha - \dfrac{\pi}{4}\right) =$ [选]

## 选项
A．$\dfrac{\sqrt{2}}{10}$
B．$\dfrac{\sqrt{2}}{5}$
C．$\dfrac{3\sqrt{2}}{10}$
D．$\dfrac{7\sqrt{2}}{10}$

## 备注

### 我的备注

### AI备注


## 答案
D

## 解析
$\cos \alpha = 2\cos^2{\dfrac{\alpha}{2}} -1 = 2\times \left(\dfrac{\sqrt{5}}{5}\right)^2 -1 = -\dfrac{3}{5},$

因为 $0 < \alpha < \pi$ ，则 $\dfrac{\pi}{2} < \alpha < \pi$ ，则 $\sin \alpha = \sqrt{1 - \cos^2 \alpha} = \sqrt{1 - \left(-\dfrac{3}{5}\right)^2} = \dfrac{4}{5}$ ，

则 $\sin \left(\alpha -\dfrac{\pi}{4}\right) = \sin \alpha \cos \dfrac{\pi}{4} -\cos \alpha \sin \dfrac{\pi}{4} = \dfrac{4}{5}\times \dfrac{\sqrt{2}}{2} -\left(-\dfrac{3}{5}\right)\times \dfrac{\sqrt{2}}{2} = \dfrac{7\sqrt{2}}{10}.$

``````

---

## 205 · mirror/math-atlas/demo-vault/题库/25全国2/25全国2-T9.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/demo-vault/%E9%A2%98%E5%BA%93/25%E5%85%A8%E5%9B%BD2/25%E5%85%A8%E5%9B%BD2-T9.md) · SHA f7e565f5e3ec9d74af1e9360fab5a4f8b665f4d9 · mode 100644

``````markdown
---
qid: 1781356597965112
grade: 高三
source: 25全国2
number: T9
type: 多选题
difficulty: 0.85
semester: 高三下学期
exam_type: 高考真题
knowledge:
  - 等比数列通项公式的基本量计算
  - 求等比数列前n项和
  - 等比数列前n项和的基本量计算
ai_tags: []
tags: []
status: 待入库
selected: false
---

## 题目
记 $S_{n}$ 为等比数列 $\{a_{n}\}$ 的前 $n$ 项和， $q$ 为 $\{a_{n}\}$ 的公比， $q > 0$ . 若 $S_{3} = 7, a_{3} = 1$ ，则 [选]

## 选项
A．$q=\dfrac{1}{2}$
B．$a_{5}=\dfrac{1}{9}$
C．$S_{5} = 8$
D．$a_{n} + \mathrm{S}_{n} = 8$

## 备注

### 我的备注

### AI备注


## 答案
AD

## 解析
对 A，由题意得 $\left\{\begin{aligned}a_{1}q^{2}&=1\\ a_{1}+a_{1}q+a_{1}q^{2}&=7\end{aligned}\right.$ ，结合 $q>0$，解得 $\left\{\begin{aligned}a_{1}&=4\\ q&=\dfrac{1}{2}\end{aligned}\right.$ 或 $\left\{\begin{aligned}a_{1}&=9\\ q&=-\dfrac{1}{3}\end{aligned}\right.$ （舍去），故 A 正确；

对 B，则 $a_5 = a_1q^4 = 4\times \left(\dfrac{1}{2}\right)^4 = \dfrac{1}{4}$ ，故 B 错误；

对 C， $S_{5}=\dfrac{a_{1}\left(1-q^{5}\right)}{1-q}=\dfrac{4\times\left(1-\dfrac{1}{32}\right)}{1-\dfrac{1}{2}}=\dfrac{31}{4}$ ，故 C 错误；

对 D， $a_{n}=4\times\left(\dfrac{1}{2}\right)^{n-1}=2^{3-n}$ ， $S_{n}=\dfrac{4\times\left[1-\left(\dfrac{1}{2}\right)^{n}\right]}{1-\dfrac{1}{2}}=8-2^{-n+3}$

则 $a_{n} + S_{n} = 2^{3 - n} + 8 - 2^{3 - n} = 8$ ，故 D 正确；

``````

---

## 206 · mirror/math-atlas/docs/AI排版提示词 - ee.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/docs/AI%E6%8E%92%E7%89%88%E6%8F%90%E7%A4%BA%E8%AF%8D%20-%20ee.md) · SHA 01daac4d68aede54ac2312763c70705feee60f1f · mode 100644

``````markdown
# AI 题目排版提示词

```
1.读取输入文件，全面分析排版结构（段落、字体等）及内容，保留文本所有内容包括识别表格。识别思维导图相关的分支用大括号代替表示。
2.将文件转换为无空格的markdown纯文本，确保编译简单。
3.一定要注意识别去除页眉页码和水印，不识别图片，但保留“如图...”“如下图...”等字样，精准保留原始排版样式。
4.按高中数学人教版A版教材格式规范所有数学公式和符号表达，向量的印刷体识别为手写体（带上标箭头），三角函数名要用正体。
5.识别并去除markdown辅助编译字符，仅保留文档原始内容。
6.检查原始内容识别准确性，确保与原文档一致，完成最终输出。
7.只识别内容，不要说多余的话，比如‘’要不要我帮你……‘’这种
8.注意根号包进数学环境，\sqrt 是 LaTeX 命令，必须放在 $ $ 美元符号数学公式内，不能写在外面。
9.数字与函数、字母注意不要混写无分隔，语法断裂，如\sqrt3 是错误写法，标准是 \sqrt{3}，大括号不能省略，省略会导致编译截断、乱码、不显示。
10.三角函数、字母、符号全部要统一包裹在一对 $ $ 里，不能半截在公式里、半截在外面。
11.注意识别长等号及长等号是否上下带问题，转译长等号用如下完整命令：\xlongequal[下面]{上面}
12.严禁生成任何形式的水平分隔线（包括但不限于 `---`、`***` 等符号），内容之间直接用段落换行（空行）分隔即可，不使用任何符号作为分段线。标题级别符号也删掉！如“#” 、“##” 、“###” 等等，数学公式、列表、表格等格式保持不变，仅移除所有人工添加的分隔线符号。
13.注意识别并保留带括号的如“【   】”和“（  ）”中的注释内容。
14.最后检查确保全文所有内容无遗漏，无增加删改内容，且全部符合前面所提的所有要求。
15.自动识别图片中所有用方框、圆圈、高亮等方式标注的重点内容。
16.无用户明确要求时，不添加额外的解释、拓展或总结，仅完整还原图片中的内容。保持内容的逻辑顺序，分段清晰，便于直接复制使用。
```

``````

---

## 207 · mirror/math-atlas/docs/AI排版提示词 -豆包-文件.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/docs/AI%E6%8E%92%E7%89%88%E6%8F%90%E7%A4%BA%E8%AF%8D%20-%E8%B1%86%E5%8C%85-%E6%96%87%E4%BB%B6.md) · SHA 5674e27ffc865de53f834ceadb90cb49061c9c8c · mode 100644

``````markdown
# AI 题目排版提示词

```
你是一个处理高中数学试卷的专家，需要从输入的图片或文档中完整提取内容，并整理成标准题库格式。整个过程分为三个阶段，严格遵循以下所有规则，**不说多余的话，不添加任何解释或拓展**。

### 第一阶段：内容识别与净化
1. 读取输入文件，全面分析排版结构（段落、字体、表格等），保留所有文本内容。若有思维导图，分支关系用大括号 `{` 表示层级。
2. 去除页眉、页码、水印，不识别图片本身，但必须保留“如图...”“如下图...”等提示性文字。精准保留原文排版层次和逻辑顺序。

### 第二阶段：数学公式与符号规范
3. 所有数学公式严格按照高中数学人教版 A 版教材表达：
   - 向量使用手写体并带上标箭头，如 $\vec{a}$、$\overrightarrow{AB}$。
   - 三角函数名使用正体，如 $\sin$、$\cos$、$\tan$。
4. 所有数学内容必须完整放入 `$...$`（行内）或 `$$...$$`（独立行），不得出现半截在公式内、半截在外的情况。数字、函数、字母统一包裹在一对 `$` 内。
5. 分数统一用 `\dfrac`，角标或指数内部需要分数时可用 `\frac`。
6. 根号必须写在数学环境内，`\sqrt` 后必须带大括号，如 `$\sqrt{3}$`，禁止写成 `\sqrt3`。
7. 长等号转换为 `\xlongequal[下面]{上面}`，若原文无上下标注则省略可选参数，如 `$\xlongequal{}$`。
8. 避免语法断裂，如 `$2\sin x$` 不能写成 `$2sin x$`，必要时在数学环境内部用空格或运算符隔开。

### 第三阶段：标准化题库整理
基于净化后的文本，按以下标准整理成最终格式。**不解题、不自编、不改变原意，原文缺失的信息一律标“（无）”**。
9. 整个输出由多道题目组成，每道题之间用独占一行的 `==========`（10 个等号）分隔。
10. 每道题严格按以下顺序组织：
    - **YAML 元数据块**，包裹在 `---` 中，模板如下（根据识别内容填充）：
qid: 留空
grade: 高三
source: （从试卷标题提取，如“16全国1文”）
number: T题号
type: 单选题/填空题/解答题
difficulty: （原文有则填，无则留空）
semester: 高三下学期
exam_type: 高考真题
knowledge: []
ai_tags: []
tags: []
status: 待入库
selected: false

- **## 题目**：题干正文。原卷选择题的空白括号替换为 `[选]`，填空题横线替换为 `[填]`，且 `[选]` 和 `[填]` 必须放在数学公式外部（即 `$...$` 之外）。保留 `【重点】` 等标记和所有注释。
- **## 选项**：**仅当题型为单选题时**才写此部分。每个选项独占一行，格式为 `A．...`、`B．...`、`C．...`、`D．...`（选项字母后用全角点），选项内的公式须遵守数学规范。
- **## 备注**：存放题目附加说明、原卷标注的重点提示等。若没有，写“（无）”。
- **## 答案**：若原文给出答案（如选项、数值），则如实转录；若没有，写“（无）”。严禁自行推理得出答案。
- **## 解析**：若原文有解析，保留；若没有，写“（无）”。
11. 最终检查：确保所有数学公式正确包裹，无裸露 LaTeX 命令，向量、三角函数等表达符合教材规范；已彻底清除原文的标题符号和分隔线；题间用 `==========` 分隔；内容无遗漏、无增删，逻辑顺序与原卷一致。
12. 仅输出整理好的题库内容，不要添加任何问候、确认或解释性话语。
```

``````

---

## 208 · mirror/math-atlas/docs/AI排版提示词.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/docs/AI%E6%8E%92%E7%89%88%E6%8F%90%E7%A4%BA%E8%AF%8D.md) · SHA c6fc3c6c042db6d76fb89d74a34e09f3cfc69fc1 · mode 100644

``````markdown
# AI 题目排版提示词

```
【统一填写】grade:  source:  semester:  exam_type:

你是高中数学题库整理专家。请把以下OCR输出的 markdown 整理为标准格式。

**⚠️ 请一次性处理下方全部题目，不要中断、不要要求我拆分。按模板逐题输出即可。**

## 硬性规则（违反即不合格）

1. **不解题**：不做任何计算、推理、判断。原文没有的答案和解析绝不补充，标「（无）」即可。
2. **不自编**：不对难度、知识点做任何猜测。原文有的就填，没有的全部留空。
3. **不生成 AI 备注**：「AI备注」标题保留，内容留空（不写任何字）。
4. **不改变内容**：只调整排版和公式格式，不增删改原文的任何一字一句。
5. **不填 qid**：qid 保留模板值「留空」。

## 格式规范

6. 所有数学公式用 $...$（行内）或 $$...$$（独立行）包裹，不要用 \(...\) 或其它格式。
   **题干中的公式必须用 $...$（行内），不要用 $$...$$**；解析中较长的推导公式可用 $$...$$。
   **分数统一用 \dfrac，仅角标/指数中的分数保留 \frac**（如 $x^{\frac{1}{2}}$）。
   **所有数学字母必须进 $...$**，哪怕是单个 $A$、$x$、$b$ 也不例外（数学环境用斜体，正文用正体，混写不规范）。
7. 选项统一为 A．... B．... C．... D．...，一行一个。
8. 每道题包含 ## 题目、## 答案、## 解析。**只有单选题和多选题才写 ## 选项**，填空题和解答题不写此节。
9. 题目末尾放置 ========== 作为分割线（等号数量固定 10 个）。
10. **空白标记规则**：
    - 单选题/多选题：把题干中的空括号（如 `(\quad)` `（\quad）` `( )` `（ ）` `（  ）`）**删掉，换成 [选]**。如果 OCR 没抓到空括号，则在句末补一个 [选]
    - 填空题：把题干中的横线（`____` `\_\_\_\_`）或空括号**删掉，换成 [填]**。填空题可能有多个空（如"$a=$____，$b=$____"→"$a=$ [填]，$b=$ [填]"），每个空各换一个 [填]。OCR 没抓到空则句末补 [填]
    - **[选] 和 [填] 不能出现在 $...$ 数学环境内部**。如果原空白在 $...$ 里面（如 `$x = (\quad)$`），需要先把 $ 闭合再放标记：`$x =$ [选]`
    - 空白可能出现在题干中间或末尾，一律原位替换
11. **题源提取**：若题干开头有题源标记（如「【25海淀一模】」「（25海淀一模）」），提取为 source 并从题干中删除该标记；若没有，则用「统一填写」行的 source 值；两者都无则留空。
12. 表格改为 markdown 表格，不要用 `<table><tr><td>`

## 目标格式（每道题按此模板输出）

---
qid: 留空
grade: （用户会统一指定，如"所有 grade 填 高一"；未指定则留空）
source: （优先从题干开头题源标记提取，没有则用「统一填写」行的值；都无则留空）
number: （题号，如 T1、T2）
type: （单选题/多选题/填空题/解答题，四选一）
difficulty: （从原文【难度】提取数值，没有则留空）
semester: （用户会统一指定，如"所有 semester 填 高二上学期"；未指定则留空）
exam_type: （用户会统一指定，如"所有 exam_type 填 模考"；未指定则留空）
knowledge: []
ai_tags: []
tags: []
status: 待入库
selected: false
---
（注意：YAML 前后各三个减号 ---，不要多也不要少）

## 题目
（题干内容，公式用 $...$ 包裹。选择题末尾加 [选]，填空题有空加 [填]）
例如：已知集合 $A = \{x \mid x > 1\}$，则 $A$ 的补集为 [选]

## 选项
（**仅单选题和多选题写此节**，格式如下）
A．（选项内容）
B．（选项内容）
...

（填空题示例）
例如：函数 $f(x)$ 的最大值为 [填]

## 备注

### 我的备注

### AI备注



## 答案
（从原文【答案】提取，没有则写「（无）」）

## 解析
（从原文【详解】提取，没有则写「（无）」）

==========

（下一道题继续按同样格式，直到全部题目处理完毕）

## 输出前自检

全部处理完后逐题检查：

- 选择题：题干中不能有 `( )` `（ ）` `（\quad）` `(\quad)` `____`，只能有 [选]；每题至少一个 [选]；[选] 不在 $...$ 内
- 填空题：题干中不能有 `____` `___` `( )` `（ ）` `（\quad）`，只能有 [填]；每题至少一个 [填]；[填] 不在 $...$ 内
- 表格：不要用 `<table><tr><td>`，用 markdown 表格格式
- 题源：若题干开头有题源标记，检查是否已提取到 source 并从题干中删除

## OCR输出如下：
```

``````

---

## 209 · mirror/math-atlas/docs/AI排版提示词_中考真题.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/docs/AI%E6%8E%92%E7%89%88%E6%8F%90%E7%A4%BA%E8%AF%8D_%E4%B8%AD%E8%80%83%E7%9C%9F%E9%A2%98.md) · SHA 43adc56a7cbc7e0c13f91263cfac9a8fa3d71d6e · mode 100644

``````markdown
```
你是初中数学题库整理专家。请把以下 MinerU 输出的高考真题 markdown 整理为标准格式。

**⚠️ 请一次性处理下方全部题目，不要中断、不要要求我拆分。按模板逐题输出即可。**

## 硬性规则（违反即不合格）

1. **不解题**：不做任何计算、推理、判断。原文没有的答案和解析绝不补充，标「（无）」即可。
2. **不自编**：不对难度、知识点做任何猜测。原文有的就填，没有的全部留空。
3. **不生成 AI 备注**：「AI备注」标题保留，内容留空（不写任何字）。
4. **不改变内容**：只调整排版和公式格式，不增删改原文的任何一字一句。
5. **不填 qid**：qid 保留模板值「留空」。source 从文件开头的 # 标题取（如 `# 11安徽文` → `source: 11安徽文`）。

## 格式规范

6. 所有数学公式用 $...$（行内）或 $$...$$（独立行）包裹，不要用 \(...\) 或其它格式。
   **题干中的公式必须用 $...$（行内），不要用 $$...$$**；解析中较长的推导公式可用 $$...$$。
   **分数统一用 \dfrac，仅角标/指数中的分数保留 \frac**（如 $x^{\frac{1}{2}}$）。
   **所有数学字母必须进 $...$**，哪怕是单个 $A$、$x$、$b$ 也不例外（数学环境用斜体，正文用正体，混写不规范）。
7. 选项统一为 A．... B．... C．... D．...，一行一个。
8. 每道题包含 ## 题目、## 答案、## 解析。**只有单选题才写 ## 选项**，填空题和解答题不写此节。
9. 题目末尾放置==========作为分割线（等号数量固定 10 个）。
10. **空白标记规则**：
   - 单选题：把题干中的空括号（如 `(\quad)` `（\quad）` `( )` `（ ）` `（  ）`）**删掉，换成 [选]**。如果 OCR 没抓到空括号，则在句末补一个 [选]
   - 填空题：把题干中的横线（`____` `\_\_\_\_`）或空括号**删掉，换成 [填]**。填空题可能有多个空（如"$a=$____，$b=$____"→"$a=$ [填]，$b=$ [填]"），每个空各换一个 [填]。OCR 没抓到空则句末补 [填]
   - **[选] 和 [填] 不能出现在 $...$ 数学环境内部**。如果原空白在 $...$ 里面（如 `$x = (\quad)$`），需要先把 $ 闭合再放标记：`$x =$ [选]`
   - 空白可能出现在题干中间或末尾，一律原位替换
11.表格改为markdown表格,不要用<table><tr><td>
12. **输出前自检**：全部处理完后逐题检查：
   - 选择题：题干中不能有 `( )` `（ ）` `（\quad）` `(\quad)` `____`，只能有 [选]；每题至少一个 [选]；[选] 不在 $...$ 内
   - 填空题：题干中不能有 `____` `___` `( )` `（ ）` `（\quad）`，只能有 [填]；每题至少一个 [填]；[填] 不在 $...$ 内
   - 表格:不要用<table><tr><td>,用markdown表格格式

## 目标格式（每道题按此模板输出）

---
qid: 留空
grade: 九
source:
number:
type:
difficulty:
semester: 九下
exam_type: 中考真题
knowledge: []
ai_tags: []
tags: []
status: 待入库
selected: false
---
（注意：YAML 前后各三个减号 ---，不要多也不要少）

## 题目
（题干内容，公式用 $...$ 包裹，末尾加 [选]）
例如：已知集合 $A = {x \mid x > 1}$，则 $A$ 的补集为 [选]

## 选项
（**仅单选题写此节**，格式如下）
A．（选项内容）
B．（选项内容）
...

（填空题示例）
例如：函数 $f(x)$ 的最大值为 [填]

## 备注

### 我的备注

### AI备注



## 答案
（从原文【答案】提取，没有则写「（无）」）

## 解析
（从原文【详解】提取，没有则写「（无）」）

==========

（下一道题继续按同样格式，直到全部题目处理完毕）

## 字段提取指南

| YAML 字段 | 从哪里取 |
|-----------|----------|
| grade | 保留模板值「九」，不变 |
| source | 从文件开头的 # 标题取，如 `# 11安徽文` → `11安徽文` |
| number | 题号，如 T1、T2... |
| type | 从二级标题提取：单选题 / 填空题 / 解答题 |
| difficulty | 从原文【难度】提取数值，没有则留空 |
| semester | 保留模板值「九下」，不变 |
| exam_type | 保留模板值「中考真题」，不变 |
| knowledge | 从原文【知识点】提取，填入 [] 内，多个用英文逗号 + 空格分隔，如 `[交集运算, 补集运算]` |
| tags | 留空 [] |
| ai_tags | 留空 [] |
| status | 保留模板值「待入库」，不变 |
| qid | 保留模板值「留空」，不变 |

## 注意事项

- 图片保持原样（![](...) 格式），不要改动。
- 原文中的表格尽量保持 Markdown 表格格式。

## MinerU 输出如下：
```

``````

---

## 210 · mirror/math-atlas/docs/AI排版提示词_八上.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/docs/AI%E6%8E%92%E7%89%88%E6%8F%90%E7%A4%BA%E8%AF%8D_%E5%85%AB%E4%B8%8A.md) · SHA f02b4b920274fdc9c6f17bfc8e293dab8e0b42d0 · mode 100644

``````markdown
```
你是初中数学题库整理专家。请把以下 MinerU 输出的高考真题 markdown 整理为标准格式。

**⚠️ 请一次性处理下方全部题目，不要中断、不要要求我拆分。按模板逐题输出即可。**

## 硬性规则（违反即不合格）

1. **不解题**：不做任何计算、推理、判断。原文没有的答案和解析绝不补充，标「（无）」即可。
2. **不自编**：不对难度、知识点做任何猜测。原文有的就填，没有的全部留空。
3. **不生成 AI 备注**：「AI备注」标题保留，内容留空（不写任何字）。
4. **不改变内容**：只调整排版和公式格式，不增删改原文的任何一字一句。
5. **不填 qid**：qid 保留模板值「留空」。source 从文件开头的 # 标题取（如 `# 11安徽文` → `source: 11安徽文`）。

## 格式规范

6. 所有数学公式用 $...$（行内）或 $$...$$（独立行）包裹，不要用 \(...\) 或其它格式。
   **题干中的公式必须用 $...$（行内），不要用 $$...$$**；解析中较长的推导公式可用 $$...$$。
   **分数统一用 \dfrac，仅角标/指数中的分数保留 \frac**（如 $x^{\frac{1}{2}}$）。
   **所有数学字母必须进 $...$**，哪怕是单个 $A$、$x$、$b$ 也不例外（数学环境用斜体，正文用正体，混写不规范）。
7. 选项统一为 A．... B．... C．... D．...，一行一个。
8. 每道题包含 ## 题目、## 答案、## 解析。**只有单选题才写 ## 选项**，填空题和解答题不写此节。
9. 题目末尾放置==========作为分割线（等号数量固定 10 个）。
10. **空白标记规则**：
   - 单选题：把题干中的空括号（如 `(\quad)` `（\quad）` `( )` `（ ）` `（  ）`）**删掉，换成 [选]**。如果 OCR 没抓到空括号，则在句末补一个 [选]
   - 填空题：把题干中的横线（`____` `\_\_\_\_`）或空括号**删掉，换成 [填]**。填空题可能有多个空（如"$a=$____，$b=$____"→"$a=$ [填]，$b=$ [填]"），每个空各换一个 [填]。OCR 没抓到空则句末补 [填]
   - **[选] 和 [填] 不能出现在 $...$ 数学环境内部**。如果原空白在 $...$ 里面（如 `$x = (\quad)$`），需要先把 $ 闭合再放标记：`$x =$ [选]`
   - 空白可能出现在题干中间或末尾，一律原位替换
11.表格改为markdown表格,不要用<table><tr><td>
12. **输出前自检**：全部处理完后逐题检查：
   - 选择题：题干中不能有 `( )` `（ ）` `（\quad）` `(\quad)` `____`，只能有 [选]；每题至少一个 [选]；[选] 不在 $...$ 内
   - 填空题：题干中不能有 `____` `___` `( )` `（ ）` `（\quad）`，只能有 [填]；每题至少一个 [填]；[填] 不在 $...$ 内
   - 表格:不要用<table><tr><td>,用markdown表格格式

## 目标格式（每道题按此模板输出）

---
qid: 留空
grade: 八
source:25郑州外国语
number:
type:
difficulty:
semester: 八上
exam_type: 练习题
knowledge: []
ai_tags: []
tags: []
status: 待入库
selected: false
---
（注意：YAML 前后各三个减号 ---，不要多也不要少）

## 题目
（题干内容，公式用 $...$ 包裹，末尾加 [选]）
例如：已知集合 $A = {x \mid x > 1}$，则 $A$ 的补集为 [选]

## 选项
（**仅单选题写此节**，格式如下）
A．（选项内容）
B．（选项内容）
...

（填空题示例）
例如：函数 $f(x)$ 的最大值为 [填]

## 备注

### 我的备注

### AI备注



## 答案
（从原文【答案】提取，没有则写「（无）」）

## 解析
（从原文【详解】提取，没有则写「（无）」）

==========

（下一道题继续按同样格式，直到全部题目处理完毕）

## 字段提取指南

| YAML 字段 | 从哪里取 |
|-----------|----------|
| grade | 保留模板值「八」，不变 |
| source | 从文件开头的 # 标题取，如 `# 11安徽文` → `11安徽文` |
| number | 题号，如 T1、T2... |
| type | 从二级标题提取：单选题 / 填空题 / 解答题 |
| difficulty | 从原文【难度】提取数值，没有则留空 |
| semester | 保留模板值「九下」，不变 |
| exam_type | 保留模板值「中考真题」，不变 |
| knowledge | 从原文【知识点】提取，填入 [] 内，多个用英文逗号 + 空格分隔，如 `[交集运算, 补集运算]` |
| tags | 留空 [] |
| ai_tags | 留空 [] |
| status | 保留模板值「待入库」，不变 |
| qid | 保留模板值「留空」，不变 |

## 注意事项

- 图片保持原样（![](...) 格式），不要改动。
- 原文中的表格尽量保持 Markdown 表格格式。
- 分两段输出，避免输出不完整导致截断缺内容

## MinerU 输出如下：
```

``````

---

## 211 · mirror/math-atlas/docs/AI排版提示词_高考真题.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-atlas/docs/AI%E6%8E%92%E7%89%88%E6%8F%90%E7%A4%BA%E8%AF%8D_%E9%AB%98%E8%80%83%E7%9C%9F%E9%A2%98.md) · SHA ddc578a80e3ca06e2e9e268cda5879017fa629f3 · mode 100644

``````markdown
```
你是高中数学题库整理专家。请把以下 MinerU 输出的高考真题 markdown 整理为标准格式。

**⚠️ 请一次性处理下方全部题目，不要中断、不要要求我拆分。按模板逐题输出即可。**

## 硬性规则（违反即不合格）

1. **不解题**：不做任何计算、推理、判断。原文没有的答案和解析绝不补充，标「（无）」即可。
2. **不自编**：不对难度、知识点做任何猜测。原文有的就填，没有的全部留空。
3. **不生成 AI 备注**：「AI备注」标题保留，内容留空（不写任何字）。
4. **不改变内容**：只调整排版和公式格式，不增删改原文的任何一字一句。
5. **不填 qid**：qid 保留模板值「留空」。source 从文件开头的 # 标题取（如 `# 11安徽文` → `source: 11安徽文`）。

## 格式规范

6. 所有数学公式用 $...$（行内）或 $$...$$（独立行）包裹，不要用 \(...\) 或其它格式。
   **题干中的公式必须用 $...$（行内），不要用 $$...$$**；解析中较长的推导公式可用 $$...$$。
   **分数统一用 \dfrac，仅角标/指数中的分数保留 \frac**（如 $x^{\frac{1}{2}}$）。
   **所有数学字母必须进 $...$**，哪怕是单个 $A$、$x$、$b$ 也不例外（数学环境用斜体，正文用正体，混写不规范）。
7. 选项统一为 A．... B．... C．... D．...，一行一个。
8. 每道题包含 ## 题目、## 答案、## 解析。**只有单选题才写 ## 选项**，填空题和解答题不写此节。
9. 题目末尾放置==========作为分割线（等号数量固定 10 个）。
10. **空白标记规则**：
   - 单选题：把题干中的空括号（如 `(\quad)` `（\quad）` `( )` `（ ）` `（  ）`）**删掉，换成 [选]**。如果 OCR 没抓到空括号，则在句末补一个 [选]
   - 填空题：把题干中的横线（`____` `\_\_\_\_`）或空括号**删掉，换成 [填]**。填空题可能有多个空（如"$a=$____，$b=$____"→"$a=$ [填]，$b=$ [填]"），每个空各换一个 [填]。OCR 没抓到空则句末补 [填]
   - **[选] 和 [填] 不能出现在 $...$ 数学环境内部**。如果原空白在 $...$ 里面（如 `$x = (\quad)$`），需要先把 $ 闭合再放标记：`$x =$ [选]`
   - 空白可能出现在题干中间或末尾，一律原位替换
11.表格改为markdown表格,不要用<table><tr><td>
12. **输出前自检**：全部处理完后逐题检查：
   - 选择题：题干中不能有 `( )` `（ ）` `（\quad）` `(\quad)` `____`，只能有 [选]；每题至少一个 [选]；[选] 不在 $...$ 内
   - 填空题：题干中不能有 `____` `___` `( )` `（ ）` `（\quad）`，只能有 [填]；每题至少一个 [填]；[填] 不在 $...$ 内
   - 表格:不要用<table><tr><td>,用markdown表格格式

## 目标格式（每道题按此模板输出）

---
qid: 留空
grade: 高三
source:
number:
type:
difficulty:
semester: 高三下学期
exam_type: 高考真题
knowledge: []
ai_tags: []
tags: []
status: 待入库
selected: false
---
（注意：YAML 前后各三个减号 ---，不要多也不要少）

## 题目
（题干内容，公式用 $...$ 包裹，末尾加 [选]）
例如：已知集合 $A = {x \mid x > 1}$，则 $A$ 的补集为 [选]

## 选项
（**仅单选题写此节**，格式如下）
A．（选项内容）
B．（选项内容）
...

（填空题示例）
例如：函数 $f(x)$ 的最大值为 [填]

## 备注

### 我的备注

### AI备注



## 答案
（从原文【答案】提取，没有则写「（无）」）

## 解析
（从原文【详解】提取，没有则写「（无）」）

==========

（下一道题继续按同样格式，直到全部题目处理完毕）

## 字段提取指南

| YAML 字段 | 从哪里取 |
|-----------|----------|
| grade | 保留模板值「高三」，不变 |
| source | 从文件开头的 # 标题取，如 `# 11安徽文` → `11安徽文` |
| number | 题号，如 T1、T2... |
| type | 从二级标题提取：单选题 / 填空题 / 解答题 |
| difficulty | 从原文【难度】提取数值，没有则留空 |
| semester | 保留模板值「高三下学期」，不变 |
| exam_type | 保留模板值「高考真题」，不变 |
| knowledge | 从原文【知识点】提取，填入 [] 内，多个用英文逗号 + 空格分隔，如 `[交集运算, 补集运算]` |
| tags | 留空 [] |
| ai_tags | 留空 [] |
| status | 保留模板值「待入库」，不变 |
| qid | 保留模板值「留空」，不变 |

## 注意事项

- 图片保持原样（![](...) 格式），不要改动。
- 原文中的表格尽量保持 Markdown 表格格式。

## MinerU 输出如下：
```

``````

---

## 212 · mirror/math-lecture-notes/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-lecture-notes/README.md) · SHA 89e467fc9b66ffef4c66bfc141b25826985a3d57 · mode 100644

``````markdown
# 数学讲义全集 | Math Lecture Notes

高中数学教学资料库，包含 **140份** LaTeX 讲义与测试卷。

## 目录结构

```
├── 初中数学/                    # 七年级上册 ~ 九年级下册（28章）
│   ├── 七年级上册/
│   ├── 七年级下册/
│   ├── 八年级上册/
│   ├── 八年级下册/
│   ├── 九年级上册/
│   └── 九年级下册/
├── 初升高衔接/                  # 8个衔接专题
├── 高中数学/
│   ├── 高一必修第一册/          # 5章
│   ├── 高一必修第二册/          # 5章
│   ├── 高二选择性必修第一册/    # 3章
│   ├── 高二选择性必修第二册/    # 2章
│   └── 高三选择性必修第三册/    # 3章
├── 培优专题/                    # 21个拔高专题
├── 高考满分突破/                # 10讲高观点方法
└── 测试卷/
    ├── 初中测试卷/              # 6份（中考格式 120分）
    ├── 高中测试卷/              # 18份（高考格式 150分）
    ├── 培优测试卷/              # 21份（高考格式 150分）
    └── 高考满分突破测试卷/      # 10份（高考格式 150分）
```

## 内容概览

### 讲义（85份）

| 分类 | 数量 | 内容 |
|------|------|------|
| 初中数学 | 28份 | 人教版七年级上册 ~ 九年级下册全章节 |
| 初升高衔接 | 8份 | 集合、因式分解、二次函数、不等式、函数、三角函数、数列、向量 |
| 高中必修 | 10份 | 集合、函数、三角、向量、复数、立体几何、统计、概率 |
| 高中选必修 | 8份 | 空间向量、直线与圆、圆锥曲线、数列、导数、计数、统计分析 |
| 培优专题 | 21份 | 导数压轴、韦达定理、不等式放缩、数列递推、极点极线、构造法、数论等 |
| 高考满分突破 | 10份 | 极限思想、泰勒展开、线代视角、解析几何代数化、概率公理化、复数方法等 |

### 测试卷（55份）

| 分类 | 数量 | 格式 |
|------|------|------|
| 初中测试卷 | 6份 | 中考格式：120分/120分钟 |
| 高中测试卷 | 18份 | 高考格式：150分/120分钟 |
| 培优测试卷 | 21份 | 高考格式：150分/120分钟 |
| 高考满分突破测试卷 | 10份 | 高考格式：150分/120分钟 |

## 编译方式

所有 `.tex` 文件使用 XeLaTeX 编译：

```bash
xelatex -interaction=nonstopmode 文件名.tex
```

## 适用对象

- 初中数学教师（备课参考）
- 高中数学教师（课堂教学 + 培优辅导）
- 高三学生（高考冲刺 + 满分突破）
- 数学竞赛入门学生（培优专题）

## License

MIT License

``````

---

## 213 · mirror/math-lecture-notes/测试卷/测试卷模板说明.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/math-lecture-notes/%E6%B5%8B%E8%AF%95%E5%8D%B7/%E6%B5%8B%E8%AF%95%E5%8D%B7%E6%A8%A1%E6%9D%BF%E8%AF%B4%E6%98%8E.md) · SHA 8a4be5b9a9ac6483e4810844f99ecb4efebe63a7 · mode 100644

``````markdown
# 测试卷模板说明

## 中考格式（初中测试卷）
- 总分：120分，时间：120分钟
- 一、选择题：10题 × 3分 = 30分
- 二、填空题：6题 × 3分 = 18分
- 三、解答题：8题，共72分（8+8+8+9+9+10+10+10）

## 高考格式（高中/培优/满分突破测试卷）
- 总分：150分，时间：120分钟
- 一、单项选择题：8题 × 5分 = 40分
- 二、多项选择题：4题 × 5分 = 20分（全对5分，部分对2分，有错0分）
- 三、填空题：4题 × 5分 = 20分
- 四、解答题：6题，共70分（10+12+12+12+12+12）

## LaTeX文档结构

```latex
\documentclass[12pt, a4paper]{ctexart}
\usepackage[margin=2cm]{geometry}
\usepackage{amsmath, amssymb}
\usepackage{enumitem}
\usepackage{tcolorbox}
\usepackage{fancyhdr}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{graphicx}
\usepackage{pgfplots}
\usepackage{tabularx}
\pgfplotsset{compat=1.18}

\definecolor{mainblue}{RGB}{41, 98, 168}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\textcolor{mainblue}{XX学校·XX测试卷}}
\fancyhead[R]{\small\textcolor{mainblue}{数学}}
\fancyfoot[C]{\small —\ \thepage\ —}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{mainblue}\leaders\hrule height \headrulewidth\hfill}}

\setCJKmainfont{Hiragino Sans GB}
\setCJKsansfont{Heiti SC}

\begin{document}

\begin{center}
{\Large\bfseries XX学校2025-2026学年度XX测试卷}\\[6pt]
{\normalsize 数学}\\[4pt]
{\small 考试时间：120分钟\quad 满分：150分}
\end{center}

\vspace{4pt}
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
题号 & 一 & 二 & 三 \\ \hline
得分 & & & \\ \hline
\end{tabular}
\end{center}
\vspace{6pt}

\noindent\textbf{注意事项：}
\begin{enumerate}[leftmargin=2em]
  \item 答题前，请用黑色签字笔在答题卡上填写姓名、班级和考号。
  \item 选择题请用2B铅笔在答题卡上涂黑对应选项。
  \item 非选择题请用黑色签字笔在答题卡指定区域作答。
\end{enumerate}

% ============ 选择题 ============
\section*{一、单项选择题（本大题共8小题，每小题5分，共40分）}

\begin{enumerate}
  \item 题目内容
  \begin{enumerate}[label=\Alph*.]
    \item 选项A \quad \item 选项B \quad \item 选项C \quad \item 选项D
  \end{enumerate}
\end{enumerate}

% ============ 多选题 ============
\section*{二、多项选择题（本大题共4小题，每小题5分，共20分。全部选对得5分，部分选对得2分，有选错的得0分）}

% ============ 填空题 ============
\section*{三、填空题（本大题共4小题，每小题5分，共20分）}

\begin{enumerate}[resume]
  \item 题目内容 \hfill $\boxed{\qquad}$
\end{enumerate}

% ============ 解答题 ============
\section*{四、解答题（本大题共6小题，共70分。解答应写出文字说明、证明过程或演算步骤）}

\begin{enumerate}[resume]
  \item （本小题10分）题目内容

\vspace{5cm}

  \item （本小题12分）题目内容

\vspace{6cm}
\end{enumerate}

\vfill
\begin{center}
\small\textcolor{gray}{本试卷仅供教学参考}
\end{center}

\end{document}
```

## 注意事项
- 每道选择题选项用 `\begin{enumerate}[label=\Alph*.]` 排列
- 填空题用 `\hfill $\boxed{\qquad}$` 表示答案位置
- 解答题留足空白（`\vspace{}`）供作答
- 大题分值标注格式：（本小题X分）
- 题目难度分布：基础60% + 中等25% + 拔高15%

``````

---

## 214 · mirror/mathex/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/mathex/README.md) · SHA 47947f71d7d08d5c1d4c326c1edcd2fd4f178f47 · mode 100644

``````markdown
# 高中数学之旅

一本面向高考的高中数学习题集，包含习题册与配套答案册，采用 LaTeX (XeLaTeX + ctexbook) 排版。

## 📖 简介

本项目收录了高中数学各章节的典型习题与详细解析，覆盖集合与逻辑、函数与导数、向量、立体几何、解三角形、圆锥曲线、数列、概率与统计等核心知识点。每章按知识框架→选择题→解答题的结构组织，习题册采用左栏题目、右栏答题区的双栏排版设计。

## 📚 章节概览

| 章节 | 选择题 | 解答题 | 内容 |
|------|--------|--------|------|
| 集合和逻辑用语 | 8 | 5 | 集合运算、命题与逻辑 |
| 函数与导数 | 2 | — | 函数性质与导数应用 |
| 向量 | 9 | — | 向量运算、数量积与几何应用 |
| 立体几何 | 4 | — | 空间几何体、线面关系 |
| 解三角形 | — | 6 | 正余弦定理、取值范围、面积问题 |
| 圆锥曲线 | 3 | 1 | 椭圆、双曲线与抛物线 |
| 数列 | — | 3 | 等差等比、数列综合 |
| 概率与统计 | 1 | 1 | 概率计算与统计分析 |

## 📂 项目结构

```
exercise/
├── main.tex                  # 习题册主文件
├── main_solutions.tex        # 答案册主文件
├── .latexmkrc                # latexmk 编译配置
├── preamble/                 # 导言区模块
│   ├── packages.tex          # 宏包调用
│   ├── colors.tex            # 颜色定义
│   ├── fonts.tex             # 字体配置
│   ├── macros.tex            # 语义化命令与工具宏
│   ├── environments.tex      # xsim 习题环境定义 + tcolorbox 模板
│   └── pagestyle.tex         # 页眉页脚样式
├── covers/                   # 封面/封底
│   ├── cover-exercise.tex    # 习题册封面
│   ├── backcover-exercise.tex
│   ├── cover-solutions.tex   # 答案册封面
│   └── backcover-solutions.tex
├── chapters/                 # 章节结构文件（仅 \input 引用）
│   ├── 集合.tex
│   ├── 函数与导数.tex
│   ├── 向量.tex
│   ├── 立体几何.tex
│   ├── 解三角形.tex
│   ├── 圆锥曲线.tex
│   ├── 数列.tex
│   └── 概率与统计.tex
├── database/                 # 题库（一题一文件）
│   ├── 集合/                 # choice_001~008, exercise_001~005
│   ├── 函数与导数/            # choice_001~002
│   ├── 向量/                  # choice_001~009
│   ├── 立体几何/             # choice_001~004
│   ├── 解三角形/              # exercise_001~006
│   ├── 圆锥曲线/             # choice_001~003, exercise_001
│   ├── 数列/                  # exercise_001~003
│   └── 概率与统计/            # choice_001, exercise_001
└── README.md
```

### 题库文件格式

**选择题** (`choice_NNN.tex`)：
```latex
\begin{choice}[source={来源}, topic={知识点}]
题目内容
\begin{tasks}(2)
\task ... \task ... \task ... \task ...
\end{tasks}
\end{choice}
\begin{choice-sol}
解析内容
\end{choice-sol}
```

**解答题** (`exercise_NNN.tex`)：
```latex
\begin{prob}[topic={知识点}, score=12]
题目内容
\end{prob}
\begin{prob-sol}
解析内容
\end{prob-sol}
```

## 🔨 编译方式

本项目使用 **XeLaTeX** 编译，推荐在 WSL (Ubuntu) 环境下使用 `latexmk` 自动化工具：

```bash
# 编译习题册（24页，双栏答题区）
latexmk -xelatex main.tex

# 编译答案册（30页，仅解析）
latexmk -xelatex main_solutions.tex
```

### 编译依赖

- **TeX 发行版**：[TeX Live](https://www.tug.org/texlive/) 2025+（需安装 `texlive-xetex`、`texlive-latex-extra`、`texlive-fonts-extra`、`texlive-lang-chinese`、`texlive-science`）
- **中文字体**：SimSun、SimHei、STKaiti、FangSong（安装到系统字体目录）
- **数学字体**：NewCMMath（TeX Live `texlive-fonts-extra` 自带）

### 主要宏包

| 宏包 | 用途 |
|------|------|
| ctexbook | 中文文档类 |
| xsim | 习题与解析管理（choice/prob 两种类型） |
| tcolorbox | 彩色方框（题目/知识框架/解析环境） |
| paracol | 左右双栏排版（习题册专用） |
| tasks | 选择题选项排版 |
| tikz | 封面/封底绘制、答题卡方框 |
| unicode-math | Unicode 数学字体支持 |

## 🏗️ 架构设计

- **内容-格式分离**：题目内容存放于 `database/` 目录（一题一文件），格式模板集中在 `preamble/environments.tex`，章节文件 `chapters/` 仅做结构编排
- **双输出模式**：同一套数据库文件，通过 `main.tex`（习题册）和 `main_solutions.tex`（答案册）两套控制器分别编译
- **xsim 管理**：使用 xsim 的 `DeclareExerciseType` 定义 choice（选择题）和 prob（解答题）两种类型，配合 `\IfSolutionPrintF` 实现条件排版
- **语义化命令**：`\R`、`\N`、`\Z`、`\Q`、`\dd`、`\ee`、`\ii` 等数学符号宏，便于统一修改

## 🎨 设计特色

- **Springer 风格封面**：橙色主调，顶部横栏 + 左侧竖栏布局
- **镜像封底**：底部横栏 + 右侧竖栏，与封面形成镜像关系，附有习题册简介
- **灰度内页**：正文部分采用灰度配色方案，适合黑白打印
- **双栏答题设计**：习题册左栏为题目，右栏为答题区（选择题含涂卡方框，解答题含作答横线）

## 📥 下载

前往 [Releases](https://github.com/ShinozakiKasumi/exercise/releases) 页面下载最新版本的习题册与答案册 PDF。

## 📝 致谢

致那些不是从知乎来的游客：请访问知乎@余命数的文章，或添加作者 QQ 2454167821，获取详情。

## 📄 License

本项目仅供学习交流使用。

``````

---

## 215 · mirror/mathpaper/README.md

[原始文件独立链接](https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive/blob/full-source-archive/mirror/mathpaper/README.md) · SHA 315af0de3fbe977a686940d2f6c8db41a5dcc35e · mode 100644

``````markdown
# MathPaper

数学试卷，Latex 排版，多数的来源是网络。

本库所采用的是单页 A4 的格式。因为这样子兼容性最强，可以轻松改成 A3。具体参考高考试卷LaTeX模板中的2017quanguo3.tex

自定义宏包在 Package 文件夹下，记得安装。

## 目前收录

### Word 版

#### 2016

- 四川卷（文科）

### 图片版

#### 2022

- 全国乙卷（文科）

### Latex 版

#### 2016

- 上海卷（理科）

#### 2017

- 全国 III 卷（理科）
- 江苏卷

## 版本解释

- SNE: Standard National Examination 全国卷
- Jiangsu: 江苏卷
- Shanghai: 上海卷

## 特别鸣谢

- [高考试卷LaTeX模板](https://github.com/shaodongtang/gaokao_exam)

``````

