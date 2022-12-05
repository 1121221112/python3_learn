# *_*coding:utf-8 *_*
from app.utils.base import success_out_put
from flask import Blueprint, jsonify, redirect, url_for, request, abort, render_template

redirects = Blueprint('redirects', __name__)


@redirects.route('/admin')
def hello_admin():
    return success_out_put(jsonify({'msg': '成功', 'data': 'Hello Admin'}))


@redirects.route('/guest/<guest>')
def hello_guest(guest):
    return success_out_put(jsonify({'msg': '成功', 'data': 'Hello %s as Guest' % guest}))


@redirects.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('redirects.hello_admin'))
    else:
        return redirect(url_for('redirects.hello_guest', guest=name))


# 错误abort demo
@redirects.route('/')
def index():
    return render_template('log_in.html')


@redirects.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('redirects.success'))
        else:
            abort(401)
    else:
        return redirect(url_for('redirects.index'))


@redirects.route('/success')
def success():
    return 'logged in successfully'
