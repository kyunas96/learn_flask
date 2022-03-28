from flask import Blueprint
from ..controllers import UsersController

users_route = Blueprint('users_route', __name__)

@users_route.get('/<id>')
def show(id):
  user = UsersController.show(id)
  return user.to_json()

@users_route.post('/')
def post():
  pass

@users_route.patch('/<userid>')
def update(userid):
  pass