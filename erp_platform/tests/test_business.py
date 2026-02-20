# -*- coding: utf-8 -*-
"""
业务逻辑单元测试示例 - 供赛项「任务二 单元测试」参考。
选手需根据赛题要求对 business 模块进行等价类、边界值、断言、参数化等设计并编写用例。
本文件仅为示例，正式答题以赛题要求为准。
"""
import unittest
from decimal import Decimal
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from business import calculate_order_amount, discount_rate, after_discount_amount, stock_warning_threshold, is_stock_low


class TestCalculateOrderAmount(unittest.TestCase):
    """订单金额计算：数量 × 单价"""

    def test_normal(self):
        self.assertEqual(calculate_order_amount(2, 10.5), Decimal("21.00"))

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_amount(0, 100), Decimal("0.00"))

    def test_negative_quantity_raises(self):
        with self.assertRaises(ValueError):
            calculate_order_amount(-1, 10)


class TestDiscountRate(unittest.TestCase):
    """折扣率：按客户等级"""

    def test_vip(self):
        self.assertEqual(discount_rate(1000, "vip"), 0.90)

    def test_gold(self):
        self.assertEqual(discount_rate(500, "gold"), 0.95)


if __name__ == "__main__":
    unittest.main()
