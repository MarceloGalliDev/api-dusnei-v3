from ..models import vendedores_model
from sqlalchemy.orm import aliased
from api import db

def listar_vendedores():
    vend = aliased(vendedores_model.VendedoresModel)
    vendedores = db.session.query(
        vend.vend_codigo,
        vend.vend_nome,
        vend.vend_unid_codigo,
        vend.vend_func_codigo,
        vend.vend_supe_codigo,
    ).filter(
        vend.vend_codigo.notin_(['000', '9999'])
    ).order_by(
        vend.vend_codigo
    ).all() 
    return [
        {
            'vend_codigo': c.vend_codigo,
            'vend_nome': c.vend_nome,
            'vend_unid_codigo': c.vend_unid_codigo,
            'vend_func_codigo': c.vend_func_codigo,
            'vend_supe_codigo': c.vend_supe_codigo,
        } for c in vendedores]


