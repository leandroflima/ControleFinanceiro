from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Aplicacao.models import Unidade


class UnidadeList(generic.ListView):
    model = Unidade
    context_object_name = 'unidade_list'
    queryset = Unidade.objects.all()
    paginate_by = 10
    template_name = 'unidade/unidade_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_itens'] = Unidade.objects.all().count()
        context['nav'] = 'unidade'
        return context


class UnidadeDetail(generic.DetailView):
    model = Unidade
    context_object_name = 'unidade'
    template_name = 'unidade/unidade_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'unidade'
        return context


class UnidadeCreate(CreateView):
    model = Unidade
    fields = ['id', 'sigla', 'descricao']
    initial = {'id': 1}
    success_url = reverse_lazy('unidades')
    template_name = "unidade/unidade_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'unidade'
        return context


class UnidadeUpdate(UpdateView):
    model = Unidade
    fields = ['id', 'sigla', 'descricao']
    success_url = reverse_lazy('unidades')
    template_name = "unidade/unidade_form.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'unidade'
        return context


class UnidadeDelete(DeleteView):
    model = Unidade
    success_url = reverse_lazy('unidades')
    template_name = "unidade/unidade_confirm_delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'unidade'
        return context
