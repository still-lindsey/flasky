from app import db

class Cat(db.Model):
	id = db.Column(db.Integer, primary_key = True, auto_increment = True)

	name = db.Column(db.String)

	breed = db.Column(db.String)

	personality = db.Column(db.String)

	age = db.Column(db.Integer)

	caretaker_id = db.Column(db.Integer, db.ForeignKey('caretaker.id'))
	caretaker = db.relationship("Caretaker", back_populates = "cats")

	def to_json(self):
		try:
			caretaker = self.caretaker.name
		except AttributeError:
			caretaker = "Imma street cat"
		return {"id": self.id, "name": self.name,
        "personality": self.personality,
        "breed": self.breed,
		"age": self.age,
		"caretaker": caretaker}

	def update(self, request_body):
		self.name = request_body["name"]
		self.age = request_body["age"]
		self.breed = request_body["breed"]
		self.personality = request_body["personality"]


	@classmethod
	def create(cls, request_body):
		new_cat = cls(name=request_body["name"],
            breed=request_body["breed"],
            personality=request_body["personality"],
            age=int(request_body["age"]))
			
		return new_cat
