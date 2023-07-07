from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
# from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')

# jwt = JWTManager(app)

db = SQLAlchemy(app)

ma = Marshmallow(app)

mi = Migrate(app, db)

api = Api(app)

from .models import (
    departamentos_model, 
    cidades_model,
    historico_pedido_d_0123_model, 
    unidades_model,
    vendedores_model,
    dctos_model,
    historico_pedido_c_model,
    clientes_model,
    funcionarios_model,
    estoque_model,
    produtos_model,
    pendencias_financeiras_model,
    carregamentos_model,
)
from .views import (
    departamentos_view, 
    cidades_view,
    historico_pedido_d_0123_view,
    unidades_view,
    vendedores_view,
    dctos_view,
    historico_pedido_c_view,
    clientes_view,
    funcionarios_view,
    estoque_view,
    produtos_view,
    pendencias_financeiras_view,
    cobranca_view,
    carregamentos_view,
)
