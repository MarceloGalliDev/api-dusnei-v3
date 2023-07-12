from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import notas_saida_d_service

class NotasDList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 5000
        
        notas_d_query = notas_saida_d_service.listar_notas_d()
        notas_d = notas_d_query.paginate(page=page, per_page=per_page, error_out=False)
        notas_d_items = [
            {
                'codprod': str(item.nfed_prod_codigo),
                'codoper': 'S',
                'qt': item.nfed_qtde,
                'numseq': item.nfed_sequencial,
                'qtcont': item.nfed_qtde,
                'numtransvenda': int(item.nfed_transacao),
                'numtransitem': item.id,
                'numcar': str(item.mprc_carregamento),
                'numnota': int(item.nfec_numerodcto),
                'numped': int(item.nfec_transacao),
                'ptabela': item.mprc_prvdapadrao,
                'punitcont': item.nfed_valor,
                'punit': item.nfed_valor,
                'custofin': 0,
                'vlipi': 0,
                'st': 0
            } for item in notas_d.items
        ]
        response = make_response(json.dumps(notas_d_items, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(NotasDList, '/notas-saida-d') 