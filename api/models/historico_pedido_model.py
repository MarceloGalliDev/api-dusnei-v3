from api import db

class CidadesModel(db.Model):
    __tablename__ = 'movprodc'
    
    mprc_tran_codigo = db.Column(db.String(5))#codigo do transportador, ligado a tabela transportadores
    mprc_codentidade = db.Column(db.Numeric(precision=8, scale=0))#codigo do cliente
    mprc_numerodcto = db.Column(db.String(20), nullable=False)#numero nfe
    
   
    
    def to_dict(self):
        return {
            'transportador': self.mprc_tran_codigo,
            'codcli': self.mprc_codentidade,
            'numnota': self.mprc_numerodcto,
            

        }