from django.db import models
from datetime import date
class Tarefa(models.Model):
    STATUS_CHOICE = [("pendente","Pendente"),("concluído","Concluído"),("cancelado","Cancelado")]
    nome = models.CharField( max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default="Pendente")
    prazo = models.DateField(default=date.today)

# Create your models here.
