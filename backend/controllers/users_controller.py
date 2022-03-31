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
          return str(f"USERS_CONTROLLER ERROR: {e}")


    def update(user_data):
      user_id = BaseController.get_current_user().id
      

    def show(user_id):
        user = User.get_from_id(user_id)
        print(f"USER: {user}")
        return user

    def get():
        pass
