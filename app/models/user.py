#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:16

import re

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login.mixins import UserMixin
from sqlalchemy import Column, Integer, String, DECIMAL, Date, Boolean, Float

from app.models.base import BaseModel
from app import login_manager
from app.kernel.param_deal import FishBook
from app.models.gift import GiftModel
from app.models.wish import WishModel


class UserModel(BaseModel, UserMixin):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(50), nullable=False)
    phone_number = Column(String(20))
    email = Column(String(50), nullable=False, unique=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_count = Column(Integer, default=0)
    receive_count = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password=password)

    def checkout_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.id

    def can_save_to_list(self, isbn):
        if not re.match('\d', isbn):
            return False
        book = FishBook()
        book.search_data(isbn)
        if not book.first:
            return False
        gifting = GiftModel.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = WishModel.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return UserModel.query.get(int(uid))
