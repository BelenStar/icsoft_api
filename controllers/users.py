from flask import Blueprint
from utils import auth
from models import user
import json

users_controller = Blueprint('users_controller', __name__)

@users_controller.route("/users")
def login():
    return json.dumps(user.User.getAllUsers())
