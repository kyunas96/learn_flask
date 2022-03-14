from flask import Blueprint, request, jsonify

images_route = Blueprint('images_route', __name__)

@images_route.get('/images')
def index():
  return "All Images"