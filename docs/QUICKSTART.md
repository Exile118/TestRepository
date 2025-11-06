# 快速开始指南

欢迎使用 GitHub Workflow 学习项目！这份指南将帮助你在 5 分钟内开始使用。

## 🎯 目标

通过这个项目，你将学会：
- ✅ 如何设置 GitHub Actions 工作流
- ✅ 如何实现自动化测试
- ✅ 如何进行代码质量检查
- ✅ 如何自动化部署流程

## ⚡ 5 分钟快速开始

### 第一步：Fork 仓库

1. 点击右上角的 "Fork" 按钮
2. 等待 Fork 完成

### 第二步：克隆到本地

```bash
git clone https://github.com/YOUR_USERNAME/TestRepository.git
cd TestRepository
```

### 第三步：设置环境

**macOS/Linux:**
```bash
chmod +x scripts/*.sh
./scripts/setup.sh
```

**Windows:**
```cmd
scripts\setup.bat
```

### 第四步：运行测试

```bash
# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows

# 运行测试
pytest tests/ -v
```

### 第五步：查看工作流

1. 修改 README，添加你的名字
2. 提交并推送到 GitHub
3. 访问 Actions 标签页
4. 观察工作流自动运行！

```bash
git add README.md
git commit -m "docs: add my name"
git push origin main
```

## 📖 学习路径

### 初学者（第 1 天）

1. **理解项目结构** (15分钟)
   - 浏览 `src/` 目录
   - 查看 `tests/` 目录
   - 阅读 `README.md`

2. **运行第一个测试** (10分钟)
   ```bash
   pytest tests/test_calculator.py::TestCalculator::test_add_positive_numbers -v
   ```

3. **触发第一个工作流** (10分钟)
   - 修改任意文件
   - 提交并推送
   - 观察 Actions

### 进阶（第 2-3 天）

1. **添加新功能** (30分钟)
   - 在 `calculator.py` 添加新函数
   - 编写对应测试
   - 提交并观察 CI

2. **创建 Pull Request** (20分钟)
   - 创建新分支
   - 添加功能
   - 创建 PR
   - 观察自动检查

3. **查看覆盖率报告** (15分钟)
   ```bash
   pytest --cov=src --cov-report=html
   open htmlcov/index.html
   ```

### 高级（第 4-7 天）

1. **自定义工作流** (1小时)
   - 修改 `.github/workflows/ci-cd.yml`
   - 添加新的检查步骤
   - 测试效果

2. **创建 Release** (30分钟)
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. **探索 Matrix 策略** (45分钟)
   - 理解多版本测试
   - 添加新的测试平台

## 🛠️ 常用命令

### 开发

```bash
# 激活环境
source venv/bin/activate

# 运行应用
python src/main.py

# 格式化代码
black src/ tests/

# 代码检查
./scripts/check.sh
```

### 测试

```bash
# 基本测试
pytest

# 详细输出
pytest -v

# 带覆盖率
./scripts/test.sh --coverage

# HTML 报告
./scripts/test.sh --coverage --html
```

### Git 工作流

```bash
# 创建功能分支
git checkout -b feature/my-feature

# 提交更改
git add .
git commit -m "feat: add new feature"

# 推送
git push origin feature/my-feature

# 创建 tag
git tag v1.0.0
git push origin v1.0.0
```

## 📚 重要文件说明

| 文件 | 用途 |
|------|------|
| `.github/workflows/ci-cd.yml` | 主要 CI/CD 工作流 |
| `src/calculator.py` | 核心业务逻辑 |
| `tests/test_calculator.py` | 单元测试 |
| `requirements.txt` | Python 依赖 |
| `setup.py` | 包配置 |
| `.gitignore` | Git 忽略文件 |

## 🎯 练习任务

### 任务 1：添加减法的负数测试（简单）

1. 打开 `tests/test_calculator.py`
2. 添加一个测试负数减法的函数
3. 运行测试确保通过
4. 提交代码

### 任务 2：添加取模运算（中等）

1. 在 `Calculator` 类添加 `modulo` 方法
2. 编写完整的测试用例
3. 更新文档
4. 创建 PR

### 任务 3：添加自定义工作流（困难）

1. 创建 `.github/workflows/lint.yml`
2. 配置只运行代码检查
3. 设置在 PR 时触发
4. 测试工作流

## 💡 提示

### 调试技巧

1. **查看详细日志**
   ```bash
   pytest -v --tb=long
   ```

2. **只运行失败的测试**
   ```bash
   pytest --lf
   ```

3. **进入调试模式**
   ```bash
   pytest --pdb
   ```

### GitHub Actions 技巧

1. **查看工作流日志**
   - Actions → 选择运行 → 点击 Job → 展开 Step

2. **手动触发工作流**
   - Actions → 选择工作流 → Run workflow

3. **取消运行**
   - 点击运行记录右上角的 Cancel

## 🚀 下一步

完成快速开始后，你可以：

1. 📖 阅读完整的 [README.md](README.md)
2. 🔧 学习 [工作流详细指南](docs/WORKFLOWS_GUIDE.md)
3. 🤝 查看 [贡献指南](CONTRIBUTING.md)
4. 📝 浏览 [变更日志](CHANGELOG.md)

## ❓ 需要帮助？

- 📖 查看文档：`docs/` 目录
- 🐛 报告问题：创建 Issue
- 💬 讨论交流：Discussions
- 📧 联系作者：通过 GitHub

---

**记住**：学习最好的方式就是动手实践！不要害怕出错，每个错误都是学习的机会。

**祝你学习愉快！🎉**
