from api import db

class HistoricoPedidosCModel(db.Model):
    __tablename__ = 'movprodc'
    
    mprc_transacao = db.Column(db.String(16), db.ForeignKey('movdctos.mdoc_transacao'), primary_key=True)
    mprc_vend_codigo = db.Column(db.String(4), db.ForeignKey('vendedores.vend_codigo'))
    mprc_unid_codigo = db.Column(db.String(3), nullable=False)
    mprc_codentidade = db.Column(db.Numeric(precision=8, scale=0), db.ForeignKey('clientes.clie_codigo'))
    mprc_numerodcto = db.Column(db.String(20), nullable=False)
    mprc_peso = db.Column(db.Numeric(precision=12, scale=3))
    mprc_dcto_codigo = db.Column(db.String(4))
    mprc_status= db.Column(db.String(1))
    mprc_prvdapadrao = db.Column(db.Numeric(precision=12, scale=2))
    mprc_prvenda = db.Column(db.Numeric(precision=12, scale=2))
    mprc_fpgt_codigo = db.Column(db.String(3))
    mprc_datamvto = db.Column(db.Date)
    mprc_carregamento = db.Column(db.Numeric(precision=12, scale=0))
    mprc_obs = db.Column(db.String(600))
    
    dctos = db.relationship(
        'DctosModel', 
        backref='related_historico_pedido_c',
        viewonly=True
    )
    
    vendedores = db.relationship(
        'VendedoresModel', 
        backref='related_historico_pedido_c',
        viewonly=True
    )
    
    clientes = db.relationship(
        'ClientesModel',
        backref='related_historico_pedido_c',
        viewonly=True
    )
    
    
    def to_dict(self):
        return {
            'codfunccanc': self.related_dctos.mdoc_usucanc if self.related_dctos else None,
            'codemitente': self.mprc_unid_codigo,
            'codcli': self.mprc_codentidade,
            'numnota': self.mprc_numerodcto,
            'totpeso': self.mprc_peso,
            'origemped': self.mprc_dcto_codigo,
            'posicao': self.mprc_status,
            'vltabela': self.mprc_prvdapadrao,
            'numped': self.mprc_transacao,
            'condvenda': self.mprc_dcto_codigo,
            'codfilial': self.mprc_unid_codigo,
            'vlatend': self.mprc_prvenda,
            'codcob': self.mprc_fpgt_codigo,
            'vltotal': self.mprc_prvenda,
            'data': self.mprc_datamvto,
            'numcar': self.mprc_carregamento,
            'obs': self.mprc_obs,
            'codsupervisor': self.related_vendedores.vend_supe_codigo if self.related_vendedores else None,
            'totvolume': self.mprc_peso,
            'codpraca': self.clientes.clie_rota_codigo if self.clientes else None,
        }