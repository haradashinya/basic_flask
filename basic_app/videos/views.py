#coding: utf-8
from basic_app.videos import bp
from basic_app.users.models import User
from basic_app.videos.models import Video
from basic_app import db
from flask import render_template,redirect,request,session





# @bp.route("v")
# def hello():
# 	return "llflfll"

@bp.route("/new_video",methods=["GET","POST"])
def new_video_view():
	if session.get("user_id") == None:
		return "Sorry,You need login!"
	return render_template("new_video.html")


@bp.route("",methods=["GET","POST"])
def hello():
	if request.method == "GET":
		return "show all videos"
	elif request.method == "POST":
		form = request.form
		title = request.form.get("title")
		tags = request.form.get("tags","python").split(",")
		path = request.form.get("url")


		user = db.session.query(User).get(session["user_id"])
		video = Video(title,path)
		user.videos.append(video)
		db.session.add(video)
		db.session.commit()

		return "created"

