import json
from flask import Blueprint, jsonify
from controllers import UsersController

user_show_route = Blueprint('user_show_route', __name__)


@user_show_route.get('/')
def show(userid):
    user = UsersController.show(userid)
    if not user:
        return jsonify({'error': "User not found"}), 400
    return user.to_json(), 200


@user_show_route.get('/posts/<int:pagenumber>')
def users_posts(userid, pagenumber):
    posts = UsersController.users_posts(userid, pagenumber)
    return jsonify({'data': {
        'posts': [post.to_json() for post in posts]
    }}), 200
