from ..models import historico_pedido_c_model, dctos_model, vendedores_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_historico_pedido_c():
    hist = aliased(historico_pedido_c_model.HistoricoPedidosCModel)
    dctos = aliased(dctos_model.DctosModel)
    vend = aliased(vendedores_model.VendedoresModel)
    
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
        dctos.mdoc_usucanc,
        hist.mprc_carregamento,
        hist.mprc_obs,
        vend.vend_supe_codigo,
    ).join(
        dctos, dctos.mdoc_transacao == hist.mprc_transacao
    ).join(
        vend, vend.vend_codigo == hist.mprc_vend_codigo
    ).filter(
        hist.mprc_dcto_codigo.in_(['6666','7339','7338','7260','7263','7262','7268', '7267', '7319', '7318'])
    ).order_by(desc(hist.mprc_datamvto))

    return historico

