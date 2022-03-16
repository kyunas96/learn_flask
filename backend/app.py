from json import load
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import S3_BUCKET, S3_KEY, S3_SECRET, POSTGRESQL_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)

if __name__ == "__main__":
  app.run()