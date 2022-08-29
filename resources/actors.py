from flask_restful import Resource, reqparse
from models.actors import ActorModel
import sqlite3


class Actors(Resource):
    def get(self):
        atores = [ator.json() for ator in ActorModel.query.all()]
        return {"atores": atores}


class Actor(Resource):
    def get(self, ator_id):
        actor = ActorModel.find_actor_by_id(ator_id)
        if actor:
            return {"ator": actor.json()}
        else:
            return {"message": f"Actor id '{ator_id}' not found."}, 404

    def delete(self, ator_id):
        ator = ActorModel.find_actor_by_id(ator_id)
        if ator:
            ator.delete_actor()
            return {"message": f"Actor {ator.nome} has deleted"}, 200


class ActorRegister(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('foto', type=str)
    argumentos.add_argument('nome', type=str, required=True, help="The 'name' field cannot be blank")
    argumentos.add_argument('idade', type=int, required=True, help="The 'idade' field cannot be blank")
    argumentos.add_argument('altura', type=float, required=True, help="The 'altura' field cannot be blank")

    def post(self):
        dados = ActorRegister.argumentos.parse_args()
        if not ActorModel.find_actor(dados['nome']):
            actor = ActorModel(**dados)
            actor.save_actor()
            return actor.json()
        return {"message": "This actor already exists"}, 400
