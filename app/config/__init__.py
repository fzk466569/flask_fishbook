#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:19

if '$BM_ENV_FLAG$' == 'prod':
    from app.config.prod import *
else:
    from app.config.test import *
