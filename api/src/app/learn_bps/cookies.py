# *_*coding:utf-8 *_*

from app.utils.base import success_out_put
from flask import Blueprint, request, jsonify

cookies = Blueprint('cookies', __name__)


@cookies.route("/set_cookies")
def set_cookies():
    res = success_out_put(jsonify({'msg': '成功', 'data': 'success'}))
    res.set_cookie('user', 'ping', max_age=3600)
    return res


@cookies.route("/get_cookies")
def get_cookies():
    cookie_1 = request.cookies.get('user')
    if not cookie_1:
        cookie_1 = success_out_put(jsonify({'msg': '失败', 'data': 'cookies deleted'}))
    return cookie_1


@cookies.route("/del_cookies")
def del_cookies():
    resp = success_out_put(jsonify({'msg': '成功', 'data': 'del success'}))
    resp.delete_cookie('user')
    return resp
