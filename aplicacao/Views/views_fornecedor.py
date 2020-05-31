from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from Aplicacao.models import Fornecedor


class FornecedorView(generic.ListView):
    model = Fornecedor
    context_object_name = 'fornecedor_list'
    queryset = Fornecedor.objects.all()
    paginate_by = 10
    template_name = 'fornecedor/fornecedor_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_itens'] = Fornecedor.objects.all().count()
        return context


class FornecedorDetailView(generic.DetailView):
    model = Fornecedor
    context_object_name = 'fornecedor'
    template_name = 'fornecedor/fornecedor_detail.html'


class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['codigo', 'nome', 'telefonePrincipal']
    initial = {'codigo': 1}
    success_url = reverse_lazy('fornecedores')
    template_name = "fornecedor/fornecedor_form.html"


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['codigo', 'nome', 'telefonePrincipal']
    success_url = reverse_lazy('fornecedores')
    template_name = "fornecedor/fornecedor_form.html"


class FornecedorDelete(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedores')
    template_name = "fornecedor/fornecedor_confirm_delete.html"
