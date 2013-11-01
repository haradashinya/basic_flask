#coding: utf-8
from basic_app.videos import bp
from basic_app.users.models import User
from basic_app.videos.models import Video,videotags,Tag
from basic_app import db
from flask import render_template,redirect,request,session






@bp.route("/new_video/",methods=["GET","POST"])
def new_video_view():
	if session.get("user_id") == None:
		return "Sorry,You need login!"
	return render_template("new_video.html")


@bp.route("",methods=["GET","POST"])
def hello():
	if request.method == "GET":
		vts = db.session.query(videotags).all()
		print(vts)
		Tag.hello()
		tag_name = request.args.get("tag")
		# タグが存在していると,マッチした動画しか返さないようにする。
		if tag_name:
			videos = []
			tag = db.session.query(Tag).filter_by(title = tag_name).first()
			vts = db.session.query(videotags).filter_by(tag_id = tag.id).all()
			for vt in vts:
				v = db.session.query(Video).get(vt.video_id)
				videos.append(v)

		else:
			videos = db.session.query(Video).all()



		return render_template("videos.html",videos= videos)
	elif request.method == "POST":
		default_url = "http://www.youtube.com/watch?v=hR5Pa6jxOSY"
		form = request.form
		title = request.form.get("title") or "okamurayasuyuki"
		tag_names = request.form.get("tags").split(",")
		path = request.form.get("url") or default_url

		user = db.session.query(User).get(session["user_id"])
		video = Video(title= title,path=path)
		user.videos.append(video)
		db.session.add(video)
		db.session.commit()

		for tag_name in list(set(tag_names)):
			Tag.get_or_create(tag_name)
			t = db.session.query(Tag).filter_by(title = tag_name).first()
			if t is None:
				t = Tag(tag_name)
			video.tags.append(t)
			db.session.add(t)
		db.session.commit()

		print(db.session.query(Video).all())





		return "created"

