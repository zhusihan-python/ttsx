#coding=utf8
from flask import render_template, url_for, redirect, flash

from app.model import User
from . import main
from .forms import LoginForm, RegistrationForm
from flask_login import login_required, login_user, logout_user
import sys
from app import db

reload(sys)
sys.setdefaultencoding('utf-8')



@main.route('/')
def home():
    return render_template('home.html', name='天天生鲜')

@main.route('/account')
@login_required
def user_account():
    return '欢迎登录'

@main.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('main.user_account') or url_for('main.home'))
        flash('无效的用户名或密码')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录状态')
    return redirect(url_for('main.home'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('现在可以登录了.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)