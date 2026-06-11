from django.http import HttpResponse
from django.shortcuts import render
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