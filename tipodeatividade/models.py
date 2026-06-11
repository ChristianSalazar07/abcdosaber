from django.db import models

# Create your models here.
class TipoAtividade(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=70, null=False, help_text="Informe a descrição do tipo de atividade:")

    def __str__(self):
        return f"Código: {self.codigo} - Descrição: {self.descricao}"