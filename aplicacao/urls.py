from django.urls import path
from Aplicacao.Views import views_cliente, views_produto, views_unidade, views

urlpatterns = [
    path('', views.index, name='index'),

    path('unidades/', views_unidade.UnidadeView.as_view(), name='unidades'),
    path('unidade/<int:pk>', views_unidade.UnidadeDetailView.as_view(), name='unidade'),
    path('unidade/create/', views_unidade.UnidadeCreate.as_view(), name='unidade_create'),
    path('unidade/<int:pk>/update/', views_unidade.UnidadeUpdate.as_view(), name='unidade_update'),
    path('unidade/<int:pk>/delete/', views_unidade.UnidadeDelete.as_view(), name='unidade_delete'),

    path('produtos/', views_produto.ProdutoView.as_view(), name='produtos'),
    path('produto/<int:pk>', views_produto.ProdutoDetailView.as_view(), name='produto'),
    path('produto/create/', views_produto.ProdutoCreate.as_view(), name='produto_create'),
    path('produto/<int:pk>/update/', views_produto.ProdutoUpdate.as_view(), name='produto_update'),
    path('produto/<int:pk>/delete/', views_produto.ProdutoDelete.as_view(), name='produto_delete'),

    path('clientes/', views_cliente.ClienteView.as_view(), name='clientes'),
    path('cliente/<int:pk>', views_cliente.ClienteDetailView.as_view(), name='cliente'),
    path('cliente/create/', views_cliente.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/', views_cliente.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete/', views_cliente.ClienteDelete.as_view(), name='cliente_delete'),
]