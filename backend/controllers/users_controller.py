from ..db.models import User
from .base_controller import BaseController


class UsersController(BaseController):
    # will correspond to the users followed by the current user
    def create(userdata):
      for username, email, password in userdata:
        pass

    def update(userdata):
      pass

    def show(user_id):
      user = User.get_user_from_id(user_id)
      return user

