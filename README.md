# Job Intelligence Platform

**职位数据展示与智能分析中台**

<p align="center">
  基于 Ant Design Pro + Python FastAPI 构建的招聘职位数据管理与分析平台
</p>

---

## 1. 项目介绍

Job Intelligence Platform 是一个面向招聘数据的职位展示与智能分析中台。

项目以招聘网站爬取的职位数据为基础，通过 Python 对原始招聘数据进行清洗、标准化、结构化和数据富集，并利用前后端分离架构，为用户提供统一的职位数据访问、管理和可视化分析服务。

项目旨在建立一套完整的招聘数据处理与展示体系，实现从职位数据采集、数据富集、数据库存储到数据可视化分析的完整流程。

### 核心目标

- **数据接入：** 支持 Excel、CSV 文件导入，后续对接招聘数据爬虫。
- **数据处理：** 使用 Python 完成数据清洗、标准化和数据富集。
- **数据存储：** 使用 PostgreSQL 统一管理职位及关联数据。
- **数据展示：** 使用 Ant Design Pro 构建企业级数据管理界面。
- **数据分析：** 对职位分类、招聘城市、发布时间等维度进行统计分析。
- **数据治理：** 建立数据质量监控、异常复核和数据处理记录机制。

## 2. 技术架构

项目采用前后端分离架构。

### Frontend

| 技术 | 用途 |
|---|---|
| React | 前端应用开发 |
| TypeScript | 类型安全 |
| Ant Design Pro | 企业级中后台界面 |
| Ant Design | UI 组件库 |
| Umi Max | 前端应用框架 |
| ProTable | 职位数据表格展示 |

### Backend

| 技术 | 用途 |
|---|---|
| Python | 后端开发语言 |
| FastAPI | RESTful API 接口服务 |
| Pandas | 数据清洗与统计分析 |
| OpenPyXL | Excel 文件读写 |
| SQLAlchemy | 数据库 ORM |
| Pydantic | 接口数据校验 |

### Database

| 技术 | 用途 |
|---|---|
| PostgreSQL | 关系型数据库 |
| Alembic | 数据库结构迁移 |

### Architecture

```text
                 用户
                  |
                  v
       Ant Design Pro 前端
          React / TypeScript
                  |
             HTTP / JSON
                  |
                  v
          Python FastAPI
                  |
          SQLAlchemy ORM
                  |
                  v
             PostgreSQL
                  |
       +----------+----------+
       |          |          |
       v          v          v
    职位数据    城市数据    分类数据
       |
       v
    数据分析与质量管理

                  ^
                  |
          数据采集与富集
                  |
       +----------+----------+
       |          |          |
       v          v          v
    招聘爬虫    Excel导入   数据清洗
```

## 3. 核心功能规划

### 3.1 数据总览（Dashboard）

- 职位总量统计
- 社会招聘与校园招聘分布
- 职位分类统计
- 城市招聘数量排名
- 职位发布时间趋势
- 数据质量指标展示

### 3.2 职位中心

- 职位列表展示
- 职位关键词搜索
- 多条件组合筛选
- 职位详情查看
- 职位描述与任职要求展示
- 招聘城市及地址信息展示
- 职位数据导出

### 3.3 招聘数据分析

- 一级、二级职位分类分析
- 城市招聘分布分析
- 社招与校招对比分析
- 职位发布时间分析
- 职位技能关键词分析（后续扩展）

### 3.4 数据管理

- Excel / CSV 数据导入
- 数据字段校验
- 职位数据去重
- 数据导入批次管理
- 数据导出
- 招聘爬虫数据接入（后续扩展）

### 3.5 数据质量管理

- 数据完整性检查
- 地址标准化与匹配状态监控
- 职位分类映射管理
- 异常数据复核
- 数据富集记录追踪
- 数据缺失情况分析

### 3.6 系统管理

- 用户管理
- 角色与权限管理
- 城市标准字典
- 职位分类字典
- 系统操作日志

## 4. 数据来源与数据结构

项目初期以经过清洗和富集的招聘职位 Excel 数据作为示例数据源。

当前示例数据包含六个工作表：

| 工作表 | 主要用途 |
|---|---|
| 岗位主表 | 职位基本信息及富集字段 |
| 岗位城市 | 职位与招聘城市关联 |
| 城市标准 | 城市标准化映射 |
| 同址补齐 | 地址补齐证据 |
| 复核清单 | 待复核数据 |
| 缺失登记 | 数据缺失情况 |

后续将逐步把 Excel 工作表转换为规范化的关系型数据库表。

### 数据设计原则

1. 保留原始职位数据，不直接覆盖原始字段。
2. 将标准化和富集结果与原始数据区分管理。
3. 职位与城市采用关联表设计，支持一个职位对应多个招聘城市。
4. 记录数据来源、导入批次和数据处理过程。
5. 对异常数据保留复核和追踪能力。

## 5. 项目目录结构

```text
job-intelligence-platform/
│
├── frontend/                  # Ant Design Pro 前端
│   ├── config/                # 前端配置
│   ├── src/
│   │   ├── pages/             # 页面
│   │   ├── components/        # 公共组件
│   │   ├── services/          # API 接口服务
│   │   └── ...
│   └── package.json
│
├── backend/                   # Python 后端
│   ├── app/
│   │   ├── api/               # API 路由
│   │   ├── core/              # 核心配置
│   │   ├── db/                # 数据库连接
│   │   ├── models/            # 数据库模型
│   │   ├── schemas/           # 数据校验模型
│   │   ├── services/          # 业务逻辑
│   │   └── main.py            # FastAPI 应用入口
│   │
│   ├── tests/                 # 自动化测试
│   ├── requirements.txt       # Python 依赖
│   └── .venv/                 # Python 虚拟环境（不上传）
│
├── data/
│   ├── raw/                   # 原始数据（不上传）
│   └── sample/                # 脱敏示例数据
│
├── docs/                      # 项目文档
│
├── .gitignore
└── README.md
```

## 6. 本地开发环境

### 环境要求

| 环境 | 要求 |
|---|---|
| Windows | Windows 10 / 11 |
| Node.js | 22 或更高版本 |
| npm | 与 Node.js 配套 |
| Python | 3.10 或更高版本 |
| PostgreSQL | 后续数据库阶段安装 |

### 6.1 获取项目

```bash
git clone https://github.com/desvu39-ops/job-intelligence-platform.git

cd job-intelligence-platform
```

### 6.2 启动前端

```powershell
cd frontend

npm install

npm start
```

根据终端输出打开本地前端地址。

### 6.3 启动后端

打开另一个 PowerShell 窗口：

```powershell
cd job-intelligence-platform\backend

python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

### 6.4 后端接口文档

后端启动后，可以访问：

- API 首页：http://127.0.0.1:8001
- 健康检查：http://127.0.0.1:8001/api/v1/health
- Swagger API 文档：http://127.0.0.1:8001/docs

## 7. API 接口规划

后端将采用 RESTful API 设计，为前端提供统一的数据访问接口。

| 接口 | 功能 |
|---|---|
| GET /api/v1/health | 服务健康检查 |
| GET /api/v1/dashboard/summary | 首页统计 |
| GET /api/v1/dashboard/trends | 职位发布时间趋势 |
| GET /api/v1/jobs | 职位分页查询 |
| GET /api/v1/jobs/{id} | 职位详情 |
| GET /api/v1/analytics/categories | 职位分类统计 |
| GET /api/v1/analytics/cities | 城市招聘统计 |
| GET /api/v1/quality/overview | 数据质量总览 |
| POST /api/v1/imports/jobs | 职位 Excel 数据导入 |

以上为规划接口，后续将随着功能开发逐步实现。

## 8. 开发路线图

| 版本 | 开发内容 | 状态 |
|---|---|---|
| v0.1.0 | 项目初始化、前后端基础环境、GitHub 仓库 | 已完成 |
| v0.2.0 | PostgreSQL 数据库建设 | 计划中 |
| v0.3.0 | Excel 数据导入与数据模型建设 | 计划中 |
| v0.4.0 | FastAPI 数据查询接口 | 计划中 |
| v0.5.0 | Dashboard 与职位管理页面 | 计划中 |
| v0.6.0 | 招聘数据分析与数据质量管理 | 计划中 |
| v1.0.0 | 完整职位数据中台 | 规划中 |

## 9. 数据安全与版本管理

项目采用 Git 进行代码版本管理。

以下内容不应直接上传到公开 GitHub 仓库：

- `.env` 环境配置文件
- 数据库密码及访问凭证
- Python 虚拟环境
- Node.js 依赖目录
- 未脱敏的原始招聘数据
- 数据库备份文件

项目通过 `.gitignore` 管理需要忽略的文件。

示例数据应经过必要的脱敏处理后再提交。

## 10. 项目信息

- **项目名称：** Job Intelligence Platform
- **项目类型：** 招聘职位数据管理与分析平台
- **开发模式：** 前后端分离
- **前端：** Ant Design Pro
- **后端：** Python FastAPI
- **数据库：** PostgreSQL
- **代码仓库：** https://github.com/desvu39-ops/job-intelligence-platform

---

## 11. 项目愿景

希望通过本项目建立一套可扩展、可维护的招聘数据基础设施。

从最初的职位数据采集和展示，逐步扩展到招聘数据治理、多维度统计分析和智能化职位信息挖掘，最终形成一个完整的职位数据智能分析平台。
