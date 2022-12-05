#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import logging
import os
import sys

import logzero

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from logzero import logger

# from .utils.FTPUtils import FTPUtils
from .utils.base import get_err_msg, request_data

app = Flask(__name__)
env = os.getenv("ENV", "3")
# 配置文件
cfg = f"../config/etc/server_config-{env}.ini"
print(cfg)
app.config.from_pyfile(cfg)

# CORS
# CORS(app)

# DB
db = SQLAlchemy(app)
# RESTFul
api = Api(app)
# Cache
# config = {
#     "DEBUG": True,  # some Flask specific configs
#     "CACHE_TYPE": "RedisCache",  # Flask-Caching related configs
#     "CACHE_REDIS_HOST": app.config.get('REDIS_SERVER_IP'),
#     "CACHE_REDIS_PORT": app.config.get('REDIS_SERVER_PORT'),
#     "CACHE_REDIS_PASSWORD": app.config.get('REDIS_SERVER_PASSWD'),
#     "CACHE_REDIS_DB": app.config.get('REDIS_CACHE_DB', 4),
# }
# app.config.from_mapping(config)

# my_cache = Cache(app)
# Keycloak
# app.config.update({
#     'SECRET_KEY': '36b85e32-8bc5-4b57-8a27-03feb47b0053',
#     'TESTING': True,
#     'DEBUG': True,
#     'OIDC_CLIENT_SECRETS': os.path.dirname(__file__) + "/../../config/etc/ctdyServer/" + f'client_secrets-{env}.json',
#     'OIDC_ID_TOKEN_COOKIE_SECURE': False,
#     'OIDC_REQUIRE_VERIFIED_EMAIL': False,
#     'OIDC_USER_INFO_ENABLED': True,
#     'OIDC_OPENID_REALM': 'test',
#     'OIDC_SCOPES': ['openid', 'email', 'profile'],
#     'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
# })
#
# oidc = OpenIDConnect(app)

# log
log_fp = "/var/log/flask.access"
log_run = "/var/log/flask.run"
if sys.platform.lower().find("win") >= 0:
    log_fp = r"C:\data\flask.access"
    log_run = r"C:\data\flask.run"
logging.basicConfig(
    level=logging.INFO,  # 控制台打印的日志级别
    # filename=log_fp,  # 将日志写入log_new.log文件中
    # filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s", )

logzero.logfile(log_run, maxBytes=int(10e8), backupCount=5, disableStderrLogger=True)
app.logger = logger
#
# app.config.setdefault("AUTH_ROLE_PUBLIC", "Public")
# app.url_map.strict_slashes = False


MSG_DATA_NOT_FOUND = "暂无数据。"
MSG_DATA_ADDED = "新增成功。"
MSG_DATA_EDITED = "更新成功。"
MSG_DATA_GET = "查询成功。"
MSG_DELETE_SUCCESS = "删除成功。"
MSG_LESS_DATA = "缺失必要参数。"
MSG_DATA_DUPLICATE = "数据已经存在。"
HTTP = "http://"
DATE_FORMAT_D_HM = "%Y-%m-%d %H:%M"
ROOT_PATH_ISO_PATH = "/opt/flask_learning/"
if sys.platform.lower().startswith("win"):
    ROOT_PATH_ISO_PATH = "E:\\tmp\\opt\\integration_iso_files\\"

# ！！！必须放到下面，不然会有循环引用的问题 ！！ ！
from app.bp.host import bp_host
from app.learn_bps.params import params
from app.learn_bps.redirects import redirects
from app.learn_bps.cookies import cookies
from app.learn_bps.sessions import sessions
from app.learn_bps.flash_api import flash_api


# 注册蓝图
app.register_blueprint(bp_host, url_prefix="/host-manager")

# 学习蓝图接口
app.register_blueprint(params, url_prefix="/params")
app.register_blueprint(redirects, url_prefix="/redirects")
app.register_blueprint(cookies, url_prefix="/cookies")
app.register_blueprint(sessions, url_prefix="/sessions")
app.register_blueprint(flash_api, url_prefix="/flash_api")
