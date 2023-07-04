from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..services import clientes_service

class ClienteList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        clientes_query = clientes_service.listar_clientes()
        clientes = clientes_query.paginate(page=page, per_page=per_page, error_out=False)
        clientes_items = [
            {
            'bairroent': item.clie_bairrores,
            'bloqueio': 'S' if item.clie_situacao == 'I' else 'N',
            'calculast': 'N',
            'cepent': item.clie_cepres,
            'cgcent': item.clie_cnpjcpf,
            'cliente': item.clie_razaosocial,
            'codatv1': item.clie_ramoatividade,
            'codcidade': item.clie_muni_codigo_res,
            'codcli': item.clie_codigo,
            'codcob': item.clie_lpgt_codigo,
            'codfuncultalter': item.clie_usualt,
            'codplpag': item.clie_fpgt_codigo,
            'codpraca': item.clie_rota_codigo,
            'codrota': item.clie_rota_codigo,
            'codusur1': item.clie_vend_codigo,
            'codusur2': item.clie_vend_alternativos,
            'condvenda1': 'S',
            'condvenda11': 'S',
            'condvenda13': 'N',
            'condvenda14': 'N',
            'condvenda20': 'N',
            'condvenda5': 'S',
            'condvenda7': 'N',
            'condvenda8': 'N',
            'condvenda9': 'N',
            'condvenda24': 'N',
            'condvenda4': 'N',
            'consumidorfinal': 'S' if 'CF' in item.clie_tipos else 'N',
            'contribuinte': item.clie_contribuinte,
            'email': item.clie_email,
            'emailnfe': item.clie_emailnfe,
            'enderent': item.clie_endres,
            'estent': item.clie_ufexprg,
            'fantasia': item.clie_nome,
            'ieent': item.clie_rgie,
            'isentoipi': 'S',
            'municent': item.muni_nome if item.muni_nome else '',
            'numeroent': item.clie_endresnumero,
            'telcom': item.clie_foneres,
            'telent': item.clie_fonecel,
            'tipofj': item.clie_tipo,
            'usadebcredrca': 'N',
            'validarmultiplovenda': 'N'
            } for item in clientes.items
        ]
        response = make_response(json.dumps({
            'items': clientes_items,
            'total': clientes.total,
            'page': clientes.page,
            'pages': clientes.pages,
            'has_prev': clientes.has_prev,
            'has_next': clientes.has_next,
            'prev_num': clientes.prev_num,
            'next_num': clientes.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(ClienteList, '/clientes') 