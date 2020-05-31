from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Aplicacao.models import Cliente


class ClienteView(generic.ListView):
    model = Cliente
    context_object_name = 'cliente_list'
    queryset = Cliente.objects.all()
    paginate_by = 10
    template_name = 'cliente/fornecedor_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_itens'] = Cliente.objects.all().count()
        return context


class ClienteDetailView(generic.DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'cliente/fornecedor_detail.html'


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['codigo', 'nome', 'documento', 'endereco', 'bairro', 'cidade', 'estado', 'telefonePrincipal', 'telefoneSecundario']
    initial = {'codigo': 1}
    success_url = reverse_lazy('clientes')
    template_name = "cliente/fornecedor_form.html"


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['codigo', 'nome', 'documento', 'endereco', 'bairro', 'cidade', 'estado', 'telefonePrincipal', 'telefoneSecundario']
    success_url = reverse_lazy('clientes')
    template_name = "cliente/fornecedor_form.html"


class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')
    template_name = "cliente/fornecedor_confirm_delete.html"
