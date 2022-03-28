from lib2to3.pytree import Base
from .import BaseController
from ..db.models import Post

class PostsController(BaseController):


  @staticmethod
  def get_post(post_id):
    return BaseController.get_session_token()

  @staticmethod
  def get_posts_for_user(user_id):
    pass

  @staticmethod
  def create_post(post):
    pass

  @staticmethod
  def update_post(post_id, post_options):
    pass

  @staticmethod
  def delete_post(post_id):
    pass
