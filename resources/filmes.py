from flask_restful import Resource, reqparse
from models.filmes import FilmeModel


class FilmeCadastro(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True)
    argumentos.add_argument('faixa_etaria', type=int, required=True)
    argumentos.add_argument('ano', type=int, required=True)
    argumentos.add_argument('genero', type=str, required=True)
    argumentos.add_argument('diretor', type=str, required=True)
    argumentos.add_argument('sinopse', type=str, required=True)

    def post(self):
        dados = FilmeCadastro.argumentos.parse_args()
        f = FilmeModel.find_filme(dados['nome'])
        print(dados.get('nome'))
        if FilmeModel.find_filme(dados.get('nome')):
            return {'message': 'This movie already exists.'}, 400
        else:
            filme = FilmeModel(**dados)
            filme.save_filme()
            return {'message': filme.json()}, 200


class Filmes(Resource):
    def get(self):
        return {"filmes": [filme.json() for filme in FilmeModel.query.all()]}, 200


class Filme(Resource):
    def get(self, filme_id):
        filme = FilmeModel.find_filme_by_id(filme_id)
        if filme:
            return filme.json()
        return {'message': 'Movie not found.'}, 404