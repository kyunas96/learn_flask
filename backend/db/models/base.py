import os
import json
import datetime
from dotenv import load_dotenv, find_dotenv
import sqlalchemy
from sqlalchemy.orm import (declarative_base, scoped_session, sessionmaker)
from .exceptions.base_exceptions import InvalidFilterParameters

load_dotenv(find_dotenv())

POSTGRESQL_URI = os.getenv('POSTGRESQL_URI')
engine = sqlalchemy.create_engine(POSTGRESQL_URI, echo=True)
session = scoped_session(sessionmaker())
session.configure(bind=engine)


class _Base():
    _Session_ = session

    @staticmethod
    def create_session():
        return _Base._Session_()

    def to_json(self, skip_keys=[]):
        json_dict = {}
        for key in self.__table__.c.keys():
            if key in skip_keys:
                continue
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
                session.flush()
                return self.to_json()
            except Exception as e:
                print("Error at BASE")
                return str(f"BASE_MODEL ERROR: {str(e)}")
            finally:
                session.close()

    def update(self, update_data):
        with _Base.create_session() as session:
            try:
                for k, v in update_data.items():
                    if k == "id":
                        continue
                    if not hasattr(self, k):
                        raise Exception(
                            f"{k} does not exist on {self.__class__}")
                    setattr(self, k, v)
                session.add(self)
                session.commit()
                session.flush()
                self.to_json()
            except:
                return None
            finally:
                session.close()

    @classmethod
    def get_by(cls, attrs_dict):
        invalids = []
        for attr in attrs_dict.keys():
            if not hasattr(cls, attr):
                invalids.append(attr)
        if len(invalids) > 0:
            raise InvalidFilterParameters(invalids)
        with _Base.create_session() as session:
            try:
                entity = session.query(cls).filter_by(attrs_dict).all()
                return entity
            except Exception as e:
                return e
            finally:
                session.close()

    @classmethod
    def get_one_by(cls, attrs_dict):
        invalids = []
        for attr in attrs_dict.keys():
            if not hasattr(cls, attr):
                invalids.append(attr)
        if len(invalids) > 0:
            raise InvalidFilterParameters(invalids)
        with _Base.create_session() as session:
            entity = session.query(cls).filter_by(**attrs_dict).scalar()
            session.close()
            return entity

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
