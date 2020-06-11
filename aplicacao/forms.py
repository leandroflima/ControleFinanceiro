import datetime

from django import forms
from django.forms import TextInput, NumberInput, Select, DateInput, SelectDateWidget, CheckboxInput

from Aplicacao.models import Produto, Cliente, Compra, Venda, Fornecedor


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('id', 'codigo', 'descricao', 'pontos')
        widgets = {
            'codigo': NumberInput(attrs={'class': 'form-control','autofocus':''}),
            'descricao': TextInput(attrs={'type': 'text','class':'form-control'}),
            'pontos': NumberInput(attrs={'class': 'form-control'}),
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


class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ('id', 'nome', 'telefonePrincipal')
        widgets = {
            'nome': TextInput(attrs={'type': 'text','class':'form-control','autofocus':''}),
            'telefonePrincipal': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
        }


class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ('id', 'numeroPedido', 'notafiscal', 'data', 'produto', 'quantidade', 'preco', 'fornecedor', 'situacao')
        widgets = {
            'data': DateInput(attrs={'class': 'form-control','autofocus':'','data-inputmask-alias':'datetime','data-inputmask-inputformat':'dd/mm/yyyy','data-mask':''}),
            'numeroPedido': TextInput(attrs={'type': 'text','class':'form-control'}),
            'notafiscal': TextInput(attrs={'type': 'text','class':'form-control'}),
            'produto': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'quantidade': NumberInput(attrs={'class': 'form-control'}),
            'preco': NumberInput(attrs={'class': 'form-control'}),
            'fornecedor': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'situacao': Select(attrs={'class': 'form-control'}),
        }


class VendaForm(forms.ModelForm):

    class Meta:
        model = Venda
        fields = ('id', 'data', 'produto', 'quantidade', 'preco', 'cliente', 'situacao')
        widgets = {
            'data': DateInput(attrs={'class': 'form-control','autofocus':'','data-inputmask-alias':'datetime','data-inputmask-inputformat':'dd/mm/yyyy','data-mask':''}),
            'produto': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'quantidade': NumberInput(attrs={'class': 'form-control'}),
            'preco': NumberInput(attrs={'class': 'form-control'}),
            'cliente': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'situacao': Select(attrs={'class': 'form-control'}),
        }




