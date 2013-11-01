#coding: utf-8
from basic_app.videos import bp
# from basic_app.users.models import User
from basic_app import db
from flask import render_template,redirect,request,session





# @bp.route("v")
# def hello():
# 	return "llflfll"

@bp.route("/new_video")
def new_video_view():
	return render_template("new_video.html")


@bp.route("/")
def hello():
	return "a"