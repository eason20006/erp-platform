# -*- coding: utf-8 -*-
"""ERP 管理平台 - 启动入口"""
import sys
import os
# 从项目根目录（练习网站）运行: python -m erp_platform.app ；或先 cd 到 练习网站 再运行
_here = os.path.dirname(os.path.abspath(__file__))
_parent = os.path.dirname(_here)
if _parent not in sys.path:
    sys.path.insert(0, _parent)
from erp_platform import create_app

app = create_app()

if __name__ == "__main__":
    import os
    # 如果端口 5000 被占用，可以使用环境变量 PORT 指定其他端口
    # 例如：PORT=5001 python -m erp_platform.app
    port = int(os.environ.get("PORT", 5001))  # 默认改为 5001，避免与 AirPlay 冲突
    app.run(host="0.0.0.0", port=port, debug=True)
