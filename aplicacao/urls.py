from django.urls import path
from Aplicacao import views

urlpatterns = [
    path('', views.index, name='index'),

    path('unidades/', views.UnidadeView.as_view(), name='unidades'),
    path('unidade/<int:pk>', views.UnidadeDetailView.as_view(), name='unidade'),
    path('unidade/create/', views.UnidadeCreate.as_view(), name='unidade_create'),
    path('unidade/<int:pk>/update/', views.UnidadeUpdate.as_view(), name='unidade_update'),
    path('unidade/<int:pk>/delete/', views.UnidadeDelete.as_view(), name='unidade_delete'),

    path('produtos/', views.ProdutoView.as_view(), name='produtos'),
    path('produto/<int:pk>', views.ProdutoDetailView.as_view(), name='produto'),
    path('produto/create/', views.ProdutoCreate.as_view(), name='produto_create'),
    path('produto/<int:pk>/update/', views.ProdutoUpdate.as_view(), name='produto_update'),
    path('produto/<int:pk>/delete/', views.ProdutoDelete.as_view(), name='produto_delete'),
]