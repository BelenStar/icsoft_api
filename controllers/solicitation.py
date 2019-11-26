from flask import Blueprint, request, jsonify
from utils import auth
from models import errors, item, solicitation
import json


solicitation_controller = Blueprint('solicitation_controller', __name__)

@solicitation_controller.route("/solicitation/items/<int:id>", methods=["GET"])
def solicitateItem(id):
    token = request.headers.get("Authorization")
    if token == "":
        return jsonify({"message":"no token provided"})
    res = auth.decode_auth_token(token)

    if isinstance(res, errors.Error):
        return jsonify({"message":res.message})

    report = solicitation.Solicitation.makeSolicitation(id, res)
    if isinstance(report, errors.Error):
        return jsonify({"message":report.message})

    return jsonify(report)
