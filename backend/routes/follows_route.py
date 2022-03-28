from flask import Blueprint
from ..controllers import FollowsController

follows_route = Blueprint('follows_route', __name__)

@follows_route.get('/followers')
def followers():
  followers = FollowsController.get_followers()
  

@follows_route.get('/followings')
def followings():
  pass
