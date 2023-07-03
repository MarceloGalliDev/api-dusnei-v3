from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
from ..schemas import supervisores_schema
from ..services import supervisores_service

class SupervisoresList(Resource):
    def get(self):
        supervisores = supervisores_service.listar_supervisores()
        cs = supervisores_schema.SupervisoresSchema()
        response =  make_response(json.dumps(supervisores, ensure_ascii=False, use_decimal=True, indent=4), 200)
        response.mimetype = 'application/json'  
        
        return response  

api.add_resource(SupervisoresList, '/supervisores')