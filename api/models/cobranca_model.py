from api import db

class CobrancaModel(db.Model):
    __tablename__ = 'movprodc'
    
    mprc_transacao = db.Column(db.String(16), db.ForeignKey('movdctos.mdoc_transacao'), primary_key=True)
    mprc_vend_codigo = db.Column(db.String(4))
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
    mprc_carregamento = db.Column(db.Numeric(precision=12, scale=0))
    mprc_obs = db.Column(db.String(600))
    
    dctos = db.relationship(
        'DctosModel', 
        backref='related_cobranca',
        viewonly=True
    )
    
    pendfin = db.relationship(
        'PendenciasFinanceirasModel', 
        backref='related_cobranca',
        viewonly=True
    )
    
    
    def to_dict(self):
        return {
            'boleto': self.related_pendfin.pfin_lpgt_codigo if self.related_pendfin else None,
            'cartao': self.related_pendfin.pfin_lpgt_codigo if self.related_pendfin else None,
            'cobranca': self.mprc_obs,
        }