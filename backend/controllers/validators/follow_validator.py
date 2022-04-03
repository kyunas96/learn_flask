from importlib.metadata import requires
from marshmallow import Schema, ValidationError, fields, validates_schema
from ...db.models import Follow

class FollowSchema(Schema):
  """
      /api/follows - POST/DELETE

  Parameters:
  - follower_id (str)
  - followee_id (str)
  """

    # VALIDATE THAT A FOLLOW DOES NOT ALREADY EXIST
    

  follower_id = fields.Int(required=True)
  followee_id = fields.Int(required=True)