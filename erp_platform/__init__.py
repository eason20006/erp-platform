# -*- coding: utf-8 -*-
import os
from flask import Flask
from .config import Config
from .models import db

try:
    from flask_cors import CORS
except ImportError:
    CORS = None


def create_app():
    # 获取当前包所在目录的绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_folder = os.path.join(base_dir, "static")
    template_folder = os.path.join(base_dir, "templates")
    app = Flask(__name__, static_folder=static_folder, static_url_path="/static", template_folder=template_folder)
    app.config.from_object(Config)
    if CORS is not None:
        CORS(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        _init_data(app)
    from .routes import api, pages
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(pages)
    return app


def _init_data(app):
    """初始化演示数据（仅当表为空时）"""
    from .models import User, Product, Order, OrderItem
    if User.query.first() is not None:
        return
    u = User(username="admin", real_name="管理员", role="admin")
    u.set_password("admin123")
    db.session.add(u)
    u2 = User(username="test", real_name="测试员", role="staff")
    u2.set_password("test123")
    db.session.add(u2)
    for code, name, cat, price, stock in [
        ("P001", "笔记本电脑", "电子产品", 5999.00, 25),
        ("P002", "鼠标", "电子产品", 89.00, 100),
        ("P003", "签字笔", "文具", 3.50, 200),
        ("P004", "A4纸", "文具", 25.00, 80),
        ("P005", "抽纸", "日用品", 12.00, 60),
    ]:
        db.session.add(Product(code=code, name=name, category=cat, price=price, stock=stock))
    db.session.commit()
