from ..db.models import User
from .base_controller import BaseController


class UsersController(BaseController):
    # will correspond to the users followed by the current user
    def index():
      pass

    def create(data):
      for username, email, password in data:
        pass

    def update(data):
      pass

    def get_valid_data(raw_data):
      raw_data