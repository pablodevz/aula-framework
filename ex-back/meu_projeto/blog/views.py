from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, CustomPasswordChangeForm
from django.contrib import messages
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()

    context = {
        'pessoas': pessoas
    }
    return render(request, 'home.html', context)

def registrar_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    contexto = {'form': form}
    return render(request, 'registrar.html', contexto)

def resetar_senha_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            return redirect('resetar_nova_senha', user_id=user.id)
        else:
            messages.error(request, 'Usuário não encontrado.')
            return redirect('resetar_senha_usuario')
    return render(request, 'resetar_senha_usuario.html')

def resetar_nova_senha(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua senha foi alterada com sucesso! Faça o login.')
            return redirect('login')
    else:
        form = SetPasswordForm(user)
    
    contexto = {'form': form}
    return render(request, 'resetar_nova_senha.html', contexto)

@login_required
def perfil_view(request):
    if request.method == 'POST':
        if 'update_info' in request.POST:
            info_form = UserUpdateForm(request.POST, instance=request.user)
            if info_form.is_valid():
                info_form.save()
                messages.success(request, 'Suas informações foram atualizadas com sucesso!')
                return redirect('perfil')
        
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Sua senha foi alterada com sucesso!')
                return redirect('perfil')
    else:
        info_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    contexto = {
        'info_form': info_form,
        'password_form': password_form
    }
    return render(request, 'perfil.html', contexto)

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def pagina_restrita_view(request):
    return render(request, 'home.html')

def erro_500_view(request):
    divisao_por_zero = 1 / 0
    return render(request, 'home.html')

from django.shortcuts import render

def permissao_negada_403(request, exception):
    return render(request, '403.html', status=403)