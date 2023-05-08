import json
from flask import request, Blueprint, Response
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.service import UserService

user_crud = Blueprint('user_crud', __name__)


@user_crud.route('/user', methods=['GET', 'POST'])
def general_users_actions():
    if request.method == 'GET':
        users = UserService.get_all_users()
        return json.dumps(users)
    else:
        try:
            data = request.json
            if data.get('name') is None:
                return Response('Name must be provided', status=400)
            if data.get('email') is None:
                return Response('Email must be provided', status=400)
            user = UserService.create_user(request.json)
            return json.dumps(user)
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
            return Response('User with this email already exists', status=400)


@user_crud.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_actions_by_id(user_id):
    if request.method == 'GET':
        user = UserService.get_user_by_id(user_id)
        if user is None:
            return Response('User not found', status=404)
        return json.dumps(user)
    if request.method == 'PUT':
        try:
            user = UserService.update_user(user_id, request.json)
            if user is None:
                return Response('User not found', status=404)
            return json.dumps(user)
        except IntegrityError as e:
            assert isinstance(e.orig, UniqueViolation)
            return Response('User with this email already exists', status=400)

    if request.method == 'DELETE':
        user = UserService.delete_user_by_id(user_id)
        if user is None:
            return Response('User not found', status=404)
        return json.dumps(user)
