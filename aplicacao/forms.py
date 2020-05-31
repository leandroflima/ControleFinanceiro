from django import forms
from Aplicacao.models import Compra, Venda


class CompraForm(forms.ModelForm):
    data = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Ano", "Mês", "Dia")))

    class Meta:
        model = Compra
        fields = ('codigo', 'notafiscal', 'data', 'produto', 'unidade', 'quantidade', 'preco', 'situacao', 'fornecedor')


class VendaForm(forms.ModelForm):
    data = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Ano", "Mês", "Dia")))

    class Meta:
        model = Venda
        fields = ('codigo', 'data', 'produto', 'unidade', 'quantidade', 'preco', 'situacao', 'cliente')




