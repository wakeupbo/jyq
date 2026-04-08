@echo off
echo ========================================
echo    ❤️ 表白网站一键部署工具 ❤️
echo ========================================
echo.

echo 正在启动本地测试服务器...
echo 访问地址: http://localhost:8000/confession.html
echo.

REM 启动HTTP服务器
python -m http.server 8000

pause