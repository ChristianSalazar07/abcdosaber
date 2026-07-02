from django import forms

class tituloForm(forms.Form):
    descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descrição do título:")

class tituloAtualizarForm(forms.Form):
    codigo = forms.IntegerField(required=True, help_text='Informe o código da titulo:')
    descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descrição do tipo de titulo:")