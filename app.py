import datetime
from flask import Flask, jsonify
from flask_restful import Api
from resources.filmes import Filme, Filmes, FilmeCadastro
from resources.user import User, UserRegister, Login, Logout
from resources.actors import Actor, Actors, ActorRegister
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'senha_secreta'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)


@app.before_request
def cria_banco():
    db.create_all()


@jwt.token_in_blocklist_loader
def verify_blocklist(self, token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_access_invalid(jwt_header, jwt_payload):
    return jsonify({"message": "You have been logged out."}), 401


api.add_resource(Filmes, '/filmes')
api.add_resource(FilmeCadastro, '/filmes/cadastro')
api.add_resource(Filme, '/filmes/<int:filme_id>')
api.add_resource(UserRegister, '/user/cadastro')
api.add_resource(Login, '/user/login')
api.add_resource(Logout, '/user/logout')
api.add_resource(Actor, '/atores/<int:ator_id>')
api.add_resource(Actors, '/atores')
api.add_resource(ActorRegister, '/atores/cadastro')
api.add_resource(User, '/user/<int:user_id>')


if __name__ == '__main__':
    from conexao import db
    db.init_app(app)
    app.run(debug=True)
