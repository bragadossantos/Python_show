# 📋 Sistema de Gestão de Tarefas - Completo

Um sistema robusto de gestão de tarefas com backend Django e frontend HTML/CSS/JavaScript, incluindo API REST, autenticação, categorias, pesquisa e muito mais!

## ✨ Funcionalidades

### Core
- ✅ **Autenticação de Utilizadores** - Sistema de login/registro com senhas encriptadas
- ✅ **Gestão de Tarefas** - CRUD completo (criar, ler, atualizar, deletar)
- ✅ **Categorias** - Organizar tarefas por categorias personalizadas
- ✅ **Prioridades** - Baixa, Média, Alta
- ✅ **Datas de Vencimento** - Rastreamento de prazos

### Avançadas
- ✅ **Pesquisa** - Buscar tarefas por título ou descrição
- ✅ **Estatísticas/Dashboard** - Gráficos com Chart.js mostrando progresso
- ✅ **Exportar PDF** - Download de relatórios em PDF
- ✅ **API REST** - Endpoints completos para integração com outros sistemas

### Interface
- ✅ **Design Responsivo** - Perfeito em desktop, tablet e mobile
- ✅ **Interface Moderna** - Gradientes, animações e ícones
- ✅ **Temas Coloridos** - Cards com cores de prioridade
- ✅ **Filtros Interativos** - Filtrar por categoria, status, etc

## 🚀 Instalação & Setup

### Pré-requisitos
- Python 3.8+
- pip (gestor de pacotes Python)

### Passos

1. **Navegar para a pasta do projeto:**
```bash
cd "c:\Users\braga\Documents\Braga Dos Santos\Python on Fire\sistema_gestao"
```

2. **Ativar ambiente virtual:**
```bash
.\venv\Scripts\Activate.ps1
```

3. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

4. **Aplicar migrações:**
```bash
python manage.py migrate
```

5. **Criar superutilizador (admin):**
```bash
python manage.py createsuperuser
```

6. **Executar servidor:**
```bash
python manage.py runserver
```

7. **Aceder à aplicação:**
- Principal: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- API: http://127.0.0.1:8000/api/

## 📱 Interface da Aplicação

### Páginas

#### 1. **Login/Registro**
- Autenticação segura com Django
- Criação de novas contas
- Validação de senhas

#### 2. **Dashboard de Tarefas**
- Lista completa de tarefas do utilizador
- Filtros por categoria
- Pesquisa em tempo real
- Status visual (concluída/pendente)

#### 3. **Dashboard de Estatísticas**
- Gráficos com Chart.js
- Contadores de tarefas
- Taxa de conclusão
- Distribuição por prioridade/categoria

#### 4. **Nova Tarefa**
- Formulário simples e intuitivo
- Suporte a descrição, categoria, prioridade, vencimento

#### 5. **Editar Tarefa**
- Modificar todos os campos
- Atualizar categoria e prioridade

## 🔌 API REST Endpoints

### Autenticação
- **POST** `/api-auth/login/` - Login
- **POST** `/api-auth/logout/` - Logout

### Tarefas
- **GET** `/api/tarefas/` - Listar tarefas
- **POST** `/api/tarefas/` - Criar tarefa
- **GET** `/api/tarefas/{id}/` - Detalhe da tarefa
- **PUT** `/api/tarefas/{id}/` - Atualizar tarefa
- **DELETE** `/api/tarefas/{id}/` - Deletar tarefa
- **GET** `/api/tarefas/minhas_tarefas/` - Minhas tarefas
- **GET** `/api/tarefas/pendentes/` - Tarefas pendentes
- **GET** `/api/tarefas/concluidas/` - Tarefas concluídas
- **POST** `/api/tarefas/{id}/marcar_concluida/` - Toggle conclusão
- **GET** `/api/tarefas/pesquisar/?q=query` - Pesquisar
- **GET** `/api/tarefas/estatisticas/` - Estatísticas

### Categorias
- **GET** `/api/categorias/` - Listar categorias
- **POST** `/api/categorias/` - Criar categoria
- **GET** `/api/categorias/minhas_categorias/` - Categorias do utilizador

## 📊 Exemplo de Uso da API

```bash
# Login
curl -X POST http://127.0.0.1:8000/api-auth/login/ \
  -d "username=seu_user&password=sua_senha"

# Listar tarefas
curl -X GET http://127.0.0.1:8000/api/tarefas/ \
  -H "Authorization: Token SEU_TOKEN"

# Criar tarefa
curl -X POST http://127.0.0.1:8000/api/tarefas/ \
  -H "Authorization: Token SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Nova tarefa",
    "descricao": "Descrição",
    "prioridade": "Alta",
    "categoria": 1
  }'

# Obter estatísticas
curl -X GET http://127.0.0.1:8000/api/tarefas/estatisticas/ \
  -H "Authorization: Token SEU_TOKEN"
```

## 📦 Dependências

```
Django==6.0.2
djangorestframework==3.16.1
reportlab==4.4.10
Pillow==12.1.1
```

## 🗂️ Estrutura do Projeto

```
sistema_gestao/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tarefas/
│   ├── models.py          # Modelos Tarefa e Categoria
│   ├── views.py           # Views principais
│   ├── api_views.py       # ViewSets da API
│   ├── serializers.py     # Serializers REST
│   ├── urls.py            # URLs principais
│   ├── api_urls.py        # URLs da API
│   ├── admin.py           # Admin panel
│   ├── templates/
│   │   └── tarefas/
│   │       ├── index.html       # Dashboard
│   │       ├── criar.html       # Nova tarefa
│   │       ├── editar.html      # Editar tarefa
│   │       ├── dashboard.html   # Estatísticas
│   │       ├── login.html       # Login
│   │       └── registro.html    # Registro
│   └── migrations/        # Migrações do banco
├── manage.py
└── db.sqlite3            # Banco de dados
```

## 🔐 Segurança

- Autenticação via Django (senhas com hash)
- CSRF Protection
- SQL Injection Prevention (ORM)
- XSS Protection
- Permissões por utilizador

## 🎨 Tecnologias Utilizadas

**Backend:**
- Django 6.0
- Django REST Framework
- ReportLab (PDF)
- SQLite (BD)

**Frontend:**
- HTML5
- CSS3 (com Gradientes, Flexbox, Grid)
- JavaScript (vanilla)
- Chart.js (gráficos)

## 📝 Notas

- O projeto usa SQLite por padrão (ideal para desenvolvimento)
- Para produção, considere usar PostgreSQL
- Implemente email notifications (opcional)
- Considere adicionar sincronização em tempo real com WebSockets

## 🤝 Contribuições

Melhorias sugeridas:
- Colaboração em tarefas (compartilhamento)
- Notificações de tarefas vencidas
- Backup automático
- Dark mode
- Suporte a múltiplos idiomas

## 📄 Licença

Este projeto é de software livre. Utilize livremente!

---

**Desenvolvido com ❤️ usando Django & Python**
