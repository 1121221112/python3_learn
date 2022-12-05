# *_*coding:utf-8 *_*
# -*- coding:utf-8 -*-
import re
import json

from pre_request import pre, Rule, BaseResponse


class CustomResponse(BaseResponse):
    def make_response(
        cls, error: "ParamsValueError", fuzzy: bool = False, formatter=None
    ):
        err_para = re.findall(r"'.*' ", error.message)[0] if error.message else ""
        result = {
            "result": 20001,
            "msg": "URL缺少参数" + err_para,
        }

        from flask import make_response  # pylint: disable=import-outside-toplevel

        response = make_response(json.dumps(result))
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response


custom_resp = CustomResponse()

pre.add_response(custom_resp)

space_rule = {"name": Rule(type=str, required=True, default="", trim=True)}
