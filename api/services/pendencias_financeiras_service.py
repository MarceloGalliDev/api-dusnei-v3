from ..models import pendencias_financeiras_model
from api import db
from sqlalchemy import desc, asc

def listar_pendencias_financeiras():
    return pendencias_financeiras_model.PendenciasFinanceirasModel.query.filter(
        pendencias_financeiras_model.PendenciasFinanceirasModel.pfin_status.in_(['P', 'B']),
        pendencias_financeiras_model.PendenciasFinanceirasModel.pfin_codentidade.isnot(None)
    ).order_by(
        desc(pendencias_financeiras_model.PendenciasFinanceirasModel.pfin_codentidade)
    )
