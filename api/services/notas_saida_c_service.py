from ..models import historico_pedido_c_model, dctos_model, clientes_model, notas_saida_c_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_notas_c():
    nota = aliased(notas_saida_c_model.NotasSaidaCModel)
    hist = aliased(historico_pedido_c_model.HistoricoPedidosCModel)
    dcto = aliased(dctos_model.DctosModel)
    clie = aliased(clientes_model.ClientesModel)
    
    notas = db.session.query(
        nota.nfec_transacao,
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
        clie.clie_lpgt_codigo,
    ).select_from(nota).join(
        hist, nota.nfec_transacao == hist.mprc_transacao
    ).join(
        dcto, nota.nfec_transacao == dcto.mdoc_transacao
    ).join(
        clie, nota.nfec_codentidade == clie.clie_codigo
    ).filter(
        nota.nfec_es == 'S',
        nota.nfec_datamvto >= '2023-01-01'
    ).order_by(desc(nota.nfec_datamvto))
    
    return notas

