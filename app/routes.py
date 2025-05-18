from flask import Blueprint, render_template
import os
from app.models import db


main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")  # Looks in `templates/`