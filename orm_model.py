import datetime
import sqlalchemy
from sqlalchemy import orm
from db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Logs(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'logs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    h = sqlalchemy.Column(sqlalchemy.String)
    l = sqlalchemy.Column(sqlalchemy.String)
    u = sqlalchemy.Column(sqlalchemy.String)
    t = sqlalchemy.Column(sqlalchemy.String)
    r = sqlalchemy.Column(sqlalchemy.String)
    s = sqlalchemy.Column(sqlalchemy.String)
    b = sqlalchemy.Column(sqlalchemy.String)


    def __repr__(self):
        return f'{self.h}, {self.l}, {self.u}, {self.t}, {self.r}, {self.s}, {self.b}'
