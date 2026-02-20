#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""快速测试页面是否能正常显示"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from erp_platform import create_app
    app = create_app()
    
    with app.test_client() as client:
        print("=" * 50)
        print("测试登录页面...")
        r = client.get("/login")
        print(f"状态码: {r.status_code}")
        if r.status_code == 200:
            content = r.data.decode('utf-8')
            if len(content) > 100:
                print(f"✅ 页面内容长度: {len(content)} 字符")
                print(f"前100字符: {content[:100]}")
                if "ERP管理平台" in content:
                    print("✅ 页面包含 'ERP管理平台'，页面正常")
                else:
                    print("⚠️  页面内容可能不完整")
            else:
                print(f"❌ 页面内容过短: {content}")
        else:
            print(f"❌ 状态码错误: {r.status_code}")
        
        print("\n测试首页重定向...")
        r2 = client.get("/")
        print(f"状态码: {r2.status_code}, 重定向到: {r2.headers.get('Location', '无')}")
        
        print("\n测试静态文件路径...")
        print(f"静态文件夹: {app.static_folder}")
        print(f"模板文件夹: {app.template_folder}")
        if os.path.exists(app.static_folder):
            print(f"✅ 静态文件夹存在")
        else:
            print(f"❌ 静态文件夹不存在: {app.static_folder}")
        if os.path.exists(app.template_folder):
            print(f"✅ 模板文件夹存在")
        else:
            print(f"❌ 模板文件夹不存在: {app.template_folder}")
        
        print("=" * 50)
        print("\n如果看到 ✅，说明配置正确。")
        print("如果看到 ❌，请检查路径配置。")
        
except Exception as e:
    print(f"❌ 错误: {e}")
    import traceback
    traceback.print_exc()
