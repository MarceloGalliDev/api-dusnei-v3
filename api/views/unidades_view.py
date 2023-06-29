from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
from ..schemas import unidades_schema
from ..services import unidades_service

class UnidadesList(Resource):
    def get(self):
        unidades = unidades_service.listar_unidades()
        cs = unidades_schema.UnidadesSchema()
        response =  make_response(json.dumps(unidades, ensure_ascii=False, use_decimal=True, indent=4), 200)
        response.mimetype = 'application/json'  
        
        return response  

api.add_resource(UnidadesList, '/unidades')