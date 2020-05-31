from django.urls import path
from Aplicacao.Views import views_venda, views_compra, views_fornecedor, views_cliente, views_produto, views_unidade, views

urlpatterns = [
    path('', views.index, name='index'),

    path('unidades/', views_unidade.UnidadeList.as_view(), name='unidades'),
    path('unidade/<int:pk>', views_unidade.UnidadeDetail.as_view(), name='unidade'),
    path('unidade/create/', views_unidade.UnidadeCreate.as_view(), name='unidade_create'),
    path('unidade/<int:pk>/update/', views_unidade.UnidadeUpdate.as_view(), name='unidade_update'),
    path('unidade/<int:pk>/delete/', views_unidade.UnidadeDelete.as_view(), name='unidade_delete'),

    path('produtos/', views_produto.ProdutoList.as_view(), name='produtos'),
    path('produto/<int:pk>', views_produto.ProdutoDetail.as_view(), name='produto'),
    path('produto/create/', views_produto.ProdutoCreate.as_view(), name='produto_create'),
    path('produto/<int:pk>/update/', views_produto.ProdutoUpdate.as_view(), name='produto_update'),
    path('produto/<int:pk>/delete/', views_produto.ProdutoDelete.as_view(), name='produto_delete'),

    path('clientes/', views_cliente.ClienteList.as_view(), name='clientes'),
    path('cliente/<int:pk>', views_cliente.ClienteDetail.as_view(), name='cliente'),
    path('cliente/create/', views_cliente.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/', views_cliente.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views_cliente.ClienteDelete.as_view(), name='cliente_delete'),

    path('fornecedores/', views_fornecedor.FornecedorList.as_view(), name='fornecedores'),
    path('fornecedor/<int:pk>', views_fornecedor.FornecedorDetail.as_view(), name='fornecedor'),
    path('fornecedor/create/', views_fornecedor.FornecedorCreate.as_view(), name='fornecedor_create'),
    path('fornecedor/<int:pk>/update/', views_fornecedor.FornecedorUpdate.as_view(), name='fornecedor_update'),
    path('fornecedor/<int:pk>/delete/', views_fornecedor.FornecedorDelete.as_view(), name='fornecedor_delete'),

    path('compras/', views_compra.CompraList.as_view(), name='compras'),
    path('compra/<int:pk>', views_compra.CompraDetail.as_view(), name='compra'),
    path('compra/create/', views_compra.CompraCreate.as_view(), name='compra_create'),
    path('compra/<int:pk>/update/', views_compra.CompraUpdate.as_view(), name='compra_update'),
    path('compra/<int:pk>/delete/', views_compra.CompraDelete.as_view(), name='compra_delete'),

    path('vendas/', views_venda.VendaList.as_view(), name='vendas'),
    path('venda/<int:pk>', views_venda.VendaDetail.as_view(), name='venda'),
    path('venda/create/', views_venda.VendaCreate.as_view(), name='venda_create'),
    path('venda/<int:pk>/update/', views_venda.VendaUpdate.as_view(), name='venda_update'),
    path('venda/<int:pk>/delete/', views_venda.VendaDelete.as_view(), name='venda_delete'),
]