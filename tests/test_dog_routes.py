import copy
from app.models.dog import Dog

def test_get_all_dogs_returns_empty_list_when_db_is_empty(client):
    # act
    response = client.get("/dogs")

    #assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_dog(client):
    # Act
    response = client.post("/dogs", json={
        "name": "jsony",
        "age": "5",
        "breed": "mutt"
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body["name"] == "jsony"
    assert response_body["age"] == "5"
    assert response_body["breed"] == "mutt"

    new_dog = Dog.query.get(1)
    assert new_dog
    assert new_dog.name == "jsony"
    assert new_dog.age == "5"
    assert new_dog.breed == "mutt"

def test_create_dog_missing_data(client):
    request_body = {
        "name": "jsony",
        "age": "5",
        "breed": "mutt"
    }

    for key in request_body:
        incomplete_request_body = copy.copy(request_body)
        incomplete_request_body.pop(key)
        response = client.post("/dogs", json=incomplete_request_body)

        response_body = response.get_json()
        
        assert response.status_code == 400
        assert response_body["error"] == "incomplete request body"
        assert Dog.query.all() == []

