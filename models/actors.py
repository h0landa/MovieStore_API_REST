from conexao import db
from models.filmes import FilmeModel


class ActorModel(db.Model):
    __tablename__ = 'atores'

    ator_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    foto = db.Column(db.Text)
    nome = db.Column(db.String(40))
    idade = db.Column(db.Integer)
    altura = db.Column(db.Float(precision=2))
    filmes = db.relationship('FilmeModel')

    def __init__(self, foto, nome, idade, altura):
        self.foto = foto
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def json(self):
        return {
            "ator_id": self.ator_id,
            "foto": self.foto,
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura,
            "filmes": [filme.json() for filme in self.filmes]
        }

    def save_actor(self):
        db.session.add(self)
        db.session.commit()

    def delete_actor(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_actor(cls, nome):
        ator = cls.query.filter_by(nome=nome).first()
        if ator:
            return ator
        return None

    @classmethod
    def find_actor_by_id(cls, ator_id):
        ator = cls.query.filter_by(ator_id=ator_id).first()
        if ator:
            return ator
        return None

