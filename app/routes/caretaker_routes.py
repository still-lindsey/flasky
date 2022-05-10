from flask import Blueprint, jsonify, make_response, abort, request


from app.models.caretaker import Caretaker
from app.models.cat import Cat
from .helpers import validate_caretaker

from app import db

caretaker_bp = Blueprint("caretaker", __name__, url_prefix="/caretakers")

@caretaker_bp.route("", methods=['GET'])
def read_all_caretakers():
	caretakers = Caretaker.query.all()
	caretakers_response = []
	for caretaker in caretakers:
		caretakers_response.append({
			'id': caretaker.id,
			"name": caretaker.name
		})
	
	return jsonify(caretakers_response), 200

@caretaker_bp.route("", methods = ["POST"])
def create_caretaker():
	request_body = request.get_json()

	new_caretaker = Caretaker(name = request_body["name"])

	db.session.add(new_caretaker)
	db.session.commit()
	return jsonify(f"Caretaker {new_caretaker.name} has been created"), 201

@caretaker_bp.route("/<caretaker_id>/cats", methods = ["POST"])
def create_cat(caretaker_id):
	caretaker = validate_caretaker(caretaker_id)

	request_body = request.get_json()
	new_cat = Cat.create(request_body)

	new_cat.caretaker = caretaker

	db.session.add(new_cat)
	db.session.commit()

	return jsonify(f"Cat {new_cat.name} cared by {new_cat.caretaker.name} created"), 201

@caretaker_bp.route("/<caretaker_id>/cats", methods = ["GET"])
def read_cats(caretaker_id):
	caretaker = validate_caretaker(caretaker_id)

	cats_response = []

	for cat in caretaker.cats:
		cats_response.append(cat.to_json())

	return jsonify(cats_response), 200