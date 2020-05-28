from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Aplicacao.models import Produto


class ProdutoView(generic.ListView):
    model = Produto
    context_object_name = 'produto_list'
    queryset = Produto.objects.all()
    paginate_by = 10
    template_name = 'produto/produto_list.html'


class ProdutoDetailView(generic.DetailView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'produto/produto_detail.html'


class ProdutoCreate(CreateView):
    model = Produto
    fields = ['codigo', 'descricao']
    initial = {'codigo': 1}
    success_url = reverse_lazy('produtos')
    template_name = "produto/produto_form.html"


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['codigo', 'descricao']
    success_url = reverse_lazy('produtos')
    template_name = "produto/produto_form.html"


class ProdutoDelete(DeleteView):
    model = Produto
    success_url = reverse_lazy('produtos')
    template_name = "produto/produto_confirm_delete.html"
