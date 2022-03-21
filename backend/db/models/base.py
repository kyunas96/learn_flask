import os
from dotenv import load_dotenv, find_dotenv
import sqlalchemy
from sqlalchemy.orm import (declarative_base, scoped_session, sessionmaker)
# from sqlalchemy.ext.declarative import declared_attr

load_dotenv(find_dotenv())

POSTGRESQL_URI = os.getenv('POSTGRESQL_URI')
engine = sqlalchemy.create_engine(POSTGRESQL_URI, echo=True)
session = scoped_session(sessionmaker())
session.configure(bind=engine)


class _Base(object):
  _Session_ = session

  @staticmethod
  def create_session():
    return _Base._Session_()

Base = declarative_base(cls=_Base)