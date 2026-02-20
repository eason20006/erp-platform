# -*- coding: utf-8 -*-
"""API 与页面路由 - 供接口测试、自动化测试、功能测试使用"""
from datetime import datetime
from decimal import Decimal
from flask import Blueprint, request, jsonify, session, redirect, url_for, send_from_directory, render_template, current_app
from functools import wraps
from .models import db, User, Product, Order, OrderItem
from .business import calculate_order_amount

api = Blueprint("api", __name__)
pages = Blueprint("pages", __name__)


def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            if request.path.startswith("/api/"):
                return jsonify({"success": False, "message": "请先登录"}), 401
            return redirect(url_for("pages.login_page"))
        return f(*args, **kwargs)
    return wrapped


# ---------- API：登录 / 登出（接口测试、性能测试会用到）----------
@api.route("/login", methods=["POST"])
def api_login():
    data = request.get_json() or {}
    username = data.get("username", "").strip()
    password = data.get("password", "")
    if not username or not password:
        return jsonify({"success": False, "message": "用户名和密码不能为空"})
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"success": False, "message": "用户名或密码错误"})
    session["user_id"] = user.id
    return jsonify({
        "success": True,
        "message": "登录成功",
        "data": {"user_id": user.id, "username": user.username, "real_name": user.real_name, "role": user.role}
    })


@api.route("/logout", methods=["POST"])
def api_logout():
    session.pop("user_id", None)
    return jsonify({"success": True, "message": "已退出登录"})


@api.route("/user/info", methods=["GET"])
@login_required
def user_info():
    user = User.query.get(session["user_id"])
    return jsonify({
        "success": True,
        "data": {"user_id": user.id, "username": user.username, "real_name": user.real_name, "role": user.role}
    })


# ---------- API：商品（接口测试常用）----------
@api.route("/products", methods=["GET"])
@login_required
def product_list():
    category = request.args.get("category")
    q = Product.query
    if category:
        q = q.filter_by(category=category)
    products = q.order_by(Product.id).all()
    return jsonify({
        "success": True,
        "data": [
            {"id": p.id, "code": p.code, "name": p.name, "category": p.category, "unit": p.unit, "price": float(p.price), "stock": p.stock}
            for p in products
        ]
    })


@api.route("/products/<int:pid>", methods=["GET"])
@login_required
def product_detail(pid):
    p = Product.query.get(pid)
    if not p:
        return jsonify({"success": False, "message": "商品不存在"}), 404
    return jsonify({
        "success": True,
        "data": {"id": p.id, "code": p.code, "name": p.name, "category": p.category, "unit": p.unit, "price": float(p.price), "stock": p.stock}
    })


@api.route("/products", methods=["POST"])
@login_required
def product_create():
    data = request.get_json() or {}
    code = (data.get("code") or "").strip()
    name = (data.get("name") or "").strip()
    if not code or not name:
        return jsonify({"success": False, "message": "商品编码和名称不能为空"})
    if Product.query.filter_by(code=code).first():
        return jsonify({"success": False, "message": "商品编码已存在"})
    price = data.get("price")
    try:
        price = Decimal(str(price)) if price is not None else Decimal("0")
    except Exception:
        return jsonify({"success": False, "message": "单价格式错误"})
    if price < 0:
        return jsonify({"success": False, "message": "单价不能为负数"})
    p = Product(
        code=code,
        name=name,
        category=(data.get("category") or "").strip() or None,
        unit=(data.get("unit") or "个").strip(),
        price=price,
        stock=int(data.get("stock") or 0)
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({"success": True, "message": "创建成功", "data": {"id": p.id}})


# ---------- API：订单（接口测试、性能测试）----------
@api.route("/orders", methods=["GET"])
@login_required
def order_list():
    status = request.args.get("status")
    q = Order.query.order_by(Order.id.desc())
    if status:
        q = q.filter_by(status=status)
    orders = q.limit(100).all()
    return jsonify({
        "success": True,
        "data": [
            {
                "id": o.id, "order_no": o.order_no, "customer_name": o.customer_name,
                "total_amount": float(o.total_amount), "status": o.status,
                "created_at": o.created_at.isoformat() if o.created_at else None
            }
            for o in orders
        ]
    })


@api.route("/orders", methods=["POST"])
@login_required
def order_create():
    data = request.get_json() or {}
    customer_name = (data.get("customer_name") or "").strip()
    items = data.get("items") or []
    if not customer_name:
        return jsonify({"success": False, "message": "客户名称不能为空"})
    if not items:
        return jsonify({"success": False, "message": "订单明细不能为空"})
    order_no = "SO" + datetime.now().strftime("%Y%m%d%H%M%S")
    total = Decimal("0")
    order = Order(order_no=order_no, customer_name=customer_name, user_id=session["user_id"])
    db.session.add(order)
    db.session.flush()
    for it in items:
        pid = it.get("product_id")
        qty = int(it.get("quantity") or 0)
        if not pid or qty <= 0:
            db.session.rollback()
            return jsonify({"success": False, "message": "商品或数量无效"})
        product = Product.query.get(pid)
        if not product:
            db.session.rollback()
            return jsonify({"success": False, "message": f"商品 id={pid} 不存在"})
        if product.stock < qty:
            db.session.rollback()
            return jsonify({"success": False, "message": f"商品 {product.name} 库存不足"})
        unit_price = product.price
        amount = calculate_order_amount(qty, unit_price)
        total += amount
        db.session.add(OrderItem(order_id=order.id, product_id=pid, product_name=product.name, quantity=qty, unit_price=unit_price, amount=amount))
    order.total_amount = total
    db.session.commit()
    return jsonify({"success": True, "message": "创建成功", "data": {"id": order.id, "order_no": order.order_no}})


# ---------- 页面：登录、首页、商品、订单（功能测试 + 自动化测试）----------
@pages.route("/")
def index():
    if session.get("user_id"):
        return redirect(url_for("pages.dashboard"))
    return redirect(url_for("pages.login_page"))


@pages.route("/login", methods=["GET", "POST"])
def login_page():
    error = None
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
        if not username or not password:
            error = "用户名和密码不能为空"
        else:
            user = User.query.filter_by(username=username).first()
            if not user or not user.check_password(password):
                error = "用户名或密码错误"
            else:
                session["user_id"] = user.id
                return redirect(url_for("pages.dashboard"))
    return render_template("login.html", error=error)


@pages.route("/static/<path:path>")
def static_file(path):
    return send_from_directory(current_app.static_folder, path)


@pages.route("/dashboard")
@login_required
def dashboard():
    return send_from_directory(current_app.static_folder, "dashboard.html")


@pages.route("/products")
@login_required
def product_page():
    return send_from_directory(current_app.static_folder, "products.html")


@pages.route("/orders")
@login_required
def order_page():
    return send_from_directory(current_app.static_folder, "orders.html")


# 兼容：带 cookie 的页面登录后，前端 JS 可调 /api/*；登出
@pages.route("/logout")
def page_logout():
    session.pop("user_id", None)
    return redirect(url_for("pages.login_page"))
