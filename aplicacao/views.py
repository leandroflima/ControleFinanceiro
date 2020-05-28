from django.shortcuts import render
from Aplicacao.models import Unidade
from Aplicacao.models import Produto
from Aplicacao.models import Cliente

def index(request):
    num_unidades = Unidade.objects.all().count()
    num_produtos = Produto.objects.all().count()
    num_clientes = Cliente.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_unidades': num_unidades,
        'num_produtos': num_produtos,
        'num_clientes': num_clientes,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)