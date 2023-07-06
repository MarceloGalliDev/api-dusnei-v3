from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import carregamentos_service

class CarregamentosList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        carregamentos = carregamentos_service.listar_carregamentos().paginate(page=page, per_page=per_page, error_out=False)
        carregamentos_items = [item.to_dict() for item in carregamentos.items]
        response = make_response(json.dumps({
            'items': carregamentos_items,
            'total': carregamentos.total,
            'page': carregamentos.page,
            'pages': carregamentos.pages,
            'has_prev': carregamentos.has_prev,
            'has_next': carregamentos.has_next,
            'prev_num': carregamentos.prev_num,
            'next_num': carregamentos.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(CarregamentosList, '/carregamentos') 

