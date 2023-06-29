from api import ma
from ..models import unidades_model
from marshmallow import fields

class UnidadesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = unidades_model.UnidadesModel
        load_instance = True
    
    unid_codigo = fields.Number(required=True)
    unid_nome = fields.String(required=True)
    unid_razaosocial = fields.String(required=True)
    unid_cnpj = fields.String(required=True)
    unid_bairro = fields.String(required=True)
    unid_municipio = fields.String(required=True)
    unid_endereco = fields.String(required=True)
    unid_cep = fields.String(required=True)
    unid_uf = fields.String(required=True)
    unid_calculaipi = fields.String(required=True)
    unid_tipoprecificacao = fields.String(required=True)
    unid_usawms = fields.String(required=True)
    unid_vendaporembalagem = fields.String(required=True)