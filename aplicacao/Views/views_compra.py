from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Aplicacao.models import Compra


class CompraList(generic.ListView):
    model = Compra
    context_object_name = 'compra_list'
    queryset = Compra.objects.all()
    paginate_by = 10
    template_name = 'compra/compra_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_itens'] = Compra.objects.all().count()
        return context


class CompraDetail(generic.DetailView):
    model = Compra
    context_object_name = 'compra'
    template_name = 'compra/compra_detail.html'


class CompraCreate(CreateView):
    model = Compra
    fields = ['codigo', 'notafiscal', 'data', 'produto', 'unidade', 'quantidade', 'preco', 'situacao', 'fornecedor']
    initial = {'codigo': 1}
    success_url = reverse_lazy('compras')
    template_name = "compra/compra_form.html"


class CompraUpdate(UpdateView):
    model = Compra
    fields = ['codigo', 'notafiscal', 'data', 'produto', 'unidade', 'quantidade', 'preco', 'situacao', 'fornecedor']
    success_url = reverse_lazy('compras')
    template_name = "compra/compra_form.html"


class CompraDelete(DeleteView):
    model = Compra
    success_url = reverse_lazy('compras')
    template_name = "compra/compra_confirm_delete.html"
