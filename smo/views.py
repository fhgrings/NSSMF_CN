from flask import request, jsonify
import json
from src.services.ControllerKeyService import ControllerKeyService


def configure(app):

    @app.route('/')
    def alive():
        return "Alive"

    @app.route("/controllerKey/", methods=['GET'])
    def getInfoCondutor():
        try:
            controller = ControllerKeyService()
            return controller.getControllerKey(request)
        except Exception as e:
            return str(e), 500
            
    @app.route("/controllerKey/", methods=['POST'])
    def getCondutor():
        try:
            controller = ControllerKeyService()
            return controller.createControllerKey(request)
        except Exception as e:
            return str(e), 500