from flask import Blueprint, jsonify

dog_bp = Blueprint("dog", __name__,url_prefix="/dogs")

# get all dogs
@dog_bp.route("", methods=["GET"])
def handle_dogs():
    dogs_response = []
    for dog in dogs:
        dogs_response.append(
            #vars(dog)
            # {
            #     "id": dog.id,
            #     "name": dog.name,
            #     "breed": dog.breed,
            #     "tricks": dog.tricks
            # }
            dog.to_json()
        )
    return jsonify(dogs_response)

@dog_bp.route("/<dog_id>", methods=["GET"])
def handle_dog(dog_id):
    print(dog_id)
    dog_id = int(dog_id)
    for dog in dogs:
        if dog.id == dog_id:
            # return {
            #     "id": dog.id,
            #     "name": dog.name,
            #     "breed": dog.breed,
            #     "tricks": dog.tricks
            # }
            return dog.to_json()

    return {"error": "Dog not found"}, 404