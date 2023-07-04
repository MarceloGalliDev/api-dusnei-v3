from api import db

class ClientesModel(db.Model):
    __tablename__ = 'clientes'
    
    clie_bairrores = db.Column(db.String(30))
    clie_situacao = db.Column(db.String(1))
    clie_cepres = db.Column(db.String(8))
    clie_cnpjcpf = db.Column(db.String(14))
    clie_razaosocial = db.Column(db.String(80))
    clie_ramoatividade = db.Column(db.String(50))
    clie_muni_codigo_res = db.Column(db.String(50), db.ForeignKey('municipios.muni_codigo'))
    clie_codigo = db.Column(db.Numeric(precision=8, scale=0), primary_key=True)
    clie_lpgt_codigo = db.Column(db.String(3))
    clie_usualt = db.Column(db.Numeric(precision=5, scale=0))
    clie_fpgt_codigo = db.Column(db.String(200))
    clie_rota_codigo = db.Column(db.String(3))
    clie_vend_codigo = db.Column(db.String(4))
    clie_vend_alternativos = db.Column(db.String(50))
    clie_tipos = db.Column(db.String(100))
    clie_contribuinte = db.Column(db.String(1))
    clie_email = db.Column(db.String(200))
    clie_emailnfe = db.Column(db.String(200))
    clie_endres = db.Column(db.String(50))
    clie_ufexprg= db.Column(db.String(2))
    clie_nome = db.Column(db.String(80))
    clie_rgie = db.Column(db.String(20))
    clie_endresnumero = db.Column(db.String(20))
    clie_foneres = db.Column(db.String(15))
    clie_fonecel = db.Column(db.String(15))
    clie_tipo = db.Column(db.String(1))
    
    cidades = db.relationship(
        'CidadesModel',
        backref='related_clientes',
        viewonly=True
    )
    
    def to_dict(self):
        return {
            'bairroent': self.clie_bairrores,
            'bloqueio': self.clie_situacao,
            'cepent': self.clie_cepres,
            'cgcent': self.clie_cnpjcpf,
            'cliente': self.clie_razaosocial,
            'codatv1': self.clie_ramoatividade,
            'codcidade': self.clie_muni_codigo_res,
            'codcli': self.clie_codigo,
            'codcob': self.clie_lpgt_codigo,
            'codfuncultalter': self.clie_usualt,
            'codplpag': self.clie_fpgt_codigo,
            'codpraca': self.clie_rota_codigo,
            'codrota': self.clie_rota_codigo,
            'codusur1': self.clie_vend_codigo,
            'codusur2': self.clie_vend_alternativos,
            'consumidorfinal': self.clie_tipos,
            'contribuinte': self.clie_contribuinte,
            'email': self.clie_email,
            'emailnfe': self.clie_emailnfe,
            'enderent': self.clie_endres,
            'estent': self.clie_ufexprg,
            'fantasia': self.clie_nome,
            'ieent': self.clie_rgie,
            'municent': self.related_cidades.muni_c if self.related_cidades else None,
            'numeroent': self.clie_endresnumero,
            'telcom': self.clie_foneres,
            'telent': self.clie_fonecel,
            'tipofj': self.clie_tipo,
        }