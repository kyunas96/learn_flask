from dotenv import load_dotenv
from flask import Flask
import boto
from boto.s3.key import Key

from routes.images import images_route

load_dotenv()

app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 'https://pxclone-dev.s3.us-west-1.amazonaws.com/'
s3 = FlaskS3(app)
app.register_blueprint(images_route)

if __name__ == "__main__":
  app.run()