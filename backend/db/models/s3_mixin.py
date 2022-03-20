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
    s3_client = boto3.client('s3',
                             aws_access_key_id=S3_KEY,
                             aws_secret_access_key=S3_SECRET
                             )

    def _verfy_opload_success(filename):
        with S3MixIn.s3_client as s3, S3MixIn._s3_bucket_ as bucket:
            try:
                res = s3.head_object(Bucket=bucket, Key=filename)
                return res is not None
            except boto3.exceptions.ClientError as e:
                return e

    def create_object(self, data, filename):
        # controller will be responsible for getting data from the request
        # and passing it in
        with S3MixIn.s3_client as s3, S3MixIn._s3_bucket_ as bucket:
            s3.upload_fileobj()

    def get_url(self):
        with S3MixIn.s3_client as s3:
            try:
                response = s3.generate_presigned_url('get_object', Params={
                    'Bucket': S3MixIn._s3_bucket_,
                    'Key': self._s3_url_
                })
                return response
            except boto3.exceptions.ClientError as e:
                return e
