from marshmallow import Schema, fields


class SessionSchema(Schema):
    """
        /api/session - POST

    """

    username = fields.Str(required=True)
    password = fields.Str(required=True)
