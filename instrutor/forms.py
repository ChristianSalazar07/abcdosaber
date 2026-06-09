from django import forms
from titulo.models import Titulo

class instrutorForm(forms.Form):
    rg = forms.IntegerField(required=True, help_text="Informe o RG:")
    nome = forms.CharField(max_length=100, required=True, help_text="Informe o nome:")
    data_nascimento = forms.DateField(required=True, help_text="Informe a data de nascimento:")
    ddd = forms.IntegerField(required=True, help_text="Informe o DDD:")
    telefone = forms.IntegerField(required=True, help_text="Informe o Telefone:")
    codigo_titulo = forms.ModelChoiceField(queryset=Titulo.objects.all(), required=True, empty_label="Selecione...", help_text="Informe o Título")