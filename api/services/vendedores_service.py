from ..models import vendedores_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import asc

def listar_vendedores():
    vend = aliased(vendedores_model.VendedoresModel)
    vendedores = db.session.query(
        vend.vend_codigo,
        vend.vend_nome,
        vend.vend_unid_codigo,
        vend.vend_supe_codigo,
    ).filter(
        vend.vend_codigo.notin_(['000', '9999'])
    ).order_by(
        asc(vend.vend_codigo)
    )
    
    return vendedores


