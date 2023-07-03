from api import ma
from ..models import vendedores_model
from marshmallow import fields

class VendedoresSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = vendedores_model.VendedoresModel
        load_instance = True
    
    vend_codigo: fields.String(required=True)
    vend_nome: fields.String(required=True)
    vend_unid_codigo: fields.String(required=True)
    vend_func_codigo: fields.String(required=True)