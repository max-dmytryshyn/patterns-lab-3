from flask_sqlalchemy.session import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from app.data_layer import db
from app.data_layer.constants import ActivityStatus
from app.data_layer.model_interface import ModelInterface


class UserLection(db.Model, ModelInterface):
    user_id = mapped_column(ForeignKey("user.id"), primary_key=True)
    lection_id = mapped_column(ForeignKey("lection.id"), primary_key=True)
    status = db.Column(db.Enum(ActivityStatus), default=ActivityStatus.NOT_ACTIVE)

    @staticmethod
    def create(data):
        user_lection = UserLection(user_id=data.get('user_id'), lection_id=data.get('lection_id'))
        session = Session(db)
        session.add(user_lection)
        session.commit()
        return UserLection.query.filter_by(user_id=user_lection.user_id, lection_id=user_lection.lection_id).first()
