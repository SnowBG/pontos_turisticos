from django.db import models

# Create your models here.


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    hora_funcionamento = models.TextField()
    idade_minima = models.IntegerField()
