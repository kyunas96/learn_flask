from .import BaseController
from db.models import Post
from .validators import PostSchema


class PostsController(BaseController):

    def index(pagenumber):
        FEED_LIMIT = 25
        followings = [user.id for user in BaseController._current_user_. \
            following]
        print(f"FOLLOWINGS: {followings}")

        posts = Post.query().filter(Post.user_id.in_(followings)). \
            order_by(Post.created_at.desc()). \
            offset(pagenumber). \
            limit(FEED_LIMIT). \
            all()
        return posts
                

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
        return Post.query().filter(Post.id == post_id).scalar()
