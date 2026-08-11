import pytest
#from Projeto_ORM.tests.conftest import client

# =============================================================TESTE - ROTA "/auth/adicionar"==============================================================
# ============================================================TESTE PARA REGISTRAR CORRETAMENTE============================================================

def test_register_usuario(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome teste", "senha":"123456"})
    assert resposta.status_code == 201


# ======================================================================TESTES ERRADOS======================================================================

def test_register_faltando_nome(client):
    resposta = client.post("/auth/adicionar", json={"senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Missing data for required field."


def test_register_faltando_senha(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome teste"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Missing data for required field."


def test_register_faltando_dados(client):
    resposta = client.post("/auth/adicionar", json=None)
    assert resposta.status_code == 415


def test_register_json_vazio(client):
    resposta = client.post("/auth/adicionar", json={})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {'nome': ['Missing data for required field.'], 'senha': ['Missing data for required field.']}


def test_register_tipo_errado_nome(client):
    resposta = client.post("/auth/adicionar", json={"nome":1, "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Not a valid string."


def test_register_tipo_errado_senha(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome teste", "senha":1})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Not a valid string."


def test_register_tipo_errado_email(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome teste", "senha":"123456", "email":123})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["email"][0] == "Not a valid string."


def test_register_chave_errada(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome teste", "senha":"123456", "idade": 12})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {'idade': ['Unknown field.']}


def test_register_nome_duplicado(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome teste", "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário já existe!"


def test_register_caracter_min_nome(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Mo", "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."


def test_register_caracter_min_senha(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome teste", "senha":"123"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."

# ==============================================================TESTE - ROTA "/auth/login"==============================================================
# ==================================================================TESTE LOGIN CORRETO=================================================================

def test_login(client):
    resposta = client.post("/auth/login", json={"nome":"Nome teste","senha":"123456"})
    assert resposta.status_code == 201
    json = resposta.get_json()
    assert "token" in json
    assert isinstance(json["token"], str) # Apenas conferimos se o token é realmente uma String.

# ==================================================================TESTE LOGIN ERRADO==================================================================

def test_login_usuario_nao_encontrado(client):
    resposta = client.post("/auth/login", json={"nome":"Nome teste", "senha":"123456"})
    assert resposta.status_code == 404
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário não encontrado!"

def test_login_senha_incorreta(client):
    resposta = client.post("/auth/login", json={"nome":"Nome teste", "senha":"654321"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "SENHA INCORRETA!"

def test_login_faltando_nome(client):
    resposta = client.post("/auth/login", json={"senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Missing data for required field."

def test_login_faltando_senha(client):
    resposta = client.post("/auth/login", json={"nome":"Nome teste"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Missing data for required field."

def test_login_faltando_dados(client):
    resposta = client.post("/auth/login", json=None)
    assert resposta.status_code == 415

def test_login_json_vazio(client):
    resposta = client.post("/auth/login", json={})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {"nome":['Missing data for required field.'], "senha":['Missing data for required field.']}

def test_login_tipo_errado_nome(client):
    resposta = client.post("/auth/login", json={"nome":1, "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Not a valid string."

def test_login_tipo_errado_senha(client):
    resposta = client.post("/auth/login", json={"nome":"Nome teste", "senha":1})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Not a valid string."

def test_login_chave_errada(client):
    resposta = client.post("/auth/login", json={"nome":"Nome teste", "senha":"123456", "idade":2})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["idade"][0] == "Unknown field."

def test_login_caracter_min_nome(client):
    resposta = client.post("/auth/login", json={"nome":"Mo", "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."

def test_login_caracter_min_senha(client):
    resposta = client.post("/auth/login", json={"nome":"Nome teste", "senha":"123"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."