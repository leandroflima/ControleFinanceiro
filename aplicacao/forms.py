from django import forms
from django.forms import TextInput, NumberInput, Select, DateInput, SelectDateWidget

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
    #data = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Ano", "Mês", "Dia")))

    class Meta:
        model = Compra
        fields = ('id', 'numeroPedido', 'notafiscal', 'data', 'produto', 'quantidade', 'preco', 'situacao', 'fornecedor')
        widgets = {
            'numeroPedido': TextInput(attrs={'type': 'text','class':'form-control','autofocus':''}),
            'notafiscal': TextInput(attrs={'type': 'text','class':'form-control'}),
            'data': TextInput(attrs={'class': 'form-control','data-inputmask-alias':'datetime','data-inputmask-inputformat':'dd/mm/yyyy','data-mask':''}),
            'produto': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'quantidade': NumberInput(attrs={'class': 'form-control'}),
            'preco': NumberInput(attrs={'class': 'form-control'}),
            'situacao': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'fornecedor': Select(attrs={'type': 'text', 'class': 'form-control'}),
        }


class VendaForm(forms.ModelForm):
    data = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Ano", "Mês", "Dia")))

    class Meta:
        model = Venda
        fields = ('id', 'data', 'produto', 'quantidade', 'preco', 'situacao', 'cliente')
        widgets = {
            #'data': DateInput(input_formats=['%d/%m/%Y %H:%M'], attrs={'input_type': 'text', 'class': 'form-control'}),
            'produto': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'quantidade': NumberInput(attrs={'class': 'form-control'}),
            'preco': NumberInput(attrs={'class': 'form-control'}),
            'situacao': Select(attrs={'type': 'text', 'class': 'form-control'}),
            'cliente': Select(attrs={'type': 'text', 'class': 'form-control'}),
        }




