from flask_restful import Resource, reqparse
from models.filmes import FilmeModel
from flask_jwt_extended import jwt_required
import sqlite3


path_params = reqparse.RequestParser()
path_params.add_argument('faixa_etaria_min', default=0, type=int, location="args")
path_params.add_argument('faixa_etaria_max', default=100, type=int, location="args")
path_params.add_argument('ano_min', default=0, type=int, location="args")
path_params.add_argument('ano_max', default=10000, type=int, location="args")
path_params.add_argument('genero', type=str, location="args")
path_params.add_argument('limit', default=10, type=int, location="args")
path_params.add_argument('offset', default=0, type=int, location="args")


class Filmes(Resource):
    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        dados = path_params.parse_args()
        dados_filtrados = {chave: dados[chave] for chave in dados if dados[chave] is not None}
        if dados.get('genero'):
            consulta = '''SELECT * FROM filmes WHERE (faixa_etaria >= ? and faixa_etaria <= ?) and (ano >= ? and ano <= ?) and
            genero = ? LIMIT ? OFFSET ?'''
            parametros = tuple([dados_filtrados[chave] for chave in dados_filtrados])
            try:
                resultado = cursor.execute(consulta, parametros).fetchall()
            except:
                return {"message": "An internal error occurred while trying to make the query"}, 500
        else:
            consulta = '''SELECT * FROM filmes WHERE (faixa_etaria >= ? and faixa_etaria <= ?) and (ano >= ? and ano <= ?)
            LIMIT ? OFFSET ?'''
            parametros = tuple([dados_filtrados[chave] for chave in dados_filtrados])
            try:
                resultado = cursor.execute(consulta, parametros).fetchall()
            except:
                return {"message": "An internal error occurred while trying to make the query"}, 500
        filmes = []
        for f in resultado:
            filmes.append({
                "nome": f[1],
                "faixa_etaria": f[2],
                "ano": f[3],
                "genero": f[4],
                "diretor": f[5],
                "sinopse": f[6]
            })
        return {"filmes": filmes}, 200


class Filme(Resource):
    def get(self, filme_id):
        filme = FilmeModel.find_filme_by_id(filme_id)
        if filme:
            return filme.json()
        return {'message': 'Movie not found.'}, 404
    @jwt_required()
    def delete(self, filme_id):
        filme = FilmeModel.find_filme_by_id(filme_id)
        if filme:
            try:
                FilmeModel.delete_filmes(filme)
                return {"message": f"Movie Name: {filme.nome}, has deleted"}
            except:
                return {"message": "An internal error occurred trying to delete movie."}, 500
        else:
            return {"message": "Movie not found."}, 404


class FilmeCadastro(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('imagem', type=str, required=True)
    argumentos.add_argument('nome', type=str, required=True)
    argumentos.add_argument('faixa_etaria', type=int, required=True)
    argumentos.add_argument('ano', type=int, required=True)
    argumentos.add_argument('genero', type=str, required=True)
    argumentos.add_argument('diretor', type=str, required=True)
    argumentos.add_argument('sinopse', type=str, required=True)
    argumentos.add_argument('ator_id', type=int)

    @jwt_required()
    def post(self):
        dados = FilmeCadastro.argumentos.parse_args()
        f = FilmeModel.find_filme(dados['nome'])
        print(dados.get('nome'))
        if FilmeModel.find_filme(dados.get('nome')):
            return {'message': f"The movie '{dados['nome']}' already exists."}, 400
        else:
            filme = FilmeModel(**dados)
            try:
                filme.save_filme()
                return {'message': filme.json()}, 200
            except:
                return {"message": "An error internal occurred trying to save a filme"}, 500
