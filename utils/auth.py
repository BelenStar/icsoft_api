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

    if password != result[0][5]:
        return errors.IncorrectPassword()

    jwt = encode_auth_token(result[0][0])
    return jwt


def encode_auth_token(id):
    try:
        token = jwt.encode( {'id': str(id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),}, "secret", algorithm = 'HS256').decode('utf-8')
        return token
    except Exception as e:
        print("utils/auth.py encode_auth_token", e)
        return e

def decode_auth_token(token):
    try:
        payload = jwt.decode(token, "secret")
        return payload["id"]

    except jwt.InvalidTokenError as e:
        return errors.InvalidToken()
