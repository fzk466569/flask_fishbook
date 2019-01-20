#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  14:08
from sqlalchemy.orm import relationship

from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, DECIMAL, Date, Boolean, ForeignKey


class WishModel(BaseModel):

    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    launched = Column(Boolean, default=False)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(50), nullable=False)
