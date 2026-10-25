# 2016 年高考数学 PDF 缺口核验及补齐（2026-10-25）

按固定上游版本 `deekur/gaokaomath@08179f1fc0a3300787155d92800ac82b57ee4118` 核对，共发现 2016 年 20 个 PDF 路径，其中原有 16 个，此轮实体补齐以下 4 个。二进制通过 GitHub Base64 API 提取，写入本仓库 Git Blob 后逐个比对 **40 位 Git SHA**，全部一致。

| 补齐文件（上游相对路径） | 原始大小（字节） | 已验证的 Blob SHA | 结果 |
|---|---:|---|---|
| `普通高考/2016/2016天津文.pdf` | 508978 | `de8a81c7e41013835fd732f3b69a9957628b327e` | SHA 一致 |
| `普通高考/2016/2016山东理.pdf` | 522207 | `83d9a18fbca14aa5d1d03f2cbda49dfc881cbabe` | SHA 一致 |
| `普通高考/2016/2016浙江文.pdf` | 546825 | `bff4bc4f22c8531faee72bc007c8f228983cf69f` | SHA 一致 |
| `普通高考/2016/2016浙江理.pdf` | 511104 | `a5d27c9ea092897aa485080613dcd4c34db328ed` | SHA 一致 |

四份文件路径在本仓库均为 `mirror/gaokaomath/<上游相对路径>`。

**校验边界：** 本轮仅确认新增四个文件的来源固定提交 SHA 与目标 Git Blob SHA 一致，不把文件名命中、PDF 字节完整视作题目数学正确性或第三方版权已核验。其余年份仍需逐项实体镜像和审校。

上游固定提交：[deekur/gaokaomath](https://github.com/deekur/gaokaomath/tree/08179f1fc0a3300787155d92800ac82b57ee4118)。
