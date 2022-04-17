import json
from flask import Blueprint, request, jsonify
from controllers import PostsController


posts_route = Blueprint('posts_route', __name__)


# @posts_route.get('/<int:pagenum>')
# def index(pagenum):
#     limit = 25
#     offset = (pagenum - 1) * limit
#     posts = PostsController.index(offset, limit)
    
#     return jsonify(posts), 200


@posts_route.get('/<id>')
def show(id):
    post = PostsController.show(id)
    if not post:
        return jsonify({'error': "Post not found"}), 400
    return post.to_json(), 200


@posts_route.post('/')
def post():
    try:
        post_dict = request.form.to_dict()
        post = PostsController.create(post_dict)
        return post.to_json(), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@posts_route.patch('<postid>')
def update(postid):
    try:
        post_dict = request.form.to_dict()
        post = PostsController.update(postid, post_dict)
        return post.to_json(), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


#   @images_route.route('/files')
# def files():
#   s3_resource = boto3.resource('s3',
#     aws_access_key_id=S3_KEY,
#     aws_secret_access_key=S3_SECRET)
#   my_bucket = s3_resource.Bucket(S3_BUCKET)
#   for key in my_bucket.objects.all():
#     print(key)
#   return jsonify("files")
