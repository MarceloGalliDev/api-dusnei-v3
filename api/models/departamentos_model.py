from api import db

class DepartamentosModel(db.Model):
    __tablename__ = 'departamentos'
    
    dpto_codigo = db.Column(db.String(3), primary_key=True, nullable=False)
    dpto_descricao = db.Column(db.String(50))
    
    def to_dict(self):
        return {
            'dpto_codigo': self.dpto_codigo,
            'dpto_descricao': self.dpto_descricao
        }