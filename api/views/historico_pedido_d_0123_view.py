from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import historico_pedido_d_0123_service
import os
import logging
import time
import requests
import traceback

class HistoricoPedidosD0123List(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 200000
        
        historico_pedido_d_query = historico_pedido_d_0123_service.listar_historico_pedido_d_0123()
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
        
        logging.basicConfig(
            filename='api_post_log_historico_pedido_d_0123.txt', 
            level=logging.INFO, 
            format='%(asctime)s %(message)s', 
            datefmt='%d/%m/%Y %I:%M:%S %p -'
        )
        
        # self.post(historico_pedido_d_items)
        
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

    # def post(self, data):
    #     url = os.getenv('URL_HISTORICOS_PEDIDOS_ITENS')
    #     token = os.getenv('TOKEN')
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': f'Bearer {token}'
    #     }
        
    #     dados_iterados = len(data) // 5000
    #     if len(data) % 5000:
    #         dados_iterados += 1
            
    #     for i in range(dados_iterados):
    #         try:
    #             start = i * 5000
    #             end = start + 5000
    #             chunk = data[start:end]
                
    #             response = requests.post(
    #                 url, 
    #                 headers=headers, 
    #                 data=json.dumps(
    #                     chunk,
    #                     ensure_ascii=False, 
    #                     use_decimal=True, 
    #                     indent=4, 
    #                     default=lambda o: o.isoformat() if isinstance(
    #                         o, 
    #                         (datetime.date, datetime.datetime)
    #                     ) else None)
    #                 )
    #             response.raise_for_status()
                
    #             logging.info(f'Dados {i+1} enviado com sucesso!')
                
    #             if i != dados_iterados - 1:
    #                 time.sleep(20)
    #         except requests.exceptions.HTTPError as err:
    #             logging.error(f'HTTP Error: {err}')
    #         except Exception as err:
    #             logging.error(f'API Error: {err}')
    #             logging.error(f'Full Error: {traceback.format_exc()}')

api.add_resource(HistoricoPedidosD0123List, '/historico-pedido-d-0123') 