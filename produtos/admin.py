from django.contrib import admin
from .models import Produto, Categoria
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'tamanho', 'categoria', 'mostrar')
    list_editable = ('mostrar', 'categoria', 'preco', 'tamanho')

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)