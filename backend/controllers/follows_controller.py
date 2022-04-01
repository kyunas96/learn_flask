from lib2to3.pytree import Base
from ..db.models import Follow
from .base_controller import BaseController


class FollowsController(BaseController):
    # move create and delete to a manager class for follows
    def create(followed_user_id):
      with BaseController._current_user_.id as user_id:
        try:
          follow = Follow(user_id, followed_user_id).create()
          return follow
        except Exception as e:
          return str(e)

    # def delete(followed_user_id):
    #   with BaseController._current_user_.id as user_id:
    #     try:
          

    # def get_followers():
    #   with BaseController._current_user_.id as user_id:
    #     followers = Follow
    #     pass

    def get_followings():
      with BaseController._current_user_.id as user_id:
        pass
