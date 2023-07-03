from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..schemas import dctos_schema
from ..services import dctos_service

class DctosList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        dctos = dctos_service.listar_dctos().paginate(page=page, per_page=per_page, error_out=False)
        dctos_items = [item.to_dict() for item in dctos.items]
        response = make_response(json.dumps({
            'items': dctos_items,
            'total': dctos.total,
            'page': dctos.page,
            'pages': dctos.pages,
            'has_prev': dctos.has_prev,
            'has_next': dctos.has_next,
            'prev_num': dctos.prev_num,
            'next_num': dctos.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(DctosList, '/dctos') 

#end_point?page=2