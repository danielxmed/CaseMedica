from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PerfilUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Adicione esta linha
from django.contrib import messages

@login_required
def perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PerfilUpdateForm(request.POST, instance=request.user.perfil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PerfilUpdateForm(instance=request.user.perfil)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'usuarios/perfil.html', context)

@login_required
def visualizar_perfil(request, username):
    user = User.objects.get(username=username)
    return render(request, 'usuarios/visualizar_perfil.html', {'user': user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/signup.html', {'form': form})

@login_required
def seguir_usuario(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    perfil_to_follow = user_to_follow.perfil
    perfil = request.user.perfil
    if perfil == perfil_to_follow:
        messages.warning(request, 'Você não pode seguir a si mesmo.')
    else:
        perfil.seguindo.add(perfil_to_follow)
        messages.success(request, f'Você agora está seguindo {user_to_follow.username}.')
    return redirect('visualizar_perfil', username=username)

@login_required
def deixar_de_seguir_usuario(request, username):
    user_to_unfollow = get_object_or_404(User, username=username)
    perfil_to_unfollow = user_to_unfollow.perfil
    perfil = request.user.perfil
    perfil.seguindo.remove(perfil_to_unfollow)
    messages.success(request, f'Você deixou de seguir {user_to_unfollow.username}.')
    return redirect('visualizar_perfil', username=username)

def buscar_usuarios(request):
    query = request.GET.get('q')
    resultados = User.objects.filter(username__icontains=query) if query else None
    return render(request, 'usuarios/buscar_usuarios.html', {'resultados': resultados, 'query': query})

def lista_seguidores(request, username):
    user = get_object_or_404(User, username=username)
    seguidores = user.perfil.seguidores.all()
    return render(request, 'usuarios/lista_seguidores.html', {'user': user, 'seguidores': seguidores})

def lista_seguindo(request, username):
    user = get_object_or_404(User, username=username)
    perfil = user.perfil
    seguindo = perfil.seguindo.all()
    return render(request, 'usuarios/lista_seguindo.html', {'user': user, 'seguindo': seguindo})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilUpdateForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('visualizar_perfil', username=request.user.username)
    else:
        form = PerfilUpdateForm(instance=perfil)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})
