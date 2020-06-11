from django.contrib import admin

from .models import Produto, Cliente, Fornecedor, Compra, Venda

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Compra)
admin.site.register(Venda)
