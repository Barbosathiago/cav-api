# Importação das bibliotecas necessárias
from flask import Flask
from flask_restful import Api

# Importação dos models
from resources.proprietario_resource import Proprietario, ProprietarioById, ProprietarioList
from resources.dp_resource import Dp, DpById, DpList
#
#
#

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'IAMTHEKIDYOUKNOWWHATIMEAN'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Registro dos resources
api.add_resource(Proprietario, '/proprietario')
api.add_resource(ProprietarioById, '/proprietario/<string:id>')
api.add_resource(ProprietarioList, '/proprietarios')

api.add_resource(Dp, '/dp')
api.add_resource(DpById, '/dp/<string:id>')
api.add_resource(DpList, '/dps')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
