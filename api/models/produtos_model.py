from api import db

class ProdutosModel(db.Model):
    __tablename__ = 'produtos'
    
    prod_codbarras = db.Column(db.String(13))
    prod_dpto_codigo = db.Column(db.String(3))
    prod_forn_codigo = db.Column(db.Numeric(precision=10, scale=0))
    prod_codigo = db.Column(db.Numeric(precision=8, scale=0), db.ForeignKey('produn.prun_prod_codigo'), primary_key=True)
    prod_grup_codigo = db.Column(db.String(5))
    prod_descricao = db.Column(db.String(100))
    prod_datacad = db.Column(db.Date)
    prod_emb = db.Column(db.String(2))
    prod_peso = db.Column(db.Numeric(precision=15, scale=5))
    prod_pesoliq = db.Column(db.Numeric(precision=15, scale=5))
    prod_balanca = db.Column(db.String(1))
    prod_qemb = db.Column(db.Numeric(precision=5, scale=0))
    prod_classe = db.Column(db.String(15))
    prod_tipo = db.Column(db.String(5))
    prod_codigoncm = db.Column(db.String(10))
    
    estoque = db.relationship(
        'EstoqueModel',
        backref=db.backref('related_produtos', uselist=True),
        viewonly=True,
    )
   
    
    def to_dict(self):
        return {
            'aceitavendafracao': 'S',
            'classificfiscal': self.prod_codigoncm,
            'codauxiliar': self.prod_codbarras,
            'codepto': self.prod_dpto_codigo,
            'codfilialretira': self.estoque.prun_unid_codigo if self.estoque else None,
            'codfornec': self.prod_forn_codigo,
            'codprod': self.prod_codigo,
            'codsec': self.prod_grup_codigo,
            'descricao': self.prod_descricao,
            'dtcadastro': self.prod_datacad,
            'dtvenc': '',
            'embalagem': self.estoque.prun_qemb if self.estoque else None,
            'embalagemmaster': self.prod_qemb,
            'enviarforcavendas': 'S',
            'pesobruto': self.prod_peso,
            'pesoliq': self.prod_pesoliq,
            'pesovariavel': self.prod_balanca,
            'qtunit': self.estoque.prun_qemb if self.estoque else None,
            'qtunitcx': self.prod_qemb,
            'revenda': 'S',
            'tipoestoque': self.estoque.prun_setordep if self.estoque else None,
            'tipomerc': 'L',
            'unidade': self.estoque.prun_emb if self.estoque else None,
            'unidademaster': self.prod_emb,
        }