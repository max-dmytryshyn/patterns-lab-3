import json
from flask import request, Blueprint, Response
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.service import CourseService

course_crud = Blueprint('course_crud', __name__)


@course_crud.route('/course', methods=['GET', 'POST'])
def general_courses_actions():
    if request.method == 'GET':
        courses = CourseService.get_all_courses()
        return json.dumps(courses)
    else:
        data = request.json
        if data.get('title') is None:
            return Response('Title must be provided', status=400)
        if data.get('description') is None:
            return Response('Description must be provided', status=400)
        course = CourseService.create_course(request.json)
        return json.dumps(course)


@course_crud.route('/course/<course_id>', methods=['GET', 'PUT', 'DELETE'])
def course_actions_by_id(course_id):
    if request.method == 'GET':
        course = CourseService.get_course_by_id(course_id)
        if course is None:
            return Response('Course not found', status=404)
        return json.dumps(course)
    if request.method == 'PUT':
        course = CourseService.update_course(course_id, request.json)
        if course is None:
            return Response('Course not found', status=404)
        return json.dumps(course)

    if request.method == 'DELETE':
        course = CourseService.delete_course_by_id(course_id)
        if course is None:
            return Response('Course not found', status=404)
        return json.dumps(course)
