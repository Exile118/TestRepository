#!/bin/bash

# 运行测试脚本
# 支持多种测试模式

set -e

echo "🧪 运行测试套件..."
echo ""

# 解析参数
COVERAGE=false
VERBOSE=false
HTML_REPORT=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -c|--coverage)
            COVERAGE=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--html)
            HTML_REPORT=true
            shift
            ;;
        *)
            echo "未知选项: $1"
            echo "用法: ./scripts/test.sh [-c|--coverage] [-v|--verbose] [-h|--html]"
            exit 1
            ;;
    esac
done

# 构建 pytest 命令
CMD="pytest tests/"

if [ "$VERBOSE" = true ]; then
    CMD="$CMD -v"
fi

if [ "$COVERAGE" = true ]; then
    CMD="$CMD --cov=src --cov-report=term-missing"
    
    if [ "$HTML_REPORT" = true ]; then
        CMD="$CMD --cov-report=html"
    fi
fi

# 运行测试
echo "执行命令: $CMD"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
eval $CMD

# 如果生成了 HTML 报告，提示打开
if [ "$HTML_REPORT" = true ] && [ "$COVERAGE" = true ]; then
    echo ""
    echo "📊 HTML 覆盖率报告已生成！"
    echo "打开: open htmlcov/index.html"
fi

echo ""
echo "✅ 测试完成！"
