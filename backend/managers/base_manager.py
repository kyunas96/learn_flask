import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv(find_dotenv())

POSTGRESQL_URI = os.getenv('POSTGRESQL_URI')
engine = create_engine(POSTGRESQL_URI, echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

class BaseManager(object):
  def __init__(self):
    self.session = Session()
