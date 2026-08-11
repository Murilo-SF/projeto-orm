# import pytest
# from Projeto_ORM.app import create_app

# app = create_app()

# client = app.test_client()

# # =============================================================TESTE - ROTA "/auth/adicionar"==============================================================
# # ============================================================TESTE PARA REGISTRAR CORRETAMENTE============================================================

# # def test_register_usuario():
# #     resposta = client.post("/auth/adicionar", json={"nome":"Murilo", "senha":"123456"})
# #     assert resposta.status_code == 201


# # ======================================================================TESTES ERRADOS======================================================================

# def test_register_faltando_nome():
#     resposta = client.post("/auth/adicionar", json={"senha":"123456"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["nome"][0] == "Missing data for required field."


# def test_register_faltando_senha():
#     resposta = client.post("/auth/adicionar", json={"nome":"Murilo"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["senha"][0] == "Missing data for required field."


# def test_register_faltando_dados():
#     resposta = client.post("/auth/adicionar", json=None)
#     assert resposta.status_code == 415


# def test_register_json_vazio():
#     resposta = client.post("/auth/adicionar", json={})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"] == {'nome': ['Missing data for required field.'], 'senha': ['Missing data for required field.']}


# def test_register_tipo_errado_nome():
#     resposta = client.post("/auth/adicionar", json={"nome":1, "senha":"123456"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["nome"][0] == "Not a valid string."


# def test_register_tipo_errado_senha():
#     resposta = client.post("/auth/adicionar", json={"nome":"Murilo", "senha":1})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["senha"][0] == "Not a valid string."


# def test_register_tipo_errado_email():
#     resposta = client.post("/auth/adicionar", json={"nome":"Murilo", "senha":"123456", "email":123})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["email"][0] == "Not a valid string."


# def test_register_chave_errada():
#     resposta = client.post("/auth/adicionar", json={"nome":"Murilo", "senha":"123456", "idade": 12})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"] == {'idade': ['Unknown field.']}


# def test_register_nome_duplicado():
#     resposta = client.post("/auth/adicionar", json={"nome":"Murilo da Silva Faccin", "senha":"123456"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"] == "Usuário já existe!"


# def test_register_caracter_min_nome():
#     resposta = client.post("/auth/adicionar", json={"nome":"Mo", "senha":"123456"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."


# def test_register_caracter_min_senha():
#     resposta = client.post("/auth/adicionar", json={"nome":"Murilo", "senha":"123"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."

# # ==============================================================TESTE - ROTA "/auth/login"==============================================================
# # ==================================================================TESTE LOGIN CORRETO=================================================================

# def test_login():
#     resposta = client.post("/auth/login", json={"nome":"Murilo da Silva Faccin", "senha":"murilo"})
#     assert resposta.status_code == 201
#     json = resposta.get_json()
#     assert "token" in json
#     assert isinstance(json["token"], str) # Apenas conferimos se o token é realmente uma String.

# # ==================================================================TESTE LOGIN ERRADO==================================================================

# def test_login_usuario_nao_encontrado():
#     resposta = client.post("/auth/login", json={"nome":"Murilo", "senha":"123456"})
#     assert resposta.status_code == 404
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"] == "Usuário não encontrado!"

# def test_login_senha_incorreta():
#     resposta = client.post("/auth/login", json={"nome":"Murilo da Silva Faccin", "senha":"654321"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"] == "SENHA INCORRETA!"

# def test_login_faltando_nome():
#     resposta = client.post("/auth/login", json={"senha":"123456"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["nome"][0] == "Missing data for required field."

# def test_login_faltando_senha():
#     resposta = client.post("/auth/login", json={"nome":"Murilo da Silva Faccin"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["senha"][0] == "Missing data for required field."

# def test_login_faltando_dados():
#     resposta = client.post("/auth/login", json=None)
#     assert resposta.status_code == 415

# def test_login_json_vazio():
#     resposta = client.post("/auth/login", json={})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"] == {"nome":['Missing data for required field.'], "senha":['Missing data for required field.']}

# def test_login_tipo_errado_nome():
#     resposta = client.post("/auth/login", json={"nome":1, "senha":"123456"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["nome"][0] == "Not a valid string."

# def test_login_tipo_errado_senha():
#     resposta = client.post("/auth/login", json={"nome":"Murilo", "senha":1})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["senha"][0] == "Not a valid string."

# def test_login_chave_errada():
#     resposta = client.post("/auth/login", json={"nome":"Murilo", "senha":"123456", "idade":2})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["idade"][0] == "Unknown field."

# def test_login_caracter_min_nome():
#     resposta = client.post("/auth/login", json={"nome":"Mo", "senha":"123456"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["nome"][0] == "Shorter than minimum length 4."


# def test_login_caracter_min_senha():
#     resposta = client.post("/auth/login", json={"nome":"Murilo", "senha":"123"})
#     assert resposta.status_code == 400
#     assert "error" in resposta.get_json()
#     assert resposta.get_json()["error"]["senha"][0] == "Shorter than minimum length 6."