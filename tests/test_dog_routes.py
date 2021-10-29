from app.models.dog import Dog
from app import db
import copy

def test_get_all_dogs_returns_empty_list_when_db_is_empty(client):
    # act
    response = client.get("/dogs")

    #assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_all_dogs_returns_one_dog(client, one_dog):
    # act
    response = client.get("/dogs")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body[0]["name"] == "joy"
    # check other attributes too

def test_make_formal_dog_name(client, one_dog):
    response = client.patch("/dogs/1/formalize")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == "Why hello, Mx. joy!"

    db.session.expire_all()
    updated_dog = Dog.query.get(1)
    assert updated_dog.name == "Mx. joy"

def test_create_dog(client):
    # act
    response = client.post("/dogs", json={
        "name": "jsony",
        "breed": "poodle",
        "age": "5"
    })

    response_body = response.get_json()

    #assert
    assert response.status_code == 201
    assert response_body["name"] == "jsony"
    assert response_body["breed"] == "poodle"
    assert response_body["age"] == "5"
    assert response_body["id"] == 1
    assert response_body["chip"] == ""

    new_dog = Dog.query.get(1)
    assert new_dog
    assert new_dog.name == "jsony"
    assert new_dog.breed == "poodle"
    assert new_dog.age == "5"
    assert new_dog.chip == ''

def test_create_dog_with_incomplete_data(client):
    request_body = {
        "name": "jsony",
        "breed": "poodle",
        "age": "5"
    }

    for key in request_body:
        incomplete_request_body = copy.copy(request_body)
        incomplete_request_body.pop(key)
        response = client.post("/dogs", json=incomplete_request_body)

        response_body = response.get_json()

        assert response.status_code == 400
        assert response_body["error"] == "incomplete request body"

    assert Dog.query.all() == []