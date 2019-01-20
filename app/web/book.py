#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:59

import json

from flask import request, render_template, flash
from app.web.blueprint import web
from app.forms.book import SearchForm
from app.kernel.param_deal import FishBook
from app.view_models.book import BookViewModel


@web.route('/book/search')
def search():
    form = SearchForm(request.values)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        books = FishBook()
        books.search_data(query=q, page=page)
        return render_template('search_result.html', books=books)
        # result = BookViewModel.package_collection(q, fb)
    else:
        flash('参数非法、请重新输入')
        return render_template('search_result.html', books=[])


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    book = FishBook()
    book.search_data(isbn)
    result = BookViewModel(book.first)
    return render_template('book_detail.html', book=result, wishes=[], gifts=[])
