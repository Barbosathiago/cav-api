from db import db
from datetime import datetime

class OcorrenciaModel(db.Model):
    __tablename__ = 'ocorrencia'

    numeroOcorrencia = db.Column(db.String(50), unique=True)
    localOcorrencia = db.Column(db.String(450))
    tipo = db.Column(db.String(50))
    observacoes = db.Column(db.String(450))
    situacao = db.Column(db.String(50))
    data = db.Column(db.Date())
    id = db.Column(db.Integer, primary_key=True)
    dp_id = db.Column(db.Integer, db.ForeignKey('dp.id'))
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculo.id'))
    veiculo = db.relationship('VeiculoModel')
    dp = db.relationship('DpModel')


    # def __init__(self, numeroOcorrencia, localOcorrencia, tipo, observacoes, situacao, data,  _id):
    # def __init__(self, numeroOcorrencia, localOcorrencia, tipo, observacoes, situacao, data, veiculo_id, _id):
    def __init__(self, numeroOcorrencia, localOcorrencia, tipo, observacoes, situacao, data, dp_id, veiculo_id, _id):
        self.id = _id
        self.numeroOcorrencia = numeroOcorrencia
        self.tipo = tipo
        self.observacoes = observacoes
        self.situacao = situacao
        self.localOcorrencia = localOcorrencia
        self.data = datetime.strptime(data,'%Y-%m-%d').date()
        self.dp_id = dp_id
        self.veiculo_id = veiculo_id
        self.id = _id

    def json(self):
        return {
            'numeroOcorrencia': self.numeroOcorrencia,
            'tipo': self.tipo,
            'observacoes': self.observacoes,
            'situacao': self.situacao,
            'data': self.data.strftime('%Y-%m-%d'),
            'dp_id': self.dp_id,
            'veiculo_id': self.veiculo_id,
            'id': self.id,
            'localOcorrencia': self.localOcorrencia
            }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
