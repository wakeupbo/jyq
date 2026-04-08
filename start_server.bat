@echo off
echo 启动表白网站公网访问...
echo.

echo 正在安装必要的工具...
pip install flask pyngrok

echo.
echo 请选择内网穿透方式:
echo 1. ngrok (需要注册账户)
echo 2. LocalTunnel (免费，无需注册)
echo 3. 仅本地运行
echo.

set /p choice="请输入选择 (1/2/3): "

if "%choice%"=="1" (
    echo.
    echo 使用ngrok:
    echo 1. 访问 https://dashboard.ngrok.com/signup 注册账户
    echo 2. 获取authtoken
    echo 3. 运行: ngrok config add-authtoken YOUR_TOKEN
    echo 4. 然后运行: python web_confession.py
    pause
) else if "%choice%"=="2" (
    echo.
    echo 使用LocalTunnel (推荐)...
    echo 正在启动LocalTunnel...

    REM 安装Node.js (如果没有的话)
    where node >nul 2>nul
    if %errorlevel% neq 0 (
        echo 需要安装Node.js才能使用LocalTunnel
        echo 请访问 https://nodejs.org 下载安装
        pause
        exit /b
    )

    REM 启动Flask服务器
    start /b python web_confession.py

    REM 等待一下让Flask启动
    timeout /t 3 /nobreak >nul

    REM 启动LocalTunnel
    echo 正在创建公网链接...
    npx localtunnel --port 5000

) else if "%choice%"=="3" (
    echo.
    echo 仅本地运行...
    python web_confession.py
) else (
    echo 无效选择
    pause
)