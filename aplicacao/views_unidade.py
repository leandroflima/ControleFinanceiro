from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Aplicacao.models import Unidade


class UnidadeView(generic.ListView):
    model = Unidade
    context_object_name = 'unidade_list'
    queryset = Unidade.objects.all()
    paginate_by = 10
    template_name = 'unidade/unidade_list.html'


class UnidadeDetailView(generic.DetailView):
    model = Unidade
    context_object_name = 'unidade'
    template_name = 'unidade/unidade_detail.html'


class UnidadeCreate(CreateView):
    model = Unidade
    fields = ['codigo', 'sigla', 'descricao']
    initial = {'codigo': 1}
    success_url = reverse_lazy('unidades')
    template_name = "unidade/unidade_form.html"


class UnidadeUpdate(UpdateView):
    model = Unidade
    fields = ['codigo', 'sigla', 'descricao']
    success_url = reverse_lazy('unidades')
    template_name = "unidade/unidade_form.html"


class UnidadeDelete(DeleteView):
    model = Unidade
    success_url = reverse_lazy('unidades')
    template_name = "unidade/unidade_confirm_delete.html"
