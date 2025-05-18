from flask import Flask
from app.models import db
from app.routes import main_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app