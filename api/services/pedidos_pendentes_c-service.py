from ..models import pedidos_pendentes_c_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_pedidos_pendentes_c():
    pend = pedidos_pendentes_c_model.PedidosPendentesCModel
    
    pedidos_pend = db.session.query(
        pend.pvec_numero,
        pend.pvec_dcto_codigo,
        pend.pvec_unid_codigo,
        pend.pvec_carregamento,
        pend.pvec_status,
        pend.pvec_datamvto,
        pend.pvec_database,
        pend.pvec_databaixa,
        pend.pvec_vend_codigo,
        pend.pvec_rota_codigo,
        pend.pvec_fpgto_codigo,
        pend.pvec_transacaobx,

    ).filter(
        pend.pvec_datamvto >= '2023-01-01'
    ).order_by(desc(pend.pvec_datamvto))
    
    return pedidos_pend

