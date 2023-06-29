from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
from ..schemas import cidades_schema
from ..services import cidades_service

class CidadesList(Resource):
    def get(self):
        cidades = cidades_service.listar_cidades()
        cs = cidades_schema.CidadesSchema()
        response =  make_response(json.dumps(cidades, ensure_ascii=False, use_decimal=True, indent=4), 200)
        response.mimetype = 'application/json'  
        
        return response  

api.add_resource(CidadesList, '/cidades')