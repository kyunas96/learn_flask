from models import Base

def create_tables(engine):
  Base.metadata.create_all(engine, checkfirst=True)

def delete_tables(engine):
  Base.metadata.drop_all(engine, checkfirst=True)
