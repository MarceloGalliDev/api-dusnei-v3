from ..models import historico_pedido_d_1023_model, estoque_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc


def listar_historico_pedido_d_1023():
    hist = aliased(historico_pedido_d_1023_model.HistoricoPedidosD1023Model)
    esto = aliased(estoque_model.EstoqueModel)
    
    historico = db.session.query(
        hist.mprd_transacao,
        hist.mprd_status,
        hist.mprd_unid_codigo,
        hist.mprd_numerodcto,
        hist.mprd_dcto_codigo,
        hist.mprd_prod_codigo,
        hist.mprd_sequencial,
        hist.mprd_valor,
        hist.mprd_qtde,
        hist.mprd_nextra6,
        hist.mprd_datamvto,
        esto.prun_comissao
    ).join(
        esto
    ).filter(
        hist.mprd_dcto_codigo.in_(['6666','7339','7338','7260','7263','7262','7268', '7267', '7319', '7318'])
    ).order_by(desc(hist.mprd_datamvto))
    
    return historico
    




 