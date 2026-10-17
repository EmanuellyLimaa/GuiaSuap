
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import CadastroForm, TutorialForm
from .models import Tutorial

Usuario = get_user_model()

# Página inicial
def inicio(request):
    return render(request, 'inicio.html')


# Cadastro dos alunos
def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Cadastro realizado! Faça login para continuar.'
            )
            return redirect('login')
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})


# Login dos alunos
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        senha = request.POST.get('senha', '')

        # O cadastro utiliza o e-mail como username.
        usuario = authenticate(
            request,
            username=email,
            password=senha
        )

        if usuario is not None and usuario.is_active:
            if usuario.is_staff:
                messages.error(
                    request,
                    'Utilize o acesso administrativo.'
                )
                return redirect('login_administrador')

            auth_login(request, usuario)
            return redirect('tutoriais')

        messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'login.html')


# Login administrativo
def login_administrador(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '')

        # Procura contas administrativas com esse e-mail.
        usuarios = Usuario.objects.filter(
            email__iexact=email,
            is_staff=True,
            is_active=True
        )

        usuario = None

        # Tenta autenticar cada conta encontrada.
        for candidato in usuarios:
            usuario = authenticate(
                request,
                username=candidato.username,
                password=senha
            )

            if usuario is not None:
                break

        if usuario is not None and usuario.is_staff:
            auth_login(request, usuario)
            return redirect('gerenciar_tutoriais')

        messages.error(
            request,
            'Acesso administrativo negado. '
            'Verifique seu e-mail e sua senha.'
        )

    return render(request, 'login_administrador.html')


# Sair da conta
@login_required
def logout_usuarios(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('tutoriais')


# Verifica se o usuário é administrador
def administrador_ativo(user):
    return user.is_authenticated and user.is_staff and user.is_active


somente_administrador = user_passes_test(
    administrador_ativo,
    login_url='login_administrador'
)


# Listar todos os tutoriais no painel administrativo
@somente_administrador
def gerenciar_tutoriais(request):
    tutoriais = Tutorial.objects.all()

    return render(
        request,
        'gerenciar_tutoriais.html',
        {'tutoriais': tutoriais}
    )

# Cadastrar um tutorial com arquivo de vídeo
@somente_administrador
def criar_tutoriais(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Tutorial cadastrado com sucesso!'
            )
            return redirect('gerenciar_tutoriais')
    else:
        form = TutorialForm()

    return render(
        request,
        'form_tutoriais.html',
        {
            'form': form,
            'titulo_pagina': 'Cadastrar tutorial',
        }
    )

# Editar um tutorial existente
@somente_administrador
def editar_tutorial(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)

    if request.method == 'POST':
        form = TutorialForm(
            request.POST,
            request.FILES,
            instance=tutorial
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Tutorial atualizado com sucesso!'
            )
            return redirect('gerenciar_tutoriais')
    else:
        form = TutorialForm(instance=tutorial)

    return render(
        request,
        'form_tutoriais.html',
        {
            'form': form,
            'titulo_pagina': 'Editar tutorial',
        }
    )

# Excluir um tutorial
@somente_administrador
def excluir_tutorial(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)

    if request.method == 'POST':
        tutorial.delete()
        messages.success(
            request,
            'Tutorial excluído com sucesso!'
        )
        return redirect('gerenciar_tutoriais')

    return render(
        request,
        'confirmar_exclusao.html',
        {'tutorial': tutorial}
    )

# Página de tutoriais para os alunos
@login_required
def tutoriais(request):
    if request.user.is_staff:
        return redirect('gerenciar_tutoriais')

    tutoriais_publicados = Tutorial.objects.filter(
        publicado=True
    )

    return render(
        request,
        'tutoriais.html',
        {'tutoriais': tutoriais_publicados}
    )

# Página base, caso seja utilizada em outras partes do projeto
def base(request):
    return render(request, 'base.html')