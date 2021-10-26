from flask import abort, Blueprint, jsonify, request
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
        dogs_response.append(dog.to_dict())
    
    return jsonify(dogs_response), 200
    

@dog_bp.route("/<dog_id>", methods=["GET", "PUT"])
def handle_dog(dog_id):
    print(dog_id)
    dog_id = int(dog_id)
    dog = Dog.query.get(dog_id)
    if not dog:
        return { "Error": f"Dog {dog_id} was not found"}, 404

    if request.method == "GET":
        return jsonify(dog.to_dict()), 200
    elif request.method == "PUT":
        input_data = request.get_json()
        input_data = sanitize_data(input_data)
        dog.name = input_data["name"]
        dog.breed = input_data["breed"]
        dog.age = input_data["age"]
        db.session.commit()
        return jsonify(dog.to_dict()), 200

def sanitize_data(input_data):
    data_types = {"name":str, "breed":str, "age":int}
    for name, val_type in data_types.items():
        try:
            val = input_data[name]
            type_test = val_type(val)
        except Exception as e:
            print(e)
            raise abort(400, "Bad Data")
    return input_data

def do_nothing():
    pass




@dog_bp.route("/<dog_id>", methods=["DELETE"])
def delete_dog(dog_id):
    print(dog_id)
    try:
        dog_id = int(dog_id)
    except ValueError:
        return {"Error": "ID must be a number"}, 404
    dog = Dog.query.get(dog_id)

    if dog:
        db.session.delete(dog)
        db.session.commit()
        return {"Success": f"Deleted Dog {dog_id}"}, 200
    else:
        return {"Error": f"No Dog with ID matching {dog_id}"}, 404




