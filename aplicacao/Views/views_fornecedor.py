from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Aplicacao.forms import FornecedorForm
from Aplicacao.models import Fornecedor


class FornecedorList(generic.ListView):
    model = Fornecedor
    context_object_name = 'fornecedor_list'
    queryset = Fornecedor.objects.all()
    paginate_by = 10
    template_name = 'fornecedor/fornecedor_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_itens'] = Fornecedor.objects.all().count()
        context['nav'] = 'fornecedor'
        return context


class FornecedorDetail(generic.DetailView):
    model = Fornecedor
    context_object_name = 'fornecedor'
    template_name = 'fornecedor/fornecedor_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'fornecedor'
        context['list_href'] = '../fornecedores/'
        return context


class FornecedorCreate(CreateView):
    model = Fornecedor
    initial = {'id': 1}
    success_url = reverse_lazy('fornecedores')
    template_name = "fornecedor/fornecedor_form.html"
    form_class = FornecedorForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'fornecedor'
        context['list_href'] = '../../fornecedores/'
        return context


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedores')
    template_name = "fornecedor/fornecedor_form.html"
    form_class = FornecedorForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'fornecedor'
        context['list_href'] = '../../../fornecedores/'
        return context


class FornecedorDelete(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedores')
    template_name = "fornecedor/fornecedor_confirm_delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'fornecedor'
        context['list_href'] = '../../../fornecedores/'
        return context
