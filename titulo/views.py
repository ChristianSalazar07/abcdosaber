from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_view(request):
    return HttpResponse('<p> Minha View do App Titulo </p>')

def listar_titulo(request):
    return render(request, "titulo/listarTitulos.html")

def abc(request):
    pagina = 'ABC!'
    return HttpResponse(pagina)

def cadastrar_titulo(request):
    return render(request, "titulo/cadastroTitulos.html")