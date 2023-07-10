from api import db

class CarregamentosModel(db.Model):
    __tablename__ = 'carregamentos'
    
    carr_numero = db.Column(db.Numeric(precision=10, scale=0), primary_key=True, nullable=False)
    carr_status = db.Column(db.String(1))
    carr_unid_codigo = db.Column(db.String(3))
    carr_rota_codigo = db.Column(db.String(3))
    carr_datamvto = db.Column(db.Date)
    carr_datasaida = db.Column(db.Date)
    carr_qpedidos = db.Column(db.Numeric(precision=10, scale=0))
    carr_motorista = db.Column(db.Numeric(precision=10, scale=0))
    carr_placa = db.Column(db.String(10))
    carr_pesoprodutos = db.Column(db.Numeric(precision=10, scale=2))
    carr_volumeprodutos = db.Column(db.Numeric(precision=12, scale=4))
    carr_totalprodutos = db.Column(db.Numeric(precision=14, scale=2))
    
    
    
    def to_dict(self):
        return {
            'numcar': self.carr_numero,
            'datamon': self.carr_datamvto,
            'dtfat': self.carr_datasaida,
            'numnotas': self.carr_qpedidos,
            'origem_car': 'ERP',
            'codmotorista': self.carr_motorista,
            'codveiculo': self.carr_placa,
            'totpeso': self.carr_pesoprodutos,
            'totvolume': self.carr_volumeprodutos,
            'vltotal': self.carr_totalprodutos,
        }