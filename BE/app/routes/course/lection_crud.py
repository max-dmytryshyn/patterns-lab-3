import json
from flask import request, Blueprint, Response
from psycopg2.errors import UniqueViolation, ForeignKeyViolation
from sqlalchemy.exc import IntegrityError

from app.service import LectionService

lection_crud = Blueprint('lection_crud', __name__)


@lection_crud.route('/lection', methods=['GET', 'POST'])
def general_lections_actions():
    if request.method == 'GET':
        lections = LectionService.get_all_lections()
        return json.dumps(lections)
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
            lection = LectionService.create_lection(request.json)
        except IntegrityError as e:
            assert isinstance(e.orig, ForeignKeyViolation)
            return Response('Course with provided id not found', status=400)
        return json.dumps(lection)


@lection_crud.route('/lection/<lection_id>', methods=['GET', 'PUT', 'DELETE'])
def lection_actions_by_id(lection_id):
    if request.method == 'GET':
        lection = LectionService.get_lection_by_id(lection_id)
        if lection is None:
            return Response('Lection not found', status=404)
        return json.dumps(lection)
    if request.method == 'PUT':
        try:
            lection = LectionService.update_lection(lection_id, request.json)
            if lection is None:
                return Response('Lection not found', status=404)
            return json.dumps(lection)
        except IntegrityError as e:
            assert isinstance(e.orig, ForeignKeyViolation)
            return Response('Course with provided id not found', status=400)

    if request.method == 'DELETE':
        lection = LectionService.delete_lection_by_id(lection_id)
        if lection is None:
            return Response('Lection not found', status=404)
        return json.dumps(lection)
