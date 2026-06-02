from django.db import models
from django.forms import ModelForm

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text="Informe a matrícula do aluno:")
    nome = models.CharField(max_length=100, null=False, help_text="Informe o nome do aluno:")
    data_matricula = models.DateField()
    data_saida = models.DateField(default=None, null=True, blank=True, help_text="Informe a data de saída:")
    aluno_monitor = models.BooleanField(default=False, help_text="Informe se é aluno monitor:")

    def __str__(self):
        return f"{self.nome} - Matrícula: {self.matricula} - Matriculado em: {self.data_matricula} - Saída: {self.data_saida} - Monitor: {'Sim' if self.aluno_monitor else 'Não'}"
