# -*- coding:utf-8 -*-
import decimal
import hashlib
import json
import os
from datetime import date, datetime
from functools import wraps

from flask import make_response, jsonify


def resp_json_format(data=dict({}), result=0, msg="successful"):
    return {"data": data, "result": result, "msg": msg}


def request_data(request):
    try:
        return dict(
            **dict(request.json),
            **dict(request.args),
            **dict(request.form),
            **dict(request.values)
        )
    except Exception:
        return dict(request.args or request.form)


def get_err_msg(code) -> str:
    fp = os.path.dirname(__file__) + os.sep + "code.json"
    with open(fp, encoding="utf-8") as f:
        d2 = json.loads(f.read())
        try:
            return d2[str(code)[0]]["codes"][str(code)]
        except ValueError:
            return ''


# AbstractKeyedTuple  特定返回某些字段时会返回这个数据类型
# TTDModel 是自定义sqlalchemy类的父类，其中重写了to_dict()函数，控制了输出
# isinstance(obj,class)判断obj是不是class类或其子类，是返回True,不是则返回False
# 数据库返回数据list 转 dict
def db_list_to_list(data):
    if not data:
        return []
    _ = list()
    for jd in data:
        d = {}
        for k, v in jd.items():
            d[k] = v
        _.append(d)
    return _


def db_data_to_dict(data):
    if not data:
        return {}
    d = {}
    for k, v in data.items():
        d[k] = v
    return d


def md5(s: str) -> str:
    m = hashlib.md5()
    m.update(str(s).encode())
    return m.hexdigest()


def md5_file(file) -> str:
    if os.path.isfile(file):
        m = hashlib.md5()  # 创建md5对象
        with open(file, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                m.update(data)  # 更新md5对象

        return m.hexdigest()  # 返回md5对象
    return ""


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


def error_out_put(code: int, msg: str = "", data=None):
    """
    失败的response。
    :return: response对象
    @param code:response状态码
    @param msg:response消息
    @param data:数据
    """
    msg = msg or get_err_msg(code)
    resp = make_response(jsonify({"result": code, "msg": msg, "data": data}), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Method'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


def ok_data(data=None, code: int = 0, msg: str = "成功。"):
    """
    失败的response。
    :return: response对象
    @param code:response状态码
    @param msg:response消息
    @param data:数据
    """
    return jsonify({"result": code, "msg": msg, "data": data})


def success_out_put(result_msg):
    """
    成功的response。
    :param result_msg: response的内容
    :return: response对象
    """
    resp = make_response(result_msg, 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Method'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp
