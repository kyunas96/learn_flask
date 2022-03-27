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
    with cls._session_token_ as session_token:
      session_token = session_token or request.cookies['session_token']
    return session_token

  @classmethod
  def get_current_user(cls):
    with cls._session_token_ as session_token:
        if session_token is not None:
          user = User.get_from_session_token(session_token)
          if user is not None:
            cls._current_user_ = user
            return user
          else:
            return None

  @classmethod
  def set_current_user(cls, current_user):
    cls._current_user_ = current_user
  
  @classmethod
  def set_session_token(cls, session_token):
    cls._session_token_ = session_token
        

  
