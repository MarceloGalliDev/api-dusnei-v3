from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..services import vendedores_service

class VendedoresList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 5000
        
        vendedores_query = vendedores_service.listar_vendedores()
        vendedores = vendedores_query.paginate(page=page, per_page=per_page, error_out=False)
        vendedores_items = [
            {
                'bloqueio': 'S' if 'Inativado' in item.vend_nome else 'N',
                'codsupervisor': item.vend_supe_codigo,
                'codusur': item.vend_codigo,
                'codfilial': item.vend_unid_codigo,
                'nome': item.vend_nome,
                'tipovend': 'R',
                'usadebcredrca': 'N'
            } for item in vendedores.items
        ]
        response = make_response(json.dumps(vendedores_items, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response 

api.add_resource(VendedoresList, '/vendedores')