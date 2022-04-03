from .import BaseController
from ..db.models import Post, Follow
from sqlalchemy.orm import Query
from .validators import PostSchema


class PostsController(BaseController):

    def create(post_dict):
        post_dict['user_id'] = BaseController._current_user_.id
        errors = PostSchema().validate(post_dict)
        if errors:
            raise Exception(str(errors))
        return Post(post_dict).create()

    def update(post_id, post_dict):
        errors = PostSchema(only=('name', 'description')). \
            validate(post_dict, partial=True)
        if errors:
            raise Exception(errors)
        post = Post.get_from_id(post_id)
        if not post:
            raise Exception("Post does not exist")
        if post.user_id != BaseController._current_user_.id:
            raise Exception("Post does not belong to current user")
        updated_post = post.update(post_dict)
        if not updated_post:
            raise Exception("Post not updated")
        return updated_post

    def show(post_id):
        return Post.get_from_id(post_id)

    def index(offset, limit):
        user_id = BaseController._current_user_.id
        subquery = Query(Follow.followee_id). \
            filter(Follow.follower_id == user_id)
        query = Query(Post).filter(Post.user_id.in_(subquery)). \
            order_by(Post.created_at.desc()). \
            limit(limit). \
            offset(offset)

        posts = Post.query()
        return [post.to_json() for post in posts]
