# *_*coding:utf-8 *_*
import uuid


COMMENT_CREATE_ON = "本条数据创建时间，一经设置，不会更改"
COMMENT_UPDATE_ON = "本条数据更新时间，每次更新数据都会更改"


def gen_id():
    return uuid.uuid4().hex
