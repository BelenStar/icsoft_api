from repository import db_logic
from models import user as us
import datetime

#Devuelve una lista de objetos(serializados) de la clase usuario

def login():

    return "NOT YET IMPLEMENTED"


def encode_auth_token(id):
    try:
        payload = {
            'iat': datetime.datetime.now(),
            'sub': id
        }
        token = jwt.encode(
            payload,
            app.config.get("SECRET_KEY"),
            algorithm = 'HS256'
        )
        return token
    except Exception as e:
        return e

def decode_auth_token(token):

    try:
        payload = jwt.decode(token, app.config.get("SECRET_KEY"))
        return payload["sub"]

    except jwt.InvalidTokenError:
        #TODO: change to custom error
        return 'Invalid token. Please log in again.'
