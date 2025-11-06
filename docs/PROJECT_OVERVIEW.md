# 项目概览

## 🎯 项目目标

这是一个完整的教学项目，旨在帮助开发者学习和掌握 GitHub Actions 工作流的使用。

## 📂 项目结构

```
TestRepository/
│
├── .github/
│   └── workflows/              # GitHub Actions 工作流
│       ├── ci-cd.yml          # 主 CI/CD 管道（5个Job）
│       ├── pr-checks.yml      # PR 自动检查
│       ├── scheduled-tests.yml # 定时测试
│       └── dependency-check.yml # 依赖安全检查
│
├── src/                        # 源代码
│   ├── __init__.py
│   ├── calculator.py          # 计算器核心逻辑
│   └── main.py               # CLI 入口
│
├── tests/                      # 测试代码
│   ├── __init__.py
│   └── test_calculator.py     # 完整的单元测试（100%覆盖）
│
├── docs/                       # 文档
│   ├── QUICKSTART.md          # 快速开始指南
│   ├── WORKFLOWS_GUIDE.md     # 工作流详细说明
│   └── FAQ.md                 # 常见问题
│
├── scripts/                    # 工具脚本
│   ├── setup.sh              # Linux/Mac 环境设置
│   ├── setup.bat             # Windows 环境设置
│   ├── check.sh              # 代码质量检查
│   └── test.sh               # 测试运行脚本
│
├── .gitignore                 # Git 忽略文件
├── LICENSE                    # MIT 许可证
├── README.md                  # 主文档
├── CONTRIBUTING.md            # 贡献指南
├── CHANGELOG.md              # 变更日志
├── requirements.txt          # Python 依赖
├── setup.py                  # 安装配置（传统）
├── setup.cfg                 # 工具配置
└── pyproject.toml           # 现代 Python 配置
```

## 🚀 核心功能

### 1. 计算器应用

- ➕ 加法
- ➖ 减法
- ✖️ 乘法
- ➗ 除法
- 🔢 幂运算
- √ 平方根

### 2. GitHub Actions 工作流

#### CI/CD Pipeline (ci-cd.yml)
- **Job 1: 代码质量检查**
  - Black (格式化)
  - isort (导入排序)
  - Flake8 (代码风格)
  - MyPy (类型检查)

- **Job 2: 多版本测试**
  - OS: Ubuntu, macOS, Windows
  - Python: 3.9, 3.10, 3.11, 3.12
  - 总计: 12 个测试组合

- **Job 3: 安全扫描**
  - Bandit (代码安全)
  - Safety (依赖安全)

- **Job 4: 构建包**
  - Python 包构建
  - Twine 验证

- **Job 5: 自动发布**
  - 创建 GitHub Release
  - 上传构建产物

#### PR 检查 (pr-checks.yml)
- 自动运行测试
- 生成覆盖率报告
- 代码格式检查
- 自动添加标签

#### 定时测试 (scheduled-tests.yml)
- 每日自动测试
- 失败时发送通知

#### 依赖检查 (dependency-check.yml)
- 每周检查过期依赖
- 安全漏洞扫描
- 自动创建 Issue

## 📊 技术栈

### 语言和框架
- Python 3.9+
- pytest (测试框架)

### 开发工具
- Black (代码格式化)
- Flake8 (代码检查)
- MyPy (类型检查)
- isort (导入排序)
- Bandit (安全扫描)

### CI/CD
- GitHub Actions
- pytest-cov (覆盖率)
- codecov (覆盖率报告)

## 🎓 学习重点

### 初级
1. ✅ 理解 CI/CD 概念
2. ✅ 基本的 YAML 语法
3. ✅ 触发条件配置
4. ✅ 查看工作流日志

### 中级
1. ✅ Job 依赖关系
2. ✅ Matrix 策略
3. ✅ 上传和下载产物
4. ✅ 使用 Actions Marketplace

### 高级
1. ✅ 复用工作流
2. ✅ 自定义 Actions
3. ✅ Secrets 管理
4. ✅ 条件执行和策略

## 📈 项目指标

- 📝 代码行数: ~500 行
- 🧪 测试数量: 25+ 测试用例
- 📊 测试覆盖率: 100%
- 🔧 工作流数量: 4 个
- 📖 文档页面: 7+ 页

## 🔄 工作流程

### 开发流程
```
1. Fork 仓库
   ↓
2. 克隆到本地
   ↓
3. 创建功能分支
   ↓
4. 编写代码 + 测试
   ↓
5. 本地测试通过
   ↓
6. 提交并推送
   ↓
7. 创建 Pull Request
   ↓
8. CI 自动检查
   ↓
9. 代码审查
   ↓
10. 合并到主分支
```

### CI/CD 流程
```
代码推送
   ↓
触发工作流
   ↓
├─ 代码质量检查
│  ├─ Black
│  ├─ Flake8
│  ├─ MyPy
│  └─ isort
│
├─ 多平台测试
│  ├─ Ubuntu (3.9, 3.10, 3.11, 3.12)
│  ├─ macOS (3.9, 3.10, 3.11, 3.12)
│  └─ Windows (3.9, 3.10, 3.11, 3.12)
│
└─ 安全扫描
   ├─ Bandit
   └─ Safety
      ↓
   构建包
      ↓
   发布 Release (仅 tag)
```

## 🎯 使用场景

### 个人学习
- 学习 GitHub Actions
- 理解 CI/CD 流程
- 练习测试驱动开发

### 教学演示
- 课堂演示 CI/CD
- 工作流最佳实践
- 代码质量管理

### 项目模板
- 新项目的起点
- 配置文件参考
- 工作流模板

## 🔧 配置文件说明

### requirements.txt
列出所有 Python 依赖，包括开发工具和测试框架。

### setup.py
传统的 Python 包配置文件，定义包的元数据和依赖。

### pyproject.toml
现代 Python 项目配置，符合 PEP 518 标准。

### setup.cfg
工具配置文件，包含 pytest、coverage、flake8 等的配置。

### .gitignore
定义 Git 应忽略的文件和目录。

## 📚 文档结构

### README.md
主文档，包含项目介绍、安装、使用等完整信息。

### CONTRIBUTING.md
贡献指南，详细说明如何为项目做贡献。

### CHANGELOG.md
变更日志，记录所有重要的项目变更。

### docs/QUICKSTART.md
快速开始指南，5分钟上手教程。

### docs/WORKFLOWS_GUIDE.md
工作流详细指南，深入讲解每个工作流的使用。

### docs/FAQ.md
常见问题解答，解决常见疑问。

## 🌟 特色功能

### 1. 完整的测试覆盖
- 100% 代码覆盖率
- 参数化测试
- 边界条件测试
- 异常处理测试

### 2. 多平台支持
- 跨操作系统测试
- 多 Python 版本兼容
- 平台特定脚本

### 3. 自动化工具
- 环境设置脚本
- 代码质量检查脚本
- 测试运行脚本

### 4. 详细文档
- 面向初学者
- 分步骤指南
- 实际示例代码

## 🎯 下一步计划

### 短期（v1.1）
- [ ] 添加更多数学函数
- [ ] Web UI 界面
- [ ] Docker 支持

### 中期（v2.0）
- [ ] GraphQL API
- [ ] 数据库集成
- [ ] 用户认证

### 长期（v3.0）
- [ ] 微服务架构
- [ ] Kubernetes 部署
- [ ] 性能优化

## 📞 联系方式

- **GitHub**: [@Exile118](https://github.com/Exile118)
- **项目**: [TestRepository](https://github.com/Exile118/TestRepository)
- **Issues**: [报告问题](https://github.com/Exile118/TestRepository/issues)
- **Discussions**: [讨论交流](https://github.com/Exile118/TestRepository/discussions)

## 📜 许可证

本项目采用 MIT 许可证。详见 [LICENSE](../LICENSE) 文件。

---

**最后更新**: 2025-11-06
**版本**: 1.0.0
**状态**: ✅ 活跃维护
