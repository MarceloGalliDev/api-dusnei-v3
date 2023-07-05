from api import db

class ProdutosModel(db.Model):
    __tablename__ = 'produtos'
    
    prod_codbarras = db.Column(db.String(13))
    prod_dpto_codigo = db.Column(db.String(3))
    prod_forn_codigo = db.Column(db.Numeric(precision=10, scale=0))
    prod_codigo = db.Column(db.Numeric(precision=8, scale=0), primary_key=True)
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
    
    
    
    def to_dict(self):
        return {
            'aceitavendafracao': 'S',
            'classificfiscal': 'N',
            'codauxiliar': self.prod_codbarras,
            'codepto': self.prod_dpto_codigo,
            'codfornec': self.prod_forn_codigo,
            'codprod': self.prod_codigo,
            'codsec': self.prod_grup_codigo,
            'descricao': self.prod_descricao,
            'dtcadastro': self.prod_datacad,
            'embalagem': 'produn',
            'embalagemmaster': self.prod_qemb,
            'enviarforcavendas': 'S',
            'pesobruto': self.prod_peso,
            'pesoliq': self.prod_pesoliq,
            'pesovariavel': self.prod_balanca,
            'qtunit': 'produn',
            'qtunitcx': self.prod_qemb,
            'revenda': 'S',
            'tipoestoque': 'produn',
            'tipomerc': 'L',
            'unidade': 'produn',
            'unidademaster': self.prod_emb,
        }