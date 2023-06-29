from ..models import departamentos_model
from sqlalchemy.orm import aliased
from api import db

def listar_departamentos():
    dpto = aliased(departamentos_model.DepartamentosModel)
    departamentos = db.session.query(dpto.dpto_codigo, dpto.dpto_descricao).filter(
        dpto.dpto_codigo.notin_ (['900', '500', '400', '300'])).order_by(dpto.dpto_codigo).all()
    return [{'dpto_codigo': d.dpto_codigo, 'dpto_descricao': d.dpto_descricao} for d in departamentos]