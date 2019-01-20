#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:16

from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, DECIMAL, Date, DateTime


class BookModel(BaseModel):

    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(50), default='未名')
    price = Column(DECIMAL)
    pubdate = Column(Date)
    isbn = Column(String(50), nullable=False, unique=True)
    pages = Column(Integer)
    summary = Column(String(1000))
    image = Column(String(100))
    binding = Column(String(20))
    publisher = Column(String(50))

