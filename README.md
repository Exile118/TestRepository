###为作者自己学习工作流 仓库用
# 🚀 GitHub Workflow 学习项目 - Python 计算器

[![CI/CD Pipeline](https://github.com/Exile118/TestRepository/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Exile118/TestRepository/actions/workflows/ci-cd.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

一个完整的 Python 项目，专门用于学习和理解 GitHub Actions 工作流。通过这个项目，你将学会如何设置 CI/CD 管道、自动化测试、代码质量检查等现代软件开发实践。

## 📋 目录

- [项目简介](#项目简介)
- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [GitHub Actions 工作流详解](#github-actions-工作流详解)
- [项目结构](#项目结构)
- [本地开发](#本地开发)
- [测试](#测试)
- [贡献指南](#贡献指南)
- [学习路径](#学习路径)

## 🎯 项目简介

这是一个简单但功能完整的 Python 计算器应用，主要目的是展示如何使用 GitHub Actions 构建一个现代化的 CI/CD 管道。

### 核心功能

- ✅ 基本数学运算（加、减、乘、除）
- ✅ 高级运算（幂运算、平方根）
- ✅ 完整的单元测试覆盖
- ✅ 代码质量检查
- ✅ 自动化 CI/CD 管道
- ✅ 多 Python 版本支持（3.9-3.12）
- ✅ 跨平台测试（Ubuntu、macOS、Windows）

## ✨ 功能特性

### GitHub Actions 工作流

本项目包含 **4 个不同的工作流**，展示了 GitHub Actions 的各种应用场景：

1. **CI/CD Pipeline** (`.github/workflows/ci-cd.yml`)
   - 代码质量检查
   - 多版本、多平台测试
   - 安全扫描
   - 自动构建和发布

2. **定时测试** (`.github/workflows/scheduled-tests.yml`)
   - 每日自动运行测试
   - 确保代码持续可用

3. **PR 检查** (`.github/workflows/pr-checks.yml`)
   - Pull Request 自动审查
   - 代码覆盖率报告
   - 自动添加标签

4. **依赖更新检查** (`.github/workflows/dependency-check.yml`)
   - 每周检查过期依赖
   - 安全漏洞扫描
   - 自动创建 Issue

## 🚀 快速开始

### 前置要求

- Python 3.9 或更高版本
- Git
- GitHub 账号

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/Exile118/TestRepository.git
cd TestRepository
```

2. **创建虚拟环境**

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **运行应用**

```bash
python src/main.py
```

## 🔧 GitHub Actions 工作流详解

### 1️⃣ CI/CD Pipeline

这是最主要的工作流，包含 5 个 Job：

#### Job 1: 代码质量检查
```yaml
- Black（代码格式化检查）
- isort（导入排序检查）
- Flake8（代码风格检查）
- MyPy（类型检查）
```

#### Job 2: 多版本测试
```yaml
测试矩阵:
  - OS: Ubuntu, macOS, Windows
  - Python: 3.9, 3.10, 3.11, 3.12
  - 总共 12 个测试组合
```

#### Job 3: 安全扫描
```yaml
- Bandit（安全漏洞扫描）
- Safety（依赖安全检查）
```

#### Job 4: 构建包
```yaml
- 使用 build 模块构建
- 使用 twine 验证包
- 上传构建产物
```

#### Job 5: 自动发布
```yaml
- 仅在创建 tag 时触发
- 自动创建 GitHub Release
- 附加构建产物
```

### 2️⃣ 如何触发工作流

#### 自动触发

```bash
# 推送到 main 或 develop 分支
git push origin main

# 创建 Pull Request
gh pr create

# 创建 tag（触发 Release）
git tag v1.0.0
git push origin v1.0.0
```

#### 手动触发

1. 进入仓库的 "Actions" 标签页
2. 选择要运行的工作流
3. 点击 "Run workflow"
4. 选择分支并确认

### 3️⃣ 查看工作流结果

1. 访问仓库 → Actions 标签页
2. 查看各个工作流的运行状态
3. 点击具体的运行记录查看详细日志
4. 下载构建产物和测试报告

## 📁 项目结构

```
TestRepository/
├── .github/
│   └── workflows/          # GitHub Actions 工作流配置
│       ├── ci-cd.yml       # 主要 CI/CD 管道
│       ├── pr-checks.yml   # PR 检查
│       ├── scheduled-tests.yml  # 定时测试
│       └── dependency-check.yml # 依赖检查
├── src/                    # 源代码目录
│   ├── __init__.py
│   ├── calculator.py       # 计算器核心逻辑
│   └── main.py            # 主程序入口
├── tests/                  # 测试目录
│   ├── __init__.py
│   └── test_calculator.py # 单元测试
├── .gitignore             # Git 忽略文件
├── LICENSE                # 开源许可证
├── README.md              # 项目文档
├── requirements.txt       # 项目依赖
├── setup.py              # 安装配置
├── setup.cfg             # 工具配置
└── pyproject.toml        # 现代 Python 项目配置
```

## 💻 本地开发

### 运行测试

```bash
# 运行所有测试
pytest

# 运行测试并生成覆盖率报告
pytest --cov=src --cov-report=html

# 查看覆盖率报告
open htmlcov/index.html  # macOS
```

### 代码质量检查

```bash
# 格式化代码
black src/ tests/

# 排序导入
isort src/ tests/

# 代码风格检查
flake8 src/ tests/

# 类型检查
mypy src/

# 安全扫描
bandit -r src/
```

### 构建包

```bash
# 构建分发包
python -m build

# 检查包
twine check dist/*

# 本地安装
pip install -e .
```

## 🧪 测试

项目使用 **pytest** 作为测试框架，测试覆盖率达到 **100%**。

### 测试文件

- `tests/test_calculator.py`: 包含所有计算器功能的单元测试
- 使用参数化测试减少重复代码
- 测试边界条件和异常情况

### 运行测试

```bash
# 基本测试
pytest tests/

# 详细输出
pytest tests/ -v

# 带覆盖率
pytest tests/ --cov=src

# 生成 HTML 报告
pytest tests/ --cov=src --cov-report=html
```

## 🤝 贡献指南

### 如何贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### Pull Request 流程

当你提交 PR 时，会自动触发以下检查：

- ✅ 所有测试必须通过
- ✅ 代码覆盖率不能降低
- ✅ 代码风格检查必须通过
- ✅ 没有安全漏洞

## 📚 学习路径

### 初级：理解基础概念

1. **什么是 CI/CD？**
   - 阅读 `.github/workflows/ci-cd.yml`
   - 理解各个 Job 的作用

2. **运行你的第一个工作流**
   - Fork 本仓库
   - 修改 README，提交并推送
   - 观察 Actions 标签页的变化

3. **查看工作流日志**
   - 点击运行的工作流
   - 展开各个步骤
   - 理解每个步骤的输出

### 中级：自定义工作流

1. **修改触发条件**
   - 尝试修改 `on:` 部分
   - 添加新的触发事件

2. **添加新的测试**
   - 在 `tests/test_calculator.py` 添加测试
   - 推送并查看测试是否运行

3. **配置代码覆盖率**
   - 修改 `setup.cfg` 中的覆盖率要求
   - 查看 PR 中的覆盖率报告

### 高级：构建复杂流程

1. **创建自定义工作流**
   - 在 `.github/workflows/` 添加新文件
   - 定义自己的 CI/CD 流程

2. **使用 Secrets**
   - 在仓库设置中添加 Secrets
   - 在工作流中使用敏感信息

3. **创建 Release**
   - 创建 Git tag
   - 自动构建和发布

## 🎓 关键概念解释

### GitHub Actions 核心组件

1. **Workflow（工作流）**: YAML 文件，定义自动化流程
2. **Job（任务）**: 工作流中的独立单元，可以并行运行
3. **Step（步骤）**: Job 中的具体操作
4. **Action（动作）**: 可重用的步骤模块
5. **Runner（运行器）**: 执行工作流的虚拟机

### 工作流触发器

```yaml
on:
  push:              # 推送代码时
  pull_request:      # PR 时
  schedule:          # 定时任务
  workflow_dispatch: # 手动触发
  release:           # 创建 Release 时
```

### Matrix 策略

```yaml
strategy:
  matrix:
    os: [ubuntu, macos, windows]
    python: [3.9, 3.10, 3.11, 3.12]
# 会创建 3 × 4 = 12 个测试任务
```

## 🔍 故障排查

### 常见问题

1. **工作流没有触发**
   - 检查 `.github/workflows/` 文件是否在正确位置
   - 确认 YAML 语法正确
   - 查看分支是否匹配触发条件

2. **测试失败**
   - 查看详细的错误日志
   - 在本地运行相同的测试
   - 检查 Python 版本兼容性

3. **权限问题**
   - 检查 `GITHUB_TOKEN` 权限
   - 查看仓库 Settings → Actions 设置

## 📊 Badge 说明

在 README 顶部，我们使用了几个 Badge：

```markdown
[![CI/CD Pipeline](URL)](LINK)  # 显示工作流状态
[![Python Version](URL)](LINK)  # 支持的 Python 版本
[![License](URL)](LINK)         # 开源许可证
```

你可以在自己的项目中添加这些 Badge！

## 🌟 下一步

1. **Fork 这个仓库**
2. **尝试修改代码并提交**
3. **观察工作流的运行**
4. **创建自己的工作流**
5. **分享你的学习成果**

## 📖 扩展阅读

- [GitHub Actions 官方文档](https://docs.github.com/en/actions)
- [Pytest 文档](https://docs.pytest.org/)
- [Python 打包指南](https://packaging.python.org/)
- [持续集成最佳实践](https://www.atlassian.com/continuous-delivery/continuous-integration)

## 📝 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👤 作者

**Your Name**

- GitHub: [@Exile118](https://github.com/Exile118)
- 项目链接: [https://github.com/Exile118/TestRepository](https://github.com/Exile118/TestRepository)

## 🙏 致谢

感谢所有为开源社区做出贡献的开发者！

---

**⭐ 如果这个项目对你有帮助，请给它一个 Star！**

**💬 有问题？欢迎创建 Issue 或 Discussion！**
