#coding: utf-8
import pytest

from basic_app import *
from basic_app.users.models import User
from basic_app.videos.models import Video
from flask.ext.sqlalchemy import SQLAlchemy

class TestUser:
    @classmethod
    def setup_class(cls):
        db_url = "mysql://root:harashin0219@localhost/orig"
        cls.app = create_app()
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = db_url
        db = SQLAlchemy(cls.app)
        cls.db = db
        User.load(cls.db)
        Video.load(cls.db)

    def test_create(self):
        User.load(self.db)
        u = User(name="test",email="harada@gmail.com")
        u.save()
        video = Video()
        u.videos.append(video)
        self.db.session.add(u)
        self.db.session.commit()
        fetched_user = self.db.session.query(User).filter_by(name ="test").first()
        assert fetched_user.name ==  "test"

    @classmethod
    def teardown_class(cls):
        fetched_user = cls.db.session.query(User).filter_by(name ="test").first()
        cls.db.session.delete(fetched_user)
        cls.db.session.commit()
        pass

