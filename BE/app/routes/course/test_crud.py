import json
from flask import request, Blueprint, Response
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError

from app.service import TestService

test_crud = Blueprint('test_crud', __name__)


@test_crud.route('/test', methods=['GET', 'POST'])
def general_tests_actions():
    if request.method == 'GET':
        tests = TestService.get_all_tests()
        return json.dumps(tests)
    else:
        data = request.json
        if data.get('title') is None:
            return Response('Title must be provided', status=400)
        if data.get('description') is None:
            return Response('Description must be provided', status=400)
        if data.get('text') is None:
            return Response('Text must be provided', status=400)
        if data.get('course_id') is None:
            return Response('Course id must be provided', status=400)
        if data.get('description') is None:
            return Response('Description must be provided', status=400)
        try:
            test = TestService.create_test(request.json)
        except IntegrityError as e:
            assert isinstance(e.orig, ForeignKeyViolation)
            return Response('Course with provided id not found', status=400)
        return json.dumps(test)


@test_crud.route('/test/<test_id>', methods=['GET', 'PUT', 'DELETE'])
def test_actions_by_id(test_id):
    if request.method == 'GET':
        test = TestService.get_test_by_id(test_id)
        if test is None:
            return Response('test not found', status=404)
        return json.dumps(test)
    if request.method == 'PUT':
        try:
            test = TestService.update_test(test_id, request.json)
            if test is None:
                return Response('test not found', status=404)
            return json.dumps(test)
        except IntegrityError as e:
            assert isinstance(e.orig, ForeignKeyViolation)
            return Response('Course with provided id not found', status=400)

    if request.method == 'DELETE':
        test = TestService.delete_test_by_id(test_id)
        if test is None:
            return Response('test not found', status=404)
        return json.dumps(test)
