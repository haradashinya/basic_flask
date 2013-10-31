from basic_app import db
import datetime
from basic_app.users.models import User

videotags = db.Table("videotags",
                db.Column("tag_id",db.Integer,db.ForeignKey("tags.id")),
                db.Column("video_id",db.Integer,db.ForeignKey("videos.id")))

class Vote(db.Model):
    __tablename__ = "votes"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    voted_date = db.Column("created_date",db.DateTime,default = datetime.datetime.utcnow())
    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'))

    def __repr__(self):
        return "<Vote: {0} user_id:{1},date:{2}>".format(self.id,self.user_id,self.voted_date)



class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer,primary_key=True)
    videos = db.relationship('Video', secondary=videotags,
                             backref=db.backref("videos",lazy="dynamic"))

    title = db.Column(db.String(30),unique=True)

    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return "<Tag:{0},title:{1}>".format(self.id,self.title)


class Video(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30))
    path = db.Column(db.String(120),default = "")
    img_path = db.Column(db.String(120),default = "")
    desc = db.Column(db.String(400),default = "")
    author_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    has_voted = db.Column(db.Boolean,default = False)
    is_owner = db.Column(db.Boolean,default = False)
    votes = db.relationship("Vote")
    created_date = db.Column(db.DateTime,default = datetime.datetime.utcnow())
    updated_date = db.Column(db.DateTime,default = datetime.datetime.utcnow())

    def __init__(self,title="",path="",desc = ""):
        self.title = title
        self.path = path
        self.desc = desc
        self.created_date = datetime.datetime.utcnow()

    def vote_up(self,user_id):
        vote = Vote()
        vote.user_id = user_id
        self.votes.append(vote)
        db.session.add(vote)
        db.session.commit()


    def __repr__(self):
        return "<Video id:{0} title:{1} voted:{2}>".format(self.id,self.title,self.has_voted)



    @classmethod
    def load(cls,new_db):
        """
        change db for production
        """
        global db
        db = new_db
