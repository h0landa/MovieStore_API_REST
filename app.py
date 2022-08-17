from flask import Flask
from flask_restful import Api
from resources.filmes import Filme, Filmes, FilmeCadastro

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'senha_secreta'


@app.before_request
def cria_banco():
    db.create_all()


api.add_resource(Filmes, '/filmes')
api.add_resource(FilmeCadastro, '/filmes/cadastro')
api.add_resource(Filme, '/filmes/<int:filme_id>')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
