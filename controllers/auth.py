from flask import Blueprint
from utils import auth
import json

auth_controller= Blueprint('auth_controller', __name__)

@auth_controller.route("/login")
def login():
    return json.dumps(auth.login())

def hello():
    return "YES YES YES"
