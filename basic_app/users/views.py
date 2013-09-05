from basic_app.users import bp
from basic_app.users.models import User
from basic_app import db



@bp.route("/")
def hello():
    u = User(name="helll")
    print "ff"
    db.session.add(u)
    db.session.commit()
    print db.session.query(User).all()
    return "hello , world"

