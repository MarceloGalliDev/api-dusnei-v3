from ..models import carregamentos_model
from api import db
from sqlalchemy import desc, asc

def listar_carregamentos():
    carr = carregamentos_model.CarregamentosModel
    
    carregamentos = db.session.query(
        carr.carr_numero,
        carr.carr_status,
        carr.carr_unid_codigo,
        carr.carr_rota_codigo,
        carr.carr_datamvto,
        carr.carr_datasaida,
        carr.carr_qpedidos,
        carr.carr_motorista,
        carr.carr_placa,
        carr.carr_pesoprodutos,
        carr.carr_volumeprodutos,
        carr.carr_totalprodutos,
    ).filter(
        carr.carr_datamvto >= '2023-01-01'
    ).order_by(
        desc(carr.carr_numero)
    )
    return carregamentos