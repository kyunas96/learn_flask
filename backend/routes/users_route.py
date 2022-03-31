import json
from flask import Blueprint, jsonify, request
from ..controllers import UsersController
from .validators import UserSchema

users_route = Blueprint('users_route', __name__)
user_validator = UserSchema()


@users_route.get('/<id>')
def show(id):
  print(f"ID: {id}")
  user = UsersController.show(id)
  return user.to_json()

# route for creating new users
@users_route.post('/')
def post():
  errors = user_validator.validate(request.form)
  if errors:
    return jsonify(errors)
  user_dict = request.form.to_dict()
  user = UsersController.create(user_dict)
  return user


@users_route.patch('/<userid>')
def update(userid):
  pass