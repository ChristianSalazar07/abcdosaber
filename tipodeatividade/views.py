from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TipoAtividade
from .forms import tipoAtividadeForm, tipoAtividadeAtualizarForm

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

def atualizar(request, codigoAtividade):
    # Receber Form
    if request.method == 'POST':
        form = tipoAtividadeAtualizarForm(request.POST)
        # Validar Form
        if form.is_valid():
            dados_atualizar = form.cleaned_data
        # Se ok então atualizar
            atividade = TipoAtividade.objects.get(pk=dados_atualizar['codigo'])
            atividade.descricao = dados_atualizar['descricao']
            atividade.save()
        # Redirecionar para a lista de tipodeatividade
        return redirect('tipodeatividade:listar')
    context = {
        "codigo": codigoAtividade,
        "atividadeAlterada": TipoAtividade.objects.get(pk=codigoAtividade)
    }
    return render(request, "tipodeatividade/atualizarTiposAtividade.html", context)