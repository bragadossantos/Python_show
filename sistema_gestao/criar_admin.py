#!/usr/bin/env python
"""
Script para criar admin do Django automaticamente
"""
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Dados do admin
ADMIN_USERNAME = 'admin'
ADMIN_EMAIL = 'admin@exemplo.com'
ADMIN_PASSWORD = 'admin123'

def criar_admin():
    """Cria superuser se não existir"""
    if User.objects.filter(username=ADMIN_USERNAME).exists():
        print(f"✓ Admin '{ADMIN_USERNAME}' já existe!")
        return False
    
    User.objects.create_superuser(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD
    )
    print(f"✅ Admin criado com sucesso!")
    print(f"   Username: {ADMIN_USERNAME}")
    print(f"   Password: {ADMIN_PASSWORD}")
    print(f"   Acesso: http://127.0.0.1:8000/admin/")
    return True

if __name__ == '__main__':
    criar_admin()
