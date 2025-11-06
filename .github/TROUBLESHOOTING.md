# 常见 GitHub Actions 错误修复指南

## 错误 1: Resource not accessible by integration

### 症状
```
Error: HttpError: Resource not accessible by integration
```

### 原因
工作流没有足够的权限执行某些操作（如创建评论、添加标签、创建 Issue）。

### ✅ 已修复
所有工作流文件已更新，添加了正确的权限配置：

- ✅ `pr-checks.yml` - 添加了 PR 和 Issue 写权限
- ✅ `dependency-check.yml` - 添加了 Issue 写权限  
- ✅ `ci-cd.yml` - 添加了基本读权限和 Release 写权限

### 如何验证修复
1. 提交更改到你的仓库
2. 创建一个 Pull Request
3. 观察 Actions 标签页，工作流应该成功运行

---

## 错误 2: setup.cfg 解析错误

### 症状
```
ERROR: setup.cfg:66: unexpected line: '/('
```

### 原因
`setup.cfg` 文件不支持多行字符串语法，但配置中使用了 Black 的多行排除规则。

### ✅ 已修复
- 从 `setup.cfg` 移除了 Black 配置
- 将所有工具配置迁移到 `pyproject.toml`（现代标准）

### 配置位置
所有工具配置现在统一在 `pyproject.toml` 中：
- `[tool.black]`
- `[tool.isort]`
- `[tool.pytest.ini_options]`
- `[tool.coverage.run]`
- `[tool.coverage.report]`

---

## 错误 3: pytest 找不到模块

### 症状
```
ModuleNotFoundError: No module named 'src'
```

### 解决方法

**方法 1: 安装为可编辑模式（推荐）**
```bash
pip install -e .
```

**方法 2: 设置 PYTHONPATH**
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pytest
```

**方法 3: 修改工作流（已在 ci-cd.yml 中配置）**
```yaml
- name: 安装项目
  run: pip install -e .
```

---

## 错误 4: Black 检查失败

### 症状
```
would reformat src/calculator.py
Oh no! 💥 💔 💥
```

### 解决方法
```bash
# 自动格式化代码
black src/ tests/

# 或使用项目脚本
./scripts/check.sh
```

---

## 错误 5: 工作流不运行

### 可能原因

1. **YAML 语法错误**
   - 使用在线 YAML 验证器检查
   - 确保缩进使用空格，不是 Tab

2. **工作流文件位置错误**
   - 必须在 `.github/workflows/` 目录
   - 文件扩展名必须是 `.yml` 或 `.yaml`

3. **触发条件不匹配**
   ```yaml
   on:
     push:
       branches: [ main ]  # 只在推送到 main 时触发
   ```

4. **Actions 未启用**
   - Settings → Actions → General
   - 确保 Actions 已启用

### 调试步骤
```yaml
# 添加调试步骤到工作流
- name: Debug Info
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "Branch: ${{ github.ref_name }}"
```

---

## 错误 6: 测试覆盖率太低

### 症状
```
TOTAL coverage: 65% (required: 80%)
```

### 解决方法

1. **添加缺失的测试**
   ```python
   def test_missing_case(self):
       calc = Calculator()
       result = calc.function_not_tested(5)
       assert result == expected
   ```

2. **查看覆盖率报告**
   ```bash
   pytest --cov=src --cov-report=html
   open htmlcov/index.html
   ```

3. **临时调整阈值（不推荐）**
   ```yaml
   # 在 pr-checks.yml 中
   MINIMUM_GREEN: 70  # 降低要求
   ```

---

## 错误 7: 依赖安装失败

### 症状
```
ERROR: Could not find a version that satisfies the requirement xxx
```

### 解决方法

1. **检查 requirements.txt**
   - 确保版本号正确
   - 确保包名拼写正确

2. **使用国内镜像（中国用户）**
   ```bash
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

3. **更新 pip**
   ```bash
   pip install --upgrade pip
   ```

---

## 错误 8: 权限拒绝

### 症状（macOS/Linux）
```
Permission denied: './scripts/setup.sh'
```

### 解决方法
```bash
# 添加执行权限
chmod +x scripts/*.sh

# 提交权限更改
git add scripts/*.sh
git commit -m "fix: add execute permission to scripts"
```

---

## 错误 9: Git 推送被拒绝

### 症状
```
! [remote rejected] main -> main (protected branch hook declined)
```

### 可能原因

1. **分支保护规则**
   - 需要 PR 审查
   - 需要状态检查通过

2. **没有推送权限**
   - 确认仓库所有权
   - 检查协作者权限

### 解决方法
- 使用 Pull Request 而不是直接推送
- 或调整分支保护规则（Settings → Branches）

---

## 错误 10: codecov 上传失败

### 症状
```
Error: Codecov: Failed to upload coverage reports
```

### 解决方法

**方法 1: 使用 continue-on-error**（已配置）
```yaml
- name: 上传覆盖率报告
  uses: codecov/codecov-action@v4
  continue-on-error: true  # 失败不会阻止工作流
```

**方法 2: 配置 Codecov token**
1. 在 Codecov.io 创建账号
2. 添加仓库
3. 获取 token
4. 添加到 GitHub Secrets
5. 更新工作流：
   ```yaml
   with:
     token: ${{ secrets.CODECOV_TOKEN }}
   ```

---

## 快速命令参考

### 本地测试
```bash
# 完整测试套件
pytest

# 带覆盖率
pytest --cov=src --cov-report=term

# HTML 报告
pytest --cov=src --cov-report=html

# 只运行失败的测试
pytest --lf

# 详细输出
pytest -v
```

### 代码质量
```bash
# 格式化代码
black src/ tests/

# 排序导入
isort src/ tests/

# 检查格式
black --check src/ tests/

# Lint
flake8 src/ tests/

# 类型检查
mypy src/

# 安全扫描
bandit -r src/
```

### Git 操作
```bash
# 查看状态
git status

# 添加文件
git add .

# 提交
git commit -m "fix: your message"

# 推送
git push origin main

# 创建分支
git checkout -b feature/new-feature

# 查看日志
git log --oneline
```

---

## 获取帮助

如果以上方法都无法解决你的问题：

1. **查看文档**
   - [README.md](../README.md)
   - [WORKFLOWS_GUIDE.md](../docs/WORKFLOWS_GUIDE.md)
   - [FAQ.md](../docs/FAQ.md)

2. **检查工作流日志**
   - Actions 标签页 → 选择运行 → 查看详细日志

3. **创建 Issue**
   - 包含完整的错误信息
   - 包含你尝试的解决方法
   - 包含相关的配置文件

4. **参考官方文档**
   - [GitHub Actions 文档](https://docs.github.com/en/actions)
   - [pytest 文档](https://docs.pytest.org/)

---

**提示**: 大多数问题都可以通过查看详细的错误日志和本指南解决。不要害怕尝试！

**最后更新**: 2025-11-06
