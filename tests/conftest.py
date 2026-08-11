import pytest
from Projeto_ORM.app import create_app
from Projeto_ORM.extensions import db
from Projeto_ORM.models.tabela_usuario import Usuario
from alembic.config import Config
from alembic import command
from werkzeug.security import generate_password_hash

@pytest.fixture(scope="session")
def app():
    app = create_app('testing')

    with app.app_context(): #Precisamos desta linha para ele não "fugir" do contexto, se não ele da erro, pois não encontrar nenhum app em atividade.
        yield app

    print("Encerrando sessão")


import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

@pytest.fixture(scope="session")
def prepare_database(app):

    alembic_cfg = Config(str(BASE_DIR / "alembic.ini"))
    alembic_cfg.set_main_option("script_location", str(BASE_DIR / "migrations"))
    command.upgrade(alembic_cfg, "head")


@pytest.fixture(scope="function")
def db_session(prepare_database):

    session = db.session

    yield session

    session.rollback() # MUITO IMPORTANTE PARA O FUNCIONAMENTO CORRETO DURANTE OS TESTES.

    session.close()


@pytest.fixture(scope="function")
def client(app, prepare_database): # Esta fixture recebe o prepare_database, apenas por questão de arquitetura, para não acontecer de rodarmos sem o banco estar preparado.
    return app.test_client()


@pytest.fixture(scope="function")
def criar_usuario_admin(db_session, client):

    usuario_admin = Usuario(nome="Admin teste", senha=generate_password_hash("123456"), role="admin")

    db_session.add(usuario_admin)

    # Neste caso onde criamos um usuário admin para testarmos nossa API e suas rotas, usamos o flush, pois ele executa os inserts, mas não encerra a sessão
    # Assim, podemos dar o rollback e voltar o banco como no início, diferentemente do commit, que encerra a sessão.
    db_session.flush()
        
    return usuario_admin

