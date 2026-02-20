# Render 连接 GitHub 详细步骤

## 🔍 当前状态

你的页面显示 **"No repositories found"**，说明需要先完成 GitHub 连接和授权。

---

## 📝 步骤 1：点击 GitHub 按钮

在页面上找到并点击 **"GitHub"** 按钮（有 GitHub 标志的按钮）

---

## 📝 步骤 2：授权 Render 访问 GitHub

点击 GitHub 按钮后，会跳转到 GitHub 授权页面：

### 2.1 GitHub 登录（如果未登录）
- 如果未登录 GitHub，先登录你的 GitHub 账号

### 2.2 授权 Render 访问
- GitHub 会询问是否授权 Render 访问你的仓库
- 页面会显示：
  - **"Authorize render"** 或 **"授权 render"**
  - 会列出 Render 需要的权限：
    - ✅ Read access to repositories（读取仓库权限）
    - ✅ Write access to code（写入代码权限，用于自动部署）

### 2.3 选择授权范围
- **推荐选择**：**"All repositories"**（所有仓库）
  - 这样以后部署其他项目也方便
- 或者选择 **"Only select repositories"**（仅选择的仓库）
  - 然后勾选你要部署的仓库

### 2.4 确认授权
- 点击 **"Authorize render"** 或 **"授权"** 按钮
- 可能会要求输入 GitHub 密码确认

---

## 📝 步骤 3：返回 Render 页面

授权完成后，会自动跳转回 Render 页面：

### 3.1 检查仓库列表
- 页面应该会显示你的 GitHub 仓库列表
- 如果还是显示 "No repositories found"：
  - 等待几秒钟刷新
  - 或者点击页面上的 **"Refresh"** 或 **"刷新"** 按钮

### 3.2 选择仓库
- 在仓库列表中找到你的 ERP 平台仓库
- 点击仓库名称或旁边的 **"Connect"** 按钮

---

## 📝 步骤 4：进入配置页面

选择仓库后，会进入 **"Create New Web Service"** 配置页面

这时你才能看到并填写：
- Name
- Environment
- Build Command
- Start Command
- Instance Type

---

## ⚠️ 常见问题

### 问题 1：点击 GitHub 按钮没反应

**解决方法**：
1. 检查浏览器是否阻止了弹窗
2. 允许 Render 的弹窗
3. 或者右键点击 GitHub 按钮，选择"在新标签页打开"

### 问题 2：授权后还是看不到仓库

**解决方法**：
1. 检查授权时是否选择了正确的仓库范围
2. 点击页面上的 **"Refresh"** 按钮
3. 或者重新点击 GitHub 按钮，检查授权状态

### 问题 3：找不到要部署的仓库

**解决方法**：
1. 确认仓库是否在 GitHub 上存在
2. 确认仓库是 **Public**（公开）或你授权了 Render 访问
3. 检查仓库名称是否正确

---

## ✅ 连接成功的标志

连接成功后，你会看到：
- ✅ 仓库列表显示你的仓库
- ✅ 可以点击仓库进入配置页面
- ✅ 不再显示 "No repositories found"

---

## 🎯 完整流程

```
1. 点击 "GitHub" 按钮
   ↓
2. 在 GitHub 授权页面登录（如需要）
   ↓
3. 选择授权范围（All repositories 或特定仓库）
   ↓
4. 点击 "Authorize render" 授权
   ↓
5. 自动返回 Render 页面
   ↓
6. 看到仓库列表，选择你的仓库
   ↓
7. 进入配置页面，填写 Build Command 和 Start Command
```

---

## 💡 提示

- 授权是一次性的，以后部署其他项目不需要重新授权
- 如果授权失败，可以重新点击 GitHub 按钮
- 确保 GitHub 账号有权限访问你要部署的仓库

**现在请点击页面上的 "GitHub" 按钮，完成授权！** 🚀
