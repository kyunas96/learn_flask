from flask import Blueprint, request, jsonify
from ..controllers import PostsController

posts_route = Blueprint('posts_route', __name__)

@posts_route.get('/')
def index():
  return "All Images"

@posts_route.get('/<id>')
def show(id):
  res = PostsController.get_post(5)
  return f"Res: {res}"

#   @images_route.route('/files')
# def files():
#   s3_resource = boto3.resource('s3',
#     aws_access_key_id=S3_KEY,
#     aws_secret_access_key=S3_SECRET)
#   my_bucket = s3_resource.Bucket(S3_BUCKET)
#   for key in my_bucket.objects.all():
#     print(key)
#   return jsonify("files")