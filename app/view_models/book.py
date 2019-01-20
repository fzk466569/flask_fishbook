#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  10:03


class BookViewModel(object):
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = book['author']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, (self.author, self.publisher, self.price))
        return '/'.join(intros)


class BookCollection(object):
    def __init__(self, keyword):
        self.total = 0
        self.books = []
        self.keyword = keyword

    def fill(self, book, keyword):
        pass
