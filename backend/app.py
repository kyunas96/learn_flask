from dotenv import load_dotenv
from flask import Flask
from .config import POSTGRESQL_URI
import backend.db.models as models
from backend.db import get_db_engine
from sqlalchemy import *
from .routes import session_route, post_route
from .controllers import BaseController

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = get_db_engine()
# create a function that will seed the database after the tables for
# the models are created in the database
app.register_blueprint(session_route, url_prefix='/session')
app.register_blueprint(post_route, url_prefix='/posts')

# get the current user before further processing
# @app.before_request
# def get_current_user():
#   # BaseController.get_current_user()
#   print("before request")


if __name__ == "__main__":
  app.run(debug=True)