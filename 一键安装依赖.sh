#!/bin/bash
# ERP 平台依赖一键安装脚本

echo "正在检查 Python 环境..."
python --version
echo "Python 路径: $(which python)"
echo ""

echo "正在安装依赖包..."
pip install Flask Flask-SQLAlchemy Flask-CORS Werkzeug

echo ""
echo "验证安装..."
python -c "import flask; import flask_sqlalchemy; print('✅ 所有依赖安装成功！')" && echo "可以运行: python -m erp_platform.app" || echo "❌ 安装失败，请检查错误信息"
