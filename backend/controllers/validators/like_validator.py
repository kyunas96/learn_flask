from marshmallow import Schema, fields

class LikeSchema(Schema):
  """
      /api/likes - POST/DELETE

      Parameters:
      - user_id (str)
      - post_id (str)
  """

  post_id = fields.Int(required=True)
  user_id = fields.Int(required=True)

  