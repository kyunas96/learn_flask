import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

load_dotenv(find_dotenv())

def get_db_engine():
  POSTGRESQL_URI = os.getenv('POSTGRESQL_URI')
  engine = create_engine(POSTGRESQL_URI)

  if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database created at: {POSTGRESQL_URI}")
  # else:
  #   drop_database(engine.url)

  return engine