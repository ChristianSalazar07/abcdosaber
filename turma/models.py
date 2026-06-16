from django.db import models
from tipodeatividade.models import TipoAtividade
from aluno.models import Aluno
from instrutor.models import Instrutor
from datetime import datetime

# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True)
    horario_aula = models.TimeField(null=False, blank=False, help_text="Informe o horário da turma:")
    duracao_aula = models.PositiveIntegerField(null=False, blank=False, help_text="Informe a duração da turma:")
    data_inicial = models.DateField(null=False, blank=False, help_text="Informe a data de inicio da turma:")
    data_final = models.DateField(null=True, blank=True, help_text="Informe a data de fim da turma:")
    codigo_tipo_atividade = models.ForeignKey(TipoAtividade, on_delete=models.SET_NULL, null=True ,help_text="Informe o tipo de atividade")
    matricula_monitor = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True ,help_text="Informe o aluno monitor")
    id_instrutor = models.ForeignKey(Instrutor, on_delete=models.SET_NULL, null=True ,help_text="Informe o instrutor")

    def __str__(self):
        return f"Número: {self.numero} - Atividade: {self.codigo_tipo_atividade.descricao} - Instrutor: {self.id_instrutor.nome} - Aluno Monitor: {self.matricula_monitor.nome}"
    

#Relação Turma e Aluno
class TurmaAluno(models.Model):
    numero_turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, help_text="Informe a Turma")
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True ,help_text="Informe o Aluno Monitor")
    data_matricula = models.DateField(null=False, blank=False, help_text="Informe a data de matrícula na Turma:", default=datetime.now)

    def __str__(self):
        return f"Turma: {self.numero_turma.numero} - Aluno: {self.matricula_aluno.nome} - Data: {self.data_matricula}"
    

#
class Ausencia(models.Model):
    numero_turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, help_text="Informe a Turma")
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True ,help_text="Informe o Aluno Monitor")
    data_ausencia = models.DateField(null=False, blank=False, help_text="Informe a data de ausência na Turma:")

    def __str__(self):
        return f"Turma: {self.numero_turma.numero} - Aluno: {self.matricula_aluno.nome} - Data: {self.data_ausencia}"