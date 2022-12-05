# *_*coding:utf-8 *_*
from app.utils.base import success_out_put
from flask import Blueprint, jsonify

params = Blueprint('params', __name__)


@params.route('/blog/<int:postID>')
def showBlog(postID):
    return success_out_put(jsonify({'msg': '成功', 'data': 'Blog Number %d' % postID}))


@params.route('/rev/<float:revNo>')
def revision(revNo):
    return success_out_put(jsonify({'msg': '成功', 'data': 'Revision Number %f' % revNo}))


@params.route('/path/<path:viewPath>')
def viewPath(viewPath):
    return success_out_put(jsonify({'msg': '成功', 'data': 'Revision Number %s' % viewPath}))
