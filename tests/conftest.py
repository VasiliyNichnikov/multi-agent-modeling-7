import pytest

from app.database.session import engine
from tests.testsession import MySession


@pytest.fixture
def session():
    connection = engine.connect()
    transaction = connection.begin()

    MySession.configure(bind=engine)
    session = MySession()

    try:
        yield session
    finally:
        MySession.remove()
        transaction.rollback()
        connection.close()
