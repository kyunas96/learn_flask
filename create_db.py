from config import POSTGRESQL_URI
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

print(POSTGRESQL_URI)

engine = create_engine(POSTGRESQL_URI)
if not database_exists(engine.url):
  create_database(engine.url)

print(database_exists(engine.url))