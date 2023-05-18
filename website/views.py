from flask import Blueprint, render_template, request, flash
from . import db


views = Blueprint('views',__name__)

@views.route("/")
def menu():
    return render_template("menu.html")