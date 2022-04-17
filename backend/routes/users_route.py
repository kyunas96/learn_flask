from flask import Blueprint, jsonify, request
from controllers import UsersController
from controllers.validators import UserSchema

users_route = Blueprint('users_route', __name__)


@users_route.get('/<int:userid>')
def show(userid):
    user = UsersController.show(userid)
    if not user:
        return jsonify({'error': "User not found"}), 400
    serializer = UserSchema(exclude=("password", "session_token"))
    return serializer.dumps(user), 200


@users_route.post('/')
@users_route.post('')
def post():
    try:
        user_dict = request.form.to_dict()
        user = UsersController.create(user_dict)
        serializer = UserSchema(exclude=("password",))
        return serializer.dumps(user), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@users_route.patch('/<int:userid>')
def update(userid):
    try:
        user_dict = request.form.to_dict()
        updated_user = UsersController.update(userid, user_dict)
        serializer = UserSchema(exclude=("password",))
        return serializer.dumps(updated_user), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

