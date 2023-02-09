from flask import request, jsonify
import json

def configure(app):

    @app.route('/')
    def alive():
        return "Alive"

    @app.route("/condutor/info/")
    def getInfoCondutor():
        condutorService = CondutorService()
        print(condutorService.getInformacoesCondutor())
        return "ok"

    # @app.route("/condutor/get/", methods=['GET'])
    # def getCondutor():
    #     try:
    #         condutorService = CondutorService()
    #         return condutorService.getCondutor(request)
    #     except Exception as e:
    #         return str(e), 500