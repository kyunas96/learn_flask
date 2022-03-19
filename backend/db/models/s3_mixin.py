import os
import boto3
from sqlalchemy.orm import declarative_mixin
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


"""
  S3MixIn will be resonsible for getting objects from S3 based on 
  s3_file_name associated with 
"""

S3_URL = os.getenv('S3_URL')
S3_BUCKET = os.getenv('S3_BUCKET')
S3_KEY = os.getenv('S3_KEY')
S3_SECRET = os.getenv('S3_SECRET')


class S3MixIn(object):
    _s3_url_ = S3_URL
    _s3_bucket_ = S3_BUCKET

    def get_url(self):
        s3 = boto3.client('s3',
                          aws_access_key_id=S3_KEY,
                          aws_secret_access_key=S3_SECRET
                          )
        try:
          response = s3.generate_presigned_url('get_object', Params={
            'Bucket': S3MixIn._s3_bucket_,
            'Key': self._s3_url_
          })
          return response
        except boto3.exceptions.ClientError as e:
          return e
