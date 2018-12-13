from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
	category = None
	categories = Category.ojects.all()
	#retorna todos os produtos do banco de dados que estao disponiveis 
	products = Product.objects.filter(available=True)
	#filtra o produto de acordo com o nome da categoria (otimiza queries)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category)
	#conjunto de consulta baseado no filtro de categoria criado
	context = {
		'categoria': category,
		'categorias': categories,
		'produtos'; products
	}
	#cria o template html e passa o dicionario de dados criado (context)
	return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	context = {
		'produto': product
	}
	#cria o template com um unico produto
	return render(request, 'shop/product/detail.html', context)
