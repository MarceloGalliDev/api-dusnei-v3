from ..models import historico_pedido_c_model, dctos_model, vendedores_model, clientes_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_historico_pedido_c():
    hist = aliased(historico_pedido_c_model.HistoricoPedidosCModel)
    dctos = aliased(dctos_model.DctosModel)
    vend = aliased(vendedores_model.VendedoresModel)
    clie = aliased(clientes_model.ClientesModel)
    
    historico = db.session.query(
        hist.mprc_transacao,
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
        clie.clie_rota_codigo,
    ).join(
        dctos
    ).join(
        vend
    ).join(
        clie
    ).filter(
        hist.mprc_dcto_codigo.in_(['6666','7339','7338','7260','7263','7262','7268', '7267', '7319', '7318']),
        hist.mprc_datamvto >= '2023-01-01'
    ).order_by(desc(hist.mprc_datamvto))

    return historico

