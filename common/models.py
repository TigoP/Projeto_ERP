from django.db import models

class Endereco(models.Model):
    logradouro = models.TextField(max_length=120)
    numero = models.CharField(max_length=6)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    complemento = models.TextField(max_length=100)
    