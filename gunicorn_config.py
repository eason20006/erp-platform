# -*- coding: utf-8 -*-
"""Gunicorn 配置文件 - 生产环境 WSGI 服务器"""
import multiprocessing
import os

# 服务器配置
bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# 日志配置
accesslog = "-"  # 输出到 stdout
errorlog = "-"   # 输出到 stderr
loglevel = "info"

# 进程名称
proc_name = "erp_platform"

# 其他配置
preload_app = True
max_requests = 1000
max_requests_jitter = 50
