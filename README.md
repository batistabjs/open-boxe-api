# Open Boxe API

API RESTful para o centro de treinamento de alto rendimento **Open Boxe**, desenvolvida em Python com FastAPI.

## Funcionalidades

- **Autenticação**: Cadastro, login e logout de usuários administrativos com JWT
- **Alunos**: Listagem paginada com ordenação e filtros
- **Atletas**: Promoção de alunos a atletas com categorias de peso
- **Treinadores**: Consulta de treinadores por ID
- **Turmas**: Consulta de turmas por ID

## Tecnologias

- **Python 3.10+**
- **FastAPI** - Framework web de alta performance
- **SQLAlchemy** - ORM para banco de dados
- **MySQL** - Banco de dados relacional
- **JWT** - Autenticação via JSON Web Token
- **Pydantic** - Validação de dados

## Estrutura do Projeto

```
open-boxe-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── config.py            # Configurações
│   ├── database.py          # Conexão com banco de dados
│   ├── models/
│   │   ├── __init__.py
│   │   ├── modelos.py       # Modelos SQLAlchemy
│   │   └── schemas.py       # Schemas Pydantic
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── autenticacao.py  # Controlador de autenticação
│   │   ├── alunos.py        # Controlador de alunos
│   │   ├── atletas.py       # Controlador de atletas
│   │   ├── treinadores.py   # Controlador de treinadores
│   │   └── turmas.py        # Controlador de turmas
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── autenticacao.py  # Rotas de autenticação
│   │   ├── alunos.py        # Rotas de alunos
│   │   ├── atletas.py       # Rotas de atletas
│   │   ├── treinadores.py   # Rotas de treinadores
│   │   └── turmas.py        # Rotas de turmas
│   └── middleware/
│       ├── __init__.py
│       └── autenticacao.py  # Middleware de autenticação
├── sql/
│   ├── estrutura.sql        # Script de criação das tabelas
│   └── semeadura.sql        # Script de dados de teste
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## Pré-requisitos

- Python 3.10 ou superior
- MySQL 8.0 ou superior (ou MariaDB 10.5+)
- pip (gerenciador de pacotes)

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/batistabjs/open-boxe-api.git
cd open-boxe-api
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar banco de dados

#### Criar banco de dados MySQL

```sql
CREATE DATABASE open_boxe
 CHARACTER SET utf8mb4
 COLLATE utf8mb4_unicode_ci;
```

#### Executar script de estrutura

```bash
mysql -u root -p open_boxe < sql/estrutura.sql
```

#### Executar script de semeadura (dados de teste)

```bash
mysql -u root -p open_boxe < sql/semeadura.sql
```

### 6. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=mysql+mysqlconnector://root:root@localhost:3306/open_boxe
SECRET_KEY=sua-chave-secreta-aqui-mude-em-producao
```

### 7. Executar a aplicação

```bash
uvicorn app.main:app --reload --host localhost --port 8000
```

A API estará disponível em: `http://localhost:8000`

## Documentação da API

Acesse a documentação interativa em:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

### Autenticação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/autenticacao/cadastro` | Cadastrar novo usuário |
| POST | `/api/v1/autenticacao/login` | Login de usuário |
| DELETE | `/api/v1/autenticacao/sair` | Encerrar sessão |

### Alunos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/alunos` | Listar alunos (paginado) |

### Atletas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/atletas` | Promover aluno a atleta |

### Treinadores

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/treinadores/{id}` | Obter treinador por ID |

### Turmas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/turmas/{id}` | Obter turma por ID |

## Exemplos de Uso

### Cadastro de Usuário

```bash
curl -X POST "http://localhost:8000/api/v1/autenticacao/cadastro" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Carlos Silva",
    "email": "carlos.silva@openboxe.com",
    "nome_usuario": "carlos_admin",
    "senha": "senha_segura"
  }'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/v1/autenticacao/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "carlos.silva@openboxe.com",
    "senha": "senha_segura"
  }'
```

### Listar Alunos (com autenticação)

```bash
curl -X GET "http://localhost:8000/api/v1/alunos?pagina=1&tamanho_pagina=10" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

### Promover Aluno a Atleta

```bash
curl -X POST "http://localhost:8000/api/v1/atletas" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -d '{
    "aluno_id": 1,
    "categoria_peso": "Peso Leve",
    "vitorias": 5,
    "derrotas": 2
  }'
```

### Obter Treinador

```bash
curl -X GET "http://localhost:8000/api/v1/treinadores/1" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

### Obter Turma

```bash
curl -X GET "http://localhost:8000/api/v1/turmas/1" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

## Estrutura do Banco de Dados

### Diagrama Entidade-Relacionamento

```
┌─────────────┐       ┌─────────────┐
│   usuarios   │       │    planos   │
├─────────────┤       ├─────────────┤
│ id (PK)     │       │ id (PK)     │
│ nome        │       │ nome        │
│ email       │       │ preco       │
│ nome_usuario│       │ duracao_mes │
│ senha       │       └─────────────┘
└─────────────┘              │
                        1:N  │
                    ┌─────────┴─────────┐
                    │                   │
              ┌─────────────┐    ┌─────────────┐
              │   alunos    │    │  treinadores │
              ├─────────────┤    ├─────────────┤
              │ id (PK)     │    │ id (PK)     │
              │ plano_id(FK)│    │ nome        │
              │ nome        │    │ especialidade│
              │ email       │    │ biografia   │
              │ data_nasc.  │    └─────────────┘
              └─────────────┘           │
                   │                1:N  │
              1:1  │           ┌─────────┴─────────┐
          ┌────────┴────────┐  │                   │
          │                 │  │                   │
    ┌─────────────┐   ┌─────────────┐       │
    │   atletas   │   │    turmas   │       │
    ├─────────────┤   ├─────────────┤       │
    │ id (PK)     │   │ id (PK)     │       │
    │ aluno_id(FK)│   │ treinador_id│◄──────┘
    │ categoria   │   │ nome        │
    │ vitorias    │   │ horario     │
    │ derrotas    │   │ capacidade  │
    └─────────────┘   └─────────────┘
```

## Regras de Negócio

1. **Usuários**: Apenas administradores podem acessar a API
2. **Alunos**: Devem estar vinculados a um plano válido
3. **Atletas**: Um aluno pode ser promovido a atleta apenas uma vez
4. **Turmas**: Cada turma pertence a apenas um treinador
5. **Autenticação**: Todos os endpoints (exceto login/cadastro) requerem token JWT

## Tratamento de Erros

| Código | Descrição |
|--------|-----------|
| 200 | Sucesso |
| 201 | Criado com sucesso |
| 204 | Sem conteúdo |
| 400 | Requisição inválida |
| 401 | Não autorizado |
| 403 | Proibido |
| 404 | Não encontrado |
| 422 | Entidade não processável |

## Licença

Este projeto é parte de um desafio técnico para avaliação de candidatos.

## Autor

Desenvolvido como parte do desafio de Back-End - Tecnologias Web.