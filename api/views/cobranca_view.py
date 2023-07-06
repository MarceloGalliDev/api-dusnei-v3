from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..services import cobranca_service

class CobrancaList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        cobranca_query = cobranca_service.listar_cobranca()
        cobranca = cobranca_query.paginate(page=page, per_page=per_page, error_out=False)
        cobranca_items = [
            {
                'boleto': 'S' if item.pfin_lpgt_codigo == '002' else 'N',
                'cartao': 'S' if item.pfin_lpgt_codigo == '011' else 'N',
                'cobranca': item.mprc_obs,
                'codcob': item.pfin_numerodcto,
                'nivelvenda': '01',
                'prazomaximovenda': ((item.pfin_datamvto - item.pfin_datavcto).days)*-1,
                'txjuros': '0,03',
                'percmulta': '2,00',
                'tipovenda': item.mprc_fpgt_codigo,
                'tipocobranca': item.mprc_fpgt_codigo,
            } for item in cobranca.items
        ]
        response = make_response(json.dumps({
            'items': cobranca_items,
            'total': cobranca.total,
            'page': cobranca.page,
            'pages': cobranca.pages,
            'has_prev': cobranca.has_prev,
            'has_next': cobranca.has_next,
            'prev_num': cobranca.prev_num,
            'next_num': cobranca.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(CobrancaList, '/cobranca') 
        