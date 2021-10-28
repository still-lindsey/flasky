# def test_get_all_books_with_no_records(client):
#     # Act
#     response = client.get("/books")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == []

def test_get_all_dogs_with_no_records(client):
    # Act
    response = client.get("/dogs")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_dogs_with_three_records(client, three_dogs):
    # Act
    response = client.get("/dogs")
    response_body = response.get_json()
    print(response_body)

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 3

def test_post(client):
    # Act
    response = client.post("/dogs", json={"name":"Dahlia", "breed":"husky", "age":1})
    response_body = response.get_json()
    print(response_body)

    # Assert
    assert response.status_code == 201

