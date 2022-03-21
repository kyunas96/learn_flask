from . import BaseController
from ..db.models import User


class SessionController(BaseController):
    @staticmethod
    def login(username, password):
        user = User.login_user(username, password)
        print(f"USER: {user}")
        if not user: return False

        BaseController.set_current_user(user.id)
        BaseController.set_session_token(user.session_token)
        return True
    @staticmethod
    def logout():
        user_id = BaseController.get_current_user()
        if not user_id:
            return False
        User.reset_session_token(user_id)
        BaseController.set_session_token(None)
        BaseController.set_current_user(None)
        return True
