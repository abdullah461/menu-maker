from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    price = db.Column(db.String(50))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# table for the user(admin)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    buisness_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phoneNo = db.Column(db.Integer)
    password = db.Column(db.String(50))
    items = db.relationship('Item')

