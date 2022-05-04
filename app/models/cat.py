from app import db

class Cat(db.Model):
	id = db.Column(db.Integer, primary_key = True, auto_increment = True)

	name = db.Column(db.String)

	breed = db.Column(db.String)

	personality = db.Column(db.String)

	age = db.Column(db.Integer)
	
	toe_beans = db.Column(db.Integer, default = 16)

	def to_json(self):
		return {"name": self.name,
        "personality": self.personality,
        "breed": self.breed,
		"age": self.age,
        "toe_beans": self.toe_beans}

