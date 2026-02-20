# -*- coding: utf-8 -*-
"""WSGI 入口文件 - 用于生产环境部署（Gunicorn、uWSGI 等）"""
from erp_platform import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
