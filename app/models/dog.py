from app import db

class Dog(db.Model):
    __tablename__ = 'dogs'
    breed = db.Column(db.String(64))
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(64))

    def to_dict(self):
        return({
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
        })


