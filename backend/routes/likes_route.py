from flask import Blueprint, make_response, request, jsonify
from ..controllers import LikesController

likes_route = Blueprint('likes_route', __name__)

@likes_route.post('/')
def create():
  
  pass

@likes_route.delete('/')
def delete():
  pass
