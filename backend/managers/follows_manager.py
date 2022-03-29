from .base_manager import BaseManager
from ..db.models import Follow

class FollowsManager(BaseManager):

  def create_follow(self, user_id, following_id):
    with self.session as session:
      follow = Follow(user_id, following_id)
      session.add(follow)
      session.commit()
      session.close()

  def delete_follow(self, user_id, followee_id):
    with self.session as session:
      session.query(Follow) \
        .filter(Follow.follower_id == user_id) \
        .filter(Follow.followee_id == followee_id) \
        .delete()
      session.commit()
      session.close()

  def get_followers(self, user_id):
    with self.session as session:
      followers = session.query(Follow) \
        .filter(Follow.followee_id == user_id) \
        .all()
      return [follow.to_json() for follow in followers]
      
      

  def get_followings(self, user_id):
    with self.session as session:
      followings = session.query(Follow) \
        .filter(Follow.follower_id == user_id) \
        .all()
      return [follow.to_json() for follow in followings]