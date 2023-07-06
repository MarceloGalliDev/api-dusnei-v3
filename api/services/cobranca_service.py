from ..models import historico_pedido_c_model, pendencias_financeiras_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc, asc

def listar_cobranca():
    cobr = aliased(historico_pedido_c_model.HistoricoPedidosCModel)
    pend = aliased(pendencias_financeiras_model.PendenciasFinanceirasModel)
    
    cobranca = db.session.query(
        cobr.mprc_transacao,
        cobr.mprc_vend_codigo,
        cobr.mprc_unid_codigo,
        cobr.mprc_codentidade,
        cobr.mprc_numerodcto,
        cobr.mprc_peso,
        cobr.mprc_dcto_codigo,
        cobr.mprc_status,
        cobr.mprc_prvdapadrao,
        cobr.mprc_prvenda,
        cobr.mprc_fpgt_codigo,
        cobr.mprc_datamvto,
        cobr.mprc_carregamento,
        cobr.mprc_obs,
        pend.pfin_lpgt_codigo,
        pend.pfin_numerodcto, 
        pend.pfin_datamvto,
        pend.pfin_datavcto,       
    ).join(
        cobr, cobr.mprc_transacao == pend.pfin_transacao
    ).filter(
        cobr.mprc_dcto_codigo.in_(['6666','7339','7338','7260','7263','7262','7268', '7267', '7319', '7318'])
    ).order_by(desc(cobr.mprc_datamvto))

    return cobranca

