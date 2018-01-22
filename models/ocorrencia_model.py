from db import db
from datetime import datetime

from models.veiculo_model import VeiculoModel
from models.proprietario_model import ProprietarioModel
from models.dp_model import DpModel

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
    veiculo = db.relationship('VeiculoModel', uselist=False, backref=db.backref('ocorrencia'), lazy=True)
    dp = db.relationship('DpModel', uselist=False, backref=db.backref('ocorrencia'), lazy=True)


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
            'dp': self.dp.json(),
            'veiculo': self.veiculo.json(),
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
    @classmethod
    def search_by_params(cls, local, placa, chassis, numeroMotor, nomeProp, numeroOcorrencia, localRegistro, tipoOcorrencia, dataInicial, dataFinal, situacao):
        ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).\
        filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
        filter(VeiculoModel.placa.like("%"+placa+"%")).\
        filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
        filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
        filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
        filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
        filter(OcorrenciaModel.tipo.like("%"+tipoOcorrencia+"%")).\
        filter(OcorrenciaModel.situacao.like("%"+situacao+"%"))
        # filter(DpModel.id.like("%"+localRegistro+"%")).\ Corrigir o nome da propriedade, visto que o que deverá ser passado é o id
        return ocorrencias
