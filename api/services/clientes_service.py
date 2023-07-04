from ..models import clientes_model, cidades_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_clientes():
    clie = aliased(clientes_model.ClientesModel)
    city = aliased(cidades_model.CidadesModel)
    
    clientes = db.session.query(
        clie.clie_bairrores,
        clie.clie_situacao,
        clie.clie_cepres,
        clie.clie_cnpjcpf,
        clie.clie_razaosocial,
        clie.clie_ramoatividade,
        clie.clie_muni_codigo_res,
        clie.clie_codigo,
        clie.clie_lpgt_codigo,
        clie.clie_usualt,
        clie.clie_fpgt_codigo,
        clie.clie_rota_codigo,
        clie.clie_vend_codigo,
        clie.clie_vend_alternativos,
        clie.clie_tipos,
        clie.clie_contribuinte,
        clie.clie_email,
        clie.clie_emailnfe,
        clie.clie_endres,
        clie.clie_ufexprg,
        clie.clie_nome,
        clie.clie_rgie,
        clie.clie_endresnumero,
        clie.clie_foneres,
        clie.clie_fonecel,
        clie.clie_tipo,
        city.muni_nome
    ).join(
        city, clie.clie_muni_codigo_res == city.muni_codigo
    ).filter(
        clie.clie_tipos.notin_(['IN','VE', 'FU', 'UN', 'NL'])
    ).order_by(desc(clie.clie_codigo))
    
    return clientes
    

