import sys
import os
import datetime


import basic_app
from basic_app import db






class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(30))





