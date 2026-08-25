# ---------------------------------------------------------------->>>IMPORTS<<<----------------------------------------------------------------
import pytest
from Projeto_ORM.app import create_app
from Projeto_ORM.extensions import db
from Projeto_ORM.models.tabela_usuario import Usuario
from Projeto_ORM.models.tabela_pedido import Pedido
from alembic.config import Config
from alembic import command
from werkzeug.security import generate_password_hash
from pathlib import Path

# ---------------------------------------------------------------->>>FIXTURES<<<----------------------------------------------------------------
# ---------------------------------------------------------------->>>fn app<<<----------------------------------------------------------------
@pytest.fixture(scope="session")
def app():
    app = create_app('testing')

    with app.app_context(): #Precisamos desta linha para ele não "fugir" do contexto, se não ele da erro, pois não encontrar nenhum app em atividade.
        yield app

    print("Encerrando sessão")

# ---------------------------------------------------------------->>>fn prepare_database<<<----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent # C:\Users\admin\CODES PYTHON\venv\Projeto_ORM/tests/conftest.py | Conforme o .parent, "voltamos" uma pasta no caminho. 

alembic_cfg = Config(str(BASE_DIR / "alembic.ini"))

print (BASE_DIR, '\n', alembic_cfg.config_file_name)  # alembic... -> C:\Users\admin\CODES PYTHON\venv\Projeto_ORM\alembic.ini

@pytest.fixture(scope="session")
def prepare_database(app):

    alembic_cfg = Config(str(BASE_DIR / "alembic.ini"))
    alembic_cfg.set_main_option("script_location", str(BASE_DIR / "migrations"))
    command.upgrade(alembic_cfg, "head")

# ---------------------------------------------------------------->>>fn db_sessio<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def db_session(prepare_database):

    session = db.session

    yield session

    session.rollback() # MUITO IMPORTANTE PARA O FUNCIONAMENTO CORRETO DURANTE OS TESTES.

    session.close()

# ---------------------------------------------------------------->>>fn app<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def client(app, prepare_database): # Esta fixture recebe o prepare_database, apenas por questão de arquitetura, para não acontecer de rodarmos sem o banco estar preparado.
    return app.test_client()

# ---------------------------------------------------------------->>>fn admin_user<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def admin_user(db_session):

    usuario_admin = Usuario(nome="Admin Teste", senha=generate_password_hash("123456"), role="admin")

    db_session.add(usuario_admin)

    # Neste caso onde criamos um usuário admin para testarmos nossa API e suas rotas, usamos o flush, pois ele executa os inserts, mas não encerra a sessão
    # Assim, podemos dar o rollback e voltar o banco como no início, diferentemente do commit, que encerra a sessão.
    db_session.flush()
        
    return usuario_admin

# ---------------------------------------------------------------->>>fn usuario_comum<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def usuario_comum(db_session):
    usuario = Usuario(nome="Usuário Comum", senha=generate_password_hash("123456"), role="user")

    db_session.add(usuario)

    db_session.flush()

    return usuario


# ---------------------------------------------------------------->>>fn token_admin<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def token_admin(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":"123456"})
    return resposta.get_json()["token"]

# ---------------------------------------------------------------->>>fn headers_admin<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def headers_admin(token_admin):
    headers = {"Authorization":f"Bearer {token_admin}"}
    return headers

# ---------------------------------------------------------------->>>fn token_usuario<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def token_usuario(client, usuario_comum):
    resposta = client.post("/auth/login", json={"nome":usuario_comum.nome, "senha":"123456"})
    return resposta.get_json()["token"]

# ---------------------------------------------------------------->>>fn headers_usuario<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def headers_usuario(token_usuario):
    headers = {"Authorization":f"Bearer {token_usuario}"}
    return headers


# ---------------------------------------------------------------->>>fn pedido_admin<<<----------------------------------------------------------------
@pytest.fixture(scope="function")
def pedido_admin(admin_user, db_session):
    pedido = Pedido(cliente_id=admin_user.id, valor=100.0)

    db_session.add(pedido)

    db_session.flush()

    return pedido