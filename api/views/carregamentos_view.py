from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import carregamentos_service

class CarregamentosList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 5000
        
        carregamentos_query = carregamentos_service.listar_carregamentos()
        carregamentos = carregamentos_query.paginate(page=page, per_page=per_page, error_out=False)
        carregamentos_items = [
            {
                'numcar': item.carr_numero,
                'datamon': item.carr_datamvto,
                'dtfat': item.carr_datasaida,
                'numnotas': item.carr_qpedidos,
                'origem_car': 'ERP',
                'codmotorista': str(item.carr_motorista),
                'codveiculo': item.carr_placa,
                'totpeso': item.carr_pesoprodutos,
                'totvolume': item.carr_volumeprodutos,
                'vltotal': item.carr_totalprodutos,
            } for item in carregamentos.items
        ]
        response = make_response(json.dumps(carregamentos_items, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(CarregamentosList, '/carregamentos') 

