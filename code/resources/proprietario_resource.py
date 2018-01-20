# Importando bibliotecas
from flask_restful import Resource, reqparse

# Importando models
from models.proprietario_model import ProprietarioModel

class Proprietario(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('contato',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('nome',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('id',
        type=int,
    )

    def post(self):
        data = Proprietario.parser.parse_args()

        if ProprietarioModel.find_by_id(data['id']):
            return {'message': 'Um proprietario com o id {} ja existe em sua base de dados.'.format(data['id'])}, 400

        proprietario = ProprietarioModel(data['contato'], data['nome'], None)
        try:
            proprietario.save_to_db()
        except:
            return {'message': 'Ocorreu um erro ao inserir o registro.'}, 500
        return proprietario.json(), 201

    def put(self):
        data = Proprietario.parser.parse_args()

        prop = ProprietarioModel.find_by_id(data['id'])
        if prop is None:
            prop = ProprietarioModel(data['contato'], data['nome'], None)
        else:
            prop.nome = data['nome']
            prop.contato = data['contato']

        prop.save_to_db()

        return prop.json()

    def delete(self):
        data = Proprietario.parser.parse_args()
        prop = ProprietarioModel.find_by_id(data['id'])
        if prop:
            prop.delete_from_db()
        return{"message": "Proprietario apagado."}

class ProprietarioById(Resource):
    def get(self, id):
        prop = ProprietarioModel.find_by_id(id)
        if prop:
            return prop.json()
        return {'message':'Nenhum proprietário com esse id foi encontrado.'}, 404

class ProprietarioList(Resource):
    def get(self):
        return {'proprietarios': [prop.json() for prop in ProprietarioModel.query.all()]}
