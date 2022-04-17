from sqlalchemy.orm import Query
from .base_controller import BaseController
from db.models import Follow, Post


class FeedController(BaseController):

    def index(pagenumber):
        FEED_LIMIT = 25
        user_id = BaseController._current_user_.id
        subquery = Query(Follow.followee_id). \
            filter(Follow.follower_id == user_id)

        posts = Post.query().filter(Post.user_id.in_(subquery)). \
            order_by(Post.created_at.desc()). \
            offset(pagenumber). \
            limit(FEED_LIMIT). \
            all()
        return posts