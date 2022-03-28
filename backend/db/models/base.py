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

  def to_json(self, skip_keys=[]):
    json_dict = {}
    for key in self.__table__.c.keys():
      if key in skip_keys: continue
      item = getattr(self, key)
      if isinstance(item, datetime.datetime):
        json_dict[key] = item.isoformat()
      else:
        json_dict[key] = item
    return json.dumps(json_dict)


Base = declarative_base(cls=_Base)