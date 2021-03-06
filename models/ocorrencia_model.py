from db import db
from datetime import datetime

from models.veiculo_model import VeiculoModel
from models.proprietario_model import ProprietarioModel
from models.dp_model import DpModel
from models.tipoOcorrencia_model import TipoOcorrenciaModel

class OcorrenciaModel(db.Model):
    __tablename__ = 'ocorrencia'

    numeroOcorrencia = db.Column(db.String(50), unique=True)
    localOcorrencia = db.Column(db.String(450))
    # tipo = db.Column(db.String(50))
    observacoes = db.Column(db.String(450))
    situacao = db.Column(db.String(50))
    data = db.Column(db.Date())
    id = db.Column(db.Integer, primary_key=True)
    dp_id = db.Column(db.Integer, db.ForeignKey('dp.id'))
    dp = db.relationship('DpModel', uselist=False, backref=db.backref('ocorrencia'), lazy=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculo.id'))
    veiculo = db.relationship('VeiculoModel', uselist=False, backref=db.backref('ocorrencia'), lazy=True)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo_ocorrencia.id'))
    tipo = db.relationship('TipoOcorrenciaModel', uselist=False, backref=db.backref('ocorrencia'), lazy=True)


    # def __init__(self, numeroOcorrencia, localOcorrencia, tipo, observacoes, situacao, data,  _id):
    # def __init__(self, numeroOcorrencia, localOcorrencia, tipo, observacoes, situacao, data, veiculo_id, _id):
    def __init__(self, numeroOcorrencia, localOcorrencia, tipo_id, observacoes, situacao, data, dp_id, veiculo_id, _id):
        self.id = _id
        self.numeroOcorrencia = numeroOcorrencia
        self.tipo_id = tipo_id
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
            'localOcorrencia': self.localOcorrencia,
            'tipo': self.tipo.json()
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
    def search_by_params(cls, local, placa, chassis, numeroMotor, nomeProp, numeroOcorrencia, dp, tipo, dataInicial, dataFinal, situacao):
        ocorrencias = []
        # Filtro completo
        if (dp and dataInicial and dataFinal and tipo):
            print('Pesquisa contém DP, Tipo e Data Inicial e Data Final!')
            ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).join(TipoOcorrenciaModel).\
            filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
            filter(VeiculoModel.placa.like("%"+placa+"%")).\
            filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
            filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
            filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
            filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
            filter(TipoOcorrenciaModel.id == tipo).\
            filter(OcorrenciaModel.situacao.like("%"+situacao+"%")).\
            filter(OcorrenciaModel.data.between(dataInicial, dataFinal)).\
            filter(DpModel.id == dp)

        elif (dp and dataInicial and dataFinal):
            print('Pesquisa contém DP, Data Inicial e Data Final!')
            ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).join(TipoOcorrenciaModel).\
            filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
            filter(VeiculoModel.placa.like("%"+placa+"%")).\
            filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
            filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
            filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
            filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
            filter(OcorrenciaModel.situacao.like("%"+situacao+"%")).\
            filter(OcorrenciaModel.data.between(dataInicial, dataFinal)).\
            filter(DpModel.id == dp)

        elif (dp and tipo):
            print('Pesquisa contém DP e Tipo!')
            ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).join(TipoOcorrenciaModel).\
            filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
            filter(VeiculoModel.placa.like("%"+placa+"%")).\
            filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
            filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
            filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
            filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
            filter(TipoOcorrenciaModel.id == tipo).\
            filter(OcorrenciaModel.situacao.like("%"+situacao+"%")).\
            filter(DpModel.id == dp)

        elif (dataInicial and dataFinal):
            print('Pesquisa contém Data!')
            ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).join(TipoOcorrenciaModel).\
            filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
            filter(VeiculoModel.placa.like("%"+placa+"%")).\
            filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
            filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
            filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
            filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
            filter(TipoOcorrenciaModel.id == tipo).\
            filter(OcorrenciaModel.situacao.like("%"+situacao+"%")).\
            filter(OcorrenciaModel.data.between(dataInicial, dataFinal))

        elif dp:
            print('Pesquisa contém DP!')
            ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).join(TipoOcorrenciaModel).\
            filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
            filter(VeiculoModel.placa.like("%"+placa+"%")).\
            filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
            filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
            filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
            filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
            filter(TipoOcorrenciaModel.id == tipo).\
            filter(OcorrenciaModel.situacao.like("%"+situacao+"%")).\
            filter(DpModel.id == dp)
        
        elif tipo:
            print('Pesquisa contém Tipo!')
            ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).join(TipoOcorrenciaModel).\
            filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
            filter(VeiculoModel.placa.like("%"+placa+"%")).\
            filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
            filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
            filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
            filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
            filter(TipoOcorrenciaModel.id == tipo).\
            filter(OcorrenciaModel.situacao == situacao)


        elif local or placa or chassis or numeroMotor or nomeProp or numeroOcorrencia or tipo or situacao:            
            print('Nenhum!')
            ocorrencias = db.session.query(OcorrenciaModel).join(VeiculoModel).join(ProprietarioModel).join(DpModel).join(TipoOcorrenciaModel).\
            filter(OcorrenciaModel.localOcorrencia.like("%"+local+"%")).\
            filter(VeiculoModel.placa.like("%"+placa+"%")).\
            filter(VeiculoModel.chassis.like("%"+chassis+"%")).\
            filter(VeiculoModel.numeroMotor.like("%"+numeroMotor+"%")).\
            filter(ProprietarioModel.nome.like("%"+nomeProp+"%")).\
            filter(OcorrenciaModel.numeroOcorrencia.like("%"+numeroOcorrencia+"%")).\
            filter(OcorrenciaModel.situacao == situacao)
            # filter(TipoOcorrenciaModel.id == tipo).\
        else:
            ocorrencias = db.session.query(OcorrenciaModel).all()

        return ocorrencias
