from ..models import supervisores_model
from api import db

def listar_supervisores():
    supervisores = supervisores_model.SupervisoresModel.query.all()
    return [u.to_dict() for u in supervisores]