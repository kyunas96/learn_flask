from marshmallow import Schema, validates, ValidationError, fields
from marshmallow.validate import Length
from db.models import User


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
    avatar_s3_object_id = fields.Str(validate=Length(min=32, max=1024))

    @validates("username")
    def validate_username_uniqueness(self, value):
        if User.query().filter(User.username == value).scalar() is not None:
            raise ValidationError("Username already exists")

    @validates('email')
    def validate_email_uniqueness(self, value):
        if User.query().filter(User.email == value).scalar():
            raise ValidationError("Account already registered with email")
