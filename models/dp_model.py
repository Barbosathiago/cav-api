from db import db

class DpModel(db.Model):
    __tablename__ = 'dp'
    
    nome = db.Column(db.String(120))
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def json(self):
        return {'nome': self.nome, 'id': self.id}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
