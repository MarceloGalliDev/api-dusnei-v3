from api import db

class PendenciasFinanceirasModel(db.Model):
    __tablename__ = 'pendfin'
    
    pfin_transacao = db.Column(db.String(16), primary_key=True)
    pfin_status = db.Column(db.String(1))
    pfin_datamvto = db.Column(db.Date())
    pfin_unid_codigo = db.Column(db.String(3))
    pfin_fpgt_codigo = db.Column(db.String(3))
    pfin_lpgt_codigo = db.Column(db.String(3))
    pfin_codentidade = db.Column(db.Numeric(precision=8, scale=0))
    pfin_numerodcto = db.Column(db.String(20))
    pfin_parcela = db.Column(db.Numeric(precision=3, scale=0))
    pfin_valor = db.Column(db.Numeric(precision=12, scale=2))
    pfin_mapacarga = db.Column(db.Numeric(precision=10, scale=0))
    pfin_nparcelas = db.Column(db.Numeric(precision=3, scale=0))
    pfin_observacao = db.Column(db.String(250))
    
    cobranca = db.relationship(
        'CobrancaModel', 
        backref='related_pendfin',
        uselist=True,
        viewonly=True
    )
    
    def to_dict(self):
        return {
            'codclie': self.pfin_codentidade,
            'status': self.pfin_status,
            'data': self.pfin_datamvto,
            'unidade': self.pfin_unid_codigo,
            'formapagamento': self.pfin_fpgt_codigo,
            'localpagamento': self.pfin_lpgt_codigo,
            'nfe': self.pfin_numerodcto,
            'parcela': self.pfin_parcela,
            'carregamento': self.pfin_mapacarga,
            'nparcelas': self.pfin_nparcelas,            
        }