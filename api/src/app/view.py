import json

from flask import request

from app import db, app
from app.utils.base import request_data, success_out_put, error_out_put


@app.before_request
def before_request_info():
    if dict(request_data(request)):
        app.logger.info(f" kws =  {json.dumps(dict(request_data(request)))}")
