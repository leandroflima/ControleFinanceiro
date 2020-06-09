from django import forms
from django.forms import TextInput, NumberInput, Select

from Aplicacao.models import Unidade, Compra, Venda, Cliente


class UnidadeForm(forms.ModelForm):

    class Meta:
        model = Unidade
        fields = ('id', 'sigla', 'descricao')
        widgets = {
            'sigla': TextInput(attrs={'type': 'text','class':'form-control','autofocus':''}),
            'descricao': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'documento', 'endereco', 'bairro', 'cidade', 'estado', 'telefonePrincipal', 'telefoneSecundario')
        widgets = {
            'nome': TextInput(attrs={'type': 'text','class':'form-control','autofocus':''}),
            'documento': NumberInput(attrs={'class': 'form-control'}),
            'endereco': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'bairro': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'cidade': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'estado': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'telefonePrincipal': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'telefoneSecundario': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }

class CompraForm(forms.ModelForm):
    data = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Ano", "Mês", "Dia")))

    class Meta:
        model = Compra
        fields = ('id', 'notafiscal', 'data', 'produto', 'unidade', 'quantidade', 'preco', 'situacao', 'fornecedor')


class VendaForm(forms.ModelForm):
    data = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Ano", "Mês", "Dia")))

    class Meta:
        model = Venda
        fields = ('id', 'data', 'produto', 'unidade', 'quantidade', 'preco', 'situacao', 'cliente')




