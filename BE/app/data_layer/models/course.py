from flask_sqlalchemy.session import Session
from sqlalchemy.orm import relationship

from app.data_layer import db
from app.data_layer.model_interface import ModelInterface


class Course(db.Model, ModelInterface):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    lections = relationship('Lection', back_populates='course', cascade="all, delete-orphan")
    tests = relationship('Test', back_populates='course', cascade="all, delete-orphan")
    course_users = relationship('UserCourse', backref='course', cascade="all, delete-orphan")

    @classmethod
    def get_all_with_filter(cls, filter):
        known_properties = [prop.key for prop in cls.__table__.columns]
        filter_kwargs = {key: value for key, value in filter.items() if key in known_properties}
        return Course.query.filter_by(**filter_kwargs).all()

    @staticmethod
    def get_by_id(id):
        course = Course.query.get(id)
        if course is None:
            return None
        return course

    @staticmethod
    def create(data):
        if data.get('title') is None:
            raise RuntimeError('Title must be provided')
        if data.get('description') is None:
            raise RuntimeError('Description must be provided')
        course = Course(title=data.get('title'), description=data.get('description'))
        session = Session(db)
        session.add(course)
        session.commit()
        return Course.query.get(course.id)

    @staticmethod
    def create_many(courses):
        new_courses = []
        session = Session(db)
        for course in courses:
            new_course = Course(title=course.get('title'), description=course.get('description'))
            new_courses.append(new_course)
            session.add(new_course)

        session.commit()
        return [new_course.id for new_course in new_courses]

    @staticmethod
    def update_by_id(id, data):
        session = Session(db)
        course = session.query(Course).get(id)
        if course is None:
            return None
        if data.get('title') is not None:
            course.title = data.get('title')
        if data.get('description') is not None:
            course.description = data.get('description')

        session.commit()
        return Course.query.get(course.id)

    @staticmethod
    def delete_by_id(id):
        session = Session(db)
        course = session.query(Course).get(id)
        if course is None:
            return None
        session.delete(course)
        session.commit()

        return course
