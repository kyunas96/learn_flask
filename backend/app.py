from dotenv import load_dotenv
from flask import Flask, request
from .config import POSTGRESQL_URI
import backend.db.models as models
from backend.db import get_db_engine
from sqlalchemy import *
from .routes import (session_route, posts_route,
                     users_route, user_show_route, follows_route, feed_route)
from .controllers import BaseController
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = get_db_engine()
# create a function that will seed the database after the tables for
# the models are created in the database
app.register_blueprint(session_route, url_prefix='/session')
app.register_blueprint(feed_route, url_prefix='/feed')
app.register_blueprint(posts_route, url_prefix='/posts')
users_route.register_blueprint(user_show_route, url_prefix='<int:userid>')
app.register_blueprint(users_route, url_prefix='/users')
app.register_blueprint(follows_route, url_prefix='/follows')

# get the current user before further processing


@app.before_request
def get_current_user():
    print("before request")
    print(request.cookies.get('session_token'))
    print(BaseController.get_current_user())


if __name__ == "__main__":
    app.run(debug=True)
