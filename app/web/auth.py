from app.models.base import db
from app.models.user import UserModel
from app.web.blueprint import web
from flask import render_template, request, url_for, redirect, flash
from app.forms.auth import RegisterForm, LoginForm
from flask_login import login_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = UserModel()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user and user.checkout_password(form.password.data):
            login_user(user)    # , remember=True)     # remember 表示此cookie长久
            next_url = request.args.get('next')
            if next_url or next_url.startswith('/'):
                return redirect(next_url)
            else:
                return render_template('index.html')
        else:
            flash('账号密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
