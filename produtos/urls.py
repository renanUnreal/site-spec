from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos, name = 'produtos'),
    path('<int:produto_id>', views.ver_produto, name = 'ver_produto'),
    path('busca', views.busca, name='busca')
]