from api import db

class VendedoresModel(db.Model):
    __tablename__ = 'vendedores'
    
    vend_supe_codigo = db.Column(db.String(30))
    vend_codigo = db.Column(db.String(4), primary_key=True)
    vend_unid_codigo = db.Column(db.String(3))
    vend_nome = db.Column(db.String(50))
    
    historico_pedido_c = db.relationship(
        'HistoricoPedidosCModel', 
        backref='related_vendedores',
        uselist=True,
        viewonly=True
    )
    
    def to_dict(self):
        return {
            'codsupervisor': self.vend_supe_codigo,
            'codusur': self.vend_codigo,
            'codfilial': self.vend_unid_codigo,
            'nome': self.vend_nome,
        }