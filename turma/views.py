from django.http import HttpResponse
from django.shortcuts import render
from .models import Turma, TurmaAluno
from .forms import TurmaForm
from tipodeatividade.models import TipoAtividade
from aluno.models import Aluno
from instrutor.models import Instrutor

# Create your views here.
def listar(request):
    lista_turmas = Turma.objects.all()
    context = {
        'lista_de_turmas':lista_turmas
    }
    return render(request, "turma/listarTurmas.html", context)

def cadastrar(request):
    lista_alunos = Aluno.objects.all()
    lista_tipos_atividade = TipoAtividade.objects.all()
    lista_instrutores = Instrutor.objects.all()
    context = {
        "lista_de_alunos": lista_alunos,
        "lista_de_atividades": lista_tipos_atividade,
        "lista_de_instrutores": lista_instrutores,
    }
    form = TurmaForm(request.POST)
    if form.is_valid():
        dados_turma = form.cleaned_data
        turma = Turma(
            horario_aula = dados_turma['horario_aula'],
            duracao_aula = dados_turma['duracao_aula'],
            data_inicial = dados_turma['data_inicial'],
            codigo_tipo_atividade = dados_turma['codigo_tipo_atividade'],
            matricula_monitor = dados_turma['matricula_monitor'],
            id_instrutor = dados_turma['id_instrutor']
        )
        turma.save()
    return render(request, "turma/cadastroTurma.html", context)

def ausencia(request):
    lista_turmas = Turma.objects.all()
    lista_turma_alunos = TurmaAluno.objects.all()
    context = {
        'lista_de_turmas':lista_turmas,
        'lista_de_turma_alunos':lista_turma_alunos
    }
    return render(request, "turma/registroAusencia.html", context)