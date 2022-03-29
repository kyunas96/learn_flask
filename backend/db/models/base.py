import os
import json
import datetime
from dotenv import load_dotenv, find_dotenv
import sqlalchemy
from sqlalchemy.orm import (declarative_base, scoped_session, sessionmaker)

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

  def create(self):
    with _Base.create_session() as session:
      try:
        session.add(self)
        session.commit()
      except Exception as e:
        return e
      finally:
        session.close()

    return self

  def update(self, update_data):
    with _Base.create_session() as session:
      try:
        for k, v in update_data.items():
          if k == "id":
            raise Exception("id property is not changeable")
          if not hasattr(self, k):
            raise Exception(f"{k} does not exist on {self.__class__}")
          setattr(self, k, v)
        session.commit()
        session.flush()
      except Exception as e:
        return e
      finally:
        session.close()

    return self

  # def get(self, attributes):
  #   for attr in attributes:
  #     if not hasattr(self, attr):
  #       raise Exception(f"{attr} does not exist on {self.__class__}")

  #   # with _Base.create_session as session:
  #   #   try:


  @classmethod
  def get_from_id(cls, id):
    with _Base.create_session() as session:
      print(f"CLS: {cls.__class__}")
      try:
        entry = session.query(cls).filter(cls.id == id).one()
        print(f"entry: {entry}")
        session.close()
        return entry
      except Exception as e:
        session.close()
        return e


Base = declarative_base(cls=_Base)