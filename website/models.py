from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    buisness_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phoneNo = db.Column(db.Integer)
    password = db.Column(db.String(50))
    

