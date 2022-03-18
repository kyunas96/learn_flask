from dotenv import load_dotenv
from flask import Flask
from .config import POSTGRESQL_URI
import backend.db.models as models
from backend.db import get_db_engine
from sqlalchemy import *

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = get_db_engine()
models.Base.metadata.create_all(engine)
# create a function that will seed the database after the tables for
# the models are created in the database


if __name__ == "__main__":
  app.run()