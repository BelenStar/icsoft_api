from flask import Blueprint, request, jsonify
from utils import auth
from models import errors, item, report
import json


report_controller = Blueprint('report_controller', __name__)

@report_controller.route("/report/items", methods=["GET"])
def generateItemsReport():

    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message":"no token given"}), 401

    res = auth.decode_auth_token(token)

    if isinstance(res, errors.InvalidToken):
        return jsonify({"message":"invalid token"}), 401

    res = report.Report.generateItemsReport()
    return jsonify(res)
