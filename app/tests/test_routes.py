
def test_get_all_cats_successfully(client):
	# Act
	response = client.get("/cats")
	response_body = response.get_json() #response has more than just json in it so we just want the json


	# Assert
	assert response.status_code == 200
	assert response_body == [] #comparing to empty list bc we are in our test database
	

def test_create_one_cat(client):
	# Act
    response = client.post("/cats", json={
        "name": "Shanks",
        "personality": "spoiled",
        "breed": "American Bob Tail",
        "age": 15
    })
    response_body = response.get_data()


    # Assert
    assert response.status_code == 201
    assert response_body == "Cat Shanks has been successfully created"
