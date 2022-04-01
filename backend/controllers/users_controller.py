from lib2to3.pytree import Base
from ..db.models import User
from .base_controller import BaseController


class UsersController(BaseController):
    def create(userdata):
        try:
          user = User(userdata).create()
          print(f"user: {user}")
          return user
        except Exception as e:
          return str(f"USERS_CONTROLLER ERROR: {str(e)}")


    def update(user_dict):
      user_id = user_dict.pop('user_id')
      current_user = BaseController.get_current_user()
      if user_id == current_user.id:
        try:
          user = current_user.update(user_dict)
          BaseController.set_current_user(user)
          return user
        except Exception as e:
          return str(e)


    def show(user_id):
        user = User.get_from_id(user_id)
        print(f"USER: {user}")
        return user

