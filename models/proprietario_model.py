from db import db

class ProprietarioModel(db.Model):
    __tablename__ = 'proprietario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    contato = db.Column(db.String(25))

    # veiculos = db.relationship('VeiculoModel', lazy='dynamic')

    def __init__(self, contato, nome, _id):
        self.id = _id
        self.contato = contato
        self.nome = nome

    def json(self):
        return {'nome': self.nome, 'contato': self.contato, 'id': self.id}

    # Procura proprietario por id
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    # Usado para atualizar e salvar dados no banco
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Usado para deletar do banco
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
