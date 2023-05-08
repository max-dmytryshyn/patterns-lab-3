from flask_sqlalchemy.session import Session
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column

from app.data_layer import db
from app.data_layer.constants import ActivityStatus
from app.data_layer.model_interface import ModelInterface


class UserTest(db.Model, ModelInterface):
    user_id = mapped_column(ForeignKey("user.id"), primary_key=True)
    test_id = mapped_column(ForeignKey("test.id"), primary_key=True)
    status = db.Column(db.Enum(ActivityStatus), default=ActivityStatus.NOT_ACTIVE)
    answer = db.Column(JSONB)

    @staticmethod
    def create(data):
        user_test = UserTest(user_id=data.get('user_id'), test_id=data.get('test_id'))
        session = Session(db)
        session.add(user_test)
        session.commit()
        return UserTest.query.filter_by(user_id=user_test.user_id, test_id=user_test.test_id).first()
