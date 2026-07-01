from django.http import HttpResponse
from django.shortcuts import render
from .models import Instrutor
from .forms import instrutorForm
from titulo.models import Titulo

# Create your views here.
def listar(request):
    lista_instrutores = Instrutor.objects.all()
    context = {
        "lista_de_instrutores": lista_instrutores
    }
    return render(request, "instrutor/listarInstrutores.html", context)

def cadastrar(request):
    lista_titulos = Titulo.objects.all()
    context = {
        "lista_de_titulos": lista_titulos
    }
    form = instrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor(
            nome = dados_instrutor['nome'],
            rg = dados_instrutor['rg'],
            data_nascimento = dados_instrutor['data_nascimento'],
            ddd = dados_instrutor['ddd'],
            telefone = dados_instrutor['telefone'],
            codigo_titulo = dados_instrutor['codigo_titulo'],
        )
        instrutor.save()
    else:
        erros = form.errors
        context = {
            'erros': erros
        }
        return render(request ,"instrutor/erroInstrutor.html", context)
    return render(request ,"instrutor/cadastroInstrutor.html", context)