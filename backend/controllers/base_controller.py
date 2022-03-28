"""
will serve as the base controller for all the other controllers
to inherit from to get access to the current user
"""

from flask import request, session
from ..db.models import User


class BaseController:
    _current_user_ = None
    _session_token_ = None

    @classmethod
    def get_session_token(cls):
        cls._session_token_ = cls._session_token_ or request.cookies.get(
            'session_token')
        return cls._session_token_

    @classmethod
    def get_current_user(cls):
        if cls._current_user_ is not None:
            return cls._current_user_
        else:
            session_token = cls.get_session_token()
            user = User.get_from_session_token(session_token)
            return user

    @classmethod
    def set_current_user(cls, current_user):
        cls._current_user_ = current_user

    @classmethod
    def set_session_token(cls, session_token):
        cls._session_token_ = session_token
