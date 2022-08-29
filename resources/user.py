from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import hmac
from blacklist import BLACKLIST


argumentos = reqparse.RequestParser()
argumentos.add_argument('login', type=str, required=True, help="The 'login' field cannot be blank")
argumentos.add_argument('password', type=str, required=True, help="The 'password' field cannot be blank")


class User(Resource):
    def get(self, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            return {
                "user_id": user_id,
                "login": user.login
            }
        return {"message": "User not found."}, 404

    @jwt_required()
    def put(self, user_id):
        user = UserModel.find_by_id(user_id)
        dados = argumentos.parse_args()
        if user:
            UserModel.update_user(**dados)
            return {"message": "User successfully changed."}, 200
        else:
            return {"message": "User not found."}, 404

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            try:
                user.delete_user()
                return {"message": f"User '{user.login}' has deleted."}, 200
            except:
                return {"message": "An internal error occurred while trying to delete user."}, 500
        return {"message": "User not found."}, 404


class UserRegister(Resource):
    def post(self):
        dados = argumentos.parse_args()
        user = UserModel(**dados)
        if not UserModel.find_user(dados['login']):
            try:
                user.save_user()
                return {"message": "User created successfully!"}, 200
            except:
                return {"message": "An internal error occurred while trying to save user"}, 500
        else:
             return {"message": f"The login {dados['login']} already exists."}

class Login(Resource):
    def safe_str_cmp(self, a: str, b: str) -> bool:
        """Esta função compara strings em um tempo relativamente constante.
        requer que o comprimento de pelo menos uma string seja conhecido antecipadamente.

        Retorna `True` se as duas strings forem iguais ou `False` se não forem.
        """

        if isinstance(a, str):
            a = a.encode("utf-8")  # type: ignore

        if isinstance(b, str):
            b = b.encode("utf-8")  # type: ignore
        return hmac.compare_digest(a, b)

    def post(self):
        dados = argumentos.parse_args()
        user = UserModel.find_user(dados['login'])
        if user and self.safe_str_cmp(user.password, dados['password']):
            access_token = create_access_token(identity=user.user_id)
            return {"access token": access_token}, 200
        else:
            return {"message": "This username or password is incorrect"}, 401


class Logout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {"message": "Logged out successfully"}
