from api import ma
from ..models import cidades_model
from marshmallow import fields

class CidadesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cidades_model.CidadesModel
        load_instance = True
    
    muni_codigo = fields.Number(required=True)
    muni_nome = fields.String(required=True)
    muni_uf = fields.String(required=True)
    muni_codigoibge = fields.String(required=True)