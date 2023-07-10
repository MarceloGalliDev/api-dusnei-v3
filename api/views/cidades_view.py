from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
from ..services import cidades_service
import datetime

class CidadesList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 5000       
        
        cidades_query = cidades_service.listar_cidades()
        cidades = cidades_query.paginate(page=page, per_page=per_page, error_out=False)
        cidades_items = [
            {
                'codcidade': str(item.muni_codigo),
                'codibge': str(item.muni_codigoibge),
                'nomecidade': item.muni_nome,
                'uf': item.muni_uf,
            } for item in cidades.items
        ]

        response = make_response(json.dumps(cidades_items, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response
  

api.add_resource(CidadesList, '/cidades')