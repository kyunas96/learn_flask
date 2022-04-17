import pytest
from db.models import User
from faker import Faker

fake = Faker()


def test_user_creation():
  user_dict = {
    "username": fake.first_name(),
    "email": fake.ascii_email(),
    "password": "password",
    "session_token": fake.md5(),
    "location": fake.city(),
    "bio": fake.paragraph(nb_sentences=5),
    "avatar_s3_object_id": fake.domain_name(),
    "date_created": fake.date_this_decade()
  }
  user = User(user_dict)
  print(f"\nUSER: {user.to_json()}")
  assert user is not None


def test_invalid_user_validation():
  pass
