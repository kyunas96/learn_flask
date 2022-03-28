import os
import json
import datetime
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

  def to_json(self):
    def get_attr_handler(obj, key):
      item = getattr(obj, key)
      if isinstance(item, datetime.datetime):
        return item.isoformat()
      return item

    keys = self.__table__.c.keys()
    values = {c: get_attr_handler(self, c) for c in keys}
    return json.dumps(values)


Base = declarative_base(cls=_Base)