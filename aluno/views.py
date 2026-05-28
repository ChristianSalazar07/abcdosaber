from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listar_aluno(request):
    return render(request, "aluno/listarAlunos.html")

def cadastrar_aluno(request):
    return render(request, "aluno/cadastroAluno.html")