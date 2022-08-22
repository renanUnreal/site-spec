from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(redirect_field_name='login')
def produtos(request):
    produtos =  Produto.objects.order_by('-id').filter(
        mostrar = True
    )
    paginator = Paginator(produtos, 25)

    page = request.GET.get('p')
    produtos = paginator.get_page(page)

    return render(request, 'produtos/index.html', {
        'produtos' : produtos
    })

def ver_produto(request, produto_id):
    #produto =  Produto.objects.get(id=produto_id)
    produto = get_object_or_404(Produto, id=produto_id)

    if not produto.mostrar:
        raise Http4004()
    return render(request, 'produtos/ver_produto.html', {
        'produto' : produto
    })

def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Algo deu errado tente novamente!')
        return redirect('produtos')



    produtos = Produto.objects.order_by('-id').filter(
        Q(nome__icontains = termo),
        mostrar=True
    )
    paginator = Paginator(produtos, 25)

    page = request.GET.get('p')
    produtos = paginator.get_page(page)

    return render(request, 'produtos/busca.html', {
        'produtos': produtos
    })
