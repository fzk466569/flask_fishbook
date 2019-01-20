#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  12:34

from app import create_app


app = create_app()

app.run('0.0.0.0', 5000)
