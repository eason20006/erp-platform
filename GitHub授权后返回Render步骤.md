# GitHub 授权后返回 Render 配置步骤

## ✅ 当前状态

你已经看到了 GitHub 的 "Render for GitHub" 应用页面，说明 Render 应用已经安装。

---

## 📝 接下来的步骤

### 步骤 1：检查授权设置（在当前 GitHub 页面）

在当前的 GitHub 页面上：

1. **查找 "Repository access"（仓库访问）部分**
   - 确认是否选择了 **"All repositories"**（所有仓库）
   - 或者选择了 **"Only select repositories"**（仅选择的仓库）

2. **如果还没选择仓库**：
   - 选择 **"Only select repositories"**
   - 在下拉列表中找到你的 ERP 平台仓库
   - 勾选该仓库

3. **保存设置**：
   - 点击页面底部的 **"Save"** 或 **"保存"** 按钮（如果有）

---

### 步骤 2：返回 Render 平台

1. **打开新标签页**，访问：https://dashboard.render.com
2. 或者点击页面上的 **"Go to Render Dashboard"** 链接（如果有）

---

### 步骤 3：重新创建 Web Service

1. 在 Render 控制台，点击 **"New +"** → **"Web Service"**

2. **这次应该能看到你的仓库了**：
   - 在 "Git Provider" 标签下
   - 应该显示你的 GitHub 仓库列表
   - 不再显示 "No repositories found"

3. **选择你的仓库**：
   - 点击你要部署的仓库名称

---

### 步骤 4：进入配置页面（现在可以填写配置了）

选择仓库后，会进入 **"Create New Web Service"** 配置页面。

#### 4.1 基本信息（页面顶部）

- **Name**: 填写 `erp-platform`（任意名称）
- **Region**: 选择 `Singapore`（推荐）
- **Branch**: 选择 `main` 或 `master`
- **Root Directory**: **留空**（如果代码在根目录）

#### 4.2 环境配置

- **Environment**: 选择 **"Python 3"**

#### 4.3 构建和启动命令（重要！）

找到 **"Build & Deploy"** 或 **"Build Settings"** 区域：

- **Build Command**（构建命令）：
  ```
  pip install -r erp_platform/requirements.txt
  ```

- **Start Command**（启动命令）：
  ```
  gunicorn -c gunicorn_config.py wsgi:app
  ```

#### 4.4 实例类型

- **Instance Type**: 选择 **"Free"**

---

### 步骤 5：开始部署

1. 检查所有配置是否正确
2. 点击页面底部的 **"Create Web Service"** 按钮
3. 等待部署完成（5-10 分钟）

---

## 🔍 如果返回 Render 后还是看不到仓库

### 解决方法 1：刷新页面
- 点击浏览器刷新按钮（F5）
- 或点击 Render 页面上的 **"Refresh"** 按钮

### 解决方法 2：重新连接
1. 在 Render 页面，点击 **"Settings"** → **"Git Providers"**
2. 找到 GitHub，点击 **"Reconnect"** 或 **"Disconnect and reconnect"**
3. 重新授权

### 解决方法 3：检查仓库权限
1. 回到 GitHub 的 Render 应用页面
2. 确认选择了正确的仓库
3. 保存设置后，返回 Render 刷新

---

## ✅ 配置检查清单

在 Render 配置页面确认：

- [ ] **Name**: 已填写
- [ ] **Environment**: 已选择 **"Python 3"**
- [ ] **Build Command**: `pip install -r erp_platform/requirements.txt`
- [ ] **Start Command**: `gunicorn -c gunicorn_config.py wsgi:app`
- [ ] **Instance Type**: 已选择 **"Free"**

---

## 🎯 快速操作

**现在请**：
1. ✅ 在当前 GitHub 页面确认仓库授权（如果需要）
2. ✅ 打开新标签页，访问 https://dashboard.render.com
3. ✅ 点击 **"New +"** → **"Web Service"**
4. ✅ 选择你的仓库
5. ✅ 填写配置（特别是 Build Command 和 Start Command）
6. ✅ 点击 **"Create Web Service"**

---

## 💡 提示

- GitHub 授权是一次性的，以后不需要重新授权
- 如果仓库列表为空，等待几秒刷新，或检查授权设置
- 确保你的仓库代码已经推送到 GitHub

**现在返回 Render 平台，应该能看到你的仓库了！** 🚀
