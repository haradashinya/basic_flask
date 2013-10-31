import sys
import os
import datetime


import basic_app
from basic_app import db






class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(80),unique=True)
    name =db.Column(db.String(30))

    def __init__(self,name,email):
        self.name = name
        self.email = email






