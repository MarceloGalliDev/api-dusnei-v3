from ..models import cidades_model
from api import db
from sqlalchemy import asc

def listar_cidades():
    cida = cidades_model.CidadesModel
    
    cidades = db.session.query(
        cida.muni_codigo,
        cida.muni_codigoibge,
        cida.muni_nome,
        cida.muni_uf
    ).order_by(
        asc(cida.muni_codigo)
    )
    return cidades