# Changelog

本文档记录了项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 计划中
- [ ] 添加更多数学函数（三角函数、对数等）
- [ ] Web UI 界面
- [ ] 计算历史记录功能

## [1.0.0] - 2025-11-06

### 新增
- ✨ 基本计算器功能（加、减、乘、除）
- ✨ 高级功能（幂运算、平方根）
- ✨ 完整的单元测试套件
- 🎯 GitHub Actions CI/CD 管道
  - 代码质量检查（Black, Flake8, MyPy, isort）
  - 多版本多平台测试矩阵
  - 安全扫描（Bandit, Safety）
  - 自动构建和发布
- 📝 详细的项目文档
- 🔧 项目配置文件
  - setup.py
  - setup.cfg
  - pyproject.toml
  - requirements.txt

### 工作流
- 🚀 主 CI/CD 管道 (`ci-cd.yml`)
  - 代码质量检查
  - 多平台测试（Ubuntu, macOS, Windows）
  - 多 Python 版本测试（3.9, 3.10, 3.11, 3.12）
  - 安全扫描
  - 自动构建
  - 自动 Release
- ⏰ 定时测试 (`scheduled-tests.yml`)
  - 每日自动测试
- 🔍 PR 检查 (`pr-checks.yml`)
  - 自动代码审查
  - 覆盖率报告
  - 自动标签
- 🔐 依赖检查 (`dependency-check.yml`)
  - 每周依赖扫描
  - 安全漏洞检测

### 文档
- 📖 完整的 README.md
- 📝 贡献指南 (CONTRIBUTING.md)
- 📜 MIT 许可证
- 📋 变更日志 (CHANGELOG.md)

### 测试
- ✅ 100% 代码覆盖率
- ✅ 参数化测试
- ✅ 边界条件测试
- ✅ 异常处理测试

## [0.1.0] - 2025-11-05

### 新增
- 🎉 项目初始化
- 📁 基础项目结构
- 🔧 开发环境配置

---

## 版本说明

### 语义化版本格式：MAJOR.MINOR.PATCH

- **MAJOR**: 不兼容的 API 变更
- **MINOR**: 向后兼容的新功能
- **PATCH**: 向后兼容的问题修复

### 变更类型

- `新增` - 新功能
- `变更` - 现有功能的变更
- `弃用` - 即将移除的功能
- `移除` - 已移除的功能
- `修复` - Bug 修复
- `安全` - 安全问题修复

---

**注意**: 对于未发布的变更，请在 `[未发布]` 部分记录。
