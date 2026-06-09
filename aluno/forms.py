from django import forms
import datetime

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, help_text="Informe o nome do aluno:")
    data_matricula = forms.DateField(required=True, help_text="Informe a data de início na escola:")