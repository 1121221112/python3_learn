# -*- coding:utf-8 -*-
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema as ModelSchema
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func,
    UniqueConstraint,
)

from app import app, db
from .base import gen_id

Model = db.Model


class Host(Model):
    id = Column(Integer, primary_key=True)
    hostname = Column(String(150), unique=True, nullable=False, comment="主机名称")

    def __repr__(self):
        return self.hostname


class HostSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Host
        sqla_session = db.session

    id = fields.String(dump_only=True)
    hostname = fields.String(required=True)


db.create_all()
