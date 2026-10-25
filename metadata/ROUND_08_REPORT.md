# 第八轮质检：数学审核与固定来源一致性（2026-10-25）

## 数学复核提交

- 对 [2023 北京卷第 20 题](https://github.com/DxAThing/Gaokao-Math-Problems-Compilation/blob/f1ae169b58a75b3db6e35c670b3f0d5c78718188/content/2023/beijing.tex#L627) 重新核对了全部三问。独立证明见 [Markdown](../derivative/reviewed/2023-beijing-q20.md) 与 [TeX](../derivative/reviewed/2023-beijing-q20.tex)。
- 参数为 $a=-1,b=1$；导函数的导数为 $g'(x)=-x(x^2-6x+6)e^{1-x}$；全域恰有 3 个极值点。逐区间验证了根的唯一性及导数变号。
- 三组 JSON/CSV 索引、主索引以及审核溯源已同步：总来源记录 248；独立数学核验 **16 条记录，对应 14 道不同题目**；余下 232 条来源记录未核验。
- 未声称新 TeX 已编译，也未把数学证明自动当作试卷真伪或版权审核。

## 工程安全修复

原同步脚本使用 \`git submodule update --remote\`，会检出未固定的上游分支 HEAD，与 \`sources.json\` 已记录 SHA 及主仓库 gitlink 不一致。

- 修改同步流程，只检出 Git 树中已固定的子模块提交，停止 \`--remote\` 漂移。
- 引入 [validate_pinned_sources.py](../scripts/validate_pinned_sources.py)：检查来源清单中 11 个 SHA、Git 暂存树 gitlink 模式与 SHA、\`.gitmodules\` 的 URL/分支，并在实体检出后验证 HEAD。
- 引入 5 条针对模式、丢失项、多余项、篡改 SHA、路径绕过的单元测试。
- 引入 [offline-qa 工作流](../.github/workflows/audit-archive.yml)：不下载数 GB 子模块即可检查来源锁定、单元测试、题目级索引与质检溯源，避免网络克隆失败掩盖本地元数据错误。

## 验收边界

数学结果通过独立解析及符号计算、数值交叉验证。文本代码已写入 GitHub；新 CI 在 GitHub Runner 真正完成之前，不声明在线测试通过。本轮未生成 PDF、ZIP 或编译成品；未进行原卷影像质检。
