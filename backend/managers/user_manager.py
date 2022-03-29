from .base_manager import BaseManager
from ..db.models import User
from ..db.validators import has_required_attrs, only_valid_attrs

class UsersManager(BaseManager):
  def create_user(self, userdata):
    with self.session as session:
      try: 
        user = User(userdata)
        session.add(user)
        session.commit()
        session.flush()
        return user
      except Exception as e:
        return e
      finally:
        session.close()


  def get_user_from_id(self, userdata):
    pass

  def get_user_from_session_token(self, session_token):
    pass

  def get_user_from_username(self, username):
    pass