import pytest

from app import create_app
from db import get_db_engine
from sqlalchemy.orm import Session


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def session():
    engine = get_db_engine()
    return Session(engine)
