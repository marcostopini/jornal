from django.db import models

# Create your models here.
class Publicacao(models.Model):
    titulo = models.CharField(max_length=300)
    texto = models.CharField(max_length=2000)
    dataPublicacao = models.DateField()

