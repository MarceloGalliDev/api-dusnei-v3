from api import db

class NotasSaidaDModel(db.Model):
    __tablename__ = 'nfed'
    
    id = db.Column(db.Integer)
    nfed_transacao = db.Column(
        db.String(16), 
        db.ForeignKey('movprodc.mprc_transacao'), 
        db.ForeignKey('nfec.nfec_transacao'), 
        primary_key=True)
    nfed_prod_codigo = db.Column(db.Numeric(precision=8, scale=0))
    nfed_qtde = db.Column(db.Numeric(precision=20, scale=6))
    nfed_sequencial = db.Column(db.Numeric(precision=20, scale=6))
    nfed_valor = db.Column(db.Numeric(precision=12, scale=3))
    
    historico_pedido_c = db.relationship(
        'HistoricoPedidosCModel',
        backref=db.backref('related_notas_saida_d', uselist=True),
        viewonly=True,
    )
    
    notas_saida_c = db.relationship(
        'NotasSaidaCModel',
        backref=db.backref('related_notas_saida_d', uselist=True),
        viewonly=True,
    )
    
    def to_dict(self):
        return {
            'codprod': str(self.nfed_prod_codigo),
            'codoper': 'S',
            'qt': self.nfed_qtde,
            'numseq': self.nfed_sequencial,
            'qtcont': self.nfed_qtde,
            'numtransvenda': int(self.nfed_transacao),
            'numtransitem': self.id,
            'numcar': str(self.movprodc.mprc_carregamento if self.movprodc else None),
            'numnota': int(self.nfec.nfec_numerodcto if self.nfec else None),
            'numped': int(self.nfec.nfec_transacao if self.nfec else None),
            'ptabela': self.movprodc.mprc_prvdapadrao if self.movprodc else None,
            'punitcont': self.nfed_valor,
            'punit': self.nfed_valor,
            'custofin': 0,
            'vlipi': 0,
            'st': 0
        }