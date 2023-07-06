from ..models import carregamentos_model
from api import db
from sqlalchemy import desc

def listar_carregamentos():
    return carregamentos_model.CarregamentosModel.query.order_by(desc(carregamentos_model.CarregamentosModel.carr_numero))