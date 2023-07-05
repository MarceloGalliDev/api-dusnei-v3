from ..models import funcionarios_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc, asc

def listar_funcionarios():
    func = aliased(funcionarios_model.FuncionariosModel)
    
    funcionarios = db.session.query(
        func.func_tipos,
        func.func_nome,
        func.func_email,
        func.func_codigo,
        func.func_celular,
        func.func_unid_codigo,
        func.func_funcao,
        func.func_cpf,
        func.func_situacao,
        func.func_observacao,
    ).order_by(asc(func.func_codigo))
    
    return funcionarios