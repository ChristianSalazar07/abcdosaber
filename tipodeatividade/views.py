from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TipoAtividade
from .forms import tipoAtividadeForm

# Create your views here.
def listar(request):
    listaAtividades = TipoAtividade.objects.all()
    context = {
        'lista_de_atividades': listaAtividades
    }
    return render(request, "tipodeatividade/listarTiposAtividade.html", context)

def cadastrar(request):
    form = tipoAtividadeForm(request.POST)
    if form.is_valid():
        dados_atividade = form.cleaned_data
        tipodeatividade = TipoAtividade(
            descricao = dados_atividade['descricao']
        )
        tipodeatividade.save()
    return render(request, "tipodeatividade/cadastroTiposAtividade.html")

def excluir(request, codigoAtividade):
    try:
        titulo = TipoAtividade.objects.get(pk=codigoAtividade)
        titulo.delete()
    except TipoAtividade.DoesNotExist:
        pass
    return redirect('tipodeatividade:listar')