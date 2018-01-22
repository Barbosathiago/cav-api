from flask_restful import Resource, reqparse

from models.tipoOcorrencia_model import TipoOcorrenciaModel

class TipoOcorrencia(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('descricao',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('id',
        type=int
    )

    def post(self):
        data = TipoOcorrencia.parser.parse_args()

        if TipoOcorrenciaModel.find_by_id(data['id']):
            return {'message': 'Um proprietário com este ID já existe na base de dados.'}, 400

        tipo = TipoOcorrenciaModel(data['descricao'], None)
        try:
            tipo.save_to_db()
        except:
            return {'message': 'Ocorreu um erro ao inserir o registro na base de dados.'}, 500
        return tipo.json(), 201

    def put(self):
        data = TipoOcorrencia.parser.parse_args()

        tipo = TipoOcorrenciaModel.find_by_id(data['id'])
        if tipo is None:
            tipo = TipoOcorrenciaModel(data['descricao'], None)
        else:
            tipo.descricao = data['descricao']

        tipo.save_to_db()

        return tipo.json()

    def delete(self):
        data = TipoOcorrencia.parser.parse_args()
        tipo = TipoOcorrenciaModel.find_by_id(data['id'])
        if tipo:
            tipo.delete_from_db()
        return{'message': 'Tipo apagado.'}


class TipoById(Resource):
        def get(self, id):
            tipo = TipoOcorrenciaModel.find_by_id(id)
            if tipo:
                return tipo.json()
            return {'message': 'Nenhum tipo com este id foi encontrado.'},404


class TipoList(Resource):
    def get(self):
        return {'tipos': [tipo.json() for tipo in TipoOcorrenciaModel.query.all()]}
