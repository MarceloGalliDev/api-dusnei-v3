from ..models import dctos_model
from api import db
from sqlalchemy import desc

def listar_dctos():
    return dctos_model.DctosModel.query.order_by(desc(dctos_model.DctosModel.mdoc_datamvto))