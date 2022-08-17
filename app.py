from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SECRET_KEY'] = 'senha_secreta'

if __name__ == '__main__':
    from sqlalchemy import db
    db.init_app()
    app.run(debug=True)
