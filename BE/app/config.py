import os
from dotenv import load_dotenv
load_dotenv()


def get_db_uri():
    engine = os.environ.get('DB_ENGINE')
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    return f"{engine}://{username}:{password}@{host}/{db_name}"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_db_uri()
