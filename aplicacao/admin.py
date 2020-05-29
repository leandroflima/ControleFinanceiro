from django.contrib import admin

from .models import Unidade, Produto, Cliente

admin.site.register(Unidade)
admin.site.register(Produto)
admin.site.register(Cliente)
