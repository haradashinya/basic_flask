
#coding: utf-8
import pytest

from basic_app import *
from basic_app.users.models import User
from basic_app.videos.models import Video
from flask.ext.sqlalchemy import SQLAlchemy

class G: pass
g = G()


def setup_module(module):
	db_url = "mysql://root:harashin0219@localhost/orig"
	app = create_app()
	app.config["SQLALCHEMY_DATABASE_URI"] = db_url
	g.db = SQLAlchemy(app)
	Video.load(g.db)
	User.load(g.db)



def test_create():
	print(g.db)
	v = Video(title="test",path="test")
	tags = ["python","ruby","js"]
	g.db.session.add(v)
	v.add_tags(tags)
	g.db.session.commit()
	_v = g.db.session.query(Video).get(v.id)
	assert _v.title == "test"
	assert len(_v.tags) == 3



def teardown_module(module):
	videos = g.db.session.query(Video).filter_by(title="test").all()
	for video in videos:
		g.db.session.delete(video)
	g.db.session.commit()

