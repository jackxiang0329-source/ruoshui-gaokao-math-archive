#Requires -Version 5.1
<#
一键将 11 个固定上游 Git 仓库的真实 Blob 导入用户的高考数学仓库。
需要 Git for Windows、Python 3 及访问私有 GitHub 仓库的账号。
不在脚本内保存 Token，不强推，不覆盖已检出的工作目录。
#>
param(
  [string]$Source = 'all',
  [string]$Destination = (Join-Path $HOME 'ruoshui-gaokao-math-archive')
)
$ErrorActionPreference = 'Stop'
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw '缺少 Git，请先安装 Git for Windows。' }
$python = Get-Command py -ErrorAction SilentlyContinue
if ($python) { $pythonArgs = @('-3') }
else {
  $python = Get-Command python -ErrorAction SilentlyContinue
  if (-not $python) { throw '缺少 Python 3，请先安装 Python 3。' }
  $pythonArgs = @()
}
$checkout = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
if (-not (Test-Path (Join-Path $checkout '.git'))) {
  $checkout = $Destination
  if (-not (Test-Path (Join-Path $checkout '.git'))) {
    Write-Host '克隆你的 GitHub 高考数学私有仓库；如需登录，请使用自己的 GitHub 账号。'
    & git clone 'https://github.com/jackxiang0329-source/ruoshui-gaokao-math-archive.git' $checkout
    if ($LASTEXITCODE -ne 0) { throw 'Git clone 失败，请检查网络和仓库权限。' }
  }
}
$script = Join-Path $checkout 'scripts/import_pinned_git_trees.py'
if (-not (Test-Path $script)) { throw '缺少最新版导入脚本，请先拉取仓库。' }
Write-Host ('开始导入固定来源：' + $Source)
Write-Host '每份来源以真实 Git 对象进入主仓库，不是子模块。'
& $python.Source @pythonArgs $script --root $checkout --source $Source --push
if ($LASTEXITCODE -ne 0) {
  throw '仍有来源未导入。修复上方错误后重跑即可；已完成的仓库会自动跳过。'
}
Write-Host '导入命令执行成功。请重新复核原文件与第三方授权。'
