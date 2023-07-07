from api import db

class HistoricoPedidosD2312Model(db.Model):
    __tablename__ = 'movprodd1223'
    
    mprd_transacao = db.Column(db.String(16), primary_key=True, nullable=False)
    mprd_status = db.Column(db.String(1))

    mprd_unid_codigo = db.Column(db.String(3))
    mprd_numerodcto = db.Column(db.String(20))
    mprd_dcto_codigo = db.Column(db.String(4))
    mprd_prod_codigo = db.Column(db.Numeric(precision=8, scale=0), db.ForeignKey('produn.prun_prod_codigo'))
    mprd_sequencial = db.Column(db.Numeric(precision=8, scale=0))
    mprd_valor = db.Column(db.Numeric(precision=12, scale=3))
    mprd_qtde = db.Column(db.Numeric(precision=10, scale=3))
    mprd_nextra6 = db.Column(db.Numeric(precision=12, scale=3))
    mprd_datamvto = db.Column(db.Date)
    
    #relacionamento para acessar as propriedades do EstoqueModel
    #temos que ter a chave estrangeira
    estoque = db.relationship(
        'EstoqueModel', 
        backref=db.backref('historicos_pedidos_d_2312', uselist=True)
    )
    
    def to_dict(self):
        return {
            'numped': self.mprd_transacao,
            'qt': self.mprd_qtde,
            'numseq': self.mprd_sequencial,
            'pvenda': self.mprd_valor,
            'codprod': self.mprd_prod_codigo,
            'ptabela': self.mprd_nextra6,
            'percom': self.estoque.prun_comissao if self.estoque else None,
            'data': self.mprd_datamvto,
            'posicao': self.mprd_status,
        }