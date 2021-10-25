from app import db
from app.models.dog import Dog
from flask import Blueprint, jsonify, make_response, request

dog_bp = Blueprint("dog", __name__,url_prefix="/dogs")

@dog_bp.route("", methods=["GET","POST"])
def handle_dogs():
    if request.method == 'POST':
        request_body = request.get_json()
        if "name" not in request_body or "breed" not in request_body:
            return {"error": "incomplete request body"}, 400


        new_dog = Dog(
            name=request_body["name"],
            breed=request_body["breed"],
        )

        db.session.add(new_dog)
        db.session.commit()

        return make_response(f"Dog {new_dog.name} created!", 201)
    elif request.method == 'GET':
        dogs = Dog.query.all()
        dogs_response = []
        for dog in dogs:
            dogs_response.append(
                dog.to_dict()
            )
        return jsonify(dogs_response)


@dog_bp.route("/<dog_id>", methods=["GET"])
def handle_dog(dog_id):
    try:
        dog_id = int(dog_id)
    except:
        return {"error": "dog_id must be an int"}, 400

    dog = Dog.query.get(dog_id)
    return dog.to_dict()

    