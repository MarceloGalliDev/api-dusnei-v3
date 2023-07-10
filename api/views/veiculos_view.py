from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import veiculos_service

class VeiculosList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        veiculos_query = veiculos_service.listar_veiculos()
        veiculos = veiculos_query.paginate(page=page, per_page=per_page, error_out=False)
        veiculos_items = [
            {
                'codveiculo': item.tran_codigo,
                'descricao': item.tran_nome,
                'placa': item.tran_placa,
                'volume': item.tran_maxvolume,
                'pesocargakg': item.tran_maxpeso,
                'situacao': 'L' if item.tran_situacao == 'N' else (
                    'I' if item.tran_situacao == 'I' else item.tran_situacao
                    ),
                'codfilial': item.tran_unid_codigo,               
            } for item in veiculos.items
        ]
        response = make_response(json.dumps({
            'items': veiculos_items,
            'total': veiculos.total,
            'page': veiculos.page,
            'pages': veiculos.pages,
            'has_prev': veiculos.has_prev,
            'has_next': veiculos.has_next,
            'prev_num': veiculos.prev_num,
            'next_num': veiculos.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(VeiculosList, '/veiculos') 