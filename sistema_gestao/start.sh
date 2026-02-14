#!/bin/bash
# Quick Start - Sistema de Gestão de Tarefas

echo "🚀 Iniciando Sistema de Gestão de Tarefas..."

# Navegar para a pasta
cd "c:\Users\braga\Documents\Braga Dos Santos\Python on Fire\sistema_gestao"

# Ativar ambiente virtual
echo "📦 Ativando ambiente virtual..."
.\venv\Scripts\Activate.ps1

# Instalar dependências (se necessário)
echo "⬇️ Verificando dependências..."
python -m pip install -q -r requirements.txt

# Aplicar migrações
echo "🗄️ Aplicando migrações do banco de dados..."
python manage.py migrate --no-input

# Iniciar servidor
echo "✅ Iniciando servidor Django..."
echo "📍 Acesse http://127.0.0.1:8000/"
echo "👤 Admin: http://127.0.0.1:8000/admin/"
echo "🔌 API: http://127.0.0.1:8000/api/"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo ""

python manage.py runserver
