from api import db

class HistoricoPedidosCModel(db.Model):
    __tablename__ = 'movprodc'
    
    mprc_transacao = db.Column(db.String(16), db.ForeignKey('movdctos.mdoc_transacao'), primary_key=True)
    mprc_unid_codigo = db.Column(db.String(3), nullable=False)
    mprc_codentidade = db.Column(db.Numeric(precision=8, scale=0))
    mprc_numerodcto = db.Column(db.String(20), nullable=False)
    mprc_peso = db.Column(db.Numeric(precision=12, scale=3))
    mprc_dcto_codigo = db.Column(db.String(4))
    mprc_status= db.Column(db.String(1))
    mprc_prvdapadrao = db.Column(db.Numeric(precision=12, scale=2))
    mprc_prvenda = db.Column(db.Numeric(precision=12, scale=2))
    mprc_fpgt_codigo = db.Column(db.String(3))
    mprc_datamvto = db.Column(db.Date)
    
    dctos = db.relationship(
        'DctosModel', 
        primaryjoin="HistoricoPedidosCModel.mprc_transacao==DctosModel.mdoc_transacao",
        back_populates='historico_pedido_c', 
        uselist=False
    )
    
    
    def to_dict(self):
        return {
            'codfunccalc': self.dctos.mdoc_usucanc if self.dctos else None,
            'codemitente': self.mprc_unid_codigo,
            'codcli': self.mprc_codentidade,
            'numnota': self.mprc_numerodcto,
            'totpeso': self.mprc_peso,
            'origemped': self.mprc_dcto_codigo,
            'posicao': self.mprc_status,
            'vltabela': self.mprc_prvdapadrao,
            'condvenda': self.mprc_dcto_codigo,
            'codfilial': self.mprc_unid_codigo,
            'vlatend': self.mprc_prvenda,
            'codcob': self.mprc_fpgt_codigo,
            'vltotal': self.mprc_prvenda,
            'data': self.mprc_datamvto,
        }