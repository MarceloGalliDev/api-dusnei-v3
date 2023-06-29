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
            'unid_codigo': self.unid_codigo,
            'unid_nome': self.unid_nome,
            'unid_razaosocial': self.unid_razaosocial,
            'unid_cnpj': self.unid_cnpj,
            'unid_bairro': self.unid_bairro,
            'unid_municipio': self.unid_municipio,
            'unid_endereco': self.unid_endereco,
            'unid_cep': self.unid_cep,
            'unid_uf': self.unid_uf,
        }