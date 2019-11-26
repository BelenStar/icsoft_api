from flask import Blueprint, request
from utils import auth
from models import errors
import json


auth_controller= Blueprint('auth_controller', __name__)

@auth_controller.route("/login", methods=["POST"])
def login():
    body = request.get_json(force=True)

    if body["username"] == "":
        return json.dumps({"message":"Username not given"}), 400
    if body["password"] == "":
        return json.dumps({"message":"Password not given"}), 400

    #si todo esta bien, result no es de tipo Error, es el JWT
    result = auth.login(body["username"], body["password"])


    if isinstance(result, errors.UsernameNotFound):
        return json.dumps({"message": result.message}), 401

    if isinstance(result, errors.IncorrectPassword):
        return json.dumps({"message": result.message}), 401

    if isinstance(result, NameError):
        return json.dumps({"message": str(result)}), 500


    
    return json.dumps({"token":str(result)})

def hello():
    return "YES YES YES"
