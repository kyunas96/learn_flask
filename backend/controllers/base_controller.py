"""
will serve as the base controller for all the other controllers
to inherit from to get access to the current user
"""

from flask import request


class BaseController:
  _current_user_ = None
  _session_token_ = None

  def set_session_token(session_token):
    BaseController._session_token_ = session_token

  def set_current_user(current_user_id):
    BaseController._current_user_ = current_user_id

  def get_session_token():
    return BaseController._session_token_

  def get_current_user():
    return BaseController._current_user_
        

  
