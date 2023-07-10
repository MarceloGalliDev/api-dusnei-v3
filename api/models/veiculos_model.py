from api import db

class DepartamentosModel(db.Model):
    __tablename__ = 'transportadores'
    
    tran_codigo = db.Column(db.String(5), primary_key=True, nullable=False)
    tran_nome = db.Column(db.String(50))
    tran_placa = db.Column(db.String(20))
    tran_maxvolume = db.Column(db.Numeric(precision=12, scale=0))
    tran_maxpeso = db.Column(db.Numeric(precision=12, scale=0))
    tran_situacao = db.Column(db.String(1))
    tran_unid_codigo = db.Column(db.String(3))
    
    def to_dict(self):
        return {
            'codveiculo': self.tran_codigo,
            'descricao': self.tran_nome,
            'placa': self.tran_placa,
            'volume': self.tran_maxvolume,
            'pesocargakg': self.tran_maxpeso,
            'situacao': self.tran_situacao,
            'codfilial': self.tran_unid_codigo,
        }