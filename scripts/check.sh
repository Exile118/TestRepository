#!/bin/bash

# 代码质量检查脚本
# 运行所有代码质量工具

set -e

echo "🔍 开始代码质量检查..."
echo ""

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Black 格式化检查
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 检查代码格式 (Black)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if black --check src/ tests/; then
    echo -e "${GREEN}✅ Black 检查通过${NC}"
else
    echo -e "${RED}❌ Black 检查失败${NC}"
    echo -e "${YELLOW}修复: black src/ tests/${NC}"
    exit 1
fi
echo ""

# isort 导入排序检查
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📚 检查导入排序 (isort)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if isort --check-only src/ tests/; then
    echo -e "${GREEN}✅ isort 检查通过${NC}"
else
    echo -e "${RED}❌ isort 检查失败${NC}"
    echo -e "${YELLOW}修复: isort src/ tests/${NC}"
    exit 1
fi
echo ""

# Flake8 代码风格检查
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎨 检查代码风格 (Flake8)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if flake8 src/ tests/ --max-line-length=127; then
    echo -e "${GREEN}✅ Flake8 检查通过${NC}"
else
    echo -e "${RED}❌ Flake8 检查失败${NC}"
    exit 1
fi
echo ""

# MyPy 类型检查
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 类型检查 (MyPy)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if mypy src/ --ignore-missing-imports; then
    echo -e "${GREEN}✅ MyPy 检查通过${NC}"
else
    echo -e "${YELLOW}⚠️  MyPy 检查有警告（不会阻止提交）${NC}"
fi
echo ""

# Bandit 安全检查
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔒 安全扫描 (Bandit)..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if bandit -r src/ -ll; then
    echo -e "${GREEN}✅ Bandit 检查通过${NC}"
else
    echo -e "${YELLOW}⚠️  发现安全警告${NC}"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}🎉 所有检查完成！${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
