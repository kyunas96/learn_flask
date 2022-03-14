from json import load
from flask import Flask, jsonify
from config import S3_BUCKET, S3_KEY, S3_SECRET, POSTGRESQL_URI
from routes.images import images_route
from db.init_db import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_URI
init_db(app)

app.register_blueprint(images_route)

if __name__ == "__main__":
  app.run()