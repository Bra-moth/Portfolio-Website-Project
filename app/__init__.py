from flask import Flask, Blueprint, render_template
from app.config import Config
import os

def create_app(config_class=Config):
    # Initialize Flask application
    app = Flask(__name__, template_folder='templates')  # <-- Specify template folder
    app.config.from_object(config_class)

    # Register blueprints (if any)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app