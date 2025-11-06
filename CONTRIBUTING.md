# 贡献指南

感谢你对本项目的关注！这份指南将帮助你了解如何为项目做出贡献。

## 📋 目录

- [行为准则](#行为准则)
- [如何贡献](#如何贡献)
- [开发流程](#开发流程)
- [代码规范](#代码规范)
- [提交规范](#提交规范)
- [Pull Request 流程](#pull-request-流程)

## 行为准则

参与本项目的所有人都应遵守以下准则：

- 使用友好和包容的语言
- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

## 如何贡献

### 报告 Bug

如果你发现了 Bug，请：

1. 检查 [Issues](https://github.com/Exile118/TestRepository/issues) 确保问题未被报告
2. 创建新 Issue，包含：
   - 清晰的标题
   - 详细的问题描述
   - 复现步骤
   - 期望行为
   - 实际行为
   - 系统环境（OS、Python 版本等）

### 建议新功能

如果你有好的想法：

1. 创建 Issue，标记为 `enhancement`
2. 详细描述功能
3. 说明为什么这个功能有用
4. 如果可能，提供实现思路

### 提交代码

1. Fork 项目
2. 创建特性分支
3. 编写代码
4. 添加测试
5. 确保所有测试通过
6. 提交 Pull Request

## 开发流程

### 1. 设置开发环境

```bash
# 克隆你 fork 的仓库
git clone https://github.com/YOUR_USERNAME/TestRepository.git
cd TestRepository

# 添加上游仓库
git remote add upstream https://github.com/Exile118/TestRepository.git

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 创建分支

```bash
# 确保主分支是最新的
git checkout main
git pull upstream main

# 创建新分支
git checkout -b feature/your-feature-name
```

分支命名约定：
- `feature/` - 新功能
- `fix/` - Bug 修复
- `docs/` - 文档更新
- `test/` - 测试相关
- `refactor/` - 代码重构

### 3. 编写代码

- 遵循项目代码风格
- 为新功能添加测试
- 更新相关文档
- 保持提交的原子性

### 4. 运行测试

```bash
# 运行所有测试
pytest

# 检查代码覆盖率
pytest --cov=src --cov-report=term-missing

# 代码格式检查
black --check src/ tests/
flake8 src/ tests/
mypy src/
```

### 5. 提交更改

```bash
git add .
git commit -m "feat: add new feature"
git push origin feature/your-feature-name
```

## 代码规范

### Python 代码风格

本项目遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范，并使用以下工具：

- **Black**: 代码格式化（行长度 127）
- **isort**: 导入排序
- **Flake8**: 代码检查
- **MyPy**: 类型检查

### 文档字符串

使用 Google 风格的文档字符串：

```python
def function_name(param1: int, param2: str) -> bool:
    """
    简短描述函数功能。
    
    详细描述（如果需要）。
    
    Args:
        param1: 参数1的描述
        param2: 参数2的描述
        
    Returns:
        返回值的描述
        
    Raises:
        ValueError: 何时抛出此异常
    """
    pass
```

### 测试

- 每个新功能都要有对应的测试
- 测试函数名应清晰描述测试内容
- 使用参数化测试避免重复代码
- 测试覆盖率应保持在 90% 以上

```python
def test_add_positive_numbers():
    """测试正数加法"""
    calc = Calculator()
    assert calc.add(5, 3) == 8
```

## 提交规范

本项目使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

### 提交消息格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响代码运行）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 示例

```bash
# 好的提交消息
git commit -m "feat(calculator): add power function"
git commit -m "fix(divide): handle division by zero"
git commit -m "docs(readme): update installation instructions"

# 不好的提交消息
git commit -m "update"
git commit -m "fix bug"
git commit -m "changes"
```

## Pull Request 流程

### 创建 PR

1. 推送分支到你的 fork
2. 在 GitHub 上创建 Pull Request
3. 填写 PR 模板
4. 等待 CI 检查通过
5. 等待代码审查

### PR 标题

使用与提交消息相同的格式：

```
feat(calculator): add square root function
```

### PR 描述

包含以下内容：

- **改动内容**: 简要说明做了什么
- **为什么**: 为什么需要这个改动
- **如何测试**: 如何验证这个改动
- **相关 Issue**: 如 `Closes #123`

### PR 模板示例

```markdown
## 改动说明
添加了平方根计算功能

## 改动类型
- [ ] Bug 修复
- [x] 新功能
- [ ] 重大变更
- [ ] 文档更新

## 测试
- [x] 添加了单元测试
- [x] 所有测试通过
- [x] 代码覆盖率未降低

## 关联 Issue
Closes #42

## 截图（如果适用）
N/A

## 检查清单
- [x] 代码遵循项目规范
- [x] 已添加/更新文档
- [x] 已添加测试
- [x] 所有测试通过
- [x] CI 检查通过
```

### 代码审查

当收到审查意见时：

1. 认真考虑反馈
2. 进行必要的修改
3. 推送更新（无需创建新 PR）
4. 回复审查意见

### 合并要求

PR 必须满足：

- ✅ 所有 CI 检查通过
- ✅ 至少一个维护者批准
- ✅ 没有合并冲突
- ✅ 代码覆盖率不降低
- ✅ 遵循代码规范

## 开发技巧

### 保持同步

定期同步上游更改：

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### 本地预检查

提交前运行：

```bash
# 格式化代码
black src/ tests/
isort src/ tests/

# 运行测试
pytest --cov=src

# 代码检查
flake8 src/ tests/
mypy src/
```

### 处理冲突

如果出现合并冲突：

```bash
git fetch upstream
git rebase upstream/main
# 解决冲突
git add .
git rebase --continue
git push -f origin feature/your-feature-name
```

## 获得帮助

如果你需要帮助：

1. 查看 [README](README.md)
2. 搜索现有 [Issues](https://github.com/Exile118/TestRepository/issues)
3. 创建新 Issue 提问
4. 在 [Discussions](https://github.com/Exile118/TestRepository/discussions) 讨论

## 致谢

感谢你考虑为本项目做出贡献！每一个贡献都很重要。

---

**Happy Coding! 🎉**
