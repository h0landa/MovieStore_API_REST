from conexao import db


class FilmeModel(db.Model):
    __tablename__ = 'filmes'

    filme_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagem = db.Column(db.Text)
    nome = db.Column(db.String(80))
    faixa_etaria = db.Column(db.Integer)
    ano = db.Column(db.Integer)
    genero = db.Column(db.String)
    diretor = db.Column(db.String)
    sinopse = db.Column(db.Text)
    ator_id = db.Column(db.Integer, db.ForeignKey('atores.ator_id'))

    def __init__(self, imagem, nome, faixa_etaria, ano, genero, diretor, sinopse, ator_id):
        self.imagem = imagem
        self.nome = nome
        self.faixa_etaria = faixa_etaria
        self.ano = ano
        self.genero = genero
        self.diretor = diretor
        self.sinopse = sinopse
        self.ator_id = ator_id

    def json(self):
        return {
            'filme_id': self.filme_id,
            'imagem': self.imagem,
            'nome': self.nome,
            'faixa_etaria': self.faixa_etaria,
            'ano': self.ano,
            'genero': self.genero,
            'diretor': self.diretor,
            'sinopse': self.sinopse,
            'ator_id': self.ator_id
        }

    @classmethod
    def find_filme(cls, nome):
        filme = cls.query.filter_by(nome=nome).first()
        if filme:
            return filme
        return None

    @classmethod
    def find_filme_by_id(cls, filme_id):
        filme = cls.query.filter_by(filme_id=filme_id).first()
        if filme:
            return filme
        return None

    @classmethod
    def catch_all(cls):
        filmes = cls.query.all()
        return filmes

    def save_filme(self):
        db.session.add(self)
        db.session.commit()

    def delete_filmes(self):
        db.session.delete(self)
        db.session.commit()

