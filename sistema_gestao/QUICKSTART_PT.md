# ⚡ Guia Rápido - Sistema de Gestão de Tarefas

## 🎯 Começo Rápido (5 minutos)

### Passo 1: Abra o Terminal
```bash
cd "c:\Users\braga\Documents\Braga Dos Santos\Python on Fire\sistema_gestao"
```

### Passo 2: Execute o Servidor
```bash
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

### Passo 3: Aceda à Aplicação
- Abra o navegador: http://127.0.0.1:8000/
- Clique em "Cria uma agora" para registar
- Preencha username, email e senha

### Passo 4: Comece a Usar!
- ✨ **Nova Tarefa** - Criar tarefa
- 📊 **Dashboard** - Ver estatísticas  
- 📄 **Exportar PDF** - Download de tarefas
- 🔍 **Pesquisar** - Procurar tarefas
- 📂 **Categorias** - Filtrar por categoria

---

## 🔑 Principais Funcionalidades

### 1. Criar Tarefa
1. Clique em "✨ Nova Tarefa"
2. Preencha título, descrição (opcional)
3. Escolha categoria, prioridade, data vencimento
4. Clique em "✓ Criar Tarefa"

### 2. Editar Tarefa
1. Na lista, clique em "✏️ Editar"
2. Modifique os campos
3. Clique em "✓ Guardar Alterações"

### 3. Marcar Concluída
1. Na lista, clique em "✓ Concluir"
2. A tarefa fica acinzentada
3. Clique novamente para reabrir

### 4. Pesquisar
1. Na barra de pesquisa, digite o termo
2. Escolha categoria (opcional)
3. Clique em "🔎 Filtrar"

### 5. Ver Estatísticas
1. Clique em "📊 Dashboard"
2. Veja gráficos e resumos
3. Clique em "📄 Exportar PDF" para baixar

### 6. Deletar Tarefa
1. Na lista, clique em "🗑️ Deletar"
2. Confirme a ação

---

## 🔌 Utilizar a API REST

### Login
```bash
curl -X POST http://127.0.0.1:8000/api-auth/login/ \
  -d "username=seu_user&password=sua_senha"
```

### Listar Tarefas
```bash
curl -H "Authorization: Token SEU_TOKEN" \
  http://127.0.0.1:8000/api/tarefas/
```

### Criar Tarefa via API
```bash
curl -X POST http://127.0.0.1:8000/api/tarefas/ \
  -H "Authorization: Token SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Tarefa", "prioridade": "Alta"}'
```

### Obter Estatísticas
```bash
curl -H "Authorization: Token SEU_TOKEN" \
  http://127.0.0.1:8000/api/tarefas/estatisticas/
```

Mais detalhes em `API_DOCS.md`

---

## 📁 Ficheiros Importantes

| Ficheiro | Função |
|----------|--------|
| `manage.py` | CLI do Django |
| `requirements.txt` | Dependências |
| `README.md` | Documentação completa |
| `API_DOCS.md` | Docs da API REST |
| `CHANGELOG.md` | Histórico de mudanças |
| `tarefas/models.py` | Modelos de dados |
| `tarefas/views.py` | Lógica das views |
| `tarefas/api_views.py` | ViewSets API |

---

## 🎨 Interface - Cheat Sheet

### Cores & Significado
- 🟩 **Verde** - Prioridade Baixa
- 🟨 **Amarelo** - Prioridade Média
- 🟥 **Vermelho** - Prioridade Alta

### Ícones Rápidos
- ✨ Novo item
- ✏️ Editar
- ✓ Concluir
- 🗑️ Deletar
- 🔍 Pesquisar
- 📊 Dashboard
- 📄 PDF
- 🚪 Sair

---

## ⚙️ Configurações Úteis

### Mudar Porta
```bash
python manage.py runserver 8001
```

### Resetar Banco de Dados
```bash
rm db.sqlite3
python manage.py migrate
```

### Criar Admin
```bash
python manage.py createsuperuser
# Depois aceda em http://127.0.0.1:8000/admin/
```

### Instalar Novo Package
```bash
pip install nome_do_pacote
pip freeze > requirements.txt
```

---

## 🆘 Problemas Comuns

### Port 8000 in use
```bash
# Use outra porta
python manage.py runserver 8001
```

### Arquivo não encontrado
```bash
# Verifique o caminho da pasta
cd "c:\Users\braga\Documents\Braga Dos Santos\Python on Fire\sistema_gestao"
```

### Template Error
```bash
# Reconstrua arquivos estáticos
python manage.py collectstatic --noinput
```

### Erro de Migração
```bash
# Refaça as migrações
python manage.py makemigrations
python manage.py migrate --fake-initial
```

---

## 📊 Estrutura de Dados

### Tarefa
```
- ID (automático)
- Título (obrigatório)
- Descrição
- Categoria (FK)
- Prioridade (Baixa/Média/Alta)
- Concluída (Sim/Não)
- Data Criação (automática)
- Data Vencimento
- Utilizador (FK)
```

### Categoria
```
- ID (automático)
- Nome (único)
- Descrição
- Cor (#HEX)
- Data Criação (automática)
```

---

## 💡 Dicas & Tricks

1. **Guardar como Favorito:** Adicione à Barra de Favoritos
2. **Atalho de Teclado:** Tab para navegar formulários
3. **Exportar PDF:** Use para fazer relatórios mensais
4. **API em Postman:** Importe endpoints no Postman
5. **Mobile:** Funciona em telefones também!

---

## 📚 Recursos Adicionais

- Django Docs: https://docs.djangoproject.com/
- Django REST: https://www.django-rest-framework.org/
- Chart.js: https://www.chartjs.org/
- ReportLab: https://www.reportlab.com/

---

## 🎯 Próximos Passos

1. ✅ Testar todas as funcionalidades
2. ✅ Criar várias tarefas e categorias
3. ✅ Explorar o Dashboard
4. ✅ Testar a API REST
5. ✅ Exportar um PDF de exemplo
6. ✅ Navegar em /admin/ (use as credenciais de criação)

---

## 👏 Parabéns!

Você agora tem um sistema completo de gestão de tarefas!

Aproveite! 🚀

---

**Dúvidas?** Consulte:
- `README.md` - Documentação geral
- `API_DOCS.md` - API REST
- `CHANGELOG.md` - Técnico
