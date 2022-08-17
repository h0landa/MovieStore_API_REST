from flask_restful import Resource, reqparse
from models.filmes import FilmeModel


class Filmes(Resource):
    def get(self):
        return [filme.json() for filme in FilmeModel.catch_all()], 200


class Filme(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True)
    argumentos.add_argument('feixa_etaria', type=int, required=True)
    argumentos.add_argument('ano', type=int, required=True)
    argumentos.add_argument('genero', type=str, required=True)
    argumentos.add_argument('diretor', type=str, required=True)
    argumentos.add_argument('sinopse', type=str, required=True)

    def post(self):
        dados = Filme.argumentos.parse_args()
        if FilmeModel.find_filme(dados.get('nome')):
            return {'message': 'This movie already exists.'}, 400
        else:
            filme = FilmeModel(**dados)
            filme.save_filme()
            return {'message': filme.json()}, 200
