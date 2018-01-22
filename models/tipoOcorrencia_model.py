from db import db

class TipoOcorrenciaModel(db.Model):
    __tablename__ = 'tipo_ocorrencia'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120))

    def __init__(self, descricao, _id):
        self.id = _id
        self.descricao = descricao

    def json(self):
        return { 'descricao': self.descricao, 'id': self.id}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
