# 11 个固定上游仓库：一键完整实体导入

目标是把 sources.json 中 11 个固定版本上游仓库的原始 Git Blob 搬入本仓库 mirror/ 对应来源目录，包括 PDF、PNG、DOCX、TeX，而不是只放链接或 gitlink 子模块。

## Windows 一键运行

1. 安装 Git for Windows 和 Python 3。克隆/推送私有仓库时通过 Git Credential Manager 登录自己的 GitHub 账号，脚本不保存令牌。
2. 使用仓库最新代码，双击 scripts/一键导入11个仓库.cmd。若尚无本地 Git 工作副本，PowerShell 启动器会克隆私有仓库到用户目录下的 ruoshui-gaokao-math-archive。
3. 脚本处理 11 个固定 SHA，已完整匹配的来源自动跳过，每个未完整仓库在 SHA 校验后单独快进推送 main；网络失败时重新运行可续接。

也可手工执行：

    python3 scripts/import_pinned_git_trees.py --push

仅导入一个来源：

    python3 scripts/import_pinned_git_trees.py --source gaokaomath --push

不加 --push 时只预览，需要下载源 Git 对象，但不上传文件。

## 数据安全与完整性

- 来源版本来自 origin/main 已提交的 sources.json，不使用上游最新浮动 HEAD。
- 采用 Git 完整对象 fetch；特意不用 blob:none 过滤，保证 PDF 和图片等 Git 对象的真实字节随同复制。
- 使用独立临时 Git index 和原生 git read-tree 将整棵上游目录树置于 mirror/<id>；不使用 rsync，也不改用户当前工作文件和普通 Git index。
- 只有在完整目标子树 SHA 与固定上游树 SHA 完全一致时才创建提交，包括子目录、内容、符号链接模式。
- 禁止强制推送；他人并行更新 main 时推送失败，重新运行即可处理。
- 遇到上游嵌套 Git 子模块会报错而非谎称已复制。已检查本批 11 个固定版递归树，没有嵌套 gitlink。
- Git LFS 指针仍需独立处理对应 LFS 真实资源。Git 对象一致不等于确认全部外部 LFS 对象已复制。

## 完整度与验收边界

已独立核算最新仓库状态：2,148 / 7,222 个上游源 Blob 严格匹配，5,074 个未完成，剩余原始 Git Blob 字节 563,289,092（约 563.3 MB）。当前聊天的 GitHub 连接对大于约 1 MB 的二进制内容经常仅返回空数据，因此通过正常 Git fetch/push 才能可靠迁入剩余大型文件。

历史 GitHub Actions 在 Runner 执行步骤前失败，不能声称在线全量镜像已通过；本地一键命令需要 Windows 电脑能够连接 GitHub 并拥有私有仓库推送权限。

即使 11 个上游 Git 树完全匹配，也不等于试题真实性、数学证明正确性、全部 PDF 可出版或第三方材料再分发权利已经核实。

本轮又直接通过 GitHub 对象写入 88 个 PDF/TeX 源文件，已逐路径核对固定上游 SHA、原始模式和大小。完整记录：mirror/DIRECT_IMPORT_88_FILES_2026_10_25.json。注意一键导入的 Git 推送完成后，镜像总量 JSON 需要按最新 main 重新复算，不应拿本轮旧快照视为全部完成。


## 最近核对（2026-10-26）

主分支已额外搬运并逐项验收 **35 个固定来源原始文件**（6 份专题 PDF、6 份历年试卷 PDF、18 份 TeX 插图源码、5 份说明／许可／注释文件），新增原始字节 **1,416,616**，最终完整比对 **2,148/7,222**。逐文件的完整 SHA、mode、路径、原始字节数保存在 [35 文件导入清单](../mirror/DIRECT_IMPORT_35_FILES_2026_10_26.json)，不是仅添加 Git 子模块。GitHub Actions 若持续在无执行步骤的状态失败，仍需由具备 GitHub 登录态和正常 Git 网络的计算机执行上述一键导入，将剩余大文件真正推送到 main。
