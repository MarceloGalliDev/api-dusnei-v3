from ..models import historico_pedido_c_model, dctos_model, clientes_model, notas_saida_c_model, pedidos_pendentes_c_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_notas_c():
    nota = aliased(notas_saida_c_model.NotasSaidaCModel)
    hist = aliased(historico_pedido_c_model.HistoricoPedidosCModel)
    dcto = aliased(dctos_model.DctosModel)
    clie = aliased(clientes_model.ClientesModel)
    pedp = aliased(pedidos_pendentes_c_model.PedidosPendentesCModel)
    
    notas = db.session.query(
        nota.nfec_numerodcto,
        nota.nfec_serie,
        nota.nfec_datasaida,
        nota.nfec_datamvto,
        nota.nfec_dataemissao,
        nota.nfec_totaldcto,
        nota.nfec_es,
        nota.nfec_codentidade,
        nota.nfec_fpgt_codigo,
        nota.nfec_unid_codigo,
        nota.nfec_idlote,
        nota.nfec_pesoliq,
        nota.nfec_volumes,
        hist.mprc_carregamento,
        hist.mprc_dcto_codigo,
        dcto.mdoc_usulcto,
        pedp.pvec_numero,
        clie.clie_lpgt_codigo,
    ).join(
        hist
    ).join(
        dcto
    ).join(
        clie
    ).join(
        pedp
    ).filter(
        nota.nfec_es.in_(['S']),
        nota.nfec_datamvto >= '2023-01-01'
    ).order_by(desc(nota.nfec_datamvto))
    
    return notas

