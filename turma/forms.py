from django import forms
from .models import Turma
from tipodeatividade.models import TipoAtividade
from aluno.models import Aluno
from instrutor.models import Instrutor

class TurmaForm(forms.Form):
    horario_aula = forms.TimeField(required=True, help_text="Informe o horário da turma:")
    duracao_aula = forms.IntegerField(min_value=0, required=True, help_text="Informe a duração da turma:")
    data_inicial = forms.DateField(required=True, help_text="Informe a data de inicio da turma:")
    codigo_tipo_atividade = forms.ModelChoiceField(queryset=TipoAtividade.objects.all(), required=True, empty_label="Selecione...", help_text="Informe o Tipo de Atividade")
    matricula_monitor = forms.ModelChoiceField(queryset=Aluno.objects.all(), required=True, empty_label="Selecione...", help_text="Informe o Aluno Monitor")
    id_instrutor = forms.ModelChoiceField(queryset=Instrutor.objects.all(), required=True, empty_label="Selecione...", help_text="Informe o Instrutor")

class AusenciaForm(forms.Form):
    numero_turma = forms.ModelChoiceField(queryset=Turma.objects.all(), required=True, help_text="Informe a Turma")
    matricula_aluno = forms.ModelChoiceField(queryset=Aluno.objects.all(), required=True, help_text="Informe o Aluno Monitor")
    data_ausencia = forms.DateField(required=True, help_text="Informe a data de ausência na Turma:")