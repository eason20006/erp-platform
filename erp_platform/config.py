# -*- coding: utf-8 -*-
"""ERP 管理平台配置"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "erp.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "erp-test-competition-secret-key")


config = Config
