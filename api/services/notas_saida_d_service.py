from ..models import historico_pedido_c_model, notas_saida_c_model, notas_saida_d_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_notas_d():
    notd = aliased(notas_saida_d_model.NotasSaidaDModel)
    notc = aliased(notas_saida_c_model.NotasSaidaCModel)
    hist = aliased(historico_pedido_c_model.HistoricoPedidosCModel)
    
    notasd = db.session.query(
        notd.id,
        notd.nfed_transacao,
        notd.nfed_prod_codigo,
        notd.nfed_qtde,
        notd.nfed_sequencial,
        notd.nfed_valor,
        hist.mprc_carregamento,
        hist.mprc_prvdapadrao,
        notc.nfec_numerodcto,
        notc.nfec_transacao
    ).select_from(notd).join(
        notc, notd.nfed_transacao == notc.nfec_transacao
    ).join(
        hist, notd.nfed_transacao == hist.mprc_transacao
    ).order_by(desc(notd.nfed_transacao))
    
    return notasd