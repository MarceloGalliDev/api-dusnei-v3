from api import db

class FuncionariosModel(db.Model):
    __tablename__ = 'motoristas'
    
    func_codpdv = db.Column(db.String(16))
    func_nome = db.Column(db.String(50))
    func_email = db.Column(db.String(100))
    func_codigo = db.Column(db.Numeric(precision=6, scale=0), primary_key=True)
    func_celular = db.Column(db.String(11))
    func_unid_codigo = db.Column(db.String(3))
    func_funcao = db.Column(db.String(3))
    func_cpf = db.Column(db.String(11))
    func_situacao = db.Column(db.String(2))
    func_observacao = db.Column(db.String(300))
    
    def to_dict(self):
        return {
            'codsetor': self.func_codpdv,
            'nome': self.func_nome,
            'email': self.func_email,
            'matricula': self.func_codigo,
            'celular': self.func_celular,
            'codfilial': self.func_unid_codigo,
            'tipo': self.func_funcao,
            'cpf': self.func_cpf,
            'situacao': self.func_situacao,
            'codveiculo': self.func_observacao,
        }