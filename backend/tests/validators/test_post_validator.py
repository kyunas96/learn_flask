import pytest
from controllers.validators import PostSchema

@pytest.fixture
def schema():
  return PostSchema()

def test_valid_post_validation(schema):
  
  pass

def test_invalid_post_validation(schema):
  pass

def test_post_name_username_uniqueness(schema):
  pass


