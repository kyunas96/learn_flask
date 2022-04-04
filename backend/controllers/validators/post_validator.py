from importlib.metadata import requires
from attr import field
from marshmallow import Schema, fields, ValidationError, validates_schema
from marshmallow.validate import Length
from ...db.models import Post

class PostSchema(Schema):
  """
      /api/posts - POST

  Parameters:
  - user_id (int)
  - name (str)
  - photodata (str)
  - description (str)
  """

  @validates_schema
  def validate_name_uniqueness_for_user(self, data, **kwargs):
    name = data['name']
    user_id = data['user_id']
    post = Post.query().filter(Post.name == name).filter(Post.user_id == user_id). \
      scalar()
    if post is not None:
      raise ValidationError("You have already created a post with the same name")


  user_id = fields.Int(required=True)
  name = fields.Str(required=True, validate=Length(min=1, max=64))
  photodata = fields.Str(required=True)
  description = fields.Str(validate=Length(max=1024))
