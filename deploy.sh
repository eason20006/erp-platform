#!/bin/bash
# 快速部署脚本 - 用于云服务器部署

set -e

echo "=========================================="
echo "ERP 管理平台 - 部署脚本"
echo "=========================================="

# 检查是否在项目根目录
if [ ! -f "wsgi.py" ]; then
    echo "❌ 错误：请在项目根目录执行此脚本"
    exit 1
fi

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

echo "✅ Python 版本: $(python3 --version)"

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📥 安装依赖..."
pip install --upgrade pip
pip install -r erp_platform/requirements.txt

# 检查 Gunicorn
if ! python -c "import gunicorn" 2>/dev/null; then
    echo "📥 安装 Gunicorn..."
    pip install gunicorn
fi

echo ""
echo "=========================================="
echo "✅ 部署准备完成！"
echo "=========================================="
echo ""
echo "启动方式："
echo "1. 开发模式：python -m erp_platform.app"
echo "2. 生产模式：gunicorn -c gunicorn_config.py wsgi:app"
echo ""
echo "后台运行："
echo "   nohup gunicorn -c gunicorn_config.py wsgi:app > app.log 2>&1 &"
echo ""
echo "查看日志："
echo "   tail -f app.log"
echo ""
