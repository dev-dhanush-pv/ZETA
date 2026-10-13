from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    flask_app = Flask(__name__)

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['Secret_Key'] = Config.SECRET_KEY

    db.init_app(flask_app)

    from app.models import models
    from app.routes import routes

    return flask_app