from app import db

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    breed = db.Column(db.String)

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "breed": self.breed
            }