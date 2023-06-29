from api import ma
from ..models import departamentos_model
from marshmallow import fields

class DepartamentosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = departamentos_model.DepartamentosModel
        load_instance = True
    
    dpto_codigo = fields.String(required=True)
    dpto_descricao = fields.String(required=True)