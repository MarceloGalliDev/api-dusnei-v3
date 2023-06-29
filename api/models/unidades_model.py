from api import db

class UnidadesModel(db.Model):
    __tablename__ = 'unidades'
    
    unid_codigo = db.Column(db.String(3), primary_key=True, nullable=False)
    unid_nome = db.Column(db.String(80))
    unid_razaosocial = db.Column(db.String(80))
    unid_cnpj = db.Column(db.String(14))
    unid_bairro = db.Column(db.String(40))
    unid_municipio = db.Column(db.String(40))
    unid_endereco = db.Column(db.String(40))
    unid_cep = db.Column(db.String(8))
    unid_uf = db.Column(db.String(2))
    
    
    def to_dict(self):
        return {
            'codigo': self.unid_codigo,
            'fantasia': self.unid_nome,
            'razaosocial': self.unid_razaosocial,
            'cgc': self.unid_cnpj,
            'cep': self.unid_cep,
            'bairro': self.unid_bairro,
            'endereco': self.unid_endereco,
            'cidade': self.unid_municipio,
            'uf': self.unid_uf,
            'calcularipivenda': 'N',
            'tipoprecificacao': 'P',
            'usawms': 'N',
            'utilizavendaporembalagem': 'S'
        }