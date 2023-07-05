from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import pendencias_financeiras_service

class PendenciasFinanceirasList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        pendfin = pendencias_financeiras_service.listar_pendencias_financeiras().paginate(page=page, per_page=per_page, error_out=False)
        pendfin_items = [item.to_dict() for item in pendfin.items]
        response = make_response(json.dumps({
            'items': pendfin_items,
            'total': pendfin.total,
            'page': pendfin.page,
            'pages': pendfin.pages,
            'has_prev': pendfin.has_prev,
            'has_next': pendfin.has_next,
            'prev_num': pendfin.prev_num,
            'next_num': pendfin.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(PendenciasFinanceirasList, '/pendencias_financeiras') 

