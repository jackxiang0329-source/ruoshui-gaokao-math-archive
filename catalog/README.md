# 去重整理目录

这是面向使用者的统一入口。**7,222 个原始文件属于来源镜像，不需要逐个打开。**

已核对 11 个固定上游镜像，发现 **198 个完全相同的 Git Blob 副本，涉及 189 个重复组**。首次正文相似度扫描由 [GitHub Actions](../.github/workflows/curate-archive.yml) 执行；本目录将自动生成按年份和专题的索引，以及代表文件/重复别名映射和待人工确认的相似内容清单。

资料不会因文件名近似而被直接删除或覆盖，所有原始 PDF、图片、答案、TeX 和来源路径保留在 [mirror/](../mirror/README.md)。

开始查看：[原有试卷索引](../index/INDEX.md) · [独立复核的导数题](../derivative/reviewed/README.md) · [重复题人工审查](../index/DUPLICATE_AUDIT.md)。
