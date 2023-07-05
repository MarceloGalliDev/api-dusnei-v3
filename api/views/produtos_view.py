from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..services import produtos_service

class ProdutosList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        produtos_query = produtos_service.listar_produtos()
        produtos = produtos_query.paginate(page=page, per_page=per_page, error_out=False)
        produtos_items = [
            {
                'aceitavendafracao': 'S',
                'classificfiscal': 'N',
                'codauxiliar': item.prod_codbarras,
                'codepto': item.prod_dpto_codigo,
                'codfornec': item.prod_forn_codigo,
                'codprod': item.prod_codigo,
                'codsec': item.prod_grup_codigo,
                'descricao': item.prod_descricao,
                'dtcadastro': item.prod_datacad,
                'embalagem': item.prun_qemb if item else None,
                'embalagemmaster': item.prod_qemb,
                'enviarforcavendas': 'S',
                'pesobruto': item.prod_peso,
                'pesoliq': item.prod_pesoliq,
                'pesovariavel': item.prod_balanca,
                'qtunit': item.prun_qemb if item else None,
                'qtunitcx': item.prod_qemb,
                'revenda': 'S',
                'tipoestoque': 'FR' if item.prun_setordep == '1' or item.prun_setordep == '3' else 'PA',
                'tipomerc': 'L',
                'unidade': item.prun_emb if item else None,
                'unidademaster': item.prod_emb,               
            } for item in produtos.items
        ]
        response = make_response(json.dumps({
            'items': produtos_items,
            'total': produtos.total,
            'page': produtos.page,
            'pages': produtos.pages,
            'has_prev': produtos.has_prev,
            'has_next': produtos.has_next,
            'prev_num': produtos.prev_num,
            'next_num': produtos.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(ProdutosList, '/produtos') 