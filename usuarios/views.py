from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, PerfilUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Adicione esta linha

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