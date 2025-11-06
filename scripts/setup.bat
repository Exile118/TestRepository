@echo off
REM Windows 环境设置脚本

echo 🚀 开始设置开发环境...

REM 检查 Python
echo 📌 检查 Python 版本...
python --version
if errorlevel 1 (
    echo ❌ 未找到 Python，请先安装 Python 3.9+
    exit /b 1
)

REM 创建虚拟环境
echo 📦 创建虚拟环境...
if exist venv (
    echo ⚠️ 虚拟环境已存在，跳过创建
) else (
    python -m venv venv
    echo ✅ 虚拟环境创建成功
)

REM 激活虚拟环境
echo 🔌 激活虚拟环境...
call venv\Scripts\activate.bat

REM 升级 pip
echo ⬆️ 升级 pip...
python -m pip install --upgrade pip

REM 安装依赖
echo 📥 安装项目依赖...
pip install -r requirements.txt

REM 安装开发工具
echo 🛠️ 安装开发工具...
pip install -e .

echo.
echo ✨ 环境设置完成！
echo.
echo 下一步:
echo   1. 激活虚拟环境: venv\Scripts\activate
echo   2. 运行测试: pytest
echo   3. 运行应用: python src\main.py
echo.
echo Happy coding! 🎉
