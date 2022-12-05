# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from pre_request import pre

from app.model.host import Host, HostSchema
from app.utils.base import success_out_put, error_out_put
from app.rules.rules import space_rule


bp_host = Blueprint("host", __name__)
api = Api(bp_host)

parser = RequestParser(trim=True)


class HostView(Resource):
    def get(self):
        params = pre.parse(rule=space_rule)
        name = params.get("name")
        hosts = Host.query.all()
        host_info_schema = HostSchema(many=True)
        host_msg = host_info_schema.dump(hosts)

        if len(hosts) == 0:
            return error_out_put(60008)

        return success_out_put(jsonify({"result": 0, "data": host_msg}))


class H(Resource):
    def get(self):
        return "hello world"


api.add_resource(HostView, "/host")
api.add_resource(H, "/H")
