from flask import Blueprint, request, jsonify
from utils import auth
from models import errors, item
import json


item_controller = Blueprint('item_controller', __name__)

@item_controller.route("/item", methods=["GET"])
def getItems():

    #TODO: check login
    items = item.Item.getAllItems()
    print(items)
    return jsonify(items)

@item_controller.route("/item/<int:id>", methods=["GET"])
def getItemById(id):

    res = item.Item.getItemById(id)

    if isinstance(res, errors.ItemNotFound):
        return json.dumps({"message":res.message})

    return jsonify(res)
