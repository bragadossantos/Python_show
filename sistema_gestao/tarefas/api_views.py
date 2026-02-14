from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Tarefa, Categoria
from .serializers import TarefaSerializer, CategoriaSerializer

class IsMeuProprio(permissions.BasePermission):
    """Permissão customizada para verificar se a tarefa pertence ao utilizador"""
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Categoria.objects.all()
    
    @action(detail=False, methods=['get'])
    def minhas_categorias(self, request):
        """Retorna categorias usadas pelas tarefas do utilizador"""
        categorias = Categoria.objects.filter(
            tarefa__user=request.user
        ).distinct()
        serializer = self.get_serializer(categorias, many=True)
        return Response(serializer.data)

class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [permissions.IsAuthenticated, IsMeuProprio]
    
    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def minhas_tarefas(self, request):
        """Retorna todas as tarefas do utilizador"""
        tarefas = self.get_queryset()
        serializer = self.get_serializer(tarefas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pendentes(self, request):
        """Retorna apenas tarefas pendentes"""
        tarefas = self.get_queryset().filter(concluida=False)
        serializer = self.get_serializer(tarefas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def concluidas(self, request):
        """Retorna apenas tarefas concluídas"""
        tarefas = self.get_queryset().filter(concluida=True)
        serializer = self.get_serializer(tarefas, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pesquisar(self, request):
        """Pesquisa tarefas por título ou descrição"""
        query = request.query_params.get('q', '')
        tarefas = self.get_queryset().filter(
            Q(titulo__icontains=query) | Q(descricao__icontains=query)
        )
        serializer = self.get_serializer(tarefas, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def marcar_concluida(self, request, pk=None):
        """Marca uma tarefa como concluída"""
        tarefa = self.get_object()
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
        serializer = self.get_serializer(tarefa)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def estatisticas(self, request):
        """Retorna estatísticas das tarefas do utilizador"""
        from datetime import date
        from django.db.models import Count
        
        tarefas = self.get_queryset()
        total = tarefas.count()
        concluidas = tarefas.filter(concluida=True).count()
        pendentes = tarefas.filter(concluida=False).count()
        vencidas = tarefas.filter(concluida=False, data_vencimento__lt=date.today()).count()
        
        stats = {
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes,
            'vencidas': vencidas,
            'taxa_conclusao': round((concluidas / total * 100) if total > 0 else 0, 1)
        }
        return Response(stats)
