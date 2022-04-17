from distutils.log import error
from marshmallow import ValidationError
import pytest
from faker import Faker
from db.models import User

fake = Faker()


def test_valid_user_validation(schema):
    user_dict = {
        "username": fake.first_name() + fake.last_name(),
        "email": fake.ascii_email(),
        "password": "password",
        "location": fake.city(),
        "bio": fake.paragraph(nb_sentences=2),
        "avatar_s3_object_id": fake.domain_name(7),
    }
    errors = schema.validate(user_dict)
    assert len(errors) == 0


def test_invalid_user_validation(schema):
    user_dict = {}
    validation_error_keys = ['username', 'email', 'password']
    errors = schema.validate(user_dict)
    assert len(errors) > 0
    for err_key in validation_error_keys:
        assert err_key in errors


def test_unique_usernames(schema):
    user_dict = {
        "username": "Kevin",
        "email": fake.ascii_email(),
        "password": "password",
        "location": fake.city(),
        "bio": fake.paragraph(nb_sentences=5),
        "avatar_s3_object_id": fake.domain_name(4),
    }
    errors = schema.validate(user_dict)
    # print(f"ERROR: {errors}")
    assert "Username already exists" in errors.get('username') 

def test_unique_emails(schema):
  user_dict = {
      "username": "Kevin1",
      "email": "kevinyunas@icloud.com",
      "password": "password",
      "location": fake.city(),
      "bio": fake.paragraph(nb_sentences=5),
      "avatar_s3_object_id": fake.domain_name(4),
  }
  errors = schema.validate(user_dict)
  assert "Account already registered with email" in errors.get('email')