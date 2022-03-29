from ..db.models import User
from .base_controller import BaseController


class UsersController(BaseController):
    # will correspond to the users followed by the current user
    def create(userdata):
      return User(userdata).create()

    def update(user_id, user_data):
      user = User.get_from_id(user_id).update(user_data)
      return user

    def show(user_id):
      user = User.get_from_id(user_id)
      print(f"USER: {user}")
      return user

    def get():
      pass