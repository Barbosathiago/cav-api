from db import db

class VeiculoModel(db.Model):
    __tablename__ = 'veiculo'

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(8))
    tipo = db.Column(db.String(50))
    ano = db.Column(db.String(12))
    chassis = db.Column(db.String(120))
    numeroMotor = db.Column(db.String(15))
    cor = db.Column(db.String(50))
    proprietario_id = db.Column(db.Integer, db.ForeignKey('proprietario.id'))
    proprietario = db.relationship('ProprietarioModel')

    def __init__(self, id, placa, tipo, ano, chassis, numeroMotor, cor, proprietario_id):
        self.id = id
        self.placa = placa
        self.tipo = tipo
        self.ano = ano
        self.chassis = chassis
        self.numeroMotor = numeroMotor
        self.cor = cor
        self.proprietario_id = proprietario_id

    def json(self):
        return {'id': self.id, 'placa': self.placa, 'tipo': self.tipo, 'ano': self.ano,'chassis': self.chassis,'numeroMotor': self.numeroMotor,'cor': self.cor, 'proprietario_id': self.proprietario_id}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        print(self.ano)
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
