from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..services import estoque_service

class EstoqueList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        estoque = estoque_service.listar_estoque().paginate(page=page, per_page=per_page, error_out=False)
        estoque_items = [item.to_dict() for item in estoque.items]
        response = make_response(json.dumps({
            'items': estoque_items,
            'total': estoque.total,
            'page': estoque.page,
            'pages': estoque.pages,
            'has_prev': estoque.has_prev,
            'has_next': estoque.has_next,
            'prev_num': estoque.prev_num,
            'next_num': estoque.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(EstoqueList, '/estoque') 

