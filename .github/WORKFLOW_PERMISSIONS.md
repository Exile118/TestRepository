# GitHub Actions 权限说明

## 问题描述

如果你遇到以下错误：
```
Error: HttpError: Resource not accessible by integration
```

这是因为 GitHub Actions 工作流需要特定的权限才能执行某些操作。

## 已修复的权限配置

### 1. PR 检查工作流 (`pr-checks.yml`)

```yaml
permissions:
  contents: read           # 读取仓库内容
  pull-requests: write     # 在 PR 上添加评论
  issues: write           # 添加标签（PR 也是 issue）
```

**需要这些权限的原因：**
- 添加代码覆盖率评论到 PR
- 为 PR 自动添加标签

### 2. 依赖检查工作流 (`dependency-check.yml`)

```yaml
permissions:
  contents: read    # 读取仓库内容
  issues: write     # 创建 Issue
```

**需要这些权限的原因：**
- 当发现过期依赖时自动创建 Issue

### 3. CI/CD 工作流 (`ci-cd.yml`)

**主工作流权限：**
```yaml
permissions:
  contents: read    # 读取仓库内容
```

**Release job 特定权限：**
```yaml
jobs:
  release:
    permissions:
      contents: write    # 创建 Release 和 tag
```

**需要这些权限的原因：**
- 创建 GitHub Release
- 上传发布产物

### 4. 定时测试工作流 (`scheduled-tests.yml`)

不需要额外权限（只读取和测试）。

## GitHub Token 权限级别

### 默认权限

GitHub Actions 的 `GITHUB_TOKEN` 有两种默认权限模式：

1. **Permissive（宽松）** - 旧的默认设置
   - 大多数操作都有写权限
   
2. **Restricted（受限）** - 新的推荐设置
   - 只有读权限
   - 需要显式声明写权限

### 检查仓库设置

1. 进入仓库 Settings
2. 点击 Actions → General
3. 滚动到 "Workflow permissions"
4. 查看当前设置

**推荐设置：**
- ✅ **Read repository contents and packages permissions**
- ✅ 在工作流中显式声明需要的权限

## 权限最佳实践

### 1. 最小权限原则

只授予工作流真正需要的权限：

```yaml
# ❌ 不好 - 过于宽松
permissions: write-all

# ✅ 好 - 明确指定
permissions:
  contents: read
  pull-requests: write
```

### 2. Job 级别权限

为特定 job 设置权限：

```yaml
jobs:
  normal-job:
    # 使用工作流级别的默认权限
    
  special-job:
    permissions:
      contents: write    # 只有这个 job 需要写权限
```

### 3. 完整的权限列表

```yaml
permissions:
  actions: read|write|none           # GitHub Actions
  checks: read|write|none            # 检查
  contents: read|write|none          # 仓库内容
  deployments: read|write|none       # 部署
  id-token: read|write|none          # OIDC token
  issues: read|write|none            # Issues
  discussions: read|write|none       # Discussions
  packages: read|write|none          # GitHub Packages
  pages: read|write|none             # GitHub Pages
  pull-requests: read|write|none     # Pull Requests
  repository-projects: read|write|none # Projects
  security-events: read|write|none   # 安全事件
  statuses: read|write|none          # 状态检查
```

## 常见场景的权限需求

### 创建 PR 评论

```yaml
permissions:
  pull-requests: write
```

### 创建 Issue

```yaml
permissions:
  issues: write
```

### 创建 Release

```yaml
permissions:
  contents: write
```

### 发布包到 GitHub Packages

```yaml
permissions:
  packages: write
```

### 上传代码扫描结果

```yaml
permissions:
  security-events: write
```

## 故障排查

### 错误：Resource not accessible by integration

**可能的原因：**
1. 工作流没有声明需要的权限
2. 仓库设置为受限权限模式
3. 使用了需要写权限的 Action

**解决方法：**
1. 在工作流中添加 `permissions` 配置
2. 或者在仓库设置中改为宽松模式（不推荐）

### 错误：Not enough permissions to create comment

**解决方法：**
```yaml
permissions:
  pull-requests: write
  issues: write
```

### 错误：Resource protected by organization SAML enforcement

**解决方法：**
- 需要授权 SSO
- 联系组织管理员

## 安全考虑

### 1. Fork 的 PR

来自 fork 的 PR 的工作流运行在受限权限下，无法：
- 访问 secrets
- 写入仓库
- 创建评论

**解决方法：**
- 使用 `pull_request_target` 事件（需谨慎）
- 将敏感操作移到单独的工作流

### 2. 第三方 Actions

使用第三方 Actions 时要特别注意：
- ✅ 固定到特定版本（如 `@v3`）
- ✅ 审查 Action 的代码
- ✅ 使用可信来源的 Actions

## 本项目的权限配置总结

| 工作流 | 权限 | 原因 |
|--------|------|------|
| `ci-cd.yml` | `contents: read` | 运行测试和构建 |
| `ci-cd.yml` (release job) | `contents: write` | 创建 Release |
| `pr-checks.yml` | `contents: read`<br>`pull-requests: write`<br>`issues: write` | 添加 PR 评论和标签 |
| `dependency-check.yml` | `contents: read`<br>`issues: write` | 创建依赖更新 Issue |
| `scheduled-tests.yml` | 默认（只读） | 运行测试 |

## 更多资源

- [GitHub Actions 权限文档](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
- [GITHUB_TOKEN 权限](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token)
- [工作流权限语法](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions)

---

**最后更新**: 2025-11-06
