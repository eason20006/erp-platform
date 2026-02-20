#!/bin/bash
# ERP 管理平台启动脚本

cd "$(dirname "$0")"

echo "正在检查依赖..."
python3 -c "import flask" 2>/dev/null || {
    echo "❌ Flask 未安装，正在安装依赖..."
    echo "请选择安装方式："
    echo "1. 使用虚拟环境（推荐）"
    echo "2. 使用 pip3 install（需要权限）"
    read -p "请选择 (1/2): " choice
    
    if [ "$choice" = "1" ]; then
        echo "创建虚拟环境..."
        python3 -m venv venv
        source venv/bin/activate
        pip install -r erp_platform/requirements.txt
        echo "✅ 依赖安装完成"
    else
        pip3 install -r erp_platform/requirements.txt --user || {
            echo "安装失败，请尝试：sudo pip3 install -r erp_platform/requirements.txt"
            exit 1
        }
    fi
}

echo "正在启动 ERP 管理平台..."
python3 -m erp_platform.app
