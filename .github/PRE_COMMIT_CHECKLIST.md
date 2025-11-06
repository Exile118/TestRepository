# 项目文件检查清单

在推送代码到 GitHub 之前，请确保以下文件和目录都存在：

## ✅ 必需的目录和文件

### 源代码目录 (`src/`)
- ✅ `src/__init__.py`
- ✅ `src/calculator.py`
- ✅ `src/main.py`

### 测试目录 (`tests/`)
- ✅ `tests/__init__.py`
- ✅ `tests/test_calculator.py`

### 配置文件
- ✅ `requirements.txt` - Python 依赖
- ✅ `setup.py` - 包配置
- ✅ `setup.cfg` - 工具配置
- ✅ `pyproject.toml` - 现代配置
- ✅ `.gitignore` - Git 忽略规则

### 工作流文件 (`.github/workflows/`)
- ✅ `ci-cd.yml` - 主 CI/CD 管道
- ✅ `pr-checks.yml` - PR 检查
- ✅ `scheduled-tests.yml` - 定时测试
- ✅ `dependency-check.yml` - 依赖检查

### 文档文件
- ✅ `README.md` - 主文档
- ✅ `LICENSE` - 许可证
- ✅ `CONTRIBUTING.md` - 贡献指南
- ✅ `CHANGELOG.md` - 变更日志

### 文档目录 (`docs/`)
- ✅ `docs/QUICKSTART.md` - 快速开始
- ✅ `docs/WORKFLOWS_GUIDE.md` - 工作流指南
- ✅ `docs/FAQ.md` - 常见问题
- ✅ `docs/PROJECT_OVERVIEW.md` - 项目概览

### GitHub 配置 (`.github/`)
- ✅ `.github/WORKFLOW_PERMISSIONS.md` - 权限说明
- ✅ `.github/TROUBLESHOOTING.md` - 故障排查

## 📋 推送前检查

运行以下命令验证项目结构：

```bash
# 检查所有必需文件
ls -la src/
ls -la tests/
ls -la .github/workflows/

# 查看 Git 状态
git status

# 查看将要提交的文件
git add -n .
```

## 🔍 验证命令

```bash
# 验证 Python 文件语法
python -m py_compile src/*.py
python -m py_compile tests/*.py

# 运行测试（如果环境已设置）
pytest tests/ -v

# 检查 YAML 文件语法
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci-cd.yml'))"
```

## 🚀 提交和推送

```bash
# 添加所有文件
git add .

# 提交
git commit -m "fix: add missing tests directory and improve workflow validation"

# 推送
git push origin feature/new-calculator
```

## ⚠️ 常见问题

### 问题 1: tests/ 目录不存在

**原因**: 目录没有被创建或没有包含任何文件

**解决**: 
```bash
mkdir -p tests
touch tests/__init__.py
```

### 问题 2: Git 不跟踪空目录

**原因**: Git 不会跟踪空目录

**解决**: 在目录中添加至少一个文件（如 `__init__.py` 或 `.gitkeep`）

### 问题 3: 文件没有被推送

**原因**: 文件可能在 `.gitignore` 中被忽略

**解决**: 
```bash
# 检查文件是否被忽略
git check-ignore -v tests/test_calculator.py

# 强制添加（如果确实需要）
git add -f tests/test_calculator.py
```

## 📊 项目结构概览

```
TestRepository/
├── .github/
│   ├── workflows/
│   │   ├── ci-cd.yml
│   │   ├── pr-checks.yml
│   │   ├── scheduled-tests.yml
│   │   └── dependency-check.yml
│   ├── WORKFLOW_PERMISSIONS.md
│   └── TROUBLESHOOTING.md
├── docs/
│   ├── QUICKSTART.md
│   ├── WORKFLOWS_GUIDE.md
│   ├── FAQ.md
│   └── PROJECT_OVERVIEW.md
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── setup.cfg
└── pyproject.toml
```

## ✨ 最后检查

推送前确认：
- [ ] 所有文件都已添加到 Git
- [ ] 提交信息清晰明确
- [ ] 本地测试通过（如果可能）
- [ ] 没有敏感信息（密码、密钥等）
- [ ] `.gitignore` 配置正确

---

**提示**: 如果 `git status` 显示大量未跟踪的文件，请检查 `.gitignore` 配置。

**最后更新**: 2025-11-06
