# -*- coding: utf-8 -*-
"""
ERP 业务逻辑模块 - 供「单元测试」任务使用。
选手需根据赛题要求对本模块中的函数进行单元测试（等价类、边界值、断言、参数化等）。
"""
from decimal import Decimal


def calculate_order_amount(quantity: int, unit_price: (int, float, Decimal)) -> Decimal:
    """
    计算订单行金额：数量 × 单价。
    :param quantity: 数量，正整数
    :param unit_price: 单价，非负数
    :return: 金额，保留两位小数
    """
    if quantity is None or unit_price is None:
        raise ValueError("数量和单价不能为空")
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("数量必须为非负整数")
    price = Decimal(str(unit_price))
    if price < 0:
        raise ValueError("单价不能为负数")
    return (Decimal(quantity) * price).quantize(Decimal("0.01"))


def discount_rate(amount: (int, float), level: str) -> float:
    """
    根据订单金额与客户等级计算折扣率。
    :param amount: 订单金额
    :param level: 客户等级 "normal" | "silver" | "gold" | "vip"
    :return: 折扣率 0~1，如 0.95 表示 95 折
    """
    if amount is None or level is None:
        raise ValueError("金额和等级不能为空")
    amt = float(amount)
    if amt < 0:
        raise ValueError("金额不能为负数")
    levels = {"normal": 1.0, "silver": 0.98, "gold": 0.95, "vip": 0.90}
    if level not in levels:
        raise ValueError("无效的客户等级")
    return levels[level]


def after_discount_amount(amount: (int, float), level: str) -> float:
    """订单金额 × 折扣率，保留两位小数。"""
    rate = discount_rate(amount, level)
    return round(float(amount) * rate, 2)


def stock_warning_threshold(category: str) -> int:
    """
    按商品类别返回库存预警阈值。
    :param category: 类别
    :return: 阈值数量
    """
    if not category or not isinstance(category, str):
        raise ValueError("类别必须为非空字符串")
    category = category.strip()
    thresholds = {"电子产品": 10, "文具": 50, "日用品": 30}
    return thresholds.get(category, 20)


def is_stock_low(current_stock: int, category: str) -> bool:
    """当前库存是否低于该类别预警阈值。"""
    return current_stock < stock_warning_threshold(category)
