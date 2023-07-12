from api import api
from flask_restful import Resource
from flask import request, make_response
import simplejson as json
import datetime
from ..services import notas_saida_c_service

class NotasCList(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = 5000
        
        notas_c_query = notas_saida_c_service.listar_notas_c()
        notas_c = notas_c_query.paginate(page=page, per_page=per_page, error_out=False)
        notas_c_items = [
            {
                'numcar': item.mprc_carregamento,
                'numnota': str(item.nfec_numerodcto),
                'serie': item.nfec_serie,
                'codusur': str(item.mdoc_usulcto),
                'condvenda': int(item.mprc_dcto_codigo),
                'numtransvenda': int(item.nfec_transacao),
                'dtsaida': item.nfec_datasaida,
                'dtfat': item.nfec_datamvto,
                'dtentrega': item.nfec_dataemissao,
                'vltotal': item.nfec_totaldcto,
                'especie': 'NF',
                'codclie': str(item.nfec_codentidade),
                'numped': int(item.nfec_transacao),
                'codcob': item.clie_lpgt_codigo,        
                'codplpag': item.nfec_fpgt_codigo,
                'codfilial': item.nfec_unid_codigo,
                'numseq': item.nfec_idlote,
                'totpeso': item.nfec_pesoliq,
                'totvolume': item.nfec_volumes,
                'codsupervisor': '001' if item.nfec_unid_codigo == '001' else (
                    '003' if item.nfec_unid_codigo == '003' or item.nfec_unid_codigo == '010' else (
                        '006' if item.nfec_unid_codigo == '002' else None 
                    )
                ) 
            } for item in notas_c.items
        ]
        response = make_response(json.dumps(notas_c_items, ensure_ascii=False, use_decimal=True, indent=4, default=lambda o: o.isoformat() if isinstance(o, (datetime.date, datetime.datetime)) else None), 200)

        response.mimetype = 'application/json'
        return response

api.add_resource(NotasCList, '/notas-saida-c') 