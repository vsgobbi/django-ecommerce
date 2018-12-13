from django.db import models

# Create your models here.

#chave unica habilitada
class Category(models.Model):
	nome = models.CharField(max_length=200, db_index=True)
	#campo unico, possibilita criar url convencional
	slug = models.SlugField(max_length=200, unique=True, db_index=True)

	class Meta:
		ordering = ('nome', )
		verbose_name = 'categoria'
		verbose_name_plural = 'categorias'
	
	def __str__(self):
		return self.nome

class Product(models.Model):
	categoria = models.ForeignKey(Category, related_name='produtos', on_delete=models.CASCADE)
	nome = models.CharField(max_length=100, db_index=True)
	#slug possibilita a criacao de uma url amigavel:
	slug = models.SlugField(max_length=100, db_index=True)
	description = models.TextField("teste") #(blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	available = models.BooleanField(default=True)
	available = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

	class Meta:
		ordering = ('nome', )
		#otimiza a performance de consultas:
		index_together = (('id', 'slug'),)
	
	def _str__(self):
		return self.name
