from flask_sqlalchemy.session import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from app.data_layer import db
from app.data_layer.constants import TestType

from app.data_layer.model_interface import ModelInterface


class Test(db.Model, ModelInterface):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(TestType), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    course_id = mapped_column(ForeignKey("course.id"), nullable=False)
    course = relationship("Course", back_populates="tests")
    questions = relationship('Question', back_populates='test', cascade="all, delete-orphan")
    test_users = relationship('UserTest', backref='test', cascade="all, delete-orphan")

    @classmethod
    def get_all_with_filter(cls, filter):
        known_properties = [prop.key for prop in cls.__table__.columns]
        filter_kwargs = {key: value for key, value in filter.items() if key in known_properties}
        return Test.query.filter_by(**filter_kwargs).all()

    @staticmethod
    def get_by_id(id):
        test = Test.query.get(id)
        if test is None:
            return None
        return test

    @staticmethod
    def create(data):
        if data.get('type') is None:
            raise RuntimeError('Type must be provided')
        if data.get('title') is None:
            raise RuntimeError('Title must be provided')
        if data.get('description') is None:
            raise RuntimeError('Description must be provided')
        if data.get('course_id') is None:
            raise RuntimeError('Course id must be provided')
        test = Test(
            title=data.get('title'), description=data.get('description'), type=data.get('type'),
            course_id=data.get('course_id')
        )
        session = Session(db)
        session.add(test)
        session.commit()
        return test.query.get(test.id)

    @staticmethod
    def create_many(tests):
        new_tests = []
        session = Session(db)
        for test in tests:
            new_test = Test(
            title=test.get('title'), description=test.get('description'), type=test.get('type'),
            course_id=test.get('course_id')
            )
            new_tests.append(new_test)
            session.add(new_test)

        session.commit()
        return [new_test.id for new_test in new_tests]

    @staticmethod
    def update_by_id(id, data):
        session = Session(db)
        test = session.query(Test).get(id)
        if test is None:
            return None
        if data.get('title') is not None:
            test.title = data.get('title')
        if data.get('description') is not None:
            test.description = data.get('description')

        session.commit()
        return test.query.get(test.id)

    @staticmethod
    def delete_by_id(id):
        session = Session(db)
        test = session.query(Test).get(id)
        if test is None:
            return None
        session.delete(test)
        session.commit()

        return test
