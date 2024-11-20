from django.shortcuts import render, get_object_or_404, redirect
from .models import CasoClinico
from django.contrib.auth.decorators import login_required
from .forms import CasoClinicoForm
from django.contrib import messages


def lista_casos(request):
    casos = CasoClinico.objects.filter(publicado=True)
    return render(request, 'casos/lista_casos.html', {'casos': casos})

def detalhe_caso(request, pk):
    caso = get_object_or_404(CasoClinico, pk=pk)
    return render(request, 'casos/detalhe_caso.html', {'caso': caso})

@login_required
def novo_caso(request):
    if request.method == 'POST':
        form = CasoClinicoForm(request.POST)
        if form.is_valid():
            caso = form.save(commit=False)
            caso.autor = request.user
            caso.save()
            messages.success(request, 'Caso clínico criado com sucesso!')
            return redirect('detalhe_caso', pk=caso.pk)
    else:
        form = CasoClinicoForm()
    return render(request, 'casos/editar_caso.html', {'form': form})


@login_required
def editar_caso(request, pk):
    caso = get_object_or_404(CasoClinico, pk=pk)
    if request.user != caso.autor:
        messages.error(request, 'Você não tem permissão para editar este caso.')
        return redirect('detalhe_caso', pk=caso.pk)
    if request.method == 'POST':
        form = CasoClinicoForm(request.POST, instance=caso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Caso clínico atualizado com sucesso!')
            return redirect('detalhe_caso', pk=caso.pk)
    else:
        form = CasoClinicoForm(instance=caso)
    return render(request, 'casos/editar_caso.html', {'form': form})

@login_required
def deletar_caso(request, pk):
    caso = get_object_or_404(CasoClinico, pk=pk)
    if request.user != caso.autor:
        messages.error(request, 'Você não tem permissão para deletar este caso.')
        return redirect('detalhe_caso', pk=caso.pk)
    if request.method == 'POST':
        caso.delete()
        messages.success(request, 'Caso clínico deletado com sucesso!')
        return redirect('lista_casos')
    return render(request, 'casos/confirmar_deletar.html', {'caso': caso})

