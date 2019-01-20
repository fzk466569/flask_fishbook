from flask import request
from threading import Timer
from app.web.blueprint import web
from flask_login import login_required, current_user
from flask.views import MethodView
from flask import render_template, url_for, current_app, flash
from app.models.gift import GiftModel
from app import db


@web.route('/my/gifts')
# @login_required
def my_gifts():
    return 'ssssssss'


class GiftView(MethodView):
    def __init__(self):
        super(GiftView, self).__init__()
        self.isbn = ''

    def get(self, isbn):
        self.isbn = isbn
        return self.isbn

    def post(self, isbn):
        self.isbn = 'post' + isbn
        return self.isbn


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    if current_user.can_save_to_list():
        with db.auto_commit():
            gift = GiftModel()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('本书已经添加至心愿清单中，请勿多次添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass


def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    web.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET', ])
    web.add_url_rule(url, view_func=view_func, methods=['POST', ])
    web.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])


register_api(GiftView, 'gift', '/users/', pk='user_id')
