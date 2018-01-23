# Importação das bibliotecas necessárias
import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# Importação dos models
from resources.proprietario_resource import Proprietario, ProprietarioById, ProprietarioList
from resources.dp_resource import Dp, DpById, DpList
from resources.veiculo_resource import Veiculo, VeiculoById, VeiculoList
from resources.ocorrencia_resource import Ocorrencia, OcorrenciabyId, OcorrenciaList
from resources.tipoOcorrencia_resource import TipoOcorrencia, TipoById, TipoList
#
#
#

app = Flask(__name__)
# CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'IAMTHEKIDYOUKNOWWHATIMEAN'
api = Api(app)


# Registro dos resources
api.add_resource(Proprietario, '/proprietario')
api.add_resource(ProprietarioById, '/proprietario/<string:id>')
api.add_resource(ProprietarioList, '/proprietarios')

api.add_resource(Dp, '/dp')
api.add_resource(DpById, '/dp/<string:id>')
api.add_resource(DpList, '/dps')

api.add_resource(Veiculo, '/veiculo')
api.add_resource(VeiculoById, '/veiculo/<string:id>')
api.add_resource(VeiculoList, '/veiculos')

api.add_resource(Ocorrencia, '/ocorrencia')
api.add_resource(OcorrenciabyId, '/ocorrencia/<string:id>')
api.add_resource(OcorrenciaList, '/ocorrencias')

api.add_resource(TipoOcorrencia, '/ocorrencia/tipo')
api.add_resource(TipoById, '/ocorrencia/tipo/<string:id>')
api.add_resource(TipoList, '/ocorrencia/tipos')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
