from dotenv import load_dotenv
from flask import Flask, jsonify
import boto3
from boto.s3.key import Key
from config import S3_BUCKET, S3_KEY, S3_SECRET
from routes.images import images_route

print(S3_KEY, S3_SECRET)

s3 = boto3.client('s3', 
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET)

app = Flask(__name__)
app.register_blueprint(images_route)

@app.route('/files')
def files():
  s3_resource = boto3.resource('s3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET)
  my_bucket = s3_resource.Bucket(S3_BUCKET)
  for key in my_bucket.objects.all():
    print(key)
  return jsonify("files")

if __name__ == "__main__":
  app.run()