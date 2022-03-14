from sqlalchemy import engine, text, create_engine
from config import POSTGRESQL_URI


def setup_database_connection():
  engine = create_engine(POSTGRESQL_URI)
  engine.connect()