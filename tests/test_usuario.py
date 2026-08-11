# Descrição de testes para as rotas do usuário

# Listar Usuários
#     Teste feliz, Funcionamento 100%
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
