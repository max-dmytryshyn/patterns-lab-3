from flask_sqlalchemy.session import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from app.data_layer import db
from app.data_layer.model_interface import ModelInterface


class Question(db.Model, ModelInterface):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    test_id = mapped_column(ForeignKey("test.id"), nullable=False)
    test = relationship('Test', back_populates='questions')
    answers = relationship('Answer', back_populates='question', cascade="all, delete-orphan")

    @classmethod
    def get_all_with_filter(cls, filter):
        known_properties = [prop.key for prop in cls.__table__.columns]
        filter_kwargs = {key: value for key, value in filter.items() if key in known_properties}
        return Question.query.filter_by(**filter_kwargs).all()

    @staticmethod
    def get_by_id(id):
        question = Question.query.get(id)
        if question is None:
            return None
        return question

    @staticmethod
    def create(data):
        if data.get('text') is None:
            raise RuntimeError('Text must be provided')
        if data.get('test_id') is None:
            raise RuntimeError('Test id must be provided')
        question = Question(text=data.get('text'), test_id=data.get('test_id'))
        session = Session(db)
        session.add(question)
        session.commit()
        return question.query.get(question.id)

    @staticmethod
    def create_many(questions):
        new_questions = []
        session = Session(db)
        for question in questions:
            new_question = Question(text=question.get('text'), test_id=question.get('test_id'))
            new_questions.append(new_question)
            session.add(new_question)

        session.commit()
        return [new_question.id for new_question in new_questions]

    @staticmethod
    def update_by_id(id, data):
        session = Session(db)
        question = session.query(Question).get(id)
        if question is None:
            return None
        if data.get('text') is not None:
            question.text = data.get('title')
        if data.get('description') is not None:
            question.test_id = data.get('test_id')

        session.commit()
        return question.query.get(question.id)

    @staticmethod
    def delete_by_id(id):
        session = Session(db)
        question = session.query(Question).get(id)
        if question is None:
            return None
        session.delete(question)
        session.commit()

        return question
