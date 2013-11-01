from flask import Blueprint
bp = Blueprint("videos",__name__,template_folder="templates")
from basic_app.videos import views