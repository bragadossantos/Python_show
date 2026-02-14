from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    cor = models.CharField(max_length=7, default='#667eea')
    criada_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_vencimento = models.DateField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    prioridade = models.CharField(
        max_length=10,
        choices=[('Baixa', 'Baixa'), ('Média', 'Média'), ('Alta', 'Alta')],
        default='Média'
    )
    
    class Meta:
        ordering = ['-data_criacao']
        
    def __str__(self):
        return self.titulo
    
    def dias_restantes(self):
        from datetime import date
        if self.data_vencimento:
            return (self.data_vencimento - date.today()).days
        return None
