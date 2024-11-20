from django.shortcuts import render, get_object_or_404, redirect
from .models import CasoClinico, Comentario
from django.contrib.auth.decorators import login_required
from .forms import CasoClinicoForm, ComentarioForm
from django.contrib import messages
from usuarios.models import Perfil
from django.core.paginator import Paginator

def lista_casos(request):
    casos = CasoClinico.objects.filter(publicado=True)
    return render(request, 'casos/lista_casos.html', {'casos': casos})

def detalhe_caso(request, pk):
    caso = get_object_or_404(CasoClinico, pk=pk)
    form = ComentarioForm()
    return render(request, 'casos/detalhe_caso.html', {'caso': caso, 'form': form})


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

@login_required
def mural(request):
    perfil = request.user.perfil
    perfis_seguidos = perfil.seguindo.all()
    usuarios_seguidos = [p.user for p in perfis_seguidos]
    casos_list = CasoClinico.objects.filter(autor__in=usuarios_seguidos, publicado=True).order_by('-data_publicacao')
    paginator = Paginator(casos_list, 5)  # 5 casos por página
    page_number = request.GET.get('page')
    casos = CasoClinico.objects.filter(autor__in=usuarios_seguidos, publicado=True).order_by('-data_publicacao')
    return render(request, 'casos/mural.html', {'casos': casos})

@login_required
def curtir_caso(request, pk):
    caso = get_object_or_404(CasoClinico, pk=pk)
    if request.user in caso.curtidas.all():
        caso.curtidas.remove(request.user)
        messages.info(request, f'Você descurtiu "{caso.titulo}".')
    else:
        caso.curtidas.add(request.user)
        messages.success(request, f'Você curtiu "{caso.titulo}".')
    return redirect(request.META.get('HTTP_REFERER', 'mural'))

@login_required
def adicionar_comentario(request, pk):
    caso = get_object_or_404(CasoClinico, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.caso = caso
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect('detalhe_caso', pk=caso.pk)
    else:
        form = ComentarioForm()
    return render(request, 'casos/adicionar_comentario.html', {'form': form, 'caso': caso})
