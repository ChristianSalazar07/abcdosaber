from django.http import HttpResponse
from django.shortcuts import render
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def listar(request):
    lista_alunos = Aluno.objects.all()
    context = {
        "lista_de_alunos": lista_alunos
    }
    return render(request, "aluno/listarAlunos.html", context)

def carregar_cadastro(request):
    return render(request ,"aluno/cadastroAluno.html")

def cadastrar(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        dados_aluno = form.cleaned_data
        aluno = Aluno(
            nome = dados_aluno['nome'],
            data_matricula = dados_aluno['data_matricula']
            )
        aluno.save()
    return render(request ,"aluno/cadastroAluno.html")