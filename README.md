# 三千弱水 · 高考数学真题与导数压轴题库

> 高考数学历年真题与高中导数大题资源总库：保留 11 个上游仓库，聚合 TeX / Markdown / PDF / ZIP，逐步建设可检索、可复核的专题题库。

**仓库状态**：已建立上游来源清单及 Git 子模块；`upstream/` 中是指向原仓库固定版本的链接，**不是将数百 MB 二进制文件平铺复制**。独立文件级索引见 [index](index/)（运行索引脚本后生成）。数学答案和试题版权均未被自动验证。

## 使用

完整下载 11 个上游的文件及本项目分类目录：

```bash
git clone --recurse-submodules https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive.git
```

主仓库的 GitHub ZIP 下载 **不含子模块实体**。请使用上面的递归克隆命令，或在 GitHub 网页直接进入各个子模块仓库。首次克隆可能需要数 GB 空间。

## 内容导航

- **[高中导数大题](derivative/)**：单调性、极值、含参讨论、恒成立、隐零点、双零点、构造函数、零点个数。
- **[历年高考真题](past-papers/)**：按年份、地区和卷种建立元数据；不擅自合并不同版本。
- **[来源清单](sources.json)**：11 个上游项目的地址、默认分支、侧重点与许可核查结果。
- **[原始文件索引](index/)**：TeX、Markdown、PDF、ZIP 与候选导数/高考文件的 CSV 列表。
- **[版权与出处](metadata/source-attribution.md)**：每个原仓库继续适用自己的许可证；第三方试题和插图另行判断。

## 自动同步

`.github/workflows/sync-upstream.yml` 提供人工触发与按来源/脚本修改触发的同步流程：更新 Git 子模块、生成文件级索引并运行验证。在仓库的 **Actions** 页面可手动运行。

如果自动提交因仓库的 Actions 写入策略失败，需要在 **Settings → Actions → General → Workflow permissions** 允许 GitHub Actions 具有读写权限，或改为本地执行 `bash scripts/sync_sources.sh` 并推送。

## 11 个来源

| 来源 | 用途 |
|---|---|
| [Dreamaker203/math-lecture-notes](https://github.com/Dreamaker203/math-lecture-notes) | 导数压轴题专题 TeX/PDF |
| [DxAThing/Gaokao-Math-Problems-Compilation](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation) | 大型高考题库 LaTeX |
| [deekur/gaokaomath](https://github.com/deekur/gaokaomath) | 历年高考 PDF |
| [hbinfrog/first_round_review](https://github.com/hbinfrog/first_round_review) | 高三一轮复习、导数讲义 |
| [TsubameHata/gaokao_math_corpus](https://github.com/TsubameHata/gaokao_math_corpus) | 新高考 Markdown / YAML 结构化题面 |
| [ajsadhotmail/2024-China-Gaokao-Math](https://github.com/ajsadhotmail/2024-China-Gaokao-Math) | 2024 新高考 I 卷 TeX/PDF |
| [shaodongtang/gaokao_exam](https://github.com/shaodongtang/gaokao_exam) | 试卷 LaTeX 模板 |
| [Yan-Zero/MathPaper](https://github.com/Yan-Zero/MathPaper) | 历史高考 TeX 试卷 |
| [daxmate/math](https://github.com/daxmate/math) | 历史试卷与排版 |
| [sdmf6/math-atlas](https://github.com/sdmf6/math-atlas) | 题库检索与导出工具 |
| [SakurakaiCat/mathex](https://github.com/SakurakaiCat/mathex) | TeX 习题册 |

## 审核原则

`unreviewed → transcribed → math-checked → latex-compiled → reviewed`。**文件名命中 ≠ 已确认是导数大题；上游已有解析 ≠ 数学正确**。保留固定提交 SHA、原始路径与来源链接，后续逐题核验。

## 许可证

上游保持独立许可，不能把整个聚合库声称为一个统一许可证。部分原仓库存在许可声明不完整或第三方素材权利不明确的情况，详见 [sources.json](sources.json)。


## 题目级导数索引（2026-10-24）

[**2010—2026 年题目级总索引：166 条**](index/DERIVATIVE_PROBLEMS_2010_2026.md)：
2010—2014 年首批 45 条、2015—2019 年首批 63 条、2020—2026 年首批 58 条。
这里是 **来源定位记录**，不是去重后的独立题目数，更不是已经审核正确的答案数。

- [主索引 CSV](index/derivative-problems-2010-2026.csv) / [JSON](index/derivative-problems-2010-2026.json)
- [2010—2014 年来源记录](index/DERIVATIVE_PROBLEMS_2010_2014.md)
- [2015—2019 年来源记录](index/DERIVATIVE_PROBLEMS_2015_2019.md)
- [2020—2026 年来源记录](index/DERIVATIVE_PROBLEMS_2020_2026.md)
- [2019 全国Ⅱ卷文科第21题：已独立核验的 MD](derivative/reviewed/2019-national2-liberal-q21.md) / [TeX](derivative/reviewed/2019-national2-liberal-q21.tex)
- [2024 新高考Ⅰ、Ⅱ卷：两道已独立核验的 MD](derivative/reviewed/2024-two-proofs.md) / [TeX](derivative/reviewed/2024-two-proofs.tex)
- [题目级全量扫描脚本](scripts/scan_derivative_questions.py) 与 [题目索引一致性校验](scripts/validate_question_index.py)
- [第四轮导入与质检报告](metadata/ROUND_04_REPORT.md)

**独立数学质检：3 道。** 其余 163 条尚未逐题完成数学核查。
2010—2019 年先覆盖重点卷种，仍有省市卷别未穷尽。多卷相同题和变式使用 `duplicate_group` 保留溯源，当前没有盲目去重。

GitHub Actions 同步工作流仍发生执行器分配前失败，目前不能宣称已通过自动同步验收。
这一轮仅向 GitHub 提交索引、脚本和文字/TeX 源文件，**未生成或上传本地 PDF/ZIP**。
