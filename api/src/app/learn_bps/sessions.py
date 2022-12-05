# *_*coding:utf-8 *_*

from app import app
from flask import Blueprint, request, session, url_for, redirect

sessions = Blueprint('sessions', __name__)

@sessions.route("/")
def index():
    if 'username' in session:
        username = session['username']

        return '登录用户名是:' + username + '<br>' + \
               "<b><a href = '/sessions/logout_session'>点击这里注销</a></b>"

    return "您暂未登录， <br><a href = '/sessions/login_session'></b>" + \
           "点击这里登录</b></a>"


@sessions.route("/login_session", methods=['GET', 'Post'])
def login_session():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('sessions.index'))
    return '''
   <form action = "" method = "post">
      <p><input type="text" name="username"/></p>
      <p><input type="submit" value ="登录"/></p>
   </form>
   '''


@sessions.route('/logout_session')
def logout_session():
    session.pop('username', None)
    return redirect(url_for('sessions.index'))
