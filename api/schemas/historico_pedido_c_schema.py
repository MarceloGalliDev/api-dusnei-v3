from api import ma
from ..models import historico_pedido_c_model 
from marshmallow import fields

class HistoricoPedidoCSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = historico_pedido_c_model.HistoricoPedidosCModel
        load_instance = True
    
    codfunccalc = fields.Number(required=True)
    codemitente = fields.String(required=True)
    codcli = fields.Number(required=True)
    numnota = fields.String(required=True)
    totpeso = fields.Number(required=True)
    origemped = fields.String(required=True)
    posicao = fields.String(required=True)
    vltabela = fields.Number(required=True)
    condvenda = fields.String(required=True)
    codfilial = fields.String(required=True)
    vlatend = fields.Number(required=True)
    codcob = fields.String(required=True)
    vltotal = fields.Number(required=True)
    data = fields.Date(required=True)
    numcar = fields.Number(required=True)
    


