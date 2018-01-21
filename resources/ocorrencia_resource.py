# Importando bibliotecas
from flask_restful import Resource, reqparse

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
        pass

    def put(self):
        pass


class OcorrenciabyId(Resource):
    def get(self, id):
        pass


class OcorrenciaList(Resource):
    def get(self):
        return {'ocorrencias': [oco.json() for oco in OcorrenciaModel.query.all()]}
