from ..models import cidades_model
from sqlalchemy.orm import aliased
from api import db

def listar_cidades():
    cidades = cidades_model.CidadesModel.query.all() 
    return [c.to_dict() for c in cidades]