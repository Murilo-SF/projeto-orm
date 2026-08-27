import pytest
from Projeto_ORM.models.tabela_usuario import Usuario

# =============================================================TESTE - ROTA "/auth/adicionar"==============================================================
# ============================================================TESTE PARA REGISTRAR CORRETAMENTE============================================================


@pytest.mark.auth
def test_register_usuario(client):
    resposta = client.post("/auth/adicionar", json={"nome":"Nome Teste", "senha":"123456"})
    assert resposta.status_code == 201
    assert resposta.get_json()['message'] == "Usuário cadastrado com sucesso!"

# ======================================================================TESTES ERRADOS======================================================================

# Esse decorator serve para evitarmos repetição de testes e código, quando os testes tem a mesma regra de negócio, porém com dados diferentes
@pytest.mark.auth
@pytest.mark.parametrize(
    "dados, campo",
    [
        ({"senha":"123456"}, "nome"), 
        ({"nome":"Murilo"}, "senha")
    ]
) 
def test_register_faltando_campo(client, campo, dados):
    resposta = client.post('/auth/adicionar', json=dados)
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"][campo][0] == ("Missing data for required field.")


@pytest.mark.auth
def test_register_faltando_dados(client):
    resposta = client.post("/auth/adicionar", json=None)
    assert resposta.status_code == 415


@pytest.mark.auth
def test_register_json_vazio(client):
    resposta = client.post("/auth/adicionar", json={})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {'nome': ['Missing data for required field.'], 'senha': ['Missing data for required field.']}


@pytest.mark.auth
@pytest.mark.parametrize(
        "dados, campo",
        [
            ({"nome":1, "senha":"123456"}, "nome"),
            ({"nome":"Joaquim", "senha":1}, "senha"),
            ({"nome":"Joaquim", "senha":"123456", "email":123}, "email")
        ]
)
def test_register_tipo_errado_dados(client, dados, campo):
    resposta = client.post('/auth/adicionar', json=dados)

    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"][campo][0] == "Not a valid string."


@pytest.mark.auth
def test_register_chave_errada(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":"123456", "idade": 12})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {'idade': ['Unknown field.']}


@pytest.mark.auth
def test_register_nome_duplicado(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário já existe!"


@pytest.mark.auth
def test_register_caracter_min_nome(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":"Mo", "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."


@pytest.mark.auth
def test_register_caracter_min_senha(client, admin_user):
    resposta = client.post("/auth/adicionar", json={"nome":admin_user.nome, "senha":"123"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."

# ==============================================================TESTE - ROTA "/auth/login"==============================================================
# ==================================================================TESTE LOGIN CORRETO=================================================================

@pytest.mark.auth
def test_login(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome,"senha":"123456"})
    assert resposta.status_code == 201
    json = resposta.get_json()
    assert "token" in json
    assert isinstance(json["token"], str) # Apenas conferimos se o token é realmente uma String.

# ==================================================================TESTE LOGIN ERRADO==================================================================

@pytest.mark.auth
def test_login_usuario_nao_encontrado(client):
    resposta = client.post("/auth/login", json={"nome":"Nome", "senha":"123456"})
    assert resposta.status_code == 404
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário não encontrado!"

@pytest.mark.auth
def test_login_senha_incorreta(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":"654321"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "SENHA INCORRETA!"

@pytest.mark.auth
@pytest.mark.parametrize(
        "dados, campo",
        [
            ({"senha":"123456"}, "nome"),
            ({"nome":"Mauro"}, "senha")
        ]
)
def test_login_faltando_dados(client, dados, campo):
    resposta = client.post('auth/login', json=dados)

    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"][campo][0] == "Missing data for required field."


@pytest.mark.auth
def test_login_faltando_dados(client):
    resposta = client.post("/auth/login", json=None)
    assert resposta.status_code == 415

@pytest.mark.auth
def test_login_json_vazio(client):
    resposta = client.post("/auth/login", json={})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {"nome":['Missing data for required field.'], "senha":['Missing data for required field.']}

@pytest.mark.auth
@pytest.mark.parametrize(
        "dados, campos",
        [
            ({"nome":1, "senha":"123456"}, "nome"),
            ({"nome":"Snoop Dog", "senha":1}, "senha")
        ]
)
def test_login_tipo_errado_dados(client, dados, campos):
    resposta = client.post('/auth/login', json=dados)

    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"][campos][0] == "Not a valid string."


@pytest.mark.auth
def test_login_chave_errada(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":"123456", "idade":2})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["idade"][0] == "Unknown field."

@pytest.mark.auth
def test_login_caracter_min_nome(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":"Mo", "senha":"123456"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."

@pytest.mark.auth
def test_login_caracter_min_senha(client, admin_user):
    resposta = client.post("/auth/login", json={"nome":admin_user.nome, "senha":"123"})
    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."


# Verificando durante os testes se o usuário realmente está no banco
@pytest.mark.auth
def test_usuario_admin_existe(admin_user, db_session):
    usuario_admin = db_session.get(Usuario, admin_user.id)

    assert usuario_admin is not None
    assert usuario_admin.nome == "Admin Teste"
    assert usuario_admin.role == "admin"


@pytest.mark.auth
def test_token_admin(token_admin): # token_admin retorna o token.
    assert isinstance(token_admin, str) # Confere se o a varíavel token admin é uma string