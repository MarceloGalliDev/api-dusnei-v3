from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import departamentos_schema
from ..services import departamentos_service

class DepartamentosList(Resource):
    def get(self):
        departamentos = departamentos_service.listar_departamentos()
        cs = departamentos_schema.DepartamentosSchema()
        return make_response(jsonify(departamentos), 200)
    

api.add_resource(DepartamentosList, '/departamentos')