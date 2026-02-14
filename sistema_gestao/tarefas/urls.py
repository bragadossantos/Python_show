from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('exportar-pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
    path('concluida/<int:id>/', views.marcar_concluida, name='marcar_concluida'),
]
