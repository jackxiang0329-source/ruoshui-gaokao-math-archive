@echo off
chcp 65001 >nul
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0import_all_11_sources.ps1"
if errorlevel 1 echo 导入有错误，请根据屏幕提示重试。
pause
