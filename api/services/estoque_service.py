from ..models import estoque_model
from api import db
from sqlalchemy import desc

def listar_estoque():
    return estoque_model.EstoqueModel.query.order_by(desc(estoque_model.EstoqueModel.prun_prod_codigo))
    