from flask_restful import Resource, reqparse

from models.dp_model import DpModel
class Dp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('id',
        type=int,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = Dp.parser.parse_args()

        if DpModel.find_by_id(data['id']):
            return {'message': 'Já existe uma DP com este ID cadastrada no banco de dados'}, 400

        dp = DpModel(data['nome'], None)
        try:
            dp.save_to_db()
        except:
            return {'message': 'Ocorreu um erro ao inserir o registro no banco de dados.'}, 500
        return dp.json(), 201

    def put(self):
        data = Dp.parser.parse_args()
        dp = DpModel.find_by_id(data['id'])
        if dp is None:
            dp = DpModel(data['nome'], None)
        else:
            dp.nome = data['nome']
            dp.id = data['id']

        dp.save_to_db()

        return dp.json()

    def delete(self):
        data = Dp.parser.parse_args()
        dp = DpModel.find_by_id(data['id'])
        if dp:
            dp.delete_from_db()
            return{'message': 'Dp apagada.'}


class DpById(Resource):
    def get(self, id):
        dp = DpModel.find_by_id(id)
        if dp:
            return dp.json()
        return {'message': 'Nenhuma dp com este ID foi encontrada.'}, 404


class DpList(Resource):
    def get(self):
        return {'dps': [dp.json() for dp in DpModel.query.all()]}
