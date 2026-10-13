
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm, TutorialForm
from .models import Tutorial

Usuario = get_user_model()


def inicio(request):
    return render(request, 'inicio.html')


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


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        senha = request.POST.get('senha', '')

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


def login_administrador(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        senha = request.POST.get('senha', '')

        usuario = authenticate(
            request,
            username=email,
            password=senha
        )

        if (
            usuario is not None
            and usuario.is_active
            and usuario.is_staff
        ):
            auth_login(request, usuario)
            return redirect('/admin/')

        messages.error(
            request,
            'Acesso administrativo negado. Verifique seus dados.'
        )

    return render(request, 'login_administrador.html')


@login_required
def tutoriais(request):
    if request.user.is_staff:
        return redirect('/admin/')

    return render(request, 'tutoriais.html')


def logout_usuarios(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('tutoriais')

def administrador_ativo(user):
    return user.is_authenticated and user.is_staff 

somente_administrador = user_passes_test(
    administrador_ativo,
    login_url ='login_administrador'
)

# read: vai listar todos os tutoriais disponivel
@somente_administrador
def gerenciar_tutoriais(request):
    tutoriais = Tutorial.objetcs.all()

    return render(request, 'Suap/gerenciar_tutoriais.html',{
        'tutoriais': tutoriais
    })

# create: cadastro de tutorial 
@somente_administrador
def criar_tutoriais(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tutorial cadastrado com sucesso.')


def base(request):
    return render(request, 'base.html')

def tutoriais(request):
    return render(request, 'tutoriais.html')