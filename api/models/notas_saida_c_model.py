from api import db

class NotasSaidaCModel(db.Model):
    __tablename__ = 'nfec'
    
    nfec_transacao = db.Column(
        db.String(16), 
        db.ForeignKey('movprodc.mprc_transacao'), 
        db.ForeignKey('movdctos.mdoc_transacao'), 
        primary_key=True
    )
    nfec_numerodcto = db.Column(db.String(20))
    nfec_serie = db.Column(db.String(3))
    nfec_datasaida = db.Column(db.Date)
    nfec_datamvto = db.Column(db.Date)
    nfec_dataemissao = db.Column(db.Date)
    nfec_totaldcto = db.Column(db.Numeric(precision=12, scale=2))
    nfec_es = db.Column(db.String(1))
    nfec_codentidade = db.Column(
        db.Numeric(precision=8, scale=0),
        db.ForeignKey('clientes.clie_codigo')
    )
    nfec_fpgt_codigo = db.Column(db.String(3))
    nfec_unid_codigo = db.Column(db.String(3))
    nfec_idlote = db.Column(db.String(15))
    nfec_pesoliq = db.Column(db.Numeric(precision=18, scale=6))
    nfec_volumes = db.Column(db.Numeric(precision=18, scale=6))
    
       
    historico_pedido_c = db.relationship(
        'HistoricoPedidosCModel',
        backref=db.backref('related_notas_saida_c', uselist=True),
        viewonly=True,
    )
    
    dctos = db.relationship(
        'DctosModel',
        backref=db.backref('related_notas_saida_c', uselist=True),
        viewonly=True,
    )
    
    clientes = db.relationship(
        'ClientesModel',
        backref=db.backref('related_notas_saida_c', uselist=True),
        viewonly=True,
    )
    
    
    def to_dict(self):
        return {
            'numcar': self.movprodc.mprc_carregamento if self.movprodc else None,
            'numnota': str(self.nfec_numerodcto),
            'serie': self.nfec_serie,
            'codusur': str(self.movdctos.mdoc_usulcto if self.movdctos else None),
            'condvenda': int(self.movprodc.mprc_dcto_codigo if self.movprodc else None),
            'numtransvenda': int(self.nfec_transacao),
            'dtsaida': self.nfec_datasaida,
            'dtfat': self.nfec_datamvto,
            'dtentrega': self.nfec_dataemissao,
            'vltotal': self.nfec_totaldcto,
            'especie': 'NF',
            'codclie': str(self.nfec_codentidade),
            'numped': int(self.nfec_transacao),
            'codcob': self.clientes.clie_lpgt_codigo if self.clientes else None,        
            'codplpag': self.nfec_fpgt_codigo,
            'codfilial': self.nfec_unid_codigo,
            'numseq': self.nfec_idlote,
            'totpeso': self.nfec_pesoliq,
            'totvolume': self.nfec_volumes,
            'codsupervisor': '001' if self.nfec_unid_codigo == '001' else (
                '003' if self.nfec_unid_codigo == '003' or self.nfec_unid_codigo == '010' else (
                    '006' if self.nfec_unid_codigo == '002' else None 
                )
            )
        }