from api import db

class EstoqueModel(db.Model):
    __tablename__ = 'produn'
    
    prun_prod_codigo = db.Column(db.Numeric(precision=8, scale=0), primary_key=True)
    prun_setordep = db.Column(db.String(10))
    prun_emb = db.Column(db.String(2))
    prun_qemb = db.Column(db.Numeric(precision=5, scale=0))
    prun_estoque1 = db.Column(db.Numeric(precision=15, scale=5))
    prun_estoque2 = db.Column(db.Numeric(precision=15, scale=5))
    prun_estoque3 = db.Column(db.Numeric(precision=15, scale=5))
    prun_estoque4 = db.Column(db.Numeric(precision=15, scale=5))
    prun_estoque5 = db.Column(db.Numeric(precision=15, scale=5))
    prun_unid_codigo = db.Column(db.String(3))
    prun_comissao = db.Column(db.Numeric(precision=15, scale=5))
    
    produtos = db.relationship(
        'ProdutosModel',
        backref='related_estoque',
        uselist=True,
        viewonly=True,
    )
       
    def to_dict(self):
        return {
            'prun_prod_codigo': self.prun_prod_codigo,
            'prun_setordep': self.prun_setordep,
            'prun_emb': self.prun_emb,
            'prun_qemb': self.prun_qemb,
            'prun_estoque1': self.prun_estoque1,
            'prun_estoque2': self.prun_estoque2,
            'prun_estoque3': self.prun_estoque3,
            'prun_estoque4': self.prun_estoque4,
            'prun_estoque5': self.prun_estoque5,
            'prun_unid_codigo': self.prun_unid_codigo,
            'prun_comissao': self.prun_comissao,
        }