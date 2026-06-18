from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Titulo
from .forms import tituloForm

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