from django.db import models
from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    id = models.AutoField(primary_key=True)
    rg = models.IntegerField(null=False, help_text="Informe o RG:")
    nome = models.CharField(max_length=100, null=False, help_text="Informe o nome:")
    data_nascimento = models.DateField(null=False, help_text="Informe a data de nascimento:")
    ddd = models.IntegerField(null=False, help_text="Informe o DDD:")
    telefone = models.IntegerField(null=False, help_text="Informe o Telefone:")
    codigo_titulo = models.ForeignKey(Titulo, on_delete=models.SET_NULL, null=True, blank=True ,help_text="Informe o Título")

    def __str__(self):
        return f"ID: {self.id} - RG: {self.rg} - Nome: {self.nome} - Data de Nascimento: {self.data_nascimento} - DDD: {self.ddd} - Telefone: {self.telefone} - Titulo: {self.codigo_titulo}"