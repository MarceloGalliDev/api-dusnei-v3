from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import historico_pedido_d_0723_service

class HistoricoPedidosD0723List(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 5000
        
        historico_pedido_d_query = historico_pedido_d_0723_service.listar_historico_pedido_d_0723()
        historico_pedido_d = historico_pedido_d_query.paginate(page=page, per_page=per_page, error_out=False)
        historico_pedido_d_items = [
            {
                'numped': int(item.mprd_transacao),
                'qt': item.mprd_qtde,
                'numseq': item.mprd_sequencial,
                'pvenda': item.mprd_valor,
                'codprod': str(item.mprd_prod_codigo),
                'ptabela': item.mprd_nextra6,
                'percom': item.prun_comissao if item else None,
                'data': item.mprd_datamvto,
                'posicao': 'F' if item.mprd_status == 'N' else 'C',             
            } for item in historico_pedido_d.items
        ]
        response = make_response(json.dumps(
            historico_pedido_d_items,
            ensure_ascii=False, 
            use_decimal=True, 
            indent=4, 
            default=lambda o: o.isoformat() if isinstance(
                o, 
                (datetime.date, datetime.datetime)
            ) else None), 
            200
        )

        response.mimetype = 'application/json'
        return response

api.add_resource(HistoricoPedidosD0723List, '/historico-pedido-d-0723') 