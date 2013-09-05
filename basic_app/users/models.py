import sys
import os
import datetime


import basic_app
from basic_app import db





class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30))
    author_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(30))
    videos = db.relationship("Video")
    description = db.Column(db.String(140))





