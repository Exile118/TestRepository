# GitHub Workflows 使用指南

本指南详细介绍如何使用和定制本项目的 GitHub Actions 工作流。

## 📚 目录

- [工作流概览](#工作流概览)
- [详细说明](#详细说明)
- [自定义工作流](#自定义工作流)
- [常见问题](#常见问题)
- [最佳实践](#最佳实践)

## 工作流概览

本项目包含 4 个主要工作流：

| 工作流 | 文件 | 触发条件 | 用途 |
|--------|------|---------|------|
| CI/CD Pipeline | `ci-cd.yml` | Push/PR to main/develop | 主要的 CI/CD 流程 |
| 定时测试 | `scheduled-tests.yml` | 每日 02:00 UTC | 定期运行测试 |
| PR 检查 | `pr-checks.yml` | Pull Request | PR 自动审查 |
| 依赖检查 | `dependency-check.yml` | 每周一 08:00 UTC | 检查过期依赖 |

## 详细说明

### 1. CI/CD Pipeline (`ci-cd.yml`)

这是最核心的工作流，包含完整的 CI/CD 流程。

#### 触发条件

```yaml
on:
  push:
    branches: [ main, develop ]  # 推送到这些分支时触发
  pull_request:
    branches: [ main, develop ]  # PR 到这些分支时触发
  workflow_dispatch:              # 允许手动触发
```

#### Job 流程图

```
代码质量检查
    ↓
    ├─→ 多版本测试 → 构建包 → 创建 Release (仅 tag)
    └─→ 安全扫描 ──┘
```

#### 使用方法

**自动触发**:
```bash
git add .
git commit -m "feat: new feature"
git push origin main
```

**手动触发**:
1. GitHub → Actions → CI/CD Pipeline
2. Run workflow → 选择分支 → Run

#### 创建 Release

```bash
# 创建并推送 tag
git tag v1.0.0
git push origin v1.0.0

# 工作流会自动：
# 1. 运行所有测试
# 2. 构建 Python 包
# 3. 创建 GitHub Release
# 4. 上传构建产物
```

### 2. 定时测试 (`scheduled-tests.yml`)

每天自动运行测试，确保代码持续可用。

#### 定时配置

```yaml
schedule:
  - cron: '0 2 * * *'  # 每天 UTC 02:00
```

#### Cron 语法说明

```
* * * * *
│ │ │ │ │
│ │ │ │ └─ 星期几 (0-6, 0=周日)
│ │ │ └─── 月份 (1-12)
│ │ └───── 日期 (1-31)
│ └─────── 小时 (0-23)
└───────── 分钟 (0-59)
```

#### 自定义定时

```yaml
# 每 6 小时运行一次
- cron: '0 */6 * * *'

# 每周一和周五上午 9 点
- cron: '0 9 * * 1,5'

# 每月 1 号
- cron: '0 0 1 * *'
```

### 3. PR 检查 (`pr-checks.yml`)

自动审查 Pull Request，提供即时反馈。

#### 功能

1. **运行测试**: 确保 PR 不会破坏现有功能
2. **代码覆盖率**: 生成并评论覆盖率报告
3. **代码格式**: 检查代码风格
4. **自动标签**: 为 PR 添加标签

#### 覆盖率阈值

```yaml
MINIMUM_GREEN: 80   # ≥80% 显示绿色
MINIMUM_ORANGE: 60  # 60-80% 显示橙色
                     # <60% 显示红色
```

#### 自定义检查

添加新的检查步骤：

```yaml
- name: 自定义检查
  run: |
    # 你的检查命令
    echo "Running custom checks..."
```

### 4. 依赖检查 (`dependency-check.yml`)

定期检查依赖更新和安全漏洞。

#### 检查内容

1. **过期包**: 使用 `pip list --outdated`
2. **安全漏洞**: 使用 `pip-audit`
3. **自动 Issue**: 发现问题时自动创建 Issue

#### 自定义通知

添加邮件或 Slack 通知：

```yaml
- name: 发送通知
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: '发现过期依赖！'
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

## 自定义工作流

### 添加新的工作流

1. 创建新文件 `.github/workflows/my-workflow.yml`
2. 定义工作流：

```yaml
name: My Custom Workflow

on:
  push:
    branches: [ main ]

jobs:
  my-job:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run my script
        run: |
          echo "Hello, GitHub Actions!"
```

### 常用 Actions

#### 检出代码
```yaml
- uses: actions/checkout@v4
```

#### 设置 Python
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'
```

#### 上传产物
```yaml
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: dist/
```

#### 下载产物
```yaml
- uses: actions/download-artifact@v4
  with:
    name: my-artifact
    path: dist/
```

### 使用 Secrets

1. 在仓库设置中添加 Secret:
   - Settings → Secrets and variables → Actions
   - New repository secret

2. 在工作流中使用:

```yaml
- name: Use secret
  run: |
    echo "Secret value: ${{ secrets.MY_SECRET }}"
  env:
    TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Matrix 策略

测试多个版本/平台：

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    python-version: ['3.9', '3.10', '3.11']
    
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: ${{ matrix.python-version }}
```

### 条件执行

```yaml
# 仅在主分支运行
- name: Deploy
  if: github.ref == 'refs/heads/main'
  run: echo "Deploying..."

# 仅在 PR 时运行
- name: PR Check
  if: github.event_name == 'pull_request'
  run: echo "Checking PR..."

# 仅在失败时运行
- name: Notify failure
  if: failure()
  run: echo "Job failed!"
```

## 常见问题

### Q1: 工作流没有运行？

**检查清单**:
- [ ] YAML 文件在 `.github/workflows/` 目录
- [ ] YAML 语法正确（使用 yamllint 检查）
- [ ] 触发条件匹配（分支名、事件类型）
- [ ] 仓库 Actions 已启用

### Q2: 如何调试工作流？

```yaml
# 添加调试步骤
- name: Debug
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "Actor: ${{ github.actor }}"
    env
```

### Q3: 如何加速工作流？

1. **使用缓存**:
```yaml
- uses: actions/setup-python@v5
  with:
    cache: 'pip'  # 缓存 pip 包
```

2. **并行运行 Jobs**:
```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
  job2:
    runs-on: ubuntu-latest  # 与 job1 并行
```

3. **减少测试矩阵**:
```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.11']  # 只测试关键版本
```

### Q4: 权限问题？

```yaml
permissions:
  contents: write      # 写入仓库
  issues: write        # 创建 Issue
  pull-requests: write # PR 评论
```

## 最佳实践

### 1. 工作流组织

```
.github/workflows/
├── ci.yml              # 持续集成
├── cd.yml              # 持续部署
├── pr-checks.yml       # PR 检查
└── scheduled.yml       # 定时任务
```

### 2. 命名规范

- **文件名**: 使用小写字母和连字符 (`ci-cd.yml`)
- **工作流名**: 清晰描述性 (`name: CI/CD Pipeline`)
- **Job 名**: 简洁明了 (`code-quality`, `test`)

### 3. 错误处理

```yaml
# 允许某些步骤失败
- name: Optional check
  run: mypy src/
  continue-on-error: true

# 失败时运行清理
- name: Cleanup
  if: always()
  run: rm -rf temp/
```

### 4. 环境变量

```yaml
env:
  PYTHON_VERSION: '3.11'
  
jobs:
  test:
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}
```

### 5. 复用工作流

创建可复用的工作流：

```yaml
# .github/workflows/reusable-test.yml
on:
  workflow_call:
    inputs:
      python-version:
        required: true
        type: string

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
```

使用可复用工作流：

```yaml
jobs:
  call-reusable:
    uses: ./.github/workflows/reusable-test.yml
    with:
      python-version: '3.11'
```

### 6. 安全建议

- ✅ 使用固定版本的 Actions (`uses: actions/checkout@v4`)
- ✅ 不要在日志中打印 Secrets
- ✅ 最小化权限范围
- ✅ 使用 Dependabot 更新 Actions
- ✅ 审查第三方 Actions 代码

### 7. 成本优化

- 使用缓存减少重复下载
- 只在必要时运行全量测试
- 使用 `fail-fast: false` 时要谨慎
- 定时任务不要过于频繁

## 监控和维护

### 查看运行历史

1. GitHub → Actions 标签页
2. 选择具体工作流
3. 查看所有运行记录

### 下载日志

1. 点击具体的运行
2. 右上角 ⋮ → Download log archive

### 设置通知

1. Watch 仓库
2. Settings → Notifications
3. 配置 Actions 通知

## 进一步学习

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Actions Marketplace](https://github.com/marketplace?type=actions)
- [Workflow 语法](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [示例仓库](https://github.com/actions/starter-workflows)

---

**提示**: 实践是最好的学习方式！尝试修改现有工作流，观察结果，不断优化。
