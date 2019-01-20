#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:53
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=(Length(min=1, max=30, message='q参数非法'), DataRequired()))
    page = IntegerField(validators=(NumberRange(1, 99), ), default=1)

