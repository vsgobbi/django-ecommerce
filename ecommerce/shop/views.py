from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import cartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    #retorna todos os produtos do banco de dados que estao disponiveis
    products = Product.objects.filter(available=True)
    #filtra o produto de acordo com o nome da categoria (otimiza queries)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    #conjunto de consulta baseado no filtro de categoria criado
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    #cria o template html e passa o dicionario de dados criado (context)
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = cartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    #cria o template com um unico produto
    return render(request, 'shop/product/detail.html', context)
