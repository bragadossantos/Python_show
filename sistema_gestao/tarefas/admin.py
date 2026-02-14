from django.contrib import admin
from .models import Tarefa, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'cor')
    search_fields = ('nome',)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'prioridade', 'concluida', 'data_criacao')
    list_filter = ('concluida', 'prioridade', 'categoria')
    search_fields = ('titulo', 'descricao')
    readonly_fields = ('data_criacao',)
