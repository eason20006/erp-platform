# Render 部署详细步骤（已完成连接 GitHub）

## ✅ 你已经完成：连接 GitHub 仓库

接下来按照以下步骤完成部署：

---

## 📝 步骤 1：创建 Web Service

1. **在 Render 控制台**，点击页面右上角的 **"New +"** 按钮
2. 在下拉菜单中选择 **"Web Service"**（不是 Static Site 或其他）

---

## 📝 步骤 2：选择仓库

1. 在 **"Connect a repository"** 页面
2. 找到并点击你刚才连接的 **GitHub 仓库**
3. 如果看不到，点击 **"Configure account"** 检查权限设置

---

## 📝 步骤 3：配置基本信息

在 **"Create New Web Service"** 页面，填写以下信息：

### 基本信息

- **Name（名称）**：
  - 输入：`erp-platform` 或 `erp-test-platform`（任意名称，用于标识）
  - 这个名称会出现在你的 URL 中

- **Region（区域）**：
  - 选择：`Singapore`（新加坡，离中国最近）或 `Oregon`（美国俄勒冈）
  - 建议选择 `Singapore` 以获得更好的访问速度

- **Branch（分支）**：
  - 选择：`main` 或 `master`（根据你的 GitHub 仓库分支名）
  - 通常是 `main`

- **Root Directory（根目录）**：
  - **留空**（如果你的代码在仓库根目录）
  - 如果你的代码在子目录，填写子目录名称（如：`练习网站`）

---

## 📝 步骤 4：配置构建和启动命令（重要！）

这是最关键的一步，需要正确配置：

### Environment（环境）

- **Environment**：选择 **"Python 3"**

### Build Command（构建命令）

在 **"Build Command"** 输入框中，输入：

```bash
pip install -r erp_platform/requirements.txt
```

**说明**：这个命令会在部署时安装所有 Python 依赖包。

### Start Command（启动命令）

在 **"Start Command"** 输入框中，输入：

```bash
gunicorn -c gunicorn_config.py wsgi:app
```

**说明**：这个命令会启动生产环境的 Web 服务器。

---

## 📝 步骤 5：选择实例类型

- **Instance Type（实例类型）**：
  - 选择 **"Free"**（免费版）
  - 免费版足够教学使用，有 512MB 内存

---

## 📝 步骤 6：环境变量（可选，但推荐）

点击 **"Advanced"** 展开高级选项，可以添加环境变量：

### 推荐添加的环境变量：

1. **PYTHON_VERSION**
   - Key: `PYTHON_VERSION`
   - Value: `3.9.0`（或 `3.9`）

2. **SECRET_KEY**（用于 Flask Session）
   - Key: `SECRET_KEY`
   - Value: 生成一个随机字符串（如：`your-secret-key-12345`）
   - 可以留空，系统会自动生成

**注意**：环境变量是可选的，不添加也能正常运行。

---

## 📝 步骤 7：开始部署

1. 检查所有配置是否正确：
   - ✅ Name: `erp-platform`
   - ✅ Build Command: `pip install -r erp_platform/requirements.txt`
   - ✅ Start Command: `gunicorn -c gunicorn_config.py wsgi:app`
   - ✅ Instance Type: `Free`

2. 点击页面底部的 **"Create Web Service"** 按钮

---

## 📝 步骤 8：等待部署完成

1. **部署过程**（约 5-10 分钟）：
   - 系统会显示部署日志
   - 你可以看到构建进度：
     - "Building..." - 正在构建
     - "Starting..." - 正在启动
     - "Live" - 部署成功 ✅

2. **查看日志**：
   - 点击 **"Logs"** 标签可以查看实时日志
   - 如果出错，日志会显示错误信息

---

## 📝 步骤 9：获取访问地址

部署成功后：

1. 在服务页面顶部，你会看到一个 **URL**，类似：
   ```
   https://erp-platform.onrender.com
   ```
   或
   ```
   https://erp-platform-xxxx.onrender.com
   ```

2. **复制这个 URL**

3. **测试访问**：
   - 在浏览器中打开这个 URL
   - 应该能看到登录页面
   - 使用 `admin` / `admin123` 登录测试

---

## 📝 步骤 10：分享给学生

将访问地址发给学生，格式如下：

```
ERP 管理平台访问地址：
https://your-app-name.onrender.com

默认登录账号：
- 管理员：admin / admin123
- 测试员：test / test123
```

---

## ⚠️ 常见问题处理

### 问题 1：Build Command 失败

**错误信息**：`Could not find requirements.txt`

**解决方法**：
- 检查 `erp_platform/requirements.txt` 文件是否存在
- 如果代码在子目录，修改 Build Command：
  ```bash
  cd 练习网站 && pip install -r erp_platform/requirements.txt
  ```

### 问题 2：Start Command 失败

**错误信息**：`gunicorn: command not found`

**解决方法**：
- 确保 `requirements.txt` 中包含 `gunicorn==21.2.0`
- 检查 Build Command 是否正确执行

### 问题 3：找不到 wsgi.py

**错误信息**：`No module named wsgi`

**解决方法**：
- 确认 `wsgi.py` 文件在项目根目录
- 如果代码在子目录，修改 Start Command：
  ```bash
  cd 练习网站 && gunicorn -c gunicorn_config.py wsgi:app
  ```

### 问题 4：部署成功但页面空白

**解决方法**：
1. 查看 Logs 中的错误信息
2. 检查数据库初始化是否成功
3. 确认静态文件路径配置正确

---

## 📋 配置检查清单

部署前确认：

- [ ] GitHub 仓库已连接
- [ ] `wsgi.py` 文件在项目根目录
- [ ] `gunicorn_config.py` 文件在项目根目录
- [ ] `erp_platform/requirements.txt` 文件存在
- [ ] `requirements.txt` 中包含 `gunicorn`
- [ ] Build Command: `pip install -r erp_platform/requirements.txt`
- [ ] Start Command: `gunicorn -c gunicorn_config.py wsgi:app`

---

## 🎯 快速参考：关键配置

```
Name: erp-platform
Environment: Python 3
Build Command: pip install -r erp_platform/requirements.txt
Start Command: gunicorn -c gunicorn_config.py wsgi:app
Instance Type: Free
```

---

## ✅ 部署成功标志

看到以下信息表示部署成功：

1. **状态显示**：`Live`（绿色）
2. **日志最后一行**：`Booting worker with pid: XXXX`
3. **访问 URL**：可以打开登录页面

---

## 📞 需要帮助？

如果遇到问题：
1. 查看 **Logs** 标签中的错误信息
2. 检查配置是否正确
3. 确认所有必需文件都在仓库中

**祝你部署顺利！** 🚀
