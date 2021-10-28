import pytest
from app.models.dog import Dog
from app import create_app, db

#app
@pytest.fixture
def app():
    app = create_app({"Testing": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

#client
@pytest.fixture
def client(app):
    return app.test_client()

#data
@pytest.fixture
def one_dog(app):
    dog = Dog(
        name="joy",
        breed="husky",
        age="10"
        )
    db.session.add(dog)
    db.session.commit()
