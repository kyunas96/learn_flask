from flask import Blueprint, request, jsonify
from ..controllers import PostsController

post_route = Blueprint('post_route', __name__)

@post_route.get('/')
def index():
  return "All Images"

@post_route.get('/<id>')
def show(id):
  return f"Retrieving image {id}"

#   @images_route.route('/files')
# def files():
#   s3_resource = boto3.resource('s3',
#     aws_access_key_id=S3_KEY,
#     aws_secret_access_key=S3_SECRET)
#   my_bucket = s3_resource.Bucket(S3_BUCKET)
#   for key in my_bucket.objects.all():
#     print(key)
#   return jsonify("files")