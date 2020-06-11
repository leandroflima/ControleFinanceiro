from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Aplicacao.forms import ProdutoForm
from Aplicacao.models import Produto


class ProdutoList(generic.ListView):
    model = Produto
    context_object_name = 'produto_list'
    queryset = Produto.objects.all()
    paginate_by = 10
    template_name = 'produto/produto_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_itens'] = Produto.objects.all().count()
        context['nav'] = 'produto'
        return context


class ProdutoDetail(generic.DetailView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'produto/produto_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'produto'
        context['list_href'] = '../produtos/'
        return context


class ProdutoCreate(CreateView):
    model = Produto
    initial = {'id': 1}
    success_url = reverse_lazy('produtos')
    template_name = "produto/produto_form.html"
    form_class = ProdutoForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'produto'
        context['list_href'] = '../../produtos/'
        return context


class ProdutoUpdate(UpdateView):
    model = Produto
    success_url = reverse_lazy('produtos')
    template_name = "produto/produto_form.html"
    form_class = ProdutoForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'produto'
        context['list_href'] = '../../../produtos/'
        return context


class ProdutoDelete(DeleteView):
    model = Produto
    success_url = reverse_lazy('produtos')
    template_name = "produto/produto_confirm_delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'produto'
        context['list_href'] = '../../../produtos/'
        return context
