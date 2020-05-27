from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Aplicacao.models import Unidade
from Aplicacao.models import Produto


def index(request):
    num_unidades = Unidade.objects.all().count()
    num_produtos = Produto.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_unidades': num_unidades,
        'num_produtos': num_produtos,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class UnidadeView(generic.ListView):
    model = Unidade
    context_object_name = 'unidade_list'
    queryset = Unidade.objects.all()
    paginate_by = 10
    template_name = 'unidade_list.html'


class UnidadeDetailView(generic.DetailView):
    model = Unidade
    context_object_name = 'unidade'
    template_name = 'unidade_detail.html'


class UnidadeCreate(CreateView):
    model = Unidade
    fields = '__all__'
    initial = {'codigo': 1}
    success_url = reverse_lazy('unidades')


class UnidadeUpdate(UpdateView):
    model = Unidade
    fields = ['codigo', 'sigla', 'descricao']
    success_url = reverse_lazy('unidades')


class UnidadeDelete(DeleteView):
    model = Unidade
    success_url = reverse_lazy('unidades')


# --------------------------------------------------------------------------------
class ProdutoView(generic.ListView):
    model = Produto
    context_object_name = 'produto_list'
    queryset = Produto.objects.all()
    paginate_by = 10
    template_name = 'produto_list.html'


class ProdutoDetailView(generic.DetailView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'produto_detail.html'


class ProdutoCreate(CreateView):
    model = Produto
    fields = '__all__'
    initial = {'codigo': 1}
    success_url = reverse_lazy('produtos')


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['codigo', 'descricao']
    success_url = reverse_lazy('produtos')


class ProdutoDelete(DeleteView):
    model = Produto
    success_url = reverse_lazy('produtos')
