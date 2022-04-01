from functools import partial
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
  print("USER")
  print(user)
  return user.to_json()


@users_route.patch('/<userid>')
def update(userid):
  errors = user_validator.validate(request.form, partial=("id"))
  if errors:
    return jsonify(errors)
  user_dict = request.form.to_dict()
  updated_user = UsersController.update(user_dict)
  return updated_user.to_json()