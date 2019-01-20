#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:53

from flask import Flask
from flask_login import LoginManager
from app.models.base import db

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    register_blueprint(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录'
    db.init_app(app)
    db.create_all(app=app)     # 生成数据表

    return app


def register_blueprint(app):
    from app.web.blueprint import web
    app.register_blueprint(web)

