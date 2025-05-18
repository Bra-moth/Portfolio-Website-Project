from app import create_app
import os
from flask import Flask
from app.models import db
from app.routes import main_bp
from app.config import Config



app = create_app()

if __name__ == "__main__":
    app.run()

# ...existing code...
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///service_requests.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# ...existing code...