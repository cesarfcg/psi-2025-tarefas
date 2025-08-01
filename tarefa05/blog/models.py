from django.db import models
from datetime import date
# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField( max_length=50)
    descricao = models.TextField()
    data = models.DateField(date.today)
    imagem = models.ImageField( upload_to="media/",null=True, blank=True)

class Header(models.Model):
    titulo = models.CharField(max_length=50)
    link = models.CharField(max_length=100)

class Footer(models.Model):
    descricao = models.TextField()