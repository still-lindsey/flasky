import pytest
from app import create_app
from app import db
from app.models.dog import Dog


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_dogs(app):
    dog_1 = Dog(name="Dahlia", breed="husky", age=1)
    dog_2 = Dog(name="Alife", breed="terrieroodle", age=4)
    dog_3 = Dog(name="Bella", breed="tabby", age=6)

    db.session.add_all([dog_1, dog_2, dog_3])
    db.session.commit()
