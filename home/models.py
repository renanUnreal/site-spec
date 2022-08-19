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
    tamanho = models.IntegerField()
    desc_produto = models.TextField(max_length = 400)
    created_at = models.DateTimeField(default= timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete= models.DO_NOTHING)

    def __str__(self):
        return self.nome
