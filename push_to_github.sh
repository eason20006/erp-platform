#!/bin/bash
# 自动推送代码到 GitHub 的脚本

echo "=========================================="
echo "开始推送代码到 GitHub"
echo "=========================================="

cd /Users/wangxiyue/软件测试/练习网站

# 1. 强制重新初始化 Git
echo "📦 初始化 Git 仓库..."
if [ -d ".git" ]; then
    echo "   删除旧的 .git 目录..."
    rm -rf .git
fi
git init

# 2. 添加远程仓库
echo "🔗 连接远程仓库..."
git remote add origin https://github.com/eason20006/erp-platform.git 2>/dev/null || \
git remote set-url origin https://github.com/eason20006/erp-platform.git
echo "✅ 远程仓库已连接"

# 3. 添加所有文件
echo "📝 添加文件到暂存区..."
git add .

# 4. 提交
echo "💾 提交更改..."
git commit -m "Initial commit: ERP platform for software testing competition"
echo "✅ 提交完成"

# 5. 设置主分支
echo "🌿 设置主分支..."
git branch -M main

# 6. 推送到 GitHub
echo ""
echo "🚀 推送到 GitHub..."
echo ""
echo "⚠️  注意：推送时需要 GitHub 认证"
echo "   Username: eason20006"
echo "   Password: 请使用 Personal Access Token（不是密码）"
echo "   获取 Token: https://github.com/settings/tokens"
echo ""
echo "正在推送..."

git push -u origin main

echo ""
echo "=========================================="
echo "✅ 推送完成！"
echo "=========================================="
echo ""
echo "请访问 GitHub 仓库确认："
echo "https://github.com/eason20006/erp-platform"
echo ""
echo "然后返回 Render 平台进行部署配置！"
