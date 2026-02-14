from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Tarefa, Categoria

def login_view(request):
    if request.user.is_authenticated:
        return redirect('lista_tarefas')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('lista_tarefas')
        else:
            return render(request, 'tarefas/login.html', {'erro': 'Credenciais inválidas'})
    
    return render(request, 'tarefas/login.html')

def registro_view(request):
    if request.user.is_authenticated:
        return redirect('lista_tarefas')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            return render(request, 'tarefas/registro.html', {'erro': 'As senhas não correspondem'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'tarefas/registro.html', {'erro': 'Utilizador já existe'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('lista_tarefas')
    
    return render(request, 'tarefas/registro.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(user=request.user)
    categorias = Categoria.objects.all()
    
    # Pesquisa
    pesquisa = request.GET.get('pesquisa', '')
    categoria_id = request.GET.get('categoria', '')
    
    if pesquisa:
        tarefas = tarefas.filter(
            Q(titulo__icontains=pesquisa) | Q(descricao__icontains=pesquisa)
        )
    
    if categoria_id:
        tarefas = tarefas.filter(categoria_id=categoria_id)
    
    contexto = {
        'tarefas': tarefas,
        'categorias': categorias,
        'pesquisa': pesquisa,
        'categoria_selecionada': categoria_id
    }
    return render(request, 'tarefas/index.html', contexto)

@login_required(login_url='login')
def criar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade', 'Média')
        categoria_id = request.POST.get('categoria')
        data_vencimento = request.POST.get('data_vencimento')
        
        categoria = None
        if categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
        
        Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            user=request.user,
            categoria=categoria,
            prioridade=prioridade,
            data_vencimento=data_vencimento if data_vencimento else None
        )
        return redirect('lista_tarefas')
    
    categorias = Categoria.objects.all()
    return render(request, 'tarefas/criar.html', {'categorias': categorias})

@login_required(login_url='login')
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.prioridade = request.POST.get('prioridade')
        
        categoria_id = request.POST.get('categoria')
        tarefa.categoria = None
        if categoria_id:
            tarefa.categoria = get_object_or_404(Categoria, id=categoria_id)
        
        tarefa.data_vencimento = request.POST.get('data_vencimento') or None
        tarefa.save()
        return redirect('lista_tarefas')
    
    categorias = Categoria.objects.all()
    return render(request, 'tarefas/editar.html', {'tarefa': tarefa, 'categorias': categorias})

@login_required(login_url='login')
def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    tarefa.delete()
    return redirect('lista_tarefas')

@login_required(login_url='login')
def marcar_concluida(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('lista_tarefas')

@login_required(login_url='login')
def dashboard(request):
    from datetime import date
    from django.db.models import Count
    
    tarefas = Tarefa.objects.filter(user=request.user)
    
    # Estatísticas gerais
    total_tarefas = tarefas.count()
    tarefas_concluidas = tarefas.filter(concluida=True).count()
    tarefas_pendentes = tarefas.filter(concluida=False).count()
    
    # Tarefas por prioridade
    prioridade_stats = list(tarefas.values('prioridade').annotate(count=Count('id')))
    
    # Tarefas vencidas
    tarefas_vencidas = tarefas.filter(
        concluida=False,
        data_vencimento__lt=date.today()
    ).count()
    
    # Tarefas por categoria
    categoria_stats = list(tarefas.values('categoria__nome').annotate(count=Count('id')).order_by('-count')[:5])
    
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

@login_required(login_url='login')
def exportar_pdf(request):
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer  
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from io import BytesIO
    
    tarefas = Tarefa.objects.filter(user=request.user).order_by('-data_criacao')
    
    # Buffer em memória
    buffer = BytesIO()
    
    # Criar PDF
    doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
    elements = []
    
    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=12,
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'Heading',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=6
    )
    
    # Título
    title = Paragraph(f"📋 Exporto de Tarefas - {request.user.username}", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.3*inch))
    
    # Dados da tabela
    data = [['Título', 'Categoria', 'Prioridade', 'Status', 'Vencimento']]
    
    for tarefa in tarefas:
        status = '✓ Concluída' if tarefa.concluida else '○ Pendente'
        data.append([
            tarefa.titulo[:30],
            tarefa.categoria.nome if tarefa.categoria else '-',
            tarefa.prioridade,
            status,
            tarefa.data_vencimento.strftime('%d/%m/%Y') if tarefa.data_vencimento else '-'
        ])
    
    # Criar tabela
    table = Table(data, colWidths=[2.2*inch, 1*inch, 0.8*inch, 0.9*inch, 0.9*inch])
    
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')])
    ]))
    
    elements.append(table)
    
    # Gerar PDF
    doc.build(elements)
    
    # Preparar resposta
    buffer.seek(0)
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="tarefas_{request.user.username}.pdf"'
    
    return response
