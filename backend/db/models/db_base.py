import os
import json
import datetime
from .db_base import db

class Base(db.model):
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
