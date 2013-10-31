#coding: utf-8
import pytest
from basic_app import db,create_app
from basic_app.users.models import User
# from basic_app.videos.models import Video,videotags,Tag,Vote
from flask.ext.sqlalchemy import SQLAlchemy


class TestLogin:
    @classmethod
    def setup_class(cls):
        print("init")
        db_url = "mysql://root:harashin0219@localhost/trickstar"
        cls.app = create_app()
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = db_url
        cls.db = SQLAlchemy(cls.app)

    def test_login

    @classmethod
    def teardown_class(cls):
        """
        delete test user,videos
        """
        pass

