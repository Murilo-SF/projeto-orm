from Projeto_ORM.models.tabela_usuario import Usuario

def test_buscar_usuario_admin(client, headers_admin):
    resposta = client.get('/usuario/me', headers=headers_admin)
    assert resposta.status_code == 200
    assert "user" in resposta.get_json()


def test_buscar_todos_usuarios_admin(client, headers_admin):
    resposta = client.get('/usuario/todos', headers=headers_admin)
    assert resposta.status_code == 200
    assert "usuarios" in resposta.get_json()


def test_buscar_todos_usuarios_sem_admin(client, headers_usuario):
    resposta = client.get('/usuario/todos', headers=headers_usuario)
    assert resposta.status_code == 403
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "ACESSO NEGADO!"


def test_atualizar_usuario_admin(admin_user, headers_admin, client):
    resposta = client.put(f'usuario/atualizar/{int(admin_user.id)}', json={"senha":"654321"}, headers=headers_admin)
    assert resposta.status_code == 200
    assert "message" in resposta.get_json()


def test_atualizar_usuario_sem_admin(usuario_comum, headers_usuario, client):
    resposta = client.put(f'usuario/atualizar/{int(usuario_comum.id)}', json={"senha":"654321"}, headers=headers_usuario)
    assert resposta.status_code == 403
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "ACESSO NEGADO!"


def test_deletar_usuario_sem_admin(client, headers_usuario, usuario_comum):
    usuario = Usuario.query.filter_by(nome=(usuario_comum.nome)).first()
    assert usuario is not None
    resposta = client.delete(f'usuario/deletar/{int(usuario.id)}', headers=headers_usuario)
    assert resposta.status_code == 403
    assert "error" in resposta.get_json()
    assert resposta.get_json()["error"] == "ACESSO NEGADO!"

def test_deletar_usuario_com_admin(client, headers_admin, usuario_comum):
    usuario = Usuario.query.filter_by(nome=(usuario_comum.nome)).first()

    assert usuario is not None

    resposta = client.delete(f'usuario/deletar/{int(usuario.id)}', headers=headers_admin)

    assert resposta.status_code == 200
    assert "message" in resposta.get_json()
    assert resposta.get_json()["message"] == "Usuário deletado com sucesso!"
    admin = Usuario.query.filter_by(nome="Admin Teste").first()