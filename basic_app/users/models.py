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
    videos = db.relationship("Video")

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.flush()
            db.session.rollback()
        print(self.id)

    @classmethod
    def load(cls,new_db):
        """
        change db for production
        """
        global db
        db = new_db






