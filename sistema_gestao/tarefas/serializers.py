from rest_framework import serializers
from .models import Tarefa, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao', 'cor']

class TarefaSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id', 'titulo', 'descricao', 'categoria', 'categoria_nome', 
                  'prioridade', 'concluida', 'data_criacao', 'data_vencimento']
        read_only_fields = ['data_criacao', 'user']
