from flask import Blueprint, jsonify, request
from controllers import FollowsController

follows_route = Blueprint('follows_route', __name__)


@follows_route.post('/')
def post():
    try:
        follow_dict = request.form.to_dict()
        follow = FollowsController.create(follow_dict)
        return follow.to_json(), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@follows_route.delete('/')
def delete():
    try:
        follow_dict = request.form.to_dict()
        is_deleted = FollowsController.delete(follow_dict)
        return jsonify({'data': is_deleted}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@follows_route.get('/followers')
def followers():
    followers = FollowsController.get_followers()


@follows_route.get('/followings')
def followings():
    followings = FollowsController.get_followings()
    pass
