#!/bin/bash

# 开发环境快速设置脚本
# 用法: ./scripts/setup.sh

set -e

echo "🚀 开始设置开发环境..."

# 检查 Python 版本
echo "📌 检查 Python 版本..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ 发现 Python $python_version"

# 创建虚拟环境
echo "📦 创建虚拟环境..."
if [ -d "venv" ]; then
    echo "⚠️  虚拟环境已存在，跳过创建"
else
    python3 -m venv venv
    echo "✅ 虚拟环境创建成功"
fi

# 激活虚拟环境
echo "🔌 激活虚拟环境..."
source venv/bin/activate

# 升级 pip
echo "⬆️  升级 pip..."
pip install --upgrade pip

# 安装依赖
echo "📥 安装项目依赖..."
pip install -r requirements.txt

# 安装开发工具
echo "🛠️  安装开发工具..."
pip install -e .

echo ""
echo "✨ 环境设置完成！"
echo ""
echo "下一步:"
echo "  1. 激活虚拟环境: source venv/bin/activate"
echo "  2. 运行测试: pytest"
echo "  3. 运行应用: python src/main.py"
echo ""
echo "Happy coding! 🎉"
