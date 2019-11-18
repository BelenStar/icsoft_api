from repository import db_logic
from models import user as us
from models import errors
import jwt
import datetime

#Devuelve una lista de objetos(serializados) de la clase usuario

def login(username, password):

    result = db_logic.selectUserByUsername(username)

    #Username not found
    if len(result) == 0:
        return errors.UsernameNotFound()

    print(result)
    if password != result[0][5]:
        return errors.IncorrectPassword()

    jwt = encode_auth_token(result[0])
    print("utils/auth.py",jwt)
    return jwt


def encode_auth_token(id):
    try:
        token = jwt.encode( {'id': str(id)}, "secret", algorithm = 'HS256')
        return token
    except Exception as e:
        print("utils/auth.py encode_auth_token", e)
        return e

def decode_auth_token(token):

    try:
        payload = jwt.decode(token, app.config.get("SECRET_KEY"))
        return payload["sub"]

    except jwt.InvalidTokenError:
        #TODO: change to custom error
        return 'Invalid token. Please log in again.'
