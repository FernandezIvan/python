from django.db import models

# Create your models here.

class usuario(models.Model):
    genero = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=10)
    mail = models.CharField(max_length=10)