from api import db

class CidadesModel(db.Model):
    __tablename__ = 'municipios'
    
    muni_codigo = db.Column(db.Numeric(precision=6, scale=0), primary_key=True, nullable=False)
    muni_nome = db.Column(db.String(40))
    muni_uf = db.Column(db.String(2))
    muni_codigoibge = db.Column(db.Numeric(precision=8, scale=0))
    
    
    def to_dict(self):
        return {
            'codcidade': self.muni_codigo,
            'nomecidade': self.muni_nome,
            'uf': self.muni_uf,
            'codibge': self.muni_codigoibge,
        }