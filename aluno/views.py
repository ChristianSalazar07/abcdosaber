from django.http import HttpResponse
from django.shortcuts import render
from .models import Aluno

# Create your views here.
def listar(request):
    lista_alunos = Aluno.objects.all()
    try:
        aluno_cadastrado = Aluno.objects.create()
    except ():
        context = {
        "lista_de_alunos": lista_alunos
    }
        return render(request, "aluno/listarAlunos.html", context)

def cadastrar(request):
    return render(request ,"aluno/cadastroAluno.html")