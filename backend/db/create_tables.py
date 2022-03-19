from models import Base
from get_db_engine import get_db_engine

def create_tables(engine):
  Base.metadata.create_all(engine, checkfirst=True)
