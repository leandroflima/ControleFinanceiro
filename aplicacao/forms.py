from django import forms
from Aplicacao.models import Unidade, Compra, Venda, Cliente


class UnidadeForm(forms.ModelForm):

    class Meta:
        model = Unidade
        fields = ('id', 'sigla', 'descricao')


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'documento', 'endereco', 'bairro', 'cidade', 'estado', 'telefonePrincipal', 'telefoneSecundario')


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




