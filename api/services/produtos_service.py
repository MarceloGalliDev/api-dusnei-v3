from ..models import produtos_model, estoque_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc, asc

def listar_produtos():
    prod = aliased(produtos_model.ProdutosModel)
    esto = aliased(estoque_model.EstoqueModel)
    
    produtos = db.session.query(
        prod.prod_codbarras,
        prod.prod_dpto_codigo, 
        prod.prod_forn_codigo, 
        prod.prod_codigo, 
        prod.prod_grup_codigo, 
        prod.prod_descricao, 
        prod.prod_datacad, 
        prod.prod_emb, 
        prod.prod_peso, 
        prod.prod_pesoliq, 
        prod.prod_balanca, 
        prod.prod_qemb, 
        prod.prod_classe, 
        prod.prod_tipo,
        esto.prun_emb,
        esto.prun_qemb,
        esto.prun_setordep, 
        esto.prun_unid_codigo,
        prod.prod_codigoncm,
    ).join(
        esto
    ).filter(
        esto.prun_unid_codigo.in_(['001','002','003'])
    ).order_by(asc(prod.prod_codigo))
    
    return produtos