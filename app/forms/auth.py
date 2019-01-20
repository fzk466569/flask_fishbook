#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:11

from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError
from app.models.user import UserModel


class RegisterForm(Form):
    email = StringField(validators=(DataRequired(), Length(6, 20), Email('邮箱错误')))
    nickname = StringField(validators=(DataRequired(), Length(min=1, max=30, message='昵称非法')))
    password = PasswordField(validators=(DataRequired('密码不能为空'), Length(6, 30)))

    def validate_email(self, field):
        if UserModel.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if UserModel.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')


class LoginForm(Form):
    email = StringField(validators=(DataRequired(), Length(6, 20), Email('邮箱错误')))
    password = PasswordField(validators=(DataRequired('密码不能为空'), Length(6, 30)))
