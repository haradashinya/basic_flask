from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from basic_app import config


db = SQLAlchemy()


def load_models():
    from basic_app.users import models

load_models()


def init_extensions(app):
    db.init_app(app)


def init_views(app):
    from basic_app import users

    app.register_blueprint(users.bp, url_prefix="/users")


def create_app(config=config):
    app = Flask(__name__)
    app.config.from_object(config)

    init_extensions(app)
    init_views(app)

    return app

