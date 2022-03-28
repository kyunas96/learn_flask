from ..db.models import Follow
from .base_controller import BaseController


class FollowsController(BaseController):
    def create(followed_user_id):
      with BaseController._current_user_.id as user_id:
        

      pass

    def delete(followed_user_id):
      pass

    def followers(userid):
        pass

    def followings(userid):
        pass
