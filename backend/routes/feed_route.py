from email.policy import default
from flask import Blueprint, request, jsonify
from ..controllers import FeedController

feed_route = Blueprint('feed_route', __name__)

@feed_route.get('/', defaults={'pagenumber': 1})
@feed_route.get('/<int:pagenumber>')
def index(pagenumber):
  posts = FeedController.index(pagenumber)
  return [post.to_json() for post in posts]
  

@feed_route.get('/<int:userid>', defaults={'pagenumber': 1})
@feed_route.get('/<int:userid>/<int:pagenumber>')
def get_users_feed(userid, pagenumber):
  posts = FeedController.get_users_feed(userid, pagenumber)
  return [post.to_json() for post in posts]
