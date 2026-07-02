from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Titulo
from .forms import tituloForm, tituloAtualizarForm

# Create your views here.
def listar(request):
    lista_titulos = Titulo.objects.all()
    context = {
        "lista_de_titulos": lista_titulos
    }
    return render(request, "titulo/listarTitulos.html", context)

def cadastrar(request):
    form = tituloForm(request.POST)
    status = 0
    if form.is_valid():
        dados_titulo = form.cleaned_data
        achou = Titulo.objects.filter(descricao=dados_titulo['descricao'])
        if not achou:
            titulo = Titulo(
                descricao = dados_titulo['descricao']
            )
            titulo.save()
            status = 1
        else:
            status = 2
    context = {
        "status":status
    }
    return render(request, "titulo/cadastroTitulos.html", context)

def excluir(request, codigoTitulo):
    try:
        titulo = Titulo.objects.get(pk=codigoTitulo)
        titulo.delete()
    except Titulo.DoesNotExist:
        pass
    return redirect('titulo:listar')

def atualizar(request, codigoTitulo):
    # Receber Form
    if request.method == 'POST':
        form = tituloAtualizarForm(request.POST)
        # Validar Form
        if form.is_valid():
            dados_atualizar = form.cleaned_data
        # Se ok então atualizar
            titulo = Titulo.objects.get(pk=dados_atualizar['codigo'])
            titulo.descricao = dados_atualizar['descricao']
            titulo.save()
        # Redirecionar para a lista de titulo
        return redirect('titulo:listar')
    context = {
        "codigo": codigoTitulo,
        "tituloAlterado": Titulo.objects.get(pk=codigoTitulo)
    }
    return render(request, "titulo/atualizarTitulo.html", context)