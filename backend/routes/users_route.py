import json
from flask import Blueprint, jsonify, request
from ..controllers import UsersController

users_route = Blueprint('users_route', __name__)

@users_route.get('/<id>')
def show(id):
  print(f"ID: {id}")
  user = UsersController.show(id)
  return user.to_json()

# route for creating new uses
@users_route.post('/')
def post():
  userdata = request.form.to_dict()
  newUser = UsersController.create(userdata)
  return newUser

@users_route.patch('/<userid>')
def update(userid):
  pass