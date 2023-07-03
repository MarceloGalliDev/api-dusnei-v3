from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
from ..schemas import vendedores_schema
from ..services import vendedores_service

class VendedoresList(Resource):
    def get(self):
        vendedores = vendedores_service.listar_vendedores()
        cs = vendedores_schema.VendedoresSchema()
        response =  make_response(json.dumps(vendedores, ensure_ascii=False, use_decimal=True, indent=4), 200)
        response.mimetype = 'application/json'  
        
        return response  

api.add_resource(VendedoresList, '/vendedores')