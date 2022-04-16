from .base_controller import BaseController
from db.models import Follow
from .validators import FollowSchema

follow_validator = FollowSchema()


class FollowsController(BaseController):
    # move create and delete to a manager class for follows
    def create(follow_dict):
        follow_dict['follower_id'] = BaseController._current_user_.id
        errors = follow_validator.validate(follow_dict)
        if errors:
            raise Exception(errors)
        if Follow.get_one_by(follow_dict) is not None:
            raise Exception("Follow already exists")
        return Follow(follow_dict).create()

    def delete(follow_dict):
        follow_dict['follower_id'] = BaseController._current_user_.id
        errors = follow_validator.validate(follow_dict)
        if errors:
            raise Exception(errors)
        follow = Follow.get_one_by(follow_dict)
        if follow is None:
            raise Exception("Follow does not exist")
        return follow.delete()

    def get_followers():
        user_id = BaseController._current_user_.id
        return Follow.get_by({'followee_id': user_id})

    def get_followings():
        user_id = BaseController._current_user_.id
        return Follow.get_by({'follower_id': user_id})
