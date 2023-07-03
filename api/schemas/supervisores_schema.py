from api import ma
from ..models import supervisores_model
from marshmallow import fields

class SupervisoresSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = supervisores_model.SupervisoresModel
        load_instance = True
    
    codsupervisor = fields.String(required=True)
    cod_cadrca = fields.Number(required=True)
    codgerente = fields.String(required=True)
    nome = fields.String(required=True)
    posicao = fields.String(required=True)
