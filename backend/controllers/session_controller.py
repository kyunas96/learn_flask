from . import BaseController
from ..db.models import User
from ..db.models.exceptions import UserModelError


class SessionController(BaseController):
    @staticmethod
    def login(username, password):
        user = User.get_user(username)
        if not user: 
            raise UserModelError("User does not exist")

        if not user.verify_password(password): 
            raise UserModelError("Incorrect password")

        BaseController.set_current_user(user)
        BaseController.set_session_token(user.session_token)
        print(user)
        return user
    @staticmethod
    def logout():
        user = BaseController.get_current_user()
        if not user:
            return False
        User.reset_session_token(user.id)
        BaseController.set_session_token(None)
        BaseController.set_current_user(None)
        return True
