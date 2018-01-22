# Importando bibliotecas
from flask_restful import Resource, reqparse
from flask import request
from datetime import datetime

# Importando models
from models.ocorrencia_model import OcorrenciaModel

class Ocorrencia(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('numeroOcorrencia',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('tipo',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('situacao',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('localOcorrencia',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('observacoes',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('data',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('dp_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('veiculo_id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('id',
        type=int
    )

    def post(self):
        data = Ocorrencia.parser.parse_args()

        if OcorrenciaModel.find_by_id(data['id']):
            return {'message': 'Uma ocorrencia com este ID ja existe em sua base de dados'}, 400
        ocorrencia = OcorrenciaModel(localOcorrencia=data['localOcorrencia'], tipo=data['tipo'], observacoes=data['observacoes'], situacao=data['situacao'], data=data['data'], dp_id=data['dp_id'], veiculo_id=data['veiculo_id'], _id=None, numeroOcorrencia=data['numeroOcorrencia'])
        ocorrencia.save_to_db()
        return ocorrencia.json()
        # try:
        #
        # except:
        #     return {'message': 'Ocorreu um erro ao inserir o registro.'}, 500


    def put(self):
        data = Ocorrencia.parser.parse_args()

        ocorrencia = OcorrenciaModel.find_by_id(data['id'])
        if ocorrencia is None:
            ocorrencia = OcorrenciaModel(localOcorrencia=data['localOcorrencia'], tipo=data['tipo'], observacoes=data['observacoes'], situacao=data['situacao'], data=['data'], dp_id=data['dp_id'], veiculo_id=data['veiculo_id'], _id=None, numeroOcorrencia=data['numeroOcorrencia'])
        else:
            ocorrencia.numeroOcorrencia = data['numeroOcorrencia']
            ocorrencia.localOcorrencia = data['localOcorrencia']
            ocorrencia.tipo = data['tipo']
            ocorrencia.observacoes = data['observacoes']
            ocorrencia.situacao = data['situacao']
            ocorrencia.data = datetime.strptime(data['data'],'%Y-%m-%d').date()
            ocorrencia.dp_id = data['dp_id']
            ocorrencia.veiculo_id = data['veiculo_id']

        ocorrencia.save_to_db()

        return ocorrencia.json()


class OcorrenciabyId(Resource):
    def get(self, id):

        oco = OcorrenciaModel.find_by_id(id)
        if oco:
            return oco.json()
        return {'message': 'Nenhuma ocorrencia com esse id foi encontrada.'}, 404


class OcorrenciaList(Resource):
    def get(self):
        local = request.args.get('local')
        if not local:
            local = ''
        placa = request.args.get('placa')
        if not placa:
            placa = ''
        chassis = request.args.get('chassis')
        if not chassis:
            chassis = ''
        numeroMotor = request.args.get('numeroMotor')
        if not numeroMotor:
            numeroMotor = ''
        nomeProp = request.args.get('nomeProp')
        if not nomeProp:
            nomeProp = ''
        numeroOcorrencia = request.args.get('numeroOcorrencia')
        if not numeroOcorrencia:
            numeroOcorrencia = ''
        localRegistro = request.args.get('localRegistro')
        if not localRegistro:
            localRegistro = ''
        tipoOcorrencia = request.args.get('tipoOcorrencia')
        if not tipoOcorrencia:
            tipoOcorrencia = ''
        dataInicial = request.args.get('dataInicial')
        if not dataInicial:
            dataInicial = None
        dataFinal = request.args.get('dataFinal')
        if not dataFinal:
            dataFinal = None
        situacao = request.args.get('situacao')
        if not situacao:
            situacao = ''
        return {'ocorrencias': [oco.json() for oco in OcorrenciaModel.search_by_params(local=local, placa=placa, chassis=chassis, numeroMotor=numeroMotor, nomeProp=nomeProp, numeroOcorrencia=numeroOcorrencia, localRegistro=localRegistro, tipoOcorrencia=tipoOcorrencia, dataInicial=dataInicial, dataFinal=dataFinal,situacao=situacao)]}
