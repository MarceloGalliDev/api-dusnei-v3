from api import db

class DctosModel(db.Model):
    __tablename__ = 'movdctos'
    
    mdoc_transacao = db.Column(db.String(16), primary_key=True)
    mdoc_status = db.Column(db.String(1))
    mdoc_unid_codigo = db.Column(db.String(3))
    mdoc_dcto_codigo = db.Column(db.String(4))
    mdoc_numerodcto = db.Column(db.String(20))
    mdoc_valor = db.Column(db.Numeric(precision=12, scale=2))
    mdoc_usulcto = db.Column(db.Numeric(precision=5, scale=0))
    mdoc_usucanc = db.Column(db.Numeric(precision=5, scale=0))
    mdoc_datacanc = db.Column(db.Date)
    mdoc_datamvto = db.Column(db.Date)
    
    historico_pedido_c = db.relationship(
        'HistoricoPedidosCModel', 
        backref='related_dctos',
        uselist=True,
        viewonly=True
    )
    
    def to_dict(self):
        return {
            'mdoc_transacao': self.mdoc_transacao,
            'mdoc_status': self.mdoc_status,
            'mdoc_unid_codigo': self.mdoc_unid_codigo,
            'mdoc_dcto_codigo': self.mdoc_dcto_codigo,
            'mdoc_valor': self.mdoc_valor,
            'mdoc_usulcto': self.mdoc_usulcto,
            'mdoc_usucanc': self.mdoc_usucanc,
            'mdoc_datacanc': self.mdoc_datacanc,
            'mdoc_datamvto': self.mdoc_datamvto,
        }