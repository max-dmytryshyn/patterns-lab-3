from flask_sqlalchemy.session import Session
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from app.data_layer import db
from sqlalchemy_utils import EmailType

from app.data_layer.model_interface import ModelInterface


class User(db.Model, ModelInterface):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(EmailType, nullable=False, unique=True)
    user_courses = relationship('UserCourse', backref='user', cascade="all, delete-orphan")
    user_lections = relationship('UserLection', backref='user', cascade="all, delete-orphan")

    @classmethod
    def get_all_with_filter(cls, filter):
        known_properties = [prop.key for prop in cls.__table__.columns]
        filter_kwargs = {key: value for key, value in filter.items() if key in known_properties}
        return User.query.filter_by(**filter_kwargs).all()

    @staticmethod
    def get_by_id(id):
        user = User.query.get(id)
        if user is None:
            return None
        return user

    @staticmethod
    def create(data):
        if data.get('name') is None:
            raise RuntimeError('Name must be provided')
        if data.get('email') is None:
            raise RuntimeError('Email must be provided')
        user = User(name=data.get('name'), email=data.get('email'))
        session = Session(db)
        session.add(user)
        session.commit()
        return User.query.get(user.id)

    @staticmethod
    def create_many(users):
        new_users = []
        session = Session(db)
        for user in users:
            new_user = User(name=user.get('name'), email=user.get('email'))
            new_users.append(new_user)
            session.add(new_user)

        session.commit()
        return [new_user.id for new_user in new_users]

    @staticmethod
    def update_by_id(id, data):
        session = Session(db)
        user = session.query(User).get(id)
        if user is None:
            return None
        if data.get('name') is not None:
            user.name = data.get('name')
        if data.get('email') is not None:
            user.email = data.get('name')

        session.commit()
        return User.query.get(user.id)

    @staticmethod
    def delete_by_id(id):
        session = Session(db)
        user = session.query(User).get(id)
        if user is None:
            return None
        session.delete(user)
        session.commit()

        return user
