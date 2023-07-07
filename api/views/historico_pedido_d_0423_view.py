from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import historico_pedido_d_0423_service

class HistoricoPedidosD0423List(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        historico_pedido_d_query = historico_pedido_d_0423_service.listar_historico_pedido_d_0423()
        historico_pedido_d = historico_pedido_d_query.paginate(page=page, per_page=per_page, error_out=False)
        historico_pedido_d_items = [
            {
                'numped': item.mprd_transacao,
                'qt': item.mprd_qtde,
                'numseq': item.mprd_sequencial,
                'pvenda': item.mprd_valor,
                'codprod': item.mprd_prod_codigo,
                'ptabela': item.mprd_nextra6,
                'percom': item.prun_comissao if item else None,
                'data': item.mprd_datamvto,
                'posicao': 'F' if item.mprd_status == 'N' else 'C',            
            } for item in historico_pedido_d.items
        ]
        response = make_response(json.dumps({
            'items': historico_pedido_d_items,
            'total': historico_pedido_d.total,
            'page': historico_pedido_d.page,
            'pages': historico_pedido_d.pages,
            'has_prev': historico_pedido_d.has_prev,
            'has_next': historico_pedido_d.has_next,
            'prev_num': historico_pedido_d.prev_num,
            'next_num': historico_pedido_d.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(HistoricoPedidosD0423List, '/historico_pedido_d_0423') 