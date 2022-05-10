from flask import Blueprint, jsonify, make_response, abort, request

from .helpers import validate_cat

from app.models.cat import Cat

from app import db

cat_bp = Blueprint("cat", __name__,url_prefix="/cats")

# class Cat:
#     def __init__(self, id, name, breed, personality, age):
#         self.id = id
#         self.name = name
#         self.breed = breed
#         self.personality = personality
#         self.age = age
#         self.toe_beans = 16
#         # self.tricks = tricks or []

    # def to_json(self):
    #     return {
    #         "name": self.name,
    #         "personality": self.personality,
    #         "breed": self.breed,
    #         "toe_beans": self.toe_beans,
    #         # "tricks": self.tricks
    #     }
    


# cats = [
#     Cat(1, "Muna", "tabby", "mischevious", 4),
#     Cat(2, "Matthew", "siamese", "cuddly", 3),
#     Cat(3, "George", "tabby","Sassy", 11)
# ]




@cat_bp.route("", methods = ["POST"])
def create_cat():
    request_body = request.get_json()

    # new_cat = Cat(name=request_body["name"], 
    # breed = request_body["breed"],
    # personality=request_body["personality"], 
    # age=request_body["age"], toe_beans = request_body["toe_beans"])

    new_cat = Cat.create(request_body)

    db.session.add(new_cat)
    db.session.commit()

    return make_response(f"Cat {new_cat.name} has been successfully created", 201)


# get all cats
@cat_bp.route("", methods=["GET"])
def handle_cats():
    breed_query = request.args.get("breed")

    if breed_query: 
        cats = Cat.query.filter_by(breed = breed_query)
    else:
        cats = Cat.query.all()  
    
    cats_response = []

    for cat in cats:
        cats_response.append(
        cat.to_json()
        )

    return jsonify(cats_response), 200

# get one cat
@cat_bp.route("/<cat_id>", methods=["GET"])
def handle_cat(cat_id):
    # try:
    #     cat_id = int(cat_id)
    # except:
    #     return abort(make_response({"message": f"cat {cat_id} is invalid"}, 400))

    # cats = Cat.query.all()
    # for cat in cats:
    #     if cat.id == cat_id:
    #         # return vars(cat)
    #         return jsonify({
    #             "id": cat.id,
    #             "name": cat.name,
    #             "breed": cat.breed,
    #             "personality": cat.personality,
    #             "age": cat.age,
    #             "toe_beans": cat.toe_beans
    #         })
            
    # return abort(make_response({"message": f"cat {cat_id} not found"}, 404))

    cat = validate_cat(cat_id)
    return jsonify(cat.to_json()), 200


@cat_bp.route("/<cat_id>", methods = ["PUT"])
def update_cat(cat_id):
    cat = validate_cat(cat_id)

    request_body = request.get_json()

    cat.update(request_body)
    # cat.name = request_body["name"]
    # cat.age = request_body["age"]
    # cat.breed = request_body["breed"]
    # cat.personality = request_body["personality"]
    # cat.toe_beans = request_body["toe_beans"]

    db.session.commit()

    return make_response(f"Cat #{cat_id} succesffully updated"), 200


@cat_bp.route("/<cat_id>", methods=["DELETE"])
def delete_one_cat(cat_id):
    cat = validate_cat(cat_id)

    db.session.delete(cat)
    db.session.commit()

    return make_response(f"Cat #{cat_id} was successfully deleted"), 200