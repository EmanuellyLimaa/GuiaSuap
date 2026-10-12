from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

Usuario = get_user_model()

def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Cadastro realizado! Faça login para continuar.'
            )
            return redirect('login')
        else:
            form = CadastroForm()
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username= email,
            password= senha
        )

        if usuario is not None:

            auth_login(request, usuario)
            return redirect('tutoriais')
        else:
            messages.error(
                request,
                'E-mail ou senha incorretos'
            )
        return render(request, 'login.html')

def logout_usuarios(request):
    logout(request)
    return redirect('login')

@login_required
def tutoriais(request):
    return render(request, 'tutoriais.html')
 

def base(request):
    return render(request, 'base.html')

def login_administrador(request):
    return render(request, 'login_adminstrador.html')