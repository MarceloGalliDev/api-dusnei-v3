from ..models import (
    historico_pedido_d_2301_model, 
    historico_pedido_d_2302_model, 
    historico_pedido_d_2303_model, 
    historico_pedido_d_2304_model, 
    historico_pedido_d_2305_model, 
    historico_pedido_d_2306_model, 
    historico_pedido_d_2307_model, 
    historico_pedido_d_2308_model, 
    historico_pedido_d_2309_model, 
    historico_pedido_d_2310_model, 
    historico_pedido_d_2311_model, 
    historico_pedido_d_2312_model, 
    estoque_model,
)
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc, union_all

def listar_historico_pedido_d(batch_size=100):
    hist1 = aliased(historico_pedido_d_2301_model.HistoricoPedidosD2301Model)
    hist2 = aliased(historico_pedido_d_2302_model.HistoricoPedidosD2302Model)
    hist3 = aliased(historico_pedido_d_2303_model.HistoricoPedidosD2303Model)
    hist4 = aliased(historico_pedido_d_2304_model.HistoricoPedidosD2304Model)
    hist5 = aliased(historico_pedido_d_2305_model.HistoricoPedidosD2305Model)
    hist6 = aliased(historico_pedido_d_2306_model.HistoricoPedidosD2306Model)
    hist7 = aliased(historico_pedido_d_2307_model.HistoricoPedidosD2307Model)
    hist8 = aliased(historico_pedido_d_2308_model.HistoricoPedidosD2308Model)
    hist9 = aliased(historico_pedido_d_2309_model.HistoricoPedidosD2309Model)
    hist10 = aliased(historico_pedido_d_2310_model.HistoricoPedidosD2310Model)
    hist11 = aliased(historico_pedido_d_2311_model.HistoricoPedidosD2311Model)
    hist12 = aliased(historico_pedido_d_2312_model.HistoricoPedidosD2312Model)
    esto = aliased(estoque_model.EstoqueModel)
    
    def query(hist):
        return db.session.query(
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
        )
    
    union_query = union_all(
        query(hist1), 
        query(hist2),
        query(hist3), 
        query(hist4), 
        query(hist5), 
        query(hist6), 
        query(hist7), 
        query(hist8), 
        query(hist9), 
        query(hist10), 
        query(hist11), 
        query(hist12)
    )
    
    historicos = db.session.execute(union_query)
    
    while True:
        batch = historicos.fetchmany(batch_size)
        if not batch:
            break

        yield [
            {
                'mprd_transacao': h[0],
                'mprd_status': h[1],
                'mprd_unid_codigo': h[2],
                'mprd_numerodcto': h[3],
                'mprd_dcto_codigo': h[4],
                'mprd_prod_codigo': h[5],
                'mprd_sequencial': h[6],
                'mprd_valor': h[7],
                'mprd_qtde': h[8],
                'mprd_nextra6': h[9],
                'mprd_datamvto': h[10],
                'prun_comissao': h[11],
            } for h in batch
        ]



 