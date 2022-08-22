from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login feito com sucesso.')
        return redirect('produtos')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Deslogado com sucesso!')
    return redirect('dashboard')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    nome =  request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Por favor verifique se todos os campos do formulário foram preenchidos.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido, verifique seu endereço de email e tente novamente.')
        return render(request, 'accounts/cadastro.html')
    if len(senha) < 6:
        messages.error(request, 'senha precisa ter no minimo 6 caracteres.')
        return render(request, 'accounts/cadastro.html')
    if len(usuario) < 6:
        messages.error(request, 'usuário precisa ter no minimo 6 caracteres.')
        return render(request, 'accounts/cadastro.html')
    if senha != senha2:
        messages.error(request, 'As senhas não correspondem, digite o mesmo valor para os dois campos de senha.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'O usuário ja existe no sistema.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'O email ja existe no sistema.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'USUÁRIO REGISTRADO. Utilize o formulário abaixo para fazer o login.')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')

   #messages.success(request, 'Cadastro realizado com sucesso!')
    return render(request, 'accounts/cadastro.html')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')