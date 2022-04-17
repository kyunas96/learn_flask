import pytest

from app import create_app

@pytest.fixture()
def app():
  app = create_app()
  app.config.update({
    "TESTING": True
  })

  yield app

@pytest.fixture()
def client(app):
  yield app.test_client()
