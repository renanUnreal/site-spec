from django.contrib import admin
from .models import Produto, Categoria
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'tamanho', 'categoria')


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
