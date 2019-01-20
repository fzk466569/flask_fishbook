#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:43
from sqlalchemy.orm import relationship

from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, DECIMAL, Date, Boolean, Float, ForeignKey, SmallInteger


class GiftModel(BaseModel):

    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(50), nullable=False)

    def get_id(self):
        return self.id
