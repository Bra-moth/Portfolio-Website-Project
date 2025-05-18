from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from app.models import db, ContactMessage


main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")  # Looks in `templates/`

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_msg = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_msg)
        db.session.commit()
        flash('Your message has been sent!')
        return redirect(url_for('main.contact'))
    return render_template('index.html')