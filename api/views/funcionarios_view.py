from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
import simplejson as json
import datetime
from ..services import funcionarios_service

class FuncionariosList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 100
        
        funcionarios_query = funcionarios_service.listar_funcionarios()
        funcionarios = funcionarios_query.paginate(page=page, per_page=per_page, error_out=False)
        funcionarios_items = [
            {
                'codsetor': item.func_tipos,
                'nome': item.func_nome,
                'email': item.func_email,
                'matricula': item.func_codigo,
                'celular': item.func_celular,
                'codfilial': item.func_unid_codigo,
                'tipo': 'M' if item.func_funcao == 'MOT' else 'F',
                'cpf': item.func_cpf,
                'situacao': item.func_situacao,
                'codveiculo': item.func_observacao,                
            } for item in funcionarios.items
        ]
        response = make_response(json.dumps({
            'items': funcionarios_items,
            'total': funcionarios.total,
            'page': funcionarios.page,
            'pages': funcionarios.pages,
            'has_prev': funcionarios.has_prev,
            'has_next': funcionarios.has_next,
            'prev_num': funcionarios.prev_num,
            'next_num': funcionarios.next_num
        }, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(FuncionariosList, '/funcionarios') 