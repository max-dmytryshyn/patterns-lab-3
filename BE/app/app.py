from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.data_layer import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
