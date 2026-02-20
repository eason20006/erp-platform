# 在 Conda 环境中安装依赖

## 问题
你当前在 conda 的 `(base)` 环境中，但依赖可能安装到了系统 Python，导致找不到模块。

## 解决方法

### 方法一：在 conda 环境中安装（推荐）

在终端中执行（确保看到 `(base)` 提示符）：

```bash
pip install Flask Flask-SQLAlchemy Flask-CORS Werkzeug
```

或者使用 conda（如果有的话）：
```bash
conda install -c conda-forge flask flask-sqlalchemy
pip install Flask-CORS
```

### 方法二：检查 Python 路径

确认你使用的 Python 是 conda 环境的：

```bash
which python
which python3
```

如果显示的是 `/Users/wangxiyue/anaconda3/bin/python` 或类似路径，说明是 conda 环境。

然后使用这个 Python 安装：
```bash
python -m pip install Flask Flask-SQLAlchemy Flask-CORS Werkzeug
```

### 方法三：使用虚拟环境（最可靠）

如果你想避免环境冲突，可以创建独立的虚拟环境：

```bash
# 在「练习网站」目录下
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install Flask Flask-SQLAlchemy Flask-CORS Werkzeug

# 启动应用
python -m erp_platform.app
```

---

## 验证安装

安装后，测试是否能导入：

```bash
python -c "import flask_sqlalchemy; print('OK')"
```

如果显示 `OK`，说明安装成功。

---

## 然后启动应用

```bash
python -m erp_platform.app
```
