from ..models import veiculos_model
from api import db
from sqlalchemy import desc

def listar_veiculos():
    return veiculos_model.DepartamentosModel.query.order_by(desc(veiculos_model.DepartamentosModel.tran_codigo))