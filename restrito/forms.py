from django import forms

from .models import Questao

class DateTextInput(forms.widgets.TextInput):
    input_type = 'datetime-local'

class QuestaoForm(forms.ModelForm):
    data = forms.DateTimeField(input_formats=[
        '%d/%m/%Y %H:%M'
    ])
    data_limite_entrega = forms.DateTimeField(input_formats=[
        '%d/%m/%Y %H:%M'
    ])

    class Meta:
        model = Questao
        exclude = ['turma']