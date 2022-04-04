from flask import Blueprint, request, jsonify
from ..controllers import FeedController

feed_route = Blueprint('feed_route', __name__)

@feed_route.get('/', defaults={'pagenumber': 1})
@feed_route.get('/<int:pagenumber>')
def index(pagenumber):
  posts = FeedController.index(pagenumber)
  return jsonify([post.to_json() for post in posts])
