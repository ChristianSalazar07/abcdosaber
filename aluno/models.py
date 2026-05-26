from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_matricula = models.DateField()

    def __str__(self):
        return self.nome