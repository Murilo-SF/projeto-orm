# 🚀 API Backend RESTful com Flask & SQLAlchemy

API desenvolvida em Python focada em boas práticas de backend, autenticação segura com JWT, persistência em MySQL utilizando ORM, migrações de banco de dados e suíte de testes automatizados.

---

## 🛠️ Conjunto de Tecnologias

- **Framework Web:** [Flask](https://flask.palletsprojects.com/) para a construção da API RESTful.
- **ORM & Banco de Dados:** [SQLAlchemy](https://www.sqlalchemy.org/) para manipulação do banco via objetos Python e **MySQL** para persistência de dados.
- **Validação de Dados:** [Marshmallow](https://marshmallow.readthedocs.io/) para serialização e validação dos dados da API.
- **Autenticação:** [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/) para geração e controle de Tokens JWT (JSON Web Token).
- **Segurança:** `werkzeug.security` para criptografia/hash seguro de senhas.
- **Migrações:** [Alembic](https://alembic.sqlalchemy.org/) para versionamento e migração do schema do banco de dados.
- **Testes Automatizados:** [Pytest](https://docs.pytest.org/) para execução de testes unitários e de integração.

---

## 📌 Funcionalidades Principais

- [x] Cadastro de usuários com senhas criptografadas (Hash).
- [x] Login de usuários gerando Token de Autenticação JWT.
- [x] Proteção de rotas privadas via decoradores de token.
- [x] Mapeamento de tabelas e relacionamentos via ORM (SQLAlchemy).
- [x] Validação automática dos schemas de entrada/saída de dados.
- [x] Controle de versão do banco de dados com Alembic.
- [x] Testes automatizados cobrindo as rotas da aplicação.

---

## 🚀 Como Executar o Projeto Localmente

### 1. Pré-requisitos
- Python 3.10 ou superior.
- Banco de dados MySQL rodando.

### 2. Passo a passo

# ```bash

# Clone o repositório
git clone https://github.com/Murilo-SF/projeto-orm.git

# Acesse a pasta do projeto
cd projeto-orm

# Crie e ative o ambiente virtual (venv)
python -m venv venv
# No Windows:
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações do banco de dados (Alembic)
flask db upgrade

# Execute a aplicação
python app.py

👤 Desenvolvedor
Projeto desenvolvido por Murilo da Silva Faccin.

Estou estudando desenvolvimento de software de forma autodidata, focado em criar aplicações backend robustas, organizadas e testadas. Em busca da primeira oportunidade na área de Tecnologia!

💼 LinkedIn: linkedin.com/in/murilo-da-silva-faccin-94257631a
🐙 GitHub: @Murilo-SF
