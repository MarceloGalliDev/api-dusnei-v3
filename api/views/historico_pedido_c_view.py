from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..schemas import historico_pedido_c_schema
from ..services import historico_pedido_c_service

class HistoricoPedidoCList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 5000
        
        dctos_query = historico_pedido_c_service.listar_historico_pedido_c()
        dctos = dctos_query.paginate(page=page, per_page=per_page, error_out=False)
        dctos_items = [
            {
                'codfunccanc': item.mdoc_usucanc if item.mdoc_usucanc is not None else '',
                'codemitente': item.mprc_unid_codigo,
                'codcli': str(item.mprc_codentidade),
                'numnota': int(item.mprc_numerodcto),
                'totpeso': item.mprc_peso,
                'origemped': (
                    'F' if item.mprc_dcto_codigo == '6666' else (
                        'R' if item.mprc_dcto_codigo == '7339' else (
                            'R' if item.mprc_dcto_codigo == '7338' else ''))),
                'posicao': (
                    'F' if item.mprc_status == 'N' else (
                        'C' if item.mprc_status == 'C' else (
                            'P' if item.mprc_status == 'P' else ''))),
                'vltabela': item.mprc_prvdapadrao,
                'numped': int(item.mprc_transacao),
                'condvenda': (
                    1 if item.mprc_dcto_codigo == '6666' or 
                    item.mprc_dcto_codigo == '7339' or 
                    item.mprc_dcto_codigo == '7338' else (
                        5 if item.mprc_dcto_codigo == '7267' else (
                            11 if item.mprc_dcto_codigo == '7318' or 
                            item.mprc_dcto_codigo == '7319' else ''))),
                'codfilial': item.mprc_fpgt_codigo,
                'vlatend': item.mprc_prvenda,
                'codcob': item.mprc_fpgt_codigo,
                'vltotal': item.mprc_prvenda,
                'data': item.mprc_datamvto,
                'numcar': str(item.mprc_carregamento),
                'numpedrca': 0,
                'obs': item.mprc_obs,
                'codplapg': '',
                'codsupervisor': item.vend_supe_codigo if item.vend_supe_codigo is not None else '',
                'totvolume': item.mprc_peso,
                'codpraca': item.clie_rota_codigo,
            } for item in dctos.items
        ]
        response = make_response(json.dumps(dctos_items, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(HistoricoPedidoCList, '/historicos-pedidos-c') 

