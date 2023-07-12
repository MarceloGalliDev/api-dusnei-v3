from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from dotenv import load_dotenv
# from flask_jwt_extended import JWTManager

load_dotenv()

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
    notas_saida_c_model,
    notas_saida_d_model,
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
    historico_pedido_d_0123_model, 
    historico_pedido_d_0223_model, 
    historico_pedido_d_0323_model, 
    historico_pedido_d_0423_model, 
    historico_pedido_d_0523_model, 
    historico_pedido_d_0623_model, 
    historico_pedido_d_0723_model, 
    historico_pedido_d_0823_model, 
    historico_pedido_d_0923_model, 
    historico_pedido_d_1023_model, 
    historico_pedido_d_1123_model, 
    historico_pedido_d_1223_model,
    veiculos_model, 
)
from .views import (
    departamentos_view, 
    cidades_view,
    notas_saida_c_view,
    notas_saida_d_view,
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
    historico_pedido_d_0123_view,
    historico_pedido_d_0223_view,
    historico_pedido_d_0323_view,
    historico_pedido_d_0423_view,
    historico_pedido_d_0523_view,
    historico_pedido_d_0623_view,
    historico_pedido_d_0723_view,
    historico_pedido_d_0823_view,
    historico_pedido_d_0923_view,
    historico_pedido_d_1023_view,
    historico_pedido_d_1123_view,
    historico_pedido_d_1223_view,
    veiculos_view
)
