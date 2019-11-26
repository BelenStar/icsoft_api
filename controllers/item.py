from flask import Blueprint, request, jsonify
from utils import auth
from models import errors, item
import json


item_controller = Blueprint('item_controller', __name__)

@item_controller.route("/item", methods=["GET"])
def getItems():

    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message":"no token given"}), 401

    res = auth.decode_auth_token(token)

    if isinstance(res, errors.InvalidToken):
        return jsonify({"message":"invalid token"}), 401


    items = item.Item.getAllItems()
    print(items)
    return jsonify(items)

@item_controller.route("/item/<int:id>", methods=["GET"])
def getItemById(id):
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message":"no token given"}), 401

    res = auth.decode_auth_token(token)

    if isinstance(res, errors.InvalidToken):
        return jsonify({"message":"invalid token"}), 401

    res = item.Item.getItemById(id)

    if isinstance(res, errors.ItemNotFound):
        return json.dumps({"message":res.message})

    return jsonify(res)

@item_controller.route("/additem/<int:id>", methods=["GET"])
def addItem(id):
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message":"no token given"}), 401

    res = auth.decode_auth_token(token)

    if isinstance(res, errors.InvalidToken):
        return jsonify({"message":"invalid token"}), 401

    res = item.Item.addItem(id, res)
    if isinstance(res, errors.ItemNotFound):
            return jsonify({"message": res.message}), 404
    return jsonify({"message":"item added"})
