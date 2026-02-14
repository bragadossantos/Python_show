from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Tarefa, Categoria
from datetime import date

@login_required(login_url='login')
def dashboard(request):
    tarefas = Tarefa.objects.filter(user=request.user)
    
    # Estatísticas gerais
    total_tarefas = tarefas.count()
    tarefas_concluidas = tarefas.filter(concluida=True).count()
    tarefas_pendentes = tarefas.filter(concluida=False).count()
    
    # Tarefas por prioridade
    prioridade_stats = tarefas.values('prioridade').annotate(count=Count('id')).order_by('prioridade')
    
    # Tarefas vencidas
    tarefas_vencidas = tarefas.filter(
        concluida=False,
        data_vencimento__lt=date.today()
    ).count()
    
    # Tarefas por categoria
    categoria_stats = tarefas.values('categoria__nome').annotate(count=Count('id')).order_by('-count')
    
    # Taxa de conclusão
    taxa_conclusao = round((tarefas_concluidas / total_tarefas * 100) if total_tarefas > 0 else 0, 1)
    
    contexto = {
        'total_tarefas': total_tarefas,
        'tarefas_concluidas': tarefas_concluidas,
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_vencidas': tarefas_vencidas,
        'taxa_conclusao': taxa_conclusao,
        'prioridade_stats': prioridade_stats,
        'categoria_stats': categoria_stats,
    }
    
    return render(request, 'tarefas/dashboard.html', contexto)
