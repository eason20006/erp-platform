# -*- coding: utf-8 -*-
"""ERP 数据模型 - 可供单元测试的业务逻辑依赖"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    """用户表"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    real_name = db.Column(db.String(64))
    role = db.Column(db.String(32), default="staff")  # admin, manager, staff
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Product(db.Model):
    """商品表"""
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(32), unique=True, nullable=False, index=True)
    name = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(64))
    unit = db.Column(db.String(16), default="个")
    price = db.Column(db.Numeric(12, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Order(db.Model):
    """销售订单表"""
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    order_no = db.Column(db.String(32), unique=True, nullable=False, index=True)
    customer_name = db.Column(db.String(128), nullable=False)
    total_amount = db.Column(db.Numeric(12, 2), default=0)
    status = db.Column(db.String(32), default="pending")  # pending, confirmed, shipped, completed, cancelled
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship("OrderItem", backref="order", lazy="dynamic", cascade="all, delete-orphan")


class OrderItem(db.Model):
    """订单明细表"""
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    product_name = db.Column(db.String(128))
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(12, 2), nullable=False)
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    product = db.relationship("Product", backref="order_items")
