from flask import Blueprint, render_template, request, flash
from . import db
from flask_login import login_required, current_user
from .models import Item


views = Blueprint('views',__name__)

# routing to the menu page 
@views.route("/", methods=['GET','POST'])
@login_required
def menu():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')

        # if len(title) < 1:
        #     flash('Title is too short!', category='error')
        # elif len(description) < 3:
        #     flash('description is too short', category='error')
        # elif len(price) < 2:
        #     flash('price is too small', category='error')
        # else:
        new_item = Item(title=title, description=description, price=price, user_id=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash('New item added!', category='success')
    return render_template("menu.html",user=current_user)