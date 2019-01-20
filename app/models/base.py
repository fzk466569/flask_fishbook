#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:44

from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

from sqlalchemy import SmallInteger, Column


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:

            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


class BaseModel(db.Model):
    status = Column(SmallInteger, default=0)
    __abstract__ = True

    def set_attrs(self, attrs: dict):
        for k, v in attrs.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)
