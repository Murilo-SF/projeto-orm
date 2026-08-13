import pytest
from Projeto_ORM.models.tabela_usuario import Usuario

# =============================================================TESTE - ROTA "/auth/adicionar"==============================================================
# ============================================================TESTE PARA REGISTRAR CORRETAMENTE============================================================

def test_register_usuario(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome Teste", "senha":"123456"})
    assert resposta.status_code == 201
    assert resposta.get_json()['message'] == "Usuário cadastrado com sucesso!"

# ======================================================================TESTES ERRADOS======================================================================

def test_register_faltando_nome(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Missing data for required field."


def test_register_faltando_senha(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Missing data for required field."


def test_register_faltando_dados(client, admin_user):
    resposta = client.post("/auth/adicionar", json=None)
    assert resposta.status_code == 415


def test_register_json_vazio(client, admin_user):
    resposta = client.post("/auth/adicionar", json={})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {'nome': ['Missing data for required field.'], 'senha': ['Missing data for required field.']}


def test_register_tipo_errado_nome(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":1, "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Not a valid string."


def test_register_tipo_errado_senha(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":1})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Not a valid string."


def test_register_tipo_errado_email(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":"123456", "email":123})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["email"][0] == "Not a valid string."


def test_register_chave_errada(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":"123456", "idade": 12})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {'idade': ['Unknown field.']}


def test_register_nome_duplicado(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário já existe!"


def test_register_caracter_min_nome(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":"Mo", "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."


def test_register_caracter_min_senha(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":"123"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."

# ==============================================================TESTE - ROTA "/auth/login"==============================================================
# ==================================================================TESTE LOGIN CORRETO=================================================================

def test_login(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome,"senha":"123456"})
    assert resposta.status_code == 201
    json = resposta.get_json()
    assert "token" in json
    assert isinstance(json["token"], str) # Apenas conferimos se o token é realmente uma String.

# ==================================================================TESTE LOGIN ERRADO==================================================================

def test_login_usuario_nao_encontrado(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":"Nome", "senha":"123456"})
    assert resposta.status_code == 404
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário não encontrado!"

def test_login_senha_incorreta(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":"654321"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "SENHA INCORRETA!"

def test_login_faltando_nome(client, admin_user):
    resposta = client.post("/auth/login", json={"senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Missing data for required field."

def test_login_faltando_senha(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Missing data for required field."

def test_login_faltando_dados(client, admin_user):
    resposta = client.post("/auth/login", json=None)
    assert resposta.status_code == 415

def test_login_json_vazio(client, admin_user):
    resposta = client.post("/auth/login", json={})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {"nome":['Missing data for required field.'], "senha":['Missing data for required field.']}

def test_login_tipo_errado_nome(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":1, "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Not a valid string."

def test_login_tipo_errado_senha(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":1})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Not a valid string."

def test_login_chave_errada(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":"123456", "idade":2})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["idade"][0] == "Unknown field."

def test_login_caracter_min_nome(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":"Mo", "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."

def test_login_caracter_min_senha(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":"123"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."


# Verificando durante os testes se o usuário realmente está no banco
def test_usuario_admin_existe(admin_user, db_session):
    usuario_admin = db_session.get(Usuario, admin_user.id)

    assert usuario_admin is not None
    assert usuario_admin.nome == "Admin Teste"
    assert usuario_admin.role == "admin"



def test_deletar_usuario(db_session):
    usuario = Usuario.query.filter_by(nome="Nome Teste").first()
    
    db_session.delete(usuario)

    db_session.commit()