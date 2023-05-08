from flask_sqlalchemy.session import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from app.data_layer import db
from app.data_layer.model_interface import ModelInterface


class Lection(db.Model, ModelInterface):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    video_url = db.Column(db.Text)
    course_id = mapped_column(ForeignKey("course.id"), nullable=False)
    course = relationship("Course", back_populates="lections")
    lection_users = relationship('UserLection', backref='lection', cascade="all, delete-orphan")

    @classmethod
    def get_all_with_filter(cls, filter):
        known_properties = [prop.key for prop in cls.__table__.columns]
        filter_kwargs = {key: value for key, value in filter.items() if key in known_properties}
        return Lection.query.filter_by(**filter_kwargs).all()

    @staticmethod
    def get_by_id(id):
        lection = Lection.query.get(id)
        if lection is None:
            return None
        return lection

    @staticmethod
    def create(data):
        if data.get('title') is None:
            raise RuntimeError('Title must be provided')
        if data.get('description') is None:
            raise RuntimeError('Description must be provided')
        if data.get('text') is None:
            raise RuntimeError('Text must be provided')
        if data.get('course_id') is None:
            raise RuntimeError('Course id must be provided')
        lection = Lection(
            title=data.get('title'), description=data.get('description'), text=data.get('text'),
            video_url=data.get('video_url'), course_id=data.get('course_id')
        )
        session = Session(db)
        session.add(lection)
        session.commit()
        return Lection.query.get(lection.id)

    @staticmethod
    def create_many(lections):
        new_lections = []
        session = Session(db)
        for lection in lections:
            new_lection = Lection(
            title=lection.get('title'), description=lection.get('description'), text=lection.get('text'),
            video_url=lection.get('video_url'), course_id=lection.get('course_id')
            )
            new_lections.append(new_lection)
            session.add(new_lection)

        session.commit()
        return [new_lection.id for new_lection in new_lections]

    @staticmethod
    def update_by_id(id, data):
        session = Session(db)
        lection = session.query(Lection).get(id)
        if lection is None:
            return None
        if data.get('title') is not None:
            lection.title = data.get('title')
        if data.get('description') is not None:
            lection.description = data.get('description')
        if data.get('text') is not None:
            lection.text = data.get('text')
        if 'video_url' in data.keys():
            lection.video_url = data.get('video_url')
        if data.get('course_id') is not None:
            lection.course_id = data.get('course_id')

        session.commit()
        return Lection.query.get(lection.id)

    @staticmethod
    def delete_by_id(id):
        session = Session(db)
        lection = session.query(Lection).get(id)
        if lection is None:
            return None
        session.delete(lection)
        session.commit()

        return lection
