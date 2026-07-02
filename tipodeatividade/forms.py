from django import forms

class tipoAtividadeForm(forms.Form):
    descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descrição do tipo de atividade:")

class tipoAtividadeAtualizarForm(forms.Form):
    codigo = forms.IntegerField(required=True, help_text='Informe o código da atividade:')
    descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descrição do tipo de atividade:")