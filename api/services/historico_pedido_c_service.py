from ..models import historico_pedido_c_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_historico_pedido_c():
    hist = aliased(historico_pedido_c_model.HistoricoPedidosCModel)
    historico = db.session.query(
        hist.mprc_unid_codigo,
        hist.mprc_codentidade,
        hist.mprc_numerodcto,
        hist.mprc_peso,
        hist.mprc_dcto_codigo,
        hist.mprc_status,
        hist.mprc_prvdapadrao,
        hist.mprc_prvenda,
        hist.mprc_fpgt_codigo,
        hist.mprc_datamvto,
        hist.dctos
    ).filter(
        hist.mprc_dcto_codigo.in_(['6666','7339','7338','7260','7263','7262','7268'])
    ).order_by(desc(hist.mprc_datamvto)
    ).all()
    return [
        {
            'codfunccalc': h.dctos.mdoc_usucanc if h.dctos else None,
            'codemitente': h.mprc_unid_codigo,
            'codcli': h.mprc_codentidade,
            'numnota': h.mprc_numerodcto,
            'totpeso': h.mprc_peso,
            'origemped': h.mprc_dcto_codigo,
            'posicao': h.mprc_status,
            'vltabela': h.mprc_prvdapadrao,
            'condvenda': h.mprc_dcto_codigo,
            'codfilial': h.mprc_unid_codigo,
            'vlatend': h.mprc_prvenda,
            'codcob': h.mprc_fpgt_codigo,
            'vltotal': h.mprc_prvenda,
            'data': h.mprc_datamvto,
        } for h in historico
    ]