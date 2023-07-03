from api import ma
from ..models import dctos_model
from marshmallow import fields

class DctosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = dctos_model.DctosModel
        load_instance = True
    
    mdoc_transacao = fields.String(required=True)
    mdoc_status = fields.String(required=True)
    mdoc_unid_codigo = fields.String(required=True)
    mdoc_dcto_codigo = fields.String(required=True)
    mdoc_valor = fields.Number(required=True)
    mdoc_usulcto = fields.String(required=True)
    mdoc_usucanc = fields.String(required=True)
    mdoc_datacanc = fields.Date(required=True)
    mdoc_datamvto = fields.Date(required=True)