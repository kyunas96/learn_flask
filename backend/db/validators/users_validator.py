from ..models import User

def has_required_attrs(userdata):
    return all(
        [userdata[col.name] != None for col in User.__table.columns
         if not col.nullable]
    )


def only_valid_attrs(userdata):
    return all(
        [key in User.__table__.columns for key in userdata]
    )
