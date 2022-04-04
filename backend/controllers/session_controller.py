from . import BaseController
from ..db.models import User
from ..db.models.exceptions.user_exceptions import UserModelError
from .validators import SessionSchema

session_validator = SessionSchema()


class SessionController(BaseController):
    @staticmethod
    def login(session_dict):
        errors = session_validator.validate(session_dict)
        if errors:
            raise Exception(errors)
        username = session_dict.pop('username')
        password = session_dict.pop('password')
        user = User.query().filter(User.username == username).scalar()
        if not user: raise Exception("User does not exist")
        if not user.verify_password(password): raise Exception("Incorrect password")

        BaseController.set_current_user(user)
        BaseController.set_session_token(user.session_token)
        return user


    @staticmethod
    def logout():
        user = BaseController.get_current_user()
        if not user:
            return False
        user.reset_session_token()
        BaseController.set_session_token(None)
        BaseController.set_current_user(None)
        return True
