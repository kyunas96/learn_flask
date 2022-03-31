from ast import BinOp
from marshmallow import Schema, fields
from marshmallow.validate import Length

class UserSchema(Schema):
    """
        /api/users - POST

    Parameters:
    - username (str)
    - email (str)
    - password (str)
    - location (str)
    - bio (str)
    - avatar_s3_object_id (str)
    """
    username = fields.Str(required=True, validate=Length(min=4))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=Length(min=8, max=32))
    location = fields.Str()
    bio = fields.Str(validate=Length(max=256))
    avatar_s3_object_id = fields.URL()
