import json

from flask import Blueprint, request, Response

from app.service import UserService

user_content = Blueprint('user_content', __name__)


@user_content.route('/user-content/add-to-course', methods=['POST'])
def add_user_to_course():
    data = request.json
    if data.get('user_id') is None:
        return Response('User id must be provided', status=400)
    if data.get('course_id') is None:
        return Response('Course id must be provided', status=400)
    user = UserService.add_user_to_course(data)
    return json.dumps(user)
