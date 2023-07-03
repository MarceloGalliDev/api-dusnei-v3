from api import db

class VendedoresModel(db.Model):
    __tablename__ = 'vendedores'
    
    vend_codigo = db.Column(db.String(4), primary_key=True, nullable=False)
    vend_nome = db.Column(db.String(50))
    vend_unid_codigo = db.Column(db.String(3))
    vend_func_codigo = db.Column(db.Numeric(precision=10, scale=0))
    
    
    def to_dict(self):
        return {
            'vend_codigo': self.vend_codigo,
            'vend_nome': self.vend_nome,
            'vend_unid_codigo': self.vend_unid_codigo,
            'vend_func_codigo': self.vend_func_codigo,
        }