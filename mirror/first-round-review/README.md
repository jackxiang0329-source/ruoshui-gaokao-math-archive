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
