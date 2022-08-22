from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=128)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length = 128)
    preco = models.IntegerField()
    desc_preco = models.TextField(max_length = 255)
    tamanho = models.IntegerField(default= 0)
    desc_produto = models.TextField(max_length = 1200)
    created_at = models.DateTimeField(default = timezone.now)
    mostrar = models.BooleanField(default=True)
    linkUrl = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.nome
