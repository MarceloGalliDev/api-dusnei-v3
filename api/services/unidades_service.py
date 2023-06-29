from ..models import unidades_model
from api import db

def listar_unidades():
    unidades = unidades_model.UnidadesModel.query.all()
    return [u.to_dict() for u in unidades]