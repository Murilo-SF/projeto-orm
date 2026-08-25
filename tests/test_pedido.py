# Teste criar pedido (correto)
# Teste criar pedido(errado):
    # Usuário não existe
    # Valor inválido
    # Faltando id
    # Faltando valor

# Buscar pedido (me):
    # Correto

# Buscar Pedido(admin):
    # Correto
    # Acesso negado
    # Usuário não existe

# Atualizar Pedido(admin):
    # Não admin
    # Usuário não existe
    # Faltando valor
    # Valor incorreto
    # Pedido não encontrado

# Deletar Pedido(admin):
    # Não admin
    # Pedido não existe
    # Usuário não existe

def test_criar_pedido_admin(client, admin_user, headers_admin):
    resposta = client.post('pedido/adicionar', json={"cliente_id":admin_user.id, "valor":100}, headers=headers_admin)

    assert resposta.status_code == 201
    assert "message" in resposta.get_json()
    assert resposta.get_json()["message"] == "Pedido cadastrado com sucesso!"