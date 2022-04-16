from db.models import User, Post
from .base_controller import BaseController
from .validators import UserSchema

user_validator = UserSchema()


class UsersController(BaseController):
    def create(user_dict):
        errors = user_validator.validate(user_dict)
        if errors:
            raise Exception(errors)
        return User(user_dict).create()

    def update(user_id, user_dict):
        errors = user_validator.validate(user_dict, partial=("id"))
        if errors:
            raise Exception(errors)
        current_user = BaseController._current_user_
        if user_id == current_user.id:
            user = current_user.update(user_dict)
            if not user:
                raise Exception("User not updated")
            BaseController.set_current_user(user)
            return user

    def show(user_id):
        user = User.query().filter(User.id == user_id).scalar()
        return user

    def users_posts(userid, pagenumber):
        LIMIT = 25
        offset = (pagenumber - 1) * LIMIT
        posts = Post.query().filter(Post.user_id == userid). \
            offset(offset). \
            limit(LIMIT). \
            all()
        return posts


