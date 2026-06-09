from django.http import HttpResponse
from django.shortcuts import render
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
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao = dados_titulo['descricao']
        )
        titulo.save()
    return render(request, "titulo/cadastroTitulos.html")