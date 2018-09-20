from db import db


class HelloModel(db.Model):
    __tablename__ = "hellos"
    id = db.Column(db.Integer, primary_key=True)
    hello = db.Column(db.String(50))

    def __init__(self, hello):
        self.hello = hello

    def to_json(self):
        return {'id': self.id, 'hello': self.hello}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()