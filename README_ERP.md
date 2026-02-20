# ERP 管理平台 - 软件测试赛项练习环境

本平台用于支撑「软件测试」赛项技能测试模块的练习与考核，覆盖**功能测试、单元测试、接口测试、自动化测试、性能测试**五项任务。

---

## 一、考核内容与平台对应关系

| 任务       | 考核内容概要                     | 本平台支撑说明 |
|------------|----------------------------------|----------------|
| 任务一 功能测试 | 测试计划、测试用例（等价类/边界值）、测试执行、Bug 记录 | 提供完整 Web 业务流程：登录、商品管理、订单管理，可设计用例并执行、记录缺陷 |
| 任务二 单元测试 | 单元测试要求分析、测试数据设计、测试脚本、断言与参数化 | 提供 `business` 模块（订单金额、折扣、库存预警等），选手编写 unittest 用例 |
| 任务三 接口测试 | 接口描述分析、Postman 使用、请求/参数/断言、接口测试报告 | 提供 REST API（登录、商品、订单），见 `erp_platform/API接口说明.md` |
| 任务四 自动化测试 | Selenium、元素定位、unittest、数据驱动、Page Object、自动化报告 | 提供稳定页面结构（登录、首页、商品、订单），含 id/表单/链接便于定位 |
| 任务五 性能测试 | 脚本录制/场景、JMeter/LoadRunner、性能测试报告 | 提供可压测的 API（如登录、商品列表、订单列表、创建订单） |

---

## 二、快速启动

### 环境要求

- Python 3.8+
- 建议使用虚拟环境：`python3 -m venv venv`，再 `source venv/bin/activate`（Windows: `venv\Scripts\activate`）

### 安装依赖

在**项目根目录**（即本 README 所在目录「练习网站」）下执行：

```bash
pip install -r erp_platform/requirements.txt
```

### 启动服务

在**项目根目录**下执行：

```bash
python -m erp_platform.app
```

浏览器访问：**http://localhost:5000**

- 默认账号：`admin` / `admin123`（管理员）、`test` / `test123`（普通用户）

---

## 三、目录与赛题资料

- **erp_platform/**：ERP 平台源码与运行入口  
  - **business.py**：业务逻辑（供单元测试）  
  - **API接口说明.md**：接口列表（供接口测试 / Postman）  
  - **tests/**：单元测试示例（可在此基础上按赛题扩展）  
- **01 ~ 05**：各套赛题资料（测试计划/用例/Bug 清单/测试报告模板及各项“要求”PDF）

---

## 四、使用说明摘要

1. **功能测试**：在浏览器中按业务流程操作（登录→商品管理→订单管理），结合 01~05 中的模板编写测试计划、用例与测试报告，执行用例并记录 Bug。  
2. **单元测试**：阅读赛题中的《单元测试要求》，对 `erp_platform/business.py` 进行用例设计与脚本编写（等价类、边界值、断言、参数化等），参考 `erp_platform/tests/test_business.py`。  
3. **接口测试**：按《接口测试要求》与 `API接口说明.md`，使用 Postman 完成请求设置、参数、断言、数据驱动等，并编写接口测试报告。  
4. **自动化测试**：按《自动化测试要求》，使用 Selenium + unittest 对登录、商品、订单等页面进行自动化，可采用 Page Object；页面元素含 id/name 便于定位。  
5. **性能测试**：按《性能测试要求》，使用 JMeter 等对 `/api/login`、`/api/products`、`/api/orders` 等接口进行录制/脚本与场景设计，并编写性能测试报告。

---

## 五、技术栈

- 后端：Flask + SQLAlchemy（SQLite）  
- 前端：HTML + CSS + JavaScript（便于功能与自动化测试）  
- 业务逻辑与接口分离，便于单元测试与接口/性能测试

如遇端口占用，可在 `erp_platform/app.py` 中修改 `port=5000` 或通过环境变量配置。

---

## 六、网络部署（让学生在线访问）

### 快速部署到免费云平台（推荐）

**使用 Render（5分钟部署）**：
1. 访问 https://render.com，注册账号（可用 GitHub 登录）
2. 点击 "New +" → "Web Service"
3. 连接你的 GitHub 仓库
4. 配置：
   - Build Command: `pip install -r erp_platform/requirements.txt`
   - Start Command: `gunicorn -c gunicorn_config.py wsgi:app`
5. 点击部署，获得 URL（如：`https://your-app.onrender.com`）
6. 学生访问该 URL 即可使用！

**详细部署指南**：请查看 `部署指南.md`，包含：
- ✅ 免费云平台部署（Render、Railway）
- ✅ 云服务器部署（阿里云、腾讯云）
- ✅ Docker 容器化部署
- ✅ 学校内网服务器部署

**部署文件说明**：
- `wsgi.py` - WSGI 入口（生产环境）
- `gunicorn_config.py` - Gunicorn 配置
- `Dockerfile` - Docker 镜像配置
- `deploy.sh` - 快速部署脚本
