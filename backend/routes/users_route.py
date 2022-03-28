from flask import Blueprint, jsonify
from ..controllers import UsersController

users_route = Blueprint('users_route', __name__)



@users_route.get('/<id>')
def show(id):
  user = UsersController.show(id)
  # print(dir(user.__table__.c))
  # print(user.__table__.c.keys())
  # for c in user.__table__
  #   print(c)
  return user.to_json()