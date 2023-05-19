from flask import Blueprint, render_template, request, flash
from . import db
from flask_login import login_required, current_user
from .models import User


views = Blueprint('views',__name__)

# routing to the menu page 
@views.route("/")
def menu():
    return render_template("menu.html")