from importlib.metadata import requires
from attr import field
from marshmallow import Schema, fields
from marshmallow.validate import Length

class PostSchema(Schema):
  """
      /api/posts - POST

  Parameters:
  - user_id (int)
  - name (str)
  - photodata (str)
  - description (str)
  """

  user_id = fields.Int(required=True)
  name = fields.Str(required=True, validate=Length(min=1, max=64))
  photodata = fields.Str(required=True)
  description = fields.Str(validate=Length(max=1024))
