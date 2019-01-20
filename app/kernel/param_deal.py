#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  11:57

import re

import requests
from flask import current_app


class FishBook(object):

    def __init__(self):
        self.isbn_url = 'http://t.yushu.im/v2/book/isbn/{isbn}'
        self.keyword_url = 'http://t.yushu.im/v2/book/search?q={q}&start={start}&count={count}'
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        if data:
            self.books.append(data)
            self.total = 1

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def __search_data(self, query, start, count):
        if re.match('\d', query):
            url = self.isbn_url.format(isbn=query)
            data = requests.get(url).json()
            self.__fill_single(data=data)
        else:
            url = self.keyword_url.format(q=query, start=start, count=count)
            data = requests.get(url).json()
            self.__fill_collection(data)

    def search_data(self, query, page=1):
        per_page = current_app.config['PER_PAGE']
        start = per_page * (page - 1)
        self.__search_data(query=query, start=start, count=per_page)

    @property
    def first(self):
        return self.books[0] if self.total > 0 else None


if __name__ == '__main__':
    fb = FishBook()
    # fb.search_data('红楼梦')
    print(fb.__dict__)
