from ..models import estoque_model
from api import db
from sqlalchemy import desc, asc

def listar_estoque():
    return estoque_model.EstoqueModel.query.order_by(asc(estoque_model.EstoqueModel.prun_prod_codigo)).filter(estoque_model.EstoqueModel.prun_unid_codigo.in_(['001', '002', '003']))
    