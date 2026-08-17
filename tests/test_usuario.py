# Descrição de testes para as rotas do usuário

# Listar Usuários (usuário comum)
#     Teste feliz, Funcionamento 100% (Admin)
#     token expirado
#     Sem token
#     Não é admin
#     Token inválido
#     Acho que é so isso kkk

# Admin
#     Teste feliz
#     Token expirado
#     Sem token
#     Não é admin
#     Token inválido

# Buscar Usuário
#     Teste feliz
#     Usuário não encontrado (Difícil acontecer)
#     Token expirado
#     Sem token

# Atualizar Usuário
#     Teste feliz
#     Usuário não encontrado
#     Token expirado
#     Sem token
#     Não é admin
#     Token inválido
#     Json None
#     Json vazio
#     Tipo errado Nome (Agora reparei um problema, eu não trato o caso de o nome que for atualizar já ter outra pessoa, mas acredito que vai dar erro do banco mesmo, pois ele é unique, então por enquanto vou deixar assim (preciso tratar esse problema também))
#     Tipo errado Role
#     Tipo errado Senha
#     Tipo errado email (por enquanto o email é apenas tem o mínimo de 14 caracteres, e não é unique, ele foi feito por enquanto mais para testar o alembic)
#     Caractere mínimo Nome
#     Caractere mínimo Senha
#     Caractere mínimo Email
#     Chave errada

# Deletar Usuário
#     Teste feliz
#     Usuário não encontrado
#     Token expirado
#     Sem token
#     Não é admin
#     Token inválido
#     Este preciso apenas do id (vai no http)

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

def test_atualizar_usuario_admin(admin_user, headers_admin, client, db_session):
    resposta = client.put(f'usuario/atualizar/{int(admin_user.id)}', json={"senha":"654321"}, headers=headers_admin)
    assert resposta.status_code == 200
    assert "message" in resposta.get_json()


# def test_deletar_usuarios(db_session, admin_user, usuario_comum):
#     db_session.delete(admin_user)
#     db_session.delete(usuario_comum)