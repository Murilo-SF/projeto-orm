# ======================================================================FRAMEWORK=======================================================================
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# ============================================================CONFIGURAÇÕES E BANCO DE DADOS============================================================
from Projeto_ORM.extensions import db
from Projeto_ORM.config import configs
from Projeto_ORM.transaction import init_transaction

# =======================================================================ERRORS=========================================================================
from Projeto_ORM.errors.handlers import register_error_handlers

# =======================================================================TABELAS========================================================================
from Projeto_ORM.models.tabela_usuario import Usuario
from Projeto_ORM.models.tabela_pedido import Pedido

# ========================================================================ROTAS=========================================================================
from Projeto_ORM.routes import register_blueprints

# ==========================================================INICIANDO APP, BANCO DE DADOS E JWT=========================================================
jwt = JWTManager()

def create_app(config_name="development"):

    aplicativo = Flask(__name__)

    aplicativo.config.from_object(configs[config_name]) 

    db.init_app(aplicativo) # O nome já é bem sugestivo, assim inicializamos o banco de dados
    
    Migrate(aplicativo, db)

    jwt.init_app(aplicativo)

    register_blueprints(aplicativo)

    register_error_handlers(aplicativo)

    init_transaction(aplicativo)

    return aplicativo

app = create_app() # Não precisamos passar development, pois o padrão já o mesmo.

# ==================================================================CRIANDO TABELAS=====================================================================
#with app.app_context():
#    db.create_all()
# Essa forma de criar as tabelas, é usado mais para aprendizado, pois com o Alembic, aproveitamos suas utilidades como se fosse um Git.

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)