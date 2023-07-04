from ..models import funcionarios_model
from sqlalchemy.orm import aliased
from api import db
from sqlalchemy import desc

def listar_funcionarios():
    