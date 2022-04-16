from flask import Blueprint, jsonify, request
from controllers import UsersController
from . import user_show_route

users_route = Blueprint('users_route', __name__)


# @users_route.get('/<id>')
# def show(id):
#     user = UsersController.show(id)
#     if not user:
#         return jsonify({'error': "User not found"}), 400
#     return "user"
#     # return user.to_json(), 200



@users_route.post('/')
@users_route.post('')
def post():
    try:
        user_dict = request.form.to_dict()
        user = UsersController.create(user_dict)
        return user.to_json(), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@users_route.patch('/<userid>')
def update(userid):
    try:
        user_dict = request.form.to_dict()
        updated_user = UsersController.update(userid, user_dict)
        return updated_user.to_json(), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
