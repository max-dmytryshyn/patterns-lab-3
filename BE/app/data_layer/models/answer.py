from flask_sqlalchemy.session import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column

from app.data_layer import db
from app.data_layer.model_interface import ModelInterface


class Answer(db.Model, ModelInterface):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    is_right = db.Column(db.Boolean, nullable=False, default=False)
    question_id = mapped_column(ForeignKey("question.id"), nullable=False)
    question = relationship('Question', back_populates='answers')

    @classmethod
    def get_all_with_filter(cls, filter):
        known_properties = [prop.key for prop in cls.__table__.columns]
        filter_kwargs = {key: value for key, value in filter.items() if key in known_properties}
        return Answer.query.filter_by(**filter_kwargs).all()

    @staticmethod
    def get_by_id(id):
        answer = Answer.query.get(id)
        if answer is None:
            return None
        return answer

    @staticmethod
    def create(data):
        if data.get('text') is None:
            raise RuntimeError('Text must be provided')
        if data.get('is_right') is None:
            raise RuntimeError('is_right must be provided')
        if data.get('question_id') is None:
            raise RuntimeError('Description must be provided')
        answer = Answer(text=data.get('text'), is_right=data.get('is_right'), question_id=data.get('question_id'))
        session = Session(db)
        session.add(answer)
        session.commit()
        return answer.query.get(answer.id)

    @staticmethod
    def create_many(answers):
        new_answers = []
        session = Session(db)
        for answer in answers:
            new_answer = Answer(text=answer.get('text'), is_right=answer.get('is_right'), question_id=answer.get('question_id'))
            new_answers.append(new_answer)
            session.add(new_answer)

        session.commit()
        return [new_answer.id for new_answer in new_answers]

    @staticmethod
    def update_by_id(id, data):
        session = Session(db)
        answer = session.query(Answer).get(id)
        if answer is None:
            return None
        if data.get('text') is not None:
            answer.text = data.get('text')
        if data.get('is_right') is None:
            answer.is_right = data.get('is_right')
        if data.get('question_id') is not None:
            answer.question_id = data.get('question_id')

        session.commit()
        return answer.query.get(answer.id)

    @staticmethod
    def delete_by_id(id):
        session = Session(db)
        answer = session.query(Answer).get(id)
        if answer is None:
            return None
        session.delete(answer)
        session.commit()

        return answer
