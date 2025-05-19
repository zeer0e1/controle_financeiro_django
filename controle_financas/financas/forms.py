from django import forms
from .models import Transacao, Categoria, Conta


class TransacaoForm(forms.ModelForm):
    class Meta:
        model= Transacao
        fields = [
            'tipo',
            'data',
            'valor',
            'descricao',
            'conta',
            'categoria'
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }