# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func, exc

"""
    Init DB
"""
db = SQLAlchemy()

"""
    dbCRUD helper class, provides .get_by_id(id), .create(), update(), .save()
    and .delete()
"""
class dbCRUD(object):
    __table_args__ = {'extend_existing': True}

id = db.Column(db.Integer, primary_key=True)

@classmethod
def get_by_id(cls, id):
    if any(
        (isinstance(id, basestring) and id.isdigit(),
         isinstance(id, (int, float))),
    ):
        return cls.query.get(int(id))
    return None

@classmethod
def create(cls, **kwargs):
    instance = cls(**kwargs)
    return instance.save()

def update(self, commit=True, **kwargs):
    for attr, value in kwargs.iteritems():
        setattr(self, attr, value)
    return commit and self.save() or self

def save(self, commit=True):
    db.session.add(self)
    if commit:
        db.session.commit()
    return self

def delete(self, commit=True):
    db.session.delete(self)
    return commit and db.session.commit()

"""
    Example Database Model
"""
class User(dbCRUD, db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    created_at = db.Column(db.TIMESTAMP(), server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP(), server_default=func.now(), server_onupdate=func.now())

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        print '<User id: {0} name: {1} created_at: {3}>'.format(self.id, self.name, self.created_at)

