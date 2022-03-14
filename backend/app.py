from flask import Flask, jsonify
from ..config import S3_BUCKET, S3_KEY, S3_SECRET
from routes.images import images_route
from db_connection import setup_database_connection

setup_database_connection()

app = Flask(__name__)
app.register_blueprint(images_route)

if __name__ == "__main__":
  app.run()