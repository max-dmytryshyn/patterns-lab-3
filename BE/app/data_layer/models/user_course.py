from flask_sqlalchemy.session import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from app.data_layer import db
from app.data_layer.constants import ActivityStatus
from app.data_layer.model_interface import ModelInterface
from app.data_layer.models.course import Course
from app.data_layer.models.user_lection import UserLection
from app.data_layer.models.user_test import UserTest


class UserCourse(db.Model, ModelInterface):
    user_id = mapped_column(ForeignKey("user.id"), primary_key=True)
    course_id = mapped_column(ForeignKey("course.id"), primary_key=True)
    status = db.Column(db.Enum(ActivityStatus), default=ActivityStatus.NOT_ACTIVE)

    @staticmethod
    def create(data):
        user_course = UserCourse(user_id=data.get('user_id'), course_id=data.get('course_id'))
        session = Session(db)
        session.add(user_course)
        course = session.query(Course).get(data.get('course_id'))
        for lection in course.lections:
            user_lection = UserLection(user_id=data.get('user_id'), lection_id=lection.id)
            session.add(user_lection)

        for test in course.tests:
            user_test = UserTest(user_id=data.get('user_id'), test_id=test.id)
            session.add(user_test)

        session.commit()
        return UserCourse.query.filter_by(user_id=user_course.user_id, course_id=user_course.course_id).first()

    @staticmethod
    def create_many(user_courses):
        new_user_courses = []
        session = Session(db)
        for user_course in user_courses:
            new_user_course = UserCourse(user_id=user_course.get('user_id'), course_id=user_course.get('course_id'))
            session.add(new_user_course)
            new_user_courses.append(new_user_course)
            course = session.query(Course).get(user_course.get('course_id'))
            for lection in course.lections:
                user_lection = UserLection(user_id=user_course.get('user_id'), lection_id=lection.id)
                session.add(user_lection)

            for test in course.tests:
                user_test = UserTest(user_id=user_course.get('user_id'), test_id=test.id)
                session.add(user_test)

        session.commit()
        return [(new_user_course.user_id, new_user_course.course_id) for new_user_course in new_user_courses]
