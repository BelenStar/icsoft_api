from flask import Blueprint, jsonify
from utils import auth
from models import user
import json

users_controller = Blueprint('users_controller', __name__)

@users_controller.route("/users")
def users():
    return jsonify(user.User.getAllUsers())
