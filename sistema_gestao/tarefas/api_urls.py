from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TarefaViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet, basename='api-tarefa')
router.register(r'categorias', CategoriaViewSet, basename='api-categoria')

urlpatterns = [
    path('', include(router.urls)),
]
