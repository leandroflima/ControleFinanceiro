from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Aplicacao.forms import VendaForm
from Aplicacao.models import Venda


class VendaList(generic.ListView):
    model = Venda
    context_object_name = 'venda_list'
    queryset = Venda.objects.all()
    paginate_by = 10
    template_name = 'venda/venda_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_itens'] = Venda.objects.all().count()
        context['nav'] = 'venda'
        return context


class VendaDetail(generic.DetailView):
    model = Venda
    context_object_name = 'venda'
    template_name = 'venda/venda_detail.html'


class VendaCreate(CreateView):
    model = Venda
    initial = {'codigo': 1}
    success_url = reverse_lazy('vendas')
    template_name = "venda/venda_form.html"
    form_class = VendaForm


class VendaUpdate(UpdateView):
    model = Venda
    success_url = reverse_lazy('vendas')
    template_name = "venda/venda_form.html"
    form_class = VendaForm


class VendaDelete(DeleteView):
    model = Venda
    success_url = reverse_lazy('vendas')
    template_name = "venda/venda_confirm_delete.html"
