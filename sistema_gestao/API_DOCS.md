# 📚 Documentação da API REST

## Base URL
```
http://127.0.0.1:8000/api/
```

## Autenticação

A API utiliza a autenticação nativa do Django REST Framework.

### Login
```http
POST /api-auth/login/
Content-Type: application/json

{
  "username": "seu_utilizador",
  "password": "sua_senha"
}
```

**Resposta:**
```json
{
  "key": "seu_token_aqui"
}
```

### Logout
```http
POST /api-auth/logout/
Authorization: Token seu_token_aqui
```

## Endpoints de Tarefas

### 1. Listar Todas as Tarefas
```http
GET /api/tarefas/
Authorization: Token seu_token_aqui
```

**Resposta:**
```json
[
  {
    "id": 1,
    "titulo": "Estudar Django",
    "descricao": "Aprender o framework",
    "categoria": 1,
    "categoria_nome": "Programação",
    "prioridade": "Alta",
    "concluida": false,
    "data_criacao": "2026-02-14T17:30:00Z",
    "data_vencimento": "2026-02-20"
  }
]
```

### 2. Criar Nova Tarefa
```http
POST /api/tarefas/
Authorization: Token seu_token_aqui
Content-Type: application/json

{
  "titulo": "Fazer compras",
  "descricao": "Suco, pão e leite",
  "categoria": 1,
  "prioridade": "Média",
  "data_vencimento": "2026-02-15"
}
```

**Resposta:** (201 Created)
```json
{
  "id": 5,
  "titulo": "Fazer compras",
  "descricao": "Suco, pão e leite",
  "categoria": 1,
  "categoria_nome": "Pessoal",
  "prioridade": "Média",
  "concluida": false,
  "data_criacao": "2026-02-14T18:00:00Z",
  "data_vencimento": "2026-02-15"
}
```

### 3. Obter Detalhes de Uma Tarefa
```http
GET /api/tarefas/1/
Authorization: Token seu_token_aqui
```

**Resposta:**
```json
{
  "id": 1,
  "titulo": "Estudar Django",
  "descricao": "Aprender o framework",
  "categoria": 1,
  "categoria_nome": "Programação",
  "prioridade": "Alta",
  "concluida": false,
  "data_criacao": "2026-02-14T17:30:00Z",
  "data_vencimento": "2026-02-20"
}
```

### 4. Atualizar Uma Tarefa
```http
PUT /api/tarefas/1/
Authorization: Token seu_token_aqui
Content-Type: application/json

{
  "titulo": "Estudar Django e Flask",
  "prioridade": "Alta",
  "concluida": false
}
```

### 5. Deletar Uma Tarefa
```http
DELETE /api/tarefas/1/
Authorization: Token seu_token_aqui
```

**Resposta:** (204 No Content)

### 6. Listar Minhas Tarefas
```http
GET /api/tarefas/minhas_tarefas/
Authorization: Token seu_token_aqui
```

### 7. Listar Tarefas Pendentes
```http
GET /api/tarefas/pendentes/
Authorization: Token seu_token_aqui
```

### 8. Listar Tarefas Concluídas
```http
GET /api/tarefas/concluidas/
Authorization: Token seu_token_aqui
```

### 9. Marcar Tarefa como Concluída/Pendente
```http
POST /api/tarefas/1/marcar_concluida/
Authorization: Token seu_token_aqui
```

**Resposta:** (200 OK) - Retorna a tarefa atualizada

### 10. Pesquisar Tarefas
```http
GET /api/tarefas/pesquisar/?q=Django
Authorization: Token seu_token_aqui
```

**Resposta:** Lista de tarefas que contêm "Django" no título ou descrição

### 11. Obter Estatísticas
```http
GET /api/tarefas/estatisticas/
Authorization: Token seu_token_aqui
```

**Resposta:**
```json
{
  "total": 15,
  "concluidas": 8,
  "pendentes": 7,
  "vencidas": 2,
  "taxa_conclusao": 53.3
}
```

## Endpoints de Categorias

### 1. Listar Todas as Categorias
```http
GET /api/categorias/
Authorization: Token seu_token_aqui
```

**Resposta:**
```json
[
  {
    "id": 1,
    "nome": "Trabalho",
    "descricao": "Tarefas de trabalho",
    "cor": "#667eea"
  },
  {
    "id": 2,
    "nome": "Pessoal",
    "descricao": "Tarefas pessoais",
    "cor": "#4CAF50"
  }
]
```

### 2. Criar Nova Categoria
```http
POST /api/categorias/
Authorization: Token seu_token_aqui
Content-Type: application/json

{
  "nome": "Saúde",
  "descricao": "Tarefas de saúde e bem-estar",
  "cor": "#FF6B6B"
}
```

### 3. Obter Minhas Categorias
```http
GET /api/categorias/minhas_categorias/
Authorization: Token seu_token_aqui
```

Retorna apenas as categorias usadas em suas tarefas

## Códigos de Resposta HTTP

| Código | Significa | Explicação |
|--------|-----------|-----------|
| 200 | OK | Requisição bem-sucedida |
| 201 | Created | Recurso criado com sucesso |
| 204 | No Content | Operação bem-sucedida (sem corpo de resposta) |
| 400 | Bad Request | Erro na requisição (dados inválidos) |
| 401 | Unauthorized | Autenticação necessária ou inválida |
| 403 | Forbidden | Acesso negado (sem permissão) |
| 404 | Not Found | Recurso não encontrado |
| 500 | Server Error | Erro no servidor |

## Exemplos usando Python

### Com Requests
```python
import requests

# URL base da API
BASE_URL = "http://127.0.0.1:8000/api"

# Fazer login
response = requests.post(
    f"{BASE_URL}../api-auth/login/",
    json={"username": "seu_user", "password": "sua_senha"}
)
token = response.json()["key"]

headers = {"Authorization": f"Token {token}"}

# Listar tarefas
tarefas = requests.get(f"{BASE_URL}/tarefas/", headers=headers).json()
print(tarefas)

# Criar tarefa
nova_tarefa = {
    "titulo": "Aprender API REST",
    "prioridade": "Alta",
    "categoria": 1
}
response = requests.post(
    f"{BASE_URL}/tarefas/",
    json=nova_tarefa,
    headers=headers
)
print(response.json())

# Marcar como concluída
requests.post(f"{BASE_URL}/tarefas/1/marcar_concluida/", headers=headers)

# Obter estatísticas
stats = requests.get(f"{BASE_URL}/tarefas/estatisticas/", headers=headers).json()
print(f"Total: {stats['total']}, Concluídas: {stats['concluidas']}")
```

### Com cURL
```bash
# Login
curl -X POST http://127.0.0.1:8000/api-auth/login/ \
  -d "username=seu_user&password=sua_senha"

# Listar tarefas
curl -H "Authorization: Token seu_token" \
  http://127.0.0.1:8000/api/tarefas/

# Criar tarefa
curl -X POST http://127.0.0.1:8000/api/tarefas/ \
  -H "Authorization: Token seu_token" \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Tarefa", "prioridade": "Alta"}'

# Pesquisar
curl "http://127.0.0.1:8000/api/tarefas/pesquisar/?q=Django" \
  -H "Authorization: Token seu_token"
```

## Filtros e Query Parameters

### Ordenação
```http
GET /api/tarefas/?ordering=-data_criacao
```

### Paginação
```http
GET /api/tarefas/?page=1&page_size=10
```

### Pesquisa
```http
GET /api/tarefas/pesquisar/?q=seu_termo_aqui
```

## Tratamento de Erros

### Exemplo de erro 400
```json
{
  "titulo": ["Este campo é obrigatório."]
}
```

### Exemplo de erro 401
```json
{
  "detail": "Autenticação não fornecida."
}
```

### Exemplo de erro 403
```json
{
  "detail": "Você não tem permissão para executar essa ação."
}
```

## Dicas

1. **Teste a API com Postman** - Ferramenta visual para testar APIs
2. **Use Tokens** - Guarde seu token de autenticação em segurança
3. **Verifique os Headers** - Sempre inclua `Authorization: Token`
4. **Leia os Erros** - A API retorna mensagens de erro úteis

---

**Aproveite a API! 🚀**
