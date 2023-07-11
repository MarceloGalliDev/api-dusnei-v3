from api import db

class PedidosPendentesCModel(db.Model):
    __tablename__ = 'pedvendac'
    
    pvec_numero = db.Column(db.Numeric(precision=10, scale=0), primary_key=True)
    pvec_dcto_codigo = db.Column(db.String(4))
    pvec_unid_codigo = db.Column(db.String(3))
    pvec_carregamento = db.Column(db.Numeric(precision=10, scale=0))
    pvec_status = db.Column(db.String(1))
    pvec_datamvto = db.Column(db.Date)
    pvec_database = db.Column(db.Date)
    pvec_databaixa = db.Column(db.Date)
    pvec_vend_codigo = db.Column(db.String(4))
    pvec_rota_codigo = db.Column(db.String(3))
    pvec_fpgto_codigo = db.Column(db.String(3))
    pvec_transacaobx = db.Column(db.String(16))#ligacao com movprodc
    pvec_usua_codigo = db.Column(db.Numeric(precision=5, scale=0))
    
      
    def to_dict(self):
        return {
            'pvec_numero': self.pvec_numero,
            'pvec_dcto_codigo': self.pvec_dcto_codigo,
            'pvec_unid_codigo': self.pvec_unid_codigo,
            'pvec_carregamento': self.pvec_carregamento,
            'pvec_status': self.pvec_status,
            'pvec_datamvto': self.pvec_datamvto,
            'pvec_database': self.pvec_database,
            'pvec_databaixa': self.pvec_databaixa,
            'pvec_vend_codigo': self.pvec_vend_codigo,
            'pvec_rota_codigo': self.pvec_rota_codigo,
            'pvec_fpgto_codigo': self.pvec_fpgto_codigo,
            'pvec_transacaobx': self.pvec_transacaobx,
            'pvec_usua_codigo': self.pvec_usua_codigo,
        }