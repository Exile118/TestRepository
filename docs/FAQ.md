# 常见问题解答 (FAQ)

本文档回答了关于项目和 GitHub Actions 工作流的常见问题。

## 📋 目录

- [一般问题](#一般问题)
- [安装和设置](#安装和设置)
- [GitHub Actions](#github-actions)
- [测试相关](#测试相关)
- [故障排查](#故障排查)

## 一般问题

### Q: 这个项目是做什么的？

A: 这是一个教学项目，通过一个简单的 Python 计算器应用，展示如何使用 GitHub Actions 构建完整的 CI/CD 管道。你可以通过这个项目学习：
- 自动化测试
- 代码质量检查
- 持续集成/持续部署
- GitHub Actions 工作流配置

### Q: 我需要什么基础知识？

A: 建议具备：
- ✅ 基本的 Python 知识
- ✅ Git 基础操作
- ✅ 命令行使用经验
- ⭕ GitHub 基础知识（可选，会在项目中学习）

### Q: 这个项目适合谁？

A: 适合：
- 想学习 GitHub Actions 的开发者
- 需要了解 CI/CD 流程的学生
- 想提升项目自动化水平的工程师
- 准备开源项目的贡献者

## 安装和设置

### Q: 支持哪些操作系统？

A: 本项目支持：
- ✅ macOS
- ✅ Linux (Ubuntu, Debian, Fedora 等)
- ✅ Windows 10/11

工作流在以下平台测试：
- Ubuntu Latest
- macOS Latest  
- Windows Latest

### Q: 需要什么 Python 版本？

A: 项目支持 Python 3.9 - 3.12。建议使用 Python 3.11。

检查版本：
```bash
python --version
```

### Q: 虚拟环境是必需的吗？

A: 强烈推荐使用虚拟环境，这样可以：
- 隔离项目依赖
- 避免版本冲突
- 便于管理依赖

创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Q: 依赖安装失败怎么办？

A: 尝试以下方法：

1. **升级 pip**
   ```bash
   pip install --upgrade pip
   ```

2. **清除缓存**
   ```bash
   pip cache purge
   ```

3. **使用国内镜像（中国用户）**
   ```bash
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

## GitHub Actions

### Q: 什么是 GitHub Actions？

A: GitHub Actions 是 GitHub 提供的 CI/CD 平台，允许你自动化软件开发工作流，包括：
- 自动运行测试
- 代码质量检查
- 自动部署
- 自动发布

### Q: 工作流什么时候运行？

A: 根据配置的触发条件：

**ci-cd.yml**:
- 推送到 main 或 develop 分支
- 创建 PR 到 main 或 develop
- 手动触发
- 创建 tag (触发 Release)

**scheduled-tests.yml**:
- 每天 UTC 02:00 自动运行
- 手动触发

**pr-checks.yml**:
- 创建或更新 Pull Request

**dependency-check.yml**:
- 每周一 UTC 08:00
- 手动触发

### Q: 如何手动触发工作流？

A: 步骤：
1. 进入仓库页面
2. 点击 "Actions" 标签
3. 选择要运行的工作流
4. 点击 "Run workflow"
5. 选择分支
6. 点击绿色的 "Run workflow" 按钮

### Q: 工作流运行需要多久？

A: 通常时间：
- 代码质量检查：1-2 分钟
- 单一平台测试：2-3 分钟
- 完整 Matrix 测试：5-10 分钟
- 整个 CI/CD 流程：10-15 分钟

### Q: GitHub Actions 免费吗？

A: 对于公开仓库，完全免费！

对于私有仓库：
- Free 账户：每月 2000 分钟
- Pro 账户：每月 3000 分钟
- 查看详情：[GitHub Pricing](https://github.com/pricing)

### Q: 如何查看工作流日志？

A: 步骤：
1. Actions 标签页
2. 点击具体的运行记录
3. 点击 Job 名称
4. 展开各个 Step 查看详细日志

下载日志：
- 点击运行记录右上角 ⋮
- 选择 "Download log archive"

### Q: 为什么工作流失败了？

A: 常见原因：

1. **测试失败**
   - 查看测试日志
   - 在本地运行相同测试
   - 修复代码后重新推送

2. **代码风格问题**
   ```bash
   black src/ tests/
   flake8 src/ tests/
   ```

3. **依赖问题**
   - 检查 requirements.txt
   - 确保所有依赖都已列出

4. **权限问题**
   - 检查 GITHUB_TOKEN 权限
   - 查看 workflow 的 permissions 配置

## 测试相关

### Q: 如何运行单个测试？

A: 使用 pytest 的路径语法：

```bash
# 运行单个测试文件
pytest tests/test_calculator.py

# 运行单个测试类
pytest tests/test_calculator.py::TestCalculator

# 运行单个测试函数
pytest tests/test_calculator.py::TestCalculator::test_add_positive_numbers
```

### Q: 如何查看测试覆盖率？

A: 运行带覆盖率的测试：

```bash
# 终端输出
pytest --cov=src --cov-report=term-missing

# HTML 报告
pytest --cov=src --cov-report=html
open htmlcov/index.html  # 打开报告
```

### Q: 为什么测试在 CI 中通过，本地却失败？

A: 可能的原因：

1. **Python 版本不同**
   - CI 使用特定版本（如 3.11）
   - 本地可能使用不同版本

2. **依赖版本不同**
   - 更新依赖：`pip install -r requirements.txt --upgrade`

3. **环境变量差异**
   - 检查是否依赖特定环境变量

4. **文件路径问题**
   - 使用 `pathlib` 处理路径
   - 避免硬编码路径

### Q: 如何添加新的测试？

A: 步骤：

1. **在 `tests/test_calculator.py` 添加测试函数**
   ```python
   def test_my_new_feature(self):
       """测试我的新功能"""
       calc = Calculator()
       result = calc.my_function(5)
       assert result == expected_value
   ```

2. **运行测试**
   ```bash
   pytest tests/test_calculator.py::TestCalculator::test_my_new_feature -v
   ```

3. **提交代码**
   - CI 会自动运行所有测试

## 故障排查

### Q: "No module named 'pytest'" 错误

A: pytest 未安装：
```bash
pip install pytest
# 或
pip install -r requirements.txt
```

### Q: "ImportError: No module named 'src'" 错误

A: Python 路径问题，解决方法：

1. **设置 PYTHONPATH**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

2. **安装项目为可编辑模式**
   ```bash
   pip install -e .
   ```

### Q: Git 推送被拒绝

A: 可能原因：

1. **分支保护规则**
   - 检查仓库设置
   - 可能需要通过 PR 提交

2. **没有推送权限**
   - 确认是你的仓库或已 Fork
   - 检查 Git 认证

### Q: Actions 标签页没有工作流

A: 检查：

1. **工作流文件位置**
   - 必须在 `.github/workflows/` 目录
   
2. **YAML 语法错误**
   - 使用在线工具检查 YAML 语法
   - 检查缩进（使用空格，不是 Tab）

3. **Actions 是否启用**
   - Settings → Actions → General
   - 确保 Actions 已启用

### Q: 工作流一直显示排队中

A: 可能原因：

1. **GitHub 服务繁忙**
   - 等待几分钟
   - 查看 [GitHub Status](https://www.githubstatus.com/)

2. **并发限制**
   - 同时运行的工作流过多
   - 取消不需要的运行

3. **Runner 不可用**
   - 使用 GitHub 托管的 runner
   - 检查 `runs-on` 配置

### Q: 如何调试工作流？

A: 调试技巧：

1. **添加调试步骤**
   ```yaml
   - name: Debug Info
     run: |
       echo "Event: ${{ github.event_name }}"
       echo "Ref: ${{ github.ref }}"
       env
   ```

2. **启用 Debug 日志**
   - Settings → Secrets
   - 添加 `ACTIONS_STEP_DEBUG` = `true`

3. **使用 tmate 进行 SSH 调试**
   ```yaml
   - name: Setup tmate session
     uses: mxschmitt/action-tmate@v3
   ```

## 进阶问题

### Q: 如何在工作流中使用 Secrets？

A: 步骤：

1. **添加 Secret**
   - Settings → Secrets and variables → Actions
   - New repository secret

2. **在工作流中使用**
   ```yaml
   - name: Use secret
     env:
       MY_SECRET: ${{ secrets.MY_SECRET }}
     run: |
       echo "Using secret..."
   ```

### Q: 如何创建自定义 Badge？

A: Badge 格式：
```markdown
[![工作流名称](https://github.com/用户名/仓库名/actions/workflows/文件名.yml/badge.svg)](链接)
```

示例：
```markdown
[![CI](https://github.com/Exile118/TestRepository/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Exile118/TestRepository/actions/workflows/ci-cd.yml)
```

### Q: 如何减少工作流运行时间？

A: 优化技巧：

1. **使用缓存**
   ```yaml
   - uses: actions/setup-python@v5
     with:
       cache: 'pip'
   ```

2. **并行运行 Jobs**
   - 移除不必要的 `needs`

3. **减少 Matrix 组合**
   ```yaml
   matrix:
     python-version: ['3.9', '3.12']  # 只测试最低和最高版本
   ```

4. **跳过不必要的步骤**
   ```yaml
   - name: Optional step
     if: github.event_name == 'push'
   ```

### Q: 如何贡献代码？

A: 查看 [CONTRIBUTING.md](../CONTRIBUTING.md) 了解详细流程。

简要步骤：
1. Fork 仓库
2. 创建特性分支
3. 提交更改
4. 创建 Pull Request
5. 等待审查

## 更多帮助

### 还有其他问题？

- 📖 查看 [完整文档](../README.md)
- 🔧 阅读 [工作流指南](WORKFLOWS_GUIDE.md)
- 🚀 参考 [快速开始](QUICKSTART.md)
- 🐛 [创建 Issue](https://github.com/Exile118/TestRepository/issues)
- 💬 [参与讨论](https://github.com/Exile118/TestRepository/discussions)

### 官方资源

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [pytest 文档](https://docs.pytest.org/)
- [Python 打包指南](https://packaging.python.org/)

---

**找不到答案？欢迎创建 Issue！我们很乐意帮助你。** 🎉
