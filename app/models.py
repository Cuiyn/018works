#coding=utf-8
from app import db

class Post(db.Model):
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime)
    subject = db.Column(db.String(64), primary_key = True)
    date = db.Column(db.String(32))

    def __repr__(self):
        return '<内容 %r>' % (self.body)

class Subject(db.Model):
    code = db.Column(db.String(16))
    subject = db.Column(db.String(64), primary_key = True)

    def __repr__(self):
        return '<科目 %r>' % (self.subject)