def test_criar_pedido_admin(client, admin_user, headers_admin):
    resposta = client.post('pedido/adicionar', json={"cliente_id":admin_user.id, "valor":100}, headers=headers_admin)

    assert resposta.status_code == 201
    assert "message" in resposta.get_json()
    assert resposta.get_json()["message"] == "Pedido cadastrado com sucesso!"


def test_criar_pedido_usuario_inexistente(client, admin_user, headers_admin):
    resposta = client.post('pedido/adicionar', json={"cliente_id":(admin_user.id + 1), "valor": 100}, headers=headers_admin)

    assert resposta.status_code == 404
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário não encontrado!"


def test_criar_pedido_valor_invalido(client, admin_user, headers_admin):
    resposta = client.post('/pedido/adicionar', json={"cliente_id":admin_user.id, "valor":"Cem"}, headers=headers_admin)

    assert resposta.status_code == 400
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == {'valor': ['Not a valid number.']}


def test_buscar_meu_pedido(client, headers_usuario):
    resposta = client.get('/pedido/me', headers=headers_usuario)

    assert resposta.status_code == 200

def test_buscar_pedido_admin(client, admin_user, headers_admin, pedido_admin):
    resposta = client.get(f'/pedido/{admin_user.id}', headers=headers_admin)

    assert resposta.status_code == 200
    assert "pedidos" in resposta.get_json()


def test_buscar_usuario_sem_admin(client, usuario_comum, headers_usuario):
    resposta = client.get(f'/pedido/{usuario_comum.id}', headers=headers_usuario)

    assert resposta.status_code == 403
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "ACESSO NEGADO!"


def test_buscar_usuario_inexistente(client, admin_user, headers_admin):
    resposta = client.get(f'/pedido/{admin_user.id + 1}', headers=headers_admin)

    assert resposta.status_code == 404
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Usuário não encontrado!"


def test_atualizar_pedido_admin(client, admin_user, headers_admin, pedido_admin):
    resposta = client.put(f'/pedido/atualizar/{pedido_admin.id}', json={"cliente_id": f"{admin_user.id}", "valor": "200"}, headers=headers_admin)

    assert resposta.status_code == 200
    assert "message" in resposta.get_json()
    assert resposta.get_json()["message"] == "Pedido atualizado com sucesso!"


def test_atualizar_pedido_sem_admin(client, admin_user, headers_usuario, pedido_admin):
    resposta = client.put(f'/pedido/atualizar/{pedido_admin.id}', json={"cliente_id": f"{admin_user.id}", "valor": "200"}, headers=headers_usuario)

    assert resposta.status_code == 403
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "ACESSO NEGADO!"


def test_atualizar_pedido_inexistente(client, admin_user, headers_admin):
    resposta = client.put('/pedido/atualizar/1', json={"cliente_id":f"{admin_user.id}", "valor":100}, headers=headers_admin)

    assert resposta.status_code == 404
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Pedido não encontrado!"


def test_deletar_pedido_admin(client, headers_admin, pedido_admin):
    resposta = client.delete(f'/pedido/deletar/{pedido_admin.id}', headers=headers_admin)

    assert resposta.status_code == 200
    assert "message" in resposta.get_json()
    assert resposta.get_json()["message"] == "Pedido deletado com sucesso!"


def test_deletar_usuario_sem_admin(client, headers_usuario, pedido_admin):
    resposta = client.delete(f'/pedido/deletar/{pedido_admin.id}', headers=headers_usuario)

    assert resposta.status_code == 403
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "ACESSO NEGADO!"


def test_deletar_pedido_inexistente(client, headers_admin):
    resposta = client.delete('/pedido/deletar/1', headers=headers_admin)

    assert resposta.status_code == 404
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "Pedido não encontrado!"