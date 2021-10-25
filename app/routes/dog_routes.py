from flask import Blueprint, jsonify, request
# Import Model & db
from app.models.dog import Dog
from app import db

dog_bp = Blueprint("dog", __name__,url_prefix="/dogs")

# Make a dog
@dog_bp.route("", methods=["POST"])
def create_dog():
    # Get the data from the request
    request_data = request.get_json()

    if "name" not in request_data or "age" not in request_data \
        or "breed" not in request_data:
        return jsonify({"message": "Missing data"}), 400

    new_dog = Dog(name=request_data["name"], age=request_data["age"], 
                breed=request_data["breed"])
    
    db.session.add(new_dog)
    db.session.commit()

    return f"Dog {new_dog.name} created", 201




# get all dogs
@dog_bp.route("", methods=["GET"])
def handle_dogs():
    dogs_response = []
    dogs = Dog.query.all()
    for dog in dogs:
        dogs_response.append({
            "id": dog.id,
            "name": dog.name,
            "age": dog.age,
            "breed": dog.breed,
        })
    
    return jsonify(dogs_response), 200
    

@dog_bp.route("/<dog_id>", methods=["GET"])
def handle_dog(dog_id):
    print(dog_id)
    dog_id = int(dog_id)
    dog = Dog.query.get(dog_id)

    if dog:
        return {
            "id": dog.id,
            "name": dog.name,
            "age": dog.age,
            "breed": dog.breed,
        }, 200
    
    return { "Error": f"Dog {dog_id} was not found"}, 404