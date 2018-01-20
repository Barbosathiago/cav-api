from flask_restful import Resource, reqparse

from models.veiculo_model import VeiculoModel

class Veiculo(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        help="This field cannot be left blank!"
    )
    parser.add_argument('placa',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('tipo',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('ano',
        type=str,
        help="This field cannot be left blank!"
    )
    parser.add_argument('chassis',
        type=str,
        help="This field cannot be left blank!"
    )
    parser.add_argument('numeroMotor',
        type=str,
        help="This field cannot be left blank!"
    )
    parser.add_argument('cor',
        type=str,
        help="This field cannot be left blank!"
    )
    parser.add_argument('proprietario_id',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = Veiculo.parser.parse_args()

        if VeiculoModel.find_by_id(data['id']):
            return {'message': 'Um veículo com o id informado já existe em sua base de dados'}, 400

        veiculo = VeiculoModel(None, data['placa'], data['tipo'], data['ano'],data['chassis'],data['numeroMotor'], data['cor'], data['proprietario_id'])

        try:
            veiculo.save_to_db()
        except:
            return {'message': 'Ocorreu um erro ao inserir o registro.'}, 500
        return veiculo.json(), 201

    def put(self):
        data = Veiculo.parser.parse_args()

        veiculo = VeiculoModel.find_by_id(data['id'])
        if veiculo is None:
            veiculo = VeiculoModel(None, data['placa'], data['tipo'], data['ano'],data['chassis'],data['numeroMotor'], data['cor'], data['proprietario_id'])
        else:
            veiculo.id = data['id']
            veiculo.placa = data['placa']
            veiculo.tipo = data['tipo']
            veiculo.ano = data['ano']
            veiculo.chassis = data['chassis']
            veiculo.numeroMotor = data['numeroMotor']
            veiculo.cor = data['cor']
            veiculo.proprietario_id = data['proprietario_id']

        veiculo.save_to_db()

        return veiculo.json()

    def delete(self):
        data = Veiculo.parser.parse_args()
        veiculo = VeiculoModel.find_by_id(data['id'])
        if veiculo:
            veiculo.delete_from_db()
            return {'message': 'Veiculo apagado.'}


class VeiculoById(Resource):
    def get(self, id):
        veiculo = VeiculoModel.find_by_id(id)
        if veiculo:
            return veiculo.json()
        return {'message': 'Nenhum veiculo com este ID foi encontrado.'}, 404


class VeiculoList(Resource):
    def get(self):
        return {'veiculos': [veiculo.json() for veiculo in VeiculoModel.query.all()]}
