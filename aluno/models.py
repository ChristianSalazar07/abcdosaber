from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_matricula = models.DateField()
    data_saida = models.DateField(default=None, null=True, blank=True)
    aluno_monitor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - Matriculado em: {self.data_matricula} - Saída: {self.data_saida} - Monitor: {'Sim' if self.aluno_monitor else 'Não'}"