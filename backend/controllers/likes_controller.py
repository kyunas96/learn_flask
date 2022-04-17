from .base_controller import BaseController
from db.models import Like, Post
from .validators import LikeSchema
from sqlalchemy.orm import Query


like_validator = LikeSchema()

class LikesController(BaseController):

  def create(like_dict):
    like_dict['user_id'] = BaseController._current_user_.id
    errors = like_validator.validate(like_dict)
    if errors:
      raise Exception(errors)
    return Like(like_dict).create()
    

  def delete(like_dict):
    like_dict['user_id'] = BaseController._current_user_.id
    errors = like_validator.validate(like_dict)
    if errors:
      raise Exception(errors)
    like = Like.get_one_by(like_dict)
    if like is None:
      raise Exception("Like does not exist")
    return like.delete()

  def get_liked_posts(user_id):
    subquery = Query(Like.post_id).filter_by(Like.user_id == user_id)
    query = Query(Post).filter_by(Post.id.in_(subquery))

    posts = Post.query(query)