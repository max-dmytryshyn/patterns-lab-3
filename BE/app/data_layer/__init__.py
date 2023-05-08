from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()

from app.data_layer.models import *
