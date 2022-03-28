from ..db.models import User
from .base_controller import BaseController


class UsersController(BaseController):
    # will correspond to the users followed by the current user
    def following():
      pass

    def followers():
      pass
      
    def create(data):
      for username, email, password in data:
        pass

    def update(data):
      pass

    def show(user_id):
      user = User.get_user_from_id(user_id)
      return user

