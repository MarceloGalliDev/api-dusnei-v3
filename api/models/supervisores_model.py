from api import db

class SupervisoresModel(db.Model):
    __tablename__ = 'supervisores'
    
    supe_codigo = db.Column(db.String(3), primary_key=True, nullable=False)
    supe_nome = db.Column(db.String(50))
    supe_func_codigo = db.Column(db.Numeric(precision=10, scale=0))
    
    def to_dict(self):
        return {
            'codsupervisor': self.supe_codigo,
            'cod_cadrca': self.supe_func_codigo,
            'codgerente': '001',
            'nome': self.supe_nome,
            'posicao': 'I' if 'inativo' in self.supe_nome else 'A',
        }