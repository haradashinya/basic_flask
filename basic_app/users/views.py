from basic_app.users import bp
from basic_app.users.models import User
from basic_app import db
from flask import render_template,redirect,request,session
from rauth.service import OAuth2Service

github = OAuth2Service(
    name = "github",
    base_url='https://api.github.com/',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    client_id= '9847aabfab7716bb5f59',
    client_secret= '7a790f1ece790a4afec81ca21ade51c61a0acb7d',
)


@bp.route("login")
def login_view():
    return render_template("login.html")


@bp.route("login_github")
def login_github():
    url =  github.get_authorize_url()
    return redirect(url)

@bp.route("users/github/callback")
def authorized():
    http = "http://192.168.33.10:5000/users/github/callback"
    users = db.session.query(User).all()
    code =  request.args["code"]
    data = dict(code = code,redirect_uri = http)
    _session = github.get_auth_session(data=data)
    user_data = _session.get("user").json()
    u = User(user_data.get("name"),user_data.get("email",""))
    u.save()
    obj = db.session.query(User).filter_by(name = user_data.get("name")).first()
    session["user_id"] = obj.id
    return redirect("/videos")



@bp.route("/")
def index_view():
    return render_template("index.html")

